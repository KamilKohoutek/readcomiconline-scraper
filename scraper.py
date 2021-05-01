from sys import argv
from urllib.request import urlopen, urlretrieve, Request

src_url = argv[1] + '&quality=hq&readType=1'
dest_folder = argv[2]

r = Request(src_url, headers={'User-Agent': 'Mozilla/5.0'})
lines = urlopen(r).read().decode('utf-8').split('\n');
page_number = 1;
for line in lines:
    if 'lstImages.push' in line:
        img_url = line[24:-4]
        urlretrieve(img_url, dest_folder+'/'+str(page_number)+'.jpg')
        page_number += 1
