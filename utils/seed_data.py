from collections import defaultdict
from random import randint
import codecs, yaml, json

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

outgoing_authors = []
outgoing_works = [] 

names = ['Thomas', 'Widdle', 'Pinkerton', 'Orion', 'Wommersly', 'Smith']
text = codecs.open('seed_lines.txt').read()
lines = text.split('\n')
words = text.split()
title_words = ['Tree', 'Branches', 'Moss', 'River', 'Stone', 'Ship', 'Sails']
img = 'manuscript-banner.png'
footnotes = ['II.342', 'IV.4', 'III.78', 'VI.12', 'VII.62']

def select_one(l):
  '''Return a random selection from a list'''
  return l[randint(0, len(l)-1)]

def rand_range(_min, _max):
  '''Return a range with n items > min and < max'''
  return range(randint(_min, _max))

for author_id in rand_range(3, 20):
  author_name = select_one(names) + ' ' + select_one(names)
  start_year = randint(1500, 1900)
  end_year = start_year + randint(50, 70)

  outgoing_authors.append({
    'id': author_id,
    'name': author_name,
    'years': [start_year, end_year]
  })

  for text_id in rand_range(2, 5):

    work = {
      'author_id': author_id,
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
        variant_text = line['line']
        for variant_id in rand_range(0, 3):
          for n_words_to_change in rand_range(2, 4):
            word_to_replace = ' ' + select_one(line_words) + ' '
            replacement_word = ' ' + select_one(words) + ' '
            variant_text = variant_text.replace(word_to_replace, replacement_word)

          variant = {
            'line_variant': variant_text,
            'references': []
          }

          for reference_id in rand_range(0, 1):
            reference = {
              'footnotes': [],
              'images': []
            }

            for foonote_id in rand_range(0, 2):
              reference['footnotes'].append(select_one(footnotes))

            for image_id in rand_range(0, 1):
              reference['images'].append(img)

            variant['references'].append(reference)
          line['variants'].append(variant)
        section['lines'].append(line)
      work['sections'].append(section)
    outgoing_works.append(work)

with open('../_data/variants.json', 'w') as out:
  json.dump(outgoing_works, out)

with open('../_data/authors.json', 'w') as out:
  json.dump(outgoing_authors, out)