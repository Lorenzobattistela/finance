import os
import requests

def get_actual_price(quote):
    """
    get_actual_price(quote) \n
    quote: symbol that represents stock (ex: PETR4, S&P500) \n
    returns updated price for quote \n
    use of api.hgbrasil
    """
    lower_quote = quote.lower()
    api_key = os.getenv('API_KEY')
    response = requests.get(f'https://api.hgbrasil.com/finance/stock_price?key={api_key}&symbol={lower_quote}')
    response_json = response.json()
    quote_info = response_json['results'][quote]

    try:
        actual_price = quote_info['price']
    except:
        return 'Esse símbolo não foi encontrado.'   
    return actual_price