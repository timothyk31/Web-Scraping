import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://jazzfuel.com/best-jazz-albums/').text
soup = BeautifulSoup(html_text, 'lxml')
desc = soup.find_all('b')
results = ''
for i in range (0,len(desc)-1,2):
    tempStr = str(desc[i])
    if ('<a href') in tempStr:
        tempStr = str(int(50-i/2)) + '.' + ' ' + tempStr[tempStr.index('/">')+3:tempStr.index('</a>')]
        numberName = tempStr
    elif ('<br/>') in tempStr:
        tempStr = tempStr[8:]
        numberName = tempStr
    else:
        numberName = tempStr[3:-4]
    tempStr = str(desc[i+1])
    album = tempStr[6:-8]
    print(f'{numberName} {album}')

