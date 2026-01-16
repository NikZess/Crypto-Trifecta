import requests
from async_lru import alru_cache

url = "https://pro-api.coinmarketcap.com"

headers = {
    "X-CMC_PRO_API_KEY": "eda6e843-d84c-4123-8453-a43bfa1fd486"
}


@alru_cache
async def get_currency_price_by_currency_id(currency_id: int) -> str:
    request = requests.get(
        url=(url + "/v2/cryptocurrency/quotes/latest"),
        params={"id": currency_id},
        headers=headers,
        verify=False,
    )
    result = request.json()
    
    currency_data = result["data"][str(currency_id)]
    name = currency_data["name"]
    symbol = currency_data["symbol"]
    price = currency_data["quote"]["USD"]["price"]
    
    return f"{name} ({symbol}): ${price:.2f}"