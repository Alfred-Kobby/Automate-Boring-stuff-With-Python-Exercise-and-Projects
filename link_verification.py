#! python3
# link_verification.py - Downloads every single link in a page.
import requests, os, re, bs4

match = re.compile(r'https://')

url = input('Enter a url\n')
url = re.sub('https://', '', url)
url = 'https://'+url
res = requests.get(url)
res.raise_for_status()

os.makedirs('links', exist_ok=True)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_tags = soup.select('a')
if not link_tags:
    print('Could not find any links')
else:
    for i in range(len(link_tags)):
        try:
            url = link_tags[i].get('href')
            page = requests.get(url)
            if page.status_code == 404:
                print('Link broken')
            else:
                print('Downloading page %s...' % url)
                pageFile = open(os.path.join('links', os.path.basename(url))+'.html', 'wb')
                for chunk in res.iter_content(100000):
                    pageFile.write(chunk)
                pageFile.close()
                print('Page downloaded %s...' % url)
        except Exception as err:
            print(err)

