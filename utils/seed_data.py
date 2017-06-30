from collections import defaultdict
from random import randint
import codecs, yaml, json, glob, os, shutil, glob

##
# Seed app data
##

# d[author_id][work_id][section_id][line_id][variant_id] = {footnotes: [], imgs: []}
d = defaultdict(
  lambda: defaultdict(
    lambda: defaultdict(
      lambda: defaultdict(
        lambda: defaultdict()
      )
    )
  )
)

outgoing_authors = {}
outgoing_texts = []

# get poem seed data
text = codecs.open('resources/seed-txt/seed_lines.txt').read()
lines = text.split('\n')
words = text.split()

# images seed data
manuscript_images = glob.glob('resources/seed-images/manuscript/*')
author_images = glob.glob('resources/seed-images/author/*')

bio = codecs.open('resources/seed-txt/seed_bio.txt').read()
teasers = codecs.open('resources/seed-txt/seed_teasers.txt').read().split('\n\n')
names = ['Thomas', 'Widdle', 'Pinkerton', 'Orion', 'Wommersly', 'Smith', 'Franz', 'Lambda', 'Mancin']
title_words = ['Tree', 'Branches', 'Moss', 'River', 'Stone', 'Ship', 'Sails']
footnotes = ['II.342', 'IV.4', 'III.78', 'VI.12', 'VII.62']

def select_one(l):
  '''Return a random selection from a list'''
  return l[randint(0, len(l)-1)]

def rand_range(_min, _max):
  '''Return a range with n items > min and < max'''
  return range(randint(_min, _max))

text_id_int = -1
for author_id_int in rand_range(3, 4):
  first_name = select_one(names)
  last_name = select_one(names)
  start_year = randint(1500, 1900)
  end_year = start_year + randint(50, 70)
  author_bio = bio.replace('Ezra', first_name).replace('Pound', last_name)
  author_id = 'author_id_' + str(author_id_int)

  outgoing_authors[author_id] = {
    'id': author_id,
    'first_name': first_name,
    'last_name': last_name,
    'years': [start_year, end_year],
    'bio': author_bio,
    'image': '/utils/' + select_one(author_images)
  }

  for _ in rand_range(2, 5):
    text_id_int += 1
    text_id = 'text_id_' + str(text_id_int)

    work = {
      'author_id': author_id,
      'text_id': text_id,
      'teaser': select_one(teasers),
      'cover_image': '/utils/' + select_one(manuscript_images),
      'title': ' '.join([select_one(title_words) for _ in rand_range(2, 3)]),
      'sections': []
    }

    for section_id in rand_range(2, 5):
      section = {
        'section_title': ' '.join([select_one(title_words) for _ in rand_range(2, 4)]),
        'lines': []
      }

      for line_id in rand_range(10, 50):
        line = {
          'line': select_one(lines),
          'variants': []
        }

        line_words = line['line'].split()
        for variant_id in rand_range(0, 3):
          variant_text = line['line']
          for n_words_to_change in rand_range(2, 4):
            word_to_replace = ' ' + select_one(line_words) + ' '
            replacement_word = ' ' + select_one(words) + ' '
            variant_text = variant_text.replace(word_to_replace, replacement_word)

          variant = {
            'line_variant': variant_text,
            'references': []
          }

          for reference_id in rand_range(1, 2):
            reference = {
              'footnotes': [],
              'images': []
            }

            for foonote_id in rand_range(0, 1):
              reference['footnotes'].append(select_one(footnotes))

            for image_id in rand_range(0, 1):
              reference['images'].append('/utils/' + select_one(manuscript_images))

            variant['references'].append(reference)
          line['variants'].append(variant)
        section['lines'].append(line)
      work['sections'].append(section)
    outgoing_texts.append(work)

with open('../_data/texts.json', 'w') as out:
  json.dump(outgoing_texts, out)

with open('../_data/authors.json', 'w') as out:
  json.dump(outgoing_authors, out)

##
# Seed app views
##

# delete extant views // beware!
for i in glob.glob('../_texts/*'):
  if 'index.html' not in i:
    shutil.rmtree(i)

authors = json.load(open('../_data/authors.json'))
texts = json.load(open('../_data/texts.json'))

for i in texts:
  author_id = i['author_id']
  author = authors[author_id]

  # build the author's directory
  author_dir = '../_texts/' + author['last_name'].lower()
  if not os.path.exists(author_dir):
    os.makedirs(author_dir)

  # build the author's index file
  index_content =  '---\n'
  index_content += 'layout: author\n'
  index_content += 'author_id: ' + author_id + '\n'
  index_content += '---\n'

  with open(author_dir + '/index.html', 'w') as out:
    out.write(index_content)

  # build the author's work files
  text_content =  '---\n'
  text_content += 'layout: variants\n'
  text_content += 'author_id: ' + author_id + '\n'
  text_content += 'text_id: ' + i['text_id'] + '\n'
  text_content += '---\n'

  with open(author_dir + '/' + i['text_id'] + '.html', 'w') as out:
    out.write(text_content)