import re
from urllib.request import urlopen
from html import unescape

def main():
    html = crawling('https://brunch.co.kr/')
    sent = scrapping(html)
    # print(sent)

def crawling(url):

    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html

def scrapping(html):
    print(html)
    sent = []
    for data in re.findall(r'<span class="keyword_item_txt">.*?span>', html):
        # <span class="keyword_item_txt">시사·이슈</span>
        print(1)
        print(data)
        # <span class="keyword_item_txt">지구한바퀴<br>세계여행</span>
        # sent.append({'url':url,'title':title})
    # return sent
if __name__ == '__main__':
    main()