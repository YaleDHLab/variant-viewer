from yaml.representer import SafeRepresenter
from collections import defaultdict, OrderedDict
from random import randint
import codecs, yaml, json, glob, os, shutil, glob, copy

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
seed_resources = 'seed-resources'

# get poem seed data
text = codecs.open(seed_resources + '/seed-txt/seed_lines.txt').read()
lines = text.split('\n')
words = text.split()

# images seed data
manuscript_images = glob.glob(seed_resources + '/seed-images/manuscript/*')
author_images = glob.glob(seed_resources + '/seed-images/author/*')
print_images = glob.glob(seed_resources + '/seed-images/print/*quarter.jpg')

bio = codecs.open(seed_resources + '/seed-txt/seed_bio.txt').read()
teasers = codecs.open(seed_resources + '/seed-txt/seed_teasers.txt').read().split('\n\n')
names = ['Thomas', 'Widdle', 'Pinkerton', 'Orion', 'Wommersly', 'Smith', 'Franz', 'Lambda', 'Mancin']
title_words = ['Tree', 'Branches', 'Moss', 'River', 'Stone', 'Ship', 'Sails']
footnotes = ['II.342', 'IV.4', 'III.78', 'VI.12', 'VII.62']

root_output_directory = '../_authors'

def select_one(l):
  '''Return a random selection from a list'''
  return l[randint(0, len(l)-1)]

def rand_range(_min, _max):
  '''Return a range with n items > min and < max'''
  return range(randint(_min, _max))

text_id_int = -1
for author_id_int in rand_range(2, 4):
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
      'genetic_data': {},
      'diplomatic_data': {},
      'print_data': {}
    }

    ##
    # Genetic data
    ##

    work['genetic_data']['sections'] = []

    for section_id in rand_range(2, 5):
      section = {
        'section_title': ' '.join([select_one(title_words) for _ in rand_range(2, 4)]),
        'lines': []
      }

      for line_id in rand_range(10, 25):
        line = {
          'line': select_one(lines),
          'variants': []
        }

        line_words = line['line'].split()
        for variant_id in rand_range(0, 3):
          variant_text = line['line']
          if len(variant_text.split()) > 4:
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
      work['genetic_data']['sections'].append(section)

    ##
    # Diplomatic data
    ##

    work['diplomatic_data']['editions'] = []

    for edition_id in rand_range(2, 3):
      edition = {
        'edition_id': 'Witness F314' + str(edition_id),
        'pages': []
      }

      for page_id in rand_range(20, 30):
        page_lines = []
        page_image = '/utils/' + select_one(manuscript_images)
        in_margin_div = False
        drew_margin_line = False

        for line_id in rand_range(10, 25):
          whitespace_vals = rand_range(3, 10)
          # to randomize the line's leading whitespace
          # leading_whitespace = ' '.join(['' for i in whitespace_vals])
          leading_whitespace = ''
          line_words = select_one(lines).split()

          # add text effects
          word_effects = [
            'sup',
            'sub',
            'i',
            'b',
            's',
            'u'
          ]

          for effect in word_effects:
            random_variable = rand_range(1,8)
            if random_variable[-1] == 4:
              word_idx = select_one(range(0, len(line_words)))
              word = line_words[word_idx]
              line_words[word_idx] = '<' + effect + '>' + word + '</' + effect + '>'

          # add some staggered whitespace between words
          line_text = ''
          for word in line_words:
            # to randomize whitespace between words:
            # word_whitespace = ' '.join(['' for i in rand_range(2, 6)])
            word_whitespace = ' '
            line_text += word_whitespace + word

          # build up the final text line
          composed_line_text = leading_whitespace + line_text

          # add marginal lines periodically
          random_variable = rand_range(1,8)
          if random_variable[-1] == 6 and in_margin_div == False and drew_margin_line == False:
            page_lines.append('<div class="margin-line">' + composed_line_text + '<br/>')
            drew_margin_line = True
            in_margin_div = True

          elif in_margin_div:
            page_lines.append(composed_line_text + '</div>')
            in_margin_div = False

          else:
            page_lines.append(composed_line_text + '<br/>')

        edition['pages'].append({
          'image': page_image,
          'lines': page_lines
        })

      work['diplomatic_data']['editions'].append(edition)

    ##
    # Print data
    ##

    print_image_list = []
    for i in rand_range(5, len(print_images)):
      print_image_list.append('/utils/' + print_images[i])

    work['print_data'] = {
      'pages': print_image_list
    }

    # add this work to the list of works
    outgoing_texts.append(work)

##
# JSON output
##

'''
with open('../_data/texts.json', 'w') as out:
  json.dump(outgoing_texts, out)

with open('../_data/authors.json', 'w') as out:
  json.dump(outgoing_authors, out)
'''

##
# YAML output
##

with open('../_data/texts.yaml', 'w') as out:
  yaml.dump(outgoing_texts, out, default_flow_style=False,
    width=float('inf'), default_style='')

with open('../_data/authors.yaml', 'w') as out:
  yaml.dump(outgoing_authors, out, default_flow_style=False,
    width=float('inf'))

##
# Seed app views
##

# build the root output directory if it doesn't exist
if not os.path.exists(root_output_directory):
  os.makedirs(root_output_directory)

# delete extant views // beware!
for i in glob.glob(root_output_directory + '/*'):
  if 'index.html' not in i:
    shutil.rmtree(i)

authors = yaml.load(open('../_data/authors.yaml'))
texts = yaml.load(open('../_data/texts.yaml'))

# build the authors page
with open(root_output_directory + '/index.html', 'w') as out:
  out.write('---\nlayout: authors\n---\n')

# build the individual author text views
for i in texts:
  author_id = i['author_id']
  author = authors[author_id]

  ##
  # Author index
  ##

  author_dir = root_output_directory + '/' + author['last_name'].lower()
  if not os.path.exists(author_dir):
    os.makedirs(author_dir)

  index_content =  '---\n'
  index_content += 'layout: author\n'
  index_content += 'author_id: ' + author_id + '\n'
  index_content += '---\n'

  with open(author_dir + '/index.html', 'w') as out:
    out.write(index_content)

  ##
  # Text files
  ##

  text_id = i['text_id']
  text_dir = author_dir + '/' + text_id

  if not os.path.exists(text_dir):
    os.makedirs(text_dir)

  ##
  # Reused content lines
  ##

  content_lines = [
    '---',
    'author_id: ' + author_id,
    'text_id: ' + text_id,
    '---'
  ]

  ##
  # Add text index page
  ##

  header_lines = copy.copy(content_lines)
  header_lines.insert(1, 'layout: text')
  with open(text_dir + '/index.html', 'w') as out:
    out.write( '\n'.join(header_lines) )

  ##
  # Write individual files
  ##

  for layout in ['genetic', 'diplomatic', 'print']:
    header_lines = copy.copy(content_lines)
    header_lines.insert(1, 'layout: ' + layout)
    with open(text_dir + '/' + layout + '.html', 'w') as out:
      out.write( '\n'.join(header_lines) )
