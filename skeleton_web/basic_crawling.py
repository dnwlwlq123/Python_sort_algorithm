import requests
from bs4 import BeautifulSoup


def crawl_breaking_news_list():
    news_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014907888'

    response = requests.get(news_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        td = soup.find('td', {'class' : 'content'})

        for li in td.find_all('li'):
            try:
                if li['data-comment'] is not None:
                    a = li.find('a')
                    link = a['href']
                    text = a.text
                    print(link, text)
            except KeyError:
                pass


def crawl_ranking_news():
    ranking_url = 'https://news.naver.com/main/ranking/popularDay.naver'

    response = requests.get(ranking_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 모든 뉴스 회사 div를 찾기
        divs = soup.find_all('div', {'class': '_officeCard'})

        if divs:
            for div in divs:
                company_name_tag = div.find('strong', class_='rankingnews_name')
                company_name = company_name_tag.text
                print()
                print(company_name)

                ul_tag = div.find('ul', {'class': 'rankingnews_list'})
                if ul_tag:
                    articles = []
                    for li in ul_tag.find_all('li'):
                        title_tag = li.find('a')
                        if title_tag:
                            title = title_tag.get_text(strip=True)
                            title_link = title_tag.get('href', '링크 없음')
                            articles.append({'title': title, 'link': title_link})
                        else:
                            articles.append({'title': '타이틀 없음', 'link': '링크 없음'})
                    for article in articles:
                        print(f"{article['title']}\n링크: {article['link']}")


if __name__ == '__main__':
    crawl_breaking_news_list()
    print()
    crawl_ranking_news()