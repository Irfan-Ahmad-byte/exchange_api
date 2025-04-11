from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request

from app.core.database import check_db_connection, create_db_n_tables
from app.utils.logs import get_logger
from app.api import rate
from app.configs.configs import settings

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    # create necessary tables
    logger.info("Connecting to database...")
    check_db_connection()
    # create database and tables
    logger.info("Creating database and tables...")
    create_db_n_tables()
    logger.info("Database and tables created.")
    # Perform any startup tasks here
    logger.info("Application's ready...")
    yield
    print("Shutting down...")


app = FastAPI(title="Authentication micro-service", version="1.0.0", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to Authentication API"}
@app.get("/health")
async def health():
    return {"status": "healthy"}
@app.get("/status")
async def status():
    return {"status": "running"}


@app.middleware("http")
async def verify_api_call(request: Request, call_next):
    api_key = request.headers.get("X-API-Key")
    api_secret = request.headers.get("X-API-Secret")
    
    if api_key is None or api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    if api_secret is None or api_secret != settings.API_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API Secret")
    
    response = await call_next(request)
    return response


app.include_router(
    rate.router,
    prefix="/rate",tags=["Rates"],
    # dependencies=[Depends(get_db)],  # Uncomment if you want to use the dependency for all routes, since we're checking the DB connection on startup, no need to add here
    # include_in_schema=False,  # Uncomment if you want to exclude this router from the OpenAPI schema
    # default_response_class=JSONResponse,  # Uncomment if you want to set a default response class
)