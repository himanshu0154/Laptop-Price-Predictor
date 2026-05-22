from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

class ParseData:

    def parse_data(self, html):
        soup = BeautifulSoup(html,'lxml')
        containers = soup.find_all('div',{'class':'product-name'})
        prices = soup.find_all('div', {'class':'product-card__price'})

        name = []
        processor = []
        ram = []
        storage = []
        display = []
        graphics = []
        price = []
        for container, price_div in zip(containers, prices):
            try:
                content = ' '.join(container.text.split())
                
                content = content.split('(')
                _name = content[0]
                
                content = '('.join(content[1:])
                content = content.split(')')
                content = ')'.join(content[:-1])
                
                content = content.split('/')
                
                _processor = content[0]
                _ram = content[1]
                _storage = content[2]
                _display = content[3]
                _graphics = content[4]
                _price = price_div.find('div', {'class': 'discountedPrice'}).find('span').find_next_sibling('span').text
                
                # only append if everything above succeeded
                name.append(_name)
                processor.append(_processor)
                ram.append(_ram)
                storage.append(_storage)
                display.append(_display)
                graphics.append(_graphics)
                price.append(_price)

            except (IndexError, AttributeError):
                continue
      
        df = pd.DataFrame({
            'name':name,
            'processor':processor,
            'ram':ram,
            'storage':storage,
            'display':display,
            'graphics':graphics,
            'prices':price
        })
        return df