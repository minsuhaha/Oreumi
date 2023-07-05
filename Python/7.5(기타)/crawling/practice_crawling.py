from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

# 페이지 수를 설정해주는 makePgNum 함수 (네비게이션 페이지를 의미) 
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)

# 검색어와 페이지에 맞는 url들을 생성해서 urls 배열에 담아주는 함수
def makeUrl(search, start_pg, end_pg):
    
    # url들을 담은 urls 배열 생성
    urls = []
    # start_pg 와 end_pg 즉 네비게이션 페이지가 같을 때 -> 즉 같은 페이지에 존재할때
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(start_page)
        urls.append(url)
        print("생성url: ", urls)
        return urls
    
    # 네비게이션 페이지의 시작과 끝이 다를 때 -> 즉 같은 페이지가 아닐때 -> 여러개의 url이 나올 수 있으니 for문 돌려주기
    else:
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page)
            urls.append(url)
        print("생성url: ", urls)
        return urls

# 사용자에게 입력을 받기 위한 함수
def input_start():

	# 사용자 입력 (search, page_start, page_end)
	search = input("검색할 단어?\n")
        
	page_start = int(input("시작페이지?"))
	print(f"시작할 페이지: {page_start}")

	page_end = int(input("종료페이지?"))
	print(f"종료할 페이지: {page_end}")

	# 네이버 url 생성 (입력받은 데이터를 makeUrl 함수 매개변수에 넣고 호출하여 만들어진 url 가져오기)
	search_urls = makeUrl(search, page_start, page_end)

    # webdriver 모듈의 Chrome 클래스를 사용하여 Chrome 브라우저를 제어하기 위한 driver 객체 초기화 -> 제어가 핵심
	driver = webdriver.Chrome()
    # 암묵적 대기 설정. 웹 요소가 로드될 때까지 일정 시간 동안 대기하는 기능을 제공. 3값을 줌으로써 최대 3초간 대기
	driver.implicitly_wait(3)

	naver_urls = []

    # driver.get(i)를 호출하여 해당 URL(i)로 이동합니다.
    #time.sleep(3)을 사용하여 3초 동안 대기합니다. 이는 페이지 로드나 요소가 나타날 때까지 기다리기 위한 암묵적 대기입니다.
	for i in search_urls:
		driver.get(i)
		time.sleep(3)

        # driver.find_elements()를 사용하여 CSS 선택자 'a.info'에 해당하는 모든 요소를 찾는다. 
		a = driver.find_elements(By.CSS_SELECTOR, 'a.info')

        # a변수에 담긴 a.info에 해당하는 모든 요소들에 대해 for문을 돌려 i.click()을 호출하여 해당 요소를 클릭.
		for i in a:
			i.click()
            
            # 사용하여 새로 열린 창으로 전환합니다
			driver.switch_to.window(driver.window_handles[1])
			time.sleep(3)

            # 현재 페이지의 URL을 가져옵니다.
			url = driver.current_url
			print(url)

            # url이 네이버뉴스라면 naver_urls 에 담아주기
			if "news.naver.com" in url:
				naver_urls.append(url)
    
            #  현재 사용했던 driver 닫아주기
			driver.close()

            # 사용하여 처음의 창으로 전환
			driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
	
	# input_start() 현재는 사용하지 않아서 주석처리

    # 임의로 search 입력
	search = "나비"
    
    # 임의로 naver_urls 입력 -> 입력받았다고 가정하고
	naver_urls = ['https://sports.news.naver.com/news.nhn?oid=442&aid=0000163350', 'https://n.news.naver.com/mnews/article/001/0014045673?sid=103', 'https://n.news.naver.com/mnews/article/366/0000913600?sid=101', 'https://n.news.naver.com/mnews/article/025/0003290622?sid=102']

    # 위 코드는 HTTP 요청 헤더에 사용자 정보? 를 설정하여 웹 페이지 요청 시 웹 브라우저와 유사한 동작을 수행하도록 해주는 header.
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

	titles = []
	contents = []

    # naver_urls
	for url in naver_urls:
        # requests.get()을 사용하여 해당 링크의 HTML 불러오기
		orginial_html = requests.get(url, headers=headers)
        # 가져온 HTML을 .text를 붙여 text만을 BeautifulSoup을 사용하여 파싱
		html = BeautifulSoup(orginial_html.text, "html.parser")

        # html.select()를 사용하여 HTML에서 제목 요소만을 select
		title = html.select("div#ct > div.media_end_head.go_trans > div.media_end_head_title > h2")
		title = ''.join(str(title)) # 제목 요소를 문자열로 변환
        # <> -> html 태그 제거
		pattern1 = r'<[^>]*>'
        # 제거 할 html 태그들을 re.sub()를 통해 '' 으로 대체
		title = re.sub(pattern=pattern1, repl='', string=title)
		titles.append(title)

        # html.select()를 사용하여 HTML에서 내용요소만을 선택.
		content = html.select("div#dic_area")
        # 마찬가지로 내용 요소들을 문자열로 변환
		content = ''.join(str(content))
        # html 태그들을 re.sub() 함수를 사용하여 '' 으로 변환
		content = re.sub(pattern=pattern1, repl='', string=content)
        # pattern2 와 같은 불필요한 패턴을 삭제하기 위해 content.replace()를 사용하여 패턴을 ''으로 변환 -> 즉 제거한다는 말과 동일한듯.
		pattern2 = """[\n\n\n\n\n// flash 오류를 우회하기 위한 함수 추가\nfunction _flash_removeCallback() {}"""
		content = content.replace(pattern2,  '')
		contents.append(content)

print(titles)
print(contents)

# 추출한 제목, 링크, 내용을 pandas 패키지를 이용하여 데이터프레임으로 만들어주기.
news_df = pd.DataFrame({'title':titles, 'link': naver_urls, 'content': contents})

# 생성된 데이터프레임을 csv 파일로 출력? 
# 파일명은 NaverNews_{search}.csv로 저장, utf-8 인코딩을 사용.
news_df.to_csv(f'NaverNews_{search}.csv', index=False,  encoding='utf-8')