from bs4 import BeautifulSoup
import requests
import pandas

#getting the html file with the Requests module
html_text = requests.get('https://www.bookdepository.com/bestsellers').text

#making the html file we requested, a Beautiful Soup instance, 
#so we can work on it using Beautiful Soup methods

page = BeautifulSoup(html_text, 'lxml')
books = page.find_all('div', class_= 'book-item')

#making lists down, so that we can use it later for our Pandas Data Frame
title_list = []
author_list = []
price_list = []

for book in books: 
    author = book.find('p', class_='author').text.strip()
    title = book.find('h3', class_= 'title').text.strip()
    price = book.find('div', class_='price-wrap').text.replace('\n','').strip()

    author_list.append(author)
    title_list.append(title)
    price_list.append(price)

    print(f'''
    Title: {title}  
    Author: {author}
    Price: {price}
    '''
    )

#the working-with-pandas side

df = pandas.DataFrame()
df['Title'] = title_list
df['Author'] = author_list
df['price'] = price_list

df.to_csv('Books.csv')


