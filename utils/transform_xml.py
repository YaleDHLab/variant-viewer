from yaml.representer import SafeRepresenter
from transform_helpers.parse_tei import *
import glob

manifest = get_yaml('utils/data/data-manifest.yaml')
authors = manifest['authors']

text_yaml = []
author_yaml = {}

for i in authors:
  author_id = i['author_id'].rstrip()
  author_yaml[author_id] = {
    'id': author_id,
    'bio': i['author_bio'].rstrip(),
    'image': i['author_image'].rstrip(),
    'name': i['author_name'].rstrip()
  }

  for j in i['author_works']:
    text_data = {
      'author_id': author_id,
      'text_id': j['work_id'].rstrip(),
      'title': j['work_name'].rstrip(),
      'teaser': j['work_introduction'].rstrip(),
      'cover_image': j['work_image'].rstrip(),
      'print_data': {
        'pages': j['print']['print_images']
      },
      'genetic_data': get_yaml(j['genetic']['genetic_data']),
      'diplomatic_data': {
        'editions': []
      }
    }

    for k in j['work_witnesses']:
      witness = {
        'edition_id': k['witness_name'],
        'pages': []
      }

      for witness_page in get_xml_pages( get_soup(k['witness_xml']) ):
        page = {
          'lines': [],
          'image': None
        }
        for tag in witness_page['tags']:
          if tag.name == 'lg':
            page['lines'].append('<br/>')
            page['lines'].append('<br/>')
          elif tag.name == 'l':
            line = format_line(tag)
            if line.strip():
              page['lines'].append(line.rstrip() + '<br/>')
        witness['pages'].append(page)
      text_data['diplomatic_data']['editions'].append(witness)
    text_yaml.append(text_data)

with open('author_yaml.yaml', 'w') as out:
  yaml.dump(author_yaml, out, default_flow_style=False,
    width=float('inf'), default_style='')

with open('text_yaml.yaml', 'w') as out:
  yaml.dump(text_yaml, out, default_flow_style=False,
    width=float('inf'), default_style='')
