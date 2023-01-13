import requests
import os
from urllib.parse import urljoin, urlparse
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    bitly_api = 'https://api-ssl.bitly.com/v4/'
    token = os.environ['TOKEN']
    auth = {'Authorization': f'Bearer {token}'}
    user_url = str(input("Введите ссылку: "))
    parsed_url = f'{urlparse(user_url).netloc}{urlparse(user_url).path}'

    def is_bitlink(parsed_url):
        response_is_bitlink = requests.get(urljoin(bitly_api, f'bitlinks/{parsed_url}'), headers=auth)
        if response_is_bitlink.ok != True:
            def shorten_link(token_user, link):
                payload = {'long_url': f'https://{link}'}
                response_bitlink = requests.post(urljoin(bitly_api, 'bitlinks'), headers=auth, json=payload)
                response_bitlink.raise_for_status()
                bitlink = response_bitlink.json()['link']
                bitlink_parse = f'{urlparse(bitlink).netloc}{urlparse(bitlink).path}'
                return bitlink_parse

            try:
                bitlink = shorten_link(token, parsed_url)
                print('Битлинк:', bitlink)
            except requests.exceptions.HTTPError:
                print('Invalid input')
        else:
            def count_clicks(token_user, bitlink):
                payload = {'unit': 'month', 'units': '-1'}
                response_click = requests.get(urljoin(bitly_api, f'bitlinks/{bitlink}/clicks/summary'), headers=auth, params=payload)
                response_click.raise_for_status()
                click_user = response_click.json()['total_clicks']
                return click_user

            try:
                click_user = count_clicks(token, parsed_url)
                print('По вашей ссылке прошли:', click_user)
            except requests.exceptions.HTTPError:
                print('Invalid input')

    is_bitlink(parsed_url)
