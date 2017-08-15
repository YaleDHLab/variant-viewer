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

def write_yaml(path, obj):
  with open(path, 'w') as out:
    yaml.dump(obj, out, default_flow_style=False,
      width=float('inf'), default_style='')

def get_soup(path):
  return BeautifulSoup(open(path).read(), 'xml')

def get_xml_pages(soup):
  pages = []
  page_tags = []
  image_id = None
  for tag in soup.find_all():
    if tag.name == 'milestone':
      if page_tags and image_id:
        pages.append({
          'tags': page_tags,
          'image_id': image_id
        })
      page_tags = []
      image_id = tag['id']
    else:
      page_tags.append(tag)
  return pages

def get_witness_lines(tag_array):
  witness_lines = []
  for tag in tag_array:
    if tag.name == 'lg':
      witness_lines.append('<br/>')
    elif tag.name == 'l':
      line = format_line(tag)
      if line.strip():
        witness_lines.append(line.rstrip() + '<br/>')

  # remove leading linebreaks
  if witness_lines:
    while witness_lines[0] == '<br/>':
      del witness_lines[0]

  # add message to users if there are no transcribed lines for this page
  if len(witness_lines) == 0:
    witness_lines = ['[There are no transcribed lines for this page.]']

  return witness_lines

def format_line(s):
  s = str(s)
  for tag in tag_replacements:
    s = s.replace('<'  + tag + '>', '<'  + tag_replacements[tag] + '>')
    s = s.replace('</' + tag + '>', '</' + tag_replacements[tag] + '>')
  for tag in tags_to_remove:
    s = s.replace('<'  + tag + '>', '')
    s = s.replace('</' + tag + '>', '')
  return s
