from bs4 import BeautifulSoup
import requests


url = 'https://www.falabella.com.pe/falabella-pe'
page = requests.get(url)

soup =