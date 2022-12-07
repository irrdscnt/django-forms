import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://enter.kg'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='row')
    nout = []

    for item in items:
        nout.append(
            {
                'title': URL + item.find('a').get('href'),
                'title_text': item.find('span', class_='prouct_name').get_text(),               
                'price': item.find('span', class_='price').get_text(),
                'image': URL + item.find('a', class_='product-image-link').find('img').get('src')
            }
        )
    return nout

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        proger_nout1 = []
        for page in range(0, 1):
            html = get_html(f'https://enter.kg/computers/noutbuki_bishkek', params=page)
            proger_nout1.extend(get_data(html.text))
        return proger_nout1
    else:
        raise Exception('Error in parser func........')