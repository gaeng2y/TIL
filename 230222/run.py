{query} : 네이버 뉴스검색
'{query}'의 네이버 뉴스검색 결과입니다.

import schedule
from datetime import datetime

def get_response(query):
    # naver 기사 최신순, 1일 제한
    url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=4&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1d&is_sug_officeid=0'
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_org&nso=so%3Add%2Cp%3A1d&qvt=0'
    #한달
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=2&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1m&is_sug_officeid=0'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    return soup

## 링크 크롤링
def get_new_links(query, newses, old_links={}):
    print(type(query))
    print(type(old_links))
    try:
        old_links[query] = old_links[query][-30:]
    except KeyError:
        old_links[query] = []
    
    list_links = [i.attrs['href'] for i in newses]
    print(list_links)
    new_links = [link for link in list_links if link not in old_links[query]]
    return new_links

def get_news_titles(soup):
    news_titles = soup.select('a.news_tit')
    return news_titles

def get_trimmed_news_titles(newses):
    list_titles = [i.attrs['title'] for i in newses]

    return list_titles


def set_links(query):
    global old_links
    soup = get_response(query)
    newses = get_news_titles(soup)
    print(query)
    titles = get_trimmed_news_titles(newses)
    links = get_new_links(query, newses, old_links)
    
    old_links[query] += links.copy()
    
    if links: 
        # 새로운 링크 있으면 챗봇 전송
        querya = query.split(' +%2B')
        queryb = querya[0].split(' -')
        queryc = queryb[0]

        text = f"<{queryc}> 관련 뉴스"
#         print(len(newses))
#         print(len(titles))
#         print(len(links))
        for i in range(0, len(newses)):
            title = f"{titles[i]}"
            print(title)
            text += '\n' + f"{titles[i]}"
            link = f"{links[i]}"
            print(link)
            text += '\n' + link
        text += "\n\n"
        return text
        # time.sleep(3)
        # await bot.send_message(chat_id=chat_id, text=links[i])
    else:
        return ""

## 텔레그램으로 전송
async def send_links(index, hour, text):
    if index == 5:
        text = hour + text
    await bot.send_message(chat_id=chat_id, text=text)
#실행주기
#schedule.every().day.at("15:17").do(send_links)

# program
if name == '__main__':

    # 챗봇 info
    token = '6002402443:AAFtMNq4Z0rkVQNs-sYYJk4sITv8LUeCn1w'
    bot = telegram.Bot(token = token)
    #original
    #chat_id = -847410410
    #테스트봇
    chat_id = -837932767
    #choi
    #chat_id = -847814464

    # portfolio
    queries = kclavis
    # 주기
    #job = schedule.every(10).seconds.do(send_links, query)
    old_links = dict()
    
    first_hour = "11:06:20"
    second_hour = "13:00:00"
    third_hour = "18:00:00"
        
    while True:

        now = datetime.now()
        time_string = now.strftime('%H:%M:%S')
        #print(time_string)
        date = now.strftime('<News> 케이클라비스-메타 세컨더리펀드 제일호\n%m월 %d일 %H시 기준 최신 기사입니다.\n\n')
        if time_string == first_hour:
            print(first_hour + "작동 중")
            cnt = 0
            text = ""
            for i in range(0, len(queries)):
                link = set_links(queries[i])
                if not link:
                    continue
                cnt += 1
                text += link
                if cnt % 5 == 0:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                    text = ""
                if i == len(queries) - 1:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                time.sleep(3)
        elif time_string == second_hour:
            print(second_hour + "작동 중")
            cnt = 0
            text = ""
            for i in range(0, len(queries)):
                link = set_links(queries[i])
                if not link:
                    continue
                cnt += 1
                text += link
                if cnt % 5 == 0:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                    text = ""
                if i == len(queries) - 1:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                time.sleep(3)
        elif time_string == third_hour:
            print(third_hour + "작동 중")
            cnt = 0
            text = ""
            for i in range(0, len(queries)):
                link = set_links(queries[i])
                if not link:
                    continue
                cnt += 1
                text += link
                if cnt % 5 == 0:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                    text = ""
                if i == len(queries) - 1:
                    if text:
                        asyncio.run(send_links(cnt, date, text))
                time.sleep(3)