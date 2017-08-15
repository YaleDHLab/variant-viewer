import os, yaml, shutil, glob, copy

##
# Seed app views
##

root_output_directory = '_authors'

# build the root output directory if it doesn't exist
if not os.path.exists(root_output_directory):
  os.makedirs(root_output_directory)

# delete extant views // beware!
for i in glob.glob(root_output_directory + '/*'):
  if 'index.html' not in i:
    shutil.rmtree(i)

authors = yaml.load(open('_data/authors.yaml'))
texts = yaml.load(open('_data/texts.yaml'))

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

  author_dir = root_output_directory + '/' + author['id'].lower()
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
