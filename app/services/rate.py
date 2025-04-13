import requests
from typing import Optional

from app.configs.configs import settings



def get_conversion_rate(currency: str) -> Optional[float]:
    """
    Get the conversion rate of a given currency against USDt (Tether).

    Args:
        currency (str): The symbol of the currency (e.g., BTC, ETH).

    Returns:
        Optional[float]: Conversion rate against USDt if successful, otherwise None.
    """
    # Read API details from environment variables
    base_url = settings.COIN_MARKET_CAP_URL
    api_key = settings.COIN_MARKET_CAP_API_KEY

    if not api_key:
        raise ValueError("API key for CoinMarketCap is not set in environment variables.")

    # API endpoint for conversion
    endpoint = f"{base_url}/v2/tools/price-conversion?amount=1&symbol={currency.upper()}&convert=USDT"

    # Prepare request parameters
    params = {

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx
        data = response.json()

        # Extract and return the conversion rate
        return data["data"][0]["quote"]["USDT"]["price"]
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching conversion rate: {e}")
    except KeyError as e:
        print(f"Unexpected response structure received from the API.: {e}")
    return None