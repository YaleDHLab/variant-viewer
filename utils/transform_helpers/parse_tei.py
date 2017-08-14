from bs4 import BeautifulSoup
import yaml

tag_replacements = {
  'del': 's',
  'add': 'sup',
  'emph': 'b'
}

tags_to_remove = [
  'l'
]

def get_yaml(path):
  return yaml.load(open(path))

def get_soup(path):
  return BeautifulSoup(open(path).read(), 'xml')

def get_xml_pages(soup):
  pages = []
  milestones = soup.find_all('milestone')
  next_tags = []
  for m in milestones:
    do_read = True
    for i in m.find_all_next():
      if do_read and i.name != 'milestone':
        next_tags.append(i)
      else:
        do_read = False

    pages.append({
      'tags': next_tags,
      'image_id': m['id']
    })
  return pages

def format_line(s):
  s = str(s)
  for tag in tag_replacements:
    s = s.replace('<'  + tag + '>', '<'  + tag_replacements[tag] + '>')
    s = s.replace('</' + tag + '>', '</' + tag_replacements[tag] + '>')
  for tag in tags_to_remove:
    s = s.replace('<'  + tag + '>', '')
    s = s.replace('</' + tag + '>', '')
  return s
