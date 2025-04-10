#! python3
# searchpypi.py - Opens several search results.
import requests, sys, webbrowser, bs4

print('Searching...')  # display text while downloading the search result page
# res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
}

# Pass top500 in your terminal when running the script
res = requests.get('https://moz.com/' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.text-nowrap')
print(f'length of link: {len(linkElems)}')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    urlToOpen = linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
