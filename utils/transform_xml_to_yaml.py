from bs4 import BeautifulSoup
import glob, yaml, json

with open('input-xml/C6_2IncompleteDrafts-f3134.xml') as f:
  f = f.read()
  soup = BeautifulSoup(f, 'lxml')
  

