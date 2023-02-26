import schedule
from datetime import datetime

def get_response(query):
    url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_org&nso=so%3Add%2Cp%3A1d&qvt=0'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    return soup

## 기사 크롤링
def get_new_links(newses, old_links=[]):
    # naver 기사 최신순, 1일 제한
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=4&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1d&is_sug_officeid=0'
    url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_org&nso=so%3Add%2Cp%3A1d&qvt=0'
    #한달
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=2&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1m&is_sug_officeid=0'
    list_links = [i.attrs['href'] for i in newses]
    new_links = [link for link in list_links if link not in old_links]
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
    titles = get_trimmed_news_titles(newses)
    links = get_new_links(newses, old_links)
    
    old_links += links.copy()
    
    if links: 
        # 새로운 링크 있으면 챗봇 전송
        querya = query.split(' +%2B')
        queryb = querya[0].split(' -')
        queryc = queryb[0]

        text = ' 최신 수집된 ' + f"{queryc} 뉴스입니다."
        for i in range(0, len(newses)):
            text += '\n' + f"{titles[i]}"
            text += '\n' + f"{links[i]}"
        text += "\n\n"
        return text
        # time.sleep(3)
        # await bot.send_message(chat_id=chat_id, text=links[i])
    else:
        return ""

## 텔레그램으로 전송
async def send_links(hour, text):
    text = hour + text
    await bot.send_message(chat_id=chat_id, text=text)
#실행주기
#schedule.every().day.at("15:17").do(send_links)

# program
if __name__ == '__main__':

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
    old_links = []
        
    while True:
        #schedstop = threading.Event()
        #def timer():
        #    while not schedstop.is_set():
        #        schedule.run_pending()
        #        time.sleep(3)
        #        schedthread = threading.Thread(target=timer)
        #        schedthread.start()
        #uptime = now.strftime('%Y-%m-%d %H:%M:%S')
        #await bot.send_message(chat_id=chat_id, text="관련 기사 수집 중..")
        now = datetime.now()
        time_string = now.strftime('%H:%M:%S')
        hour = now.strftime('%H 시 기준의 기사입니다.\n\n')

        if time_string == "09:00:00":
            text = ""
            for query in queries:
                text += set_links(query)
            if text:
                asyncio.run(send_links(hour, text))
            print("작동 중")
        elif time_string == "13:00:00":
            text = ""
            for query in queries:
                text += set_links(query)
            if text:
                asyncio.run(send_links(hour, text))
            print("작동 중")
        elif time_string == "18:00:00":
            text = ""
            for query in queries:
                text += set_links(query)
            if text:
                asyncio.run(send_links(hour, text))
            print("작동 중")
        sleep(1)

        