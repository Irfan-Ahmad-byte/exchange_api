from sqlalchemy import Column, Integer, String, Float, DateTime, func

from app.db.base_class import Base


class Rate(Base):
    __tablename__ = "exchange_rates"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String, nullable=False)
    target_currency = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
