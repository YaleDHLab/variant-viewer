import glob, os, codecs

for i in glob.glob('beinecke-image-urls/*'):
  record_id = i.split('/')[-1]
  out_dir = 'beinecke-images/' + record_id
  if not os.path.exists(out_dir):
    os.makedirs(out_dir)

  with codecs.open(i, 'r', 'utf-8') as f:
    f = f.read()
    for j in f.split('\n'):
      if 'VM' in j:
        url = j.split()[1]
        for k in [url, url.replace('_thumb.jpg', '_quarter.jpg')]:
          basename = os.path.basename(k)
          os.system('wget ' + k + ' -O ' + out_dir + '/' + basename)