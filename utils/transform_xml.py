from yaml.representer import SafeRepresenter
from transform_helpers.parse_tei import *
import glob, os, sys

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

      witness_soup = get_soup(k['witness_xml'])
      for witness_page in get_xml_pages(witness_soup):
        image_file = witness_page['image_id'] + k['witness_image_extension']
        witness['pages'].append({
          'lines': get_witness_lines(witness_page['tags']),
          'image': os.path.join(k['witness_image_directory'], image_file)
        })
      text_data['diplomatic_data']['editions'].append(witness)
    text_yaml.append(text_data)

write_yaml('_data/authors.yaml', author_yaml)
write_yaml('_data/texts.yaml', text_yaml)