import schedule
## 기사 크롤링
def get_new_links(query, old_links=[]):
    # naver 기사 최신순, 1일 제한
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=4&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1d&is_sug_officeid=0'
    url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_org&nso=so%3Add%2Cp%3A1d&qvt=0'
    #한달
    #url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_opt&sort=1&photo=0&field=0&pd=2&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3A1m&is_sug_officeid=0'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    news_titles = soup.select('a.news_tit')
    list_links = [i.attrs['href'] for i in news_titles]
    new_links = [link for link in list_links if link not in old_links]
    return new_links

def storeLinks(query):
    global old_links
    new_links = get_new_links(query, old_links)
    
    # 새로운 링크 있으면 저장
    old_links += new_links.copy()
    # query
    # querya = query.split(' +%2B')
    # queryb = querya[0].split(' -')
    # queryc = queryb[0]
    # queryc
    
## 텔레그램으로 전송
async def send_links(links):
    # 챗봇 전송
    # 새로운 링크 있으면 
    for link in links:
        await bot.send_message(chat_id=chat_id, text=link)
    
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
    i = 0
        
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
        i += 1
        for query in queries:
            storeLinks(query)
            
        print(" 작동 중")
        if i == 3 {
            print("3번째 돌았으니까 전송")
            asyncio.run(send_links(old_links))
            i = 0
        }
        time.sleep(1)
