# pip install selenium && brew install chromedriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import codecs, glob, os

driver = webdriver.Chrome()

url_root = 'http://brbl-dl.library.yale.edu'
with codecs.open('beinecke-record-urls/pound-manuscript-record-urls', 'r', 'utf-8') as f:
  f = f.read()
  for i in f.split('\n'):
    if 'VM' in i:
      record_id = i.split('/')[-1]
      record_images = []
      
      out_dir = 'beinecke-images/' + record_id
      if not os.path.exists(out_dir):
        os.makedirs(out_dir)

      driver.get(url_root + i.split()[1])
      #imgs = driver.find_elements_by_class_name('gridImage')
      imgs = driver.find_elements_by_class_name('brblThumb')
      if imgs:
        for j in imgs:
          src = j.get_attribute('src')
          for k in [src, src.replace('_thumb', '_quarter')]:
            basename = os.path.basename(k)
            os.system('wget ' + k + ' -O ' + out_dir)

driver.close()