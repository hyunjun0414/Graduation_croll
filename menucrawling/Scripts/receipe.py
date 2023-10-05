# -*- coding: utf-8 -*-



import os
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore





URL = "https://cjhong.tistory.com/604"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 웹 서버의 응답을 받아온 객체.
response = requests.get(URL, headers=headers)


# HTML 테이블에서 데이터를 추출하고 이를 파싱하여 Python 딕셔너리 형식으로 반환하는 함수
def parse_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    headers = [header.text.strip() for header in soup.find_all('tr')[0].find_all('td')]
    data_dict = {header: [] for header in headers}
    for header, column in zip(headers, soup.find_all('tr')[1].find_all('td')):
        items = column.find_all('span')
        data_dict[header].extend([item.text.strip() for item in items])
    return data_dict

# 응답 처리
if response.status_code == 200:

    # 첫 번째 테이블 데이터
    html1 = """<table style="border-collapse: collapse; width: 100%; height: 314px;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr style="height: 20px;">
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>밥</b></span></td>
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>죽</b></span></td>
<td style="text-align: center; height: 20px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>볶음밥 / 덮밥</b></span></td>
</tr>
<tr style="height: 294px;">
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">잡곡밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">옥수수밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">무밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">명란버터밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">가지밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">전복밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩나물밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">곤드레비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">표고버섯영양밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쌈밥</span></td>
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">야채죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">전복죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">삼계죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">미역죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">참치죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기버섯죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">팥죽</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">단호박죽</span></td>
<td style="text-align: center; height: 294px;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">베이컨볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">간장계란밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스팸볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">해물볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">카레덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">짜장밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오므라이스</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">육회비빔밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치알밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
</tr>
</tbody>
</table>"""
    data_dict1 = parse_table(html1)
    
    # 두 번째 테이블 데이터
    html2 = """<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>국/탕</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>찌개</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>전골</b></span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">미역국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">무국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩나물국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치콩나물국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">사골곰탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">북엇국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">우거지국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">시래기국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">배추된장국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">매생이국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">올갱이국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">뼈해장국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">된장국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란감자국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어무국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">어묵탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">육개장</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">갈비탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">삼계탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">추어탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꽃게탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">홍합탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">해물누룽지탕</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">된장찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">차돌된장찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꽃게된장찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">순두부찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">부대찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">청국장</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">동태찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비지찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고추장찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">짜글이찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">버섯찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기찌개</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우찌개</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">밀폐유나베</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기버섯전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">불고기전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">어묵전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">만두전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">두부전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">버섯전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">곱창전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">대창전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">아롱사태전골</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">불낙전골</span></td>
</tr>
</tbody>
</table>"""
    data_dict2 = parse_table(html2)
    
    # 세 번째 테이블 데이터
    html3 = """<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>육류</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>어류</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>기타</b></span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">삼겹살</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">수육</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스테이크구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">찹스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">갈비찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">돼지갈비</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">LA갈비</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">바베큐</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치등갈비찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">묵은지돼지갈비찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">매운쪽갈비찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">폭립</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">제육볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소불고기</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">돼지불고기</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">닭볶음탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">닭갈비</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">훈제오리구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">단호박훈제오리찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">삼겹살숙주볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">차돌숙주볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">찜닭</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소세지야채볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">돈까스</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">떡갈비</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">함박스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">동그랑땡</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">편백나무찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">곱창구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">막창구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">족발</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">치킨</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">닭강정</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">생선까스</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">연어스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">미나리오징어초무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쭈꾸미볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">아귀찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">해물찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고등어구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고등어조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">코다리조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">갈치구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">갈치조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">장어구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">조기구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">가자미구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꽁치조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">낙곱새</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">바지락술찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">바지락칼국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꽃게찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">대게찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">랍스터찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">간장게장</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">양념게장</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우장</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">회</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">생굴</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">잡채</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">골뱅이무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">곱창볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">순대볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">닭볶집볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">닭발</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오돌뼈</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">월남쌈</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">도토리묵무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쌈무말이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
</tr>
</tbody>
</table>"""
    data_dict3 = parse_table(html3)
    
    # 네 번째 테이블 데이터
    html4 = """<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>볶음 / 조림</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>무침 / 김치</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>기타</b></span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자채볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">두부조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">메추리알장조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소고기장조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">진미채볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">버섯볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">연근조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">건새우조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">우엉채볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">멸치볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">애호박볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">볶음김치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">어묵볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">햄볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">마늘쫑볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">미역줄기볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">땅콩조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩자반</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">무조림</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꽈리고추볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">베이컨숙주볶음</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">시금치무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩나물무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고사리무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">숙주무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오이소박이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">단무지무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">골뱅이무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꼬막무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">배추김치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">물김치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">열무김치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">깻잎지</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">깍두기</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">겉절이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">젓갈</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고추장오이무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">된장고추무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">파래무침</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">파절이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">양배추찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">파김치</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란찜</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란후라이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란말이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">부추계란볶음</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스크램블</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스팸구이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">치킨너겟</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">치킨텐더</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">애호박전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김치전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">부추전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">두부전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">버섯야채전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">배추전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">동태전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꼬지전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소세지전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고추장떡</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">깻잎전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">베이컨팽이버섯말이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">맛살하트전</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">참치마요</span></td>
</tr>
</tbody>
</table>"""
    data_dict4 = parse_table(html4)
    
    # 다섯 번째 테이블 데이터
    html5 = """<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>밥/떡/빵</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>면</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>튀김 등</b></span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">라면</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">주먹밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">유부초밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꼬마김밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">떡볶이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">라볶이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">궁중떡볶이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">기름떡볶이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">떡꼬치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">소떡소떡</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">샌드위치</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">마늘빵</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">토스트</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">냉면</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">잔치국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비빔국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">열무국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콩국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">수제비</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비빔만두</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쫄면</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">칼국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">떡국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">만둣국</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">우동</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">핫도그</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">찐만두</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">튀김만두</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">비빔만두</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">김말이튀김</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">야채튀김</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오징어튀김</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">가지튀김</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">팝콘치킨</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">순대</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
</tr>
</tbody>
</table>"""
    data_dict5 = parse_table(html5)
    
    # 여섯 번째 테이블 데이터
    html6 = """<table style="border-collapse: collapse; width: 100%;" border="1" data-ke-align="alignLeft" data-ke-style="style7">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>중식</b></span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><b>양식</b></span></td>
<td style="text-align: center;"><b><span><span>일식 등</span></span></b></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">짜장면</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">짬뽕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">마라탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">탕수육</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">꿔바로우</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">마파두부</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">계란토마토볶음밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">양장피</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">깐풍기</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">깐풍새우</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">크림새우</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">유린기</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">팔보채</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고추잡채</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">춘권</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">딤섬</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">토마토스파게티</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">크림파스타</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">명란파스타</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">봉골레파스타</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감바스</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">또띠아피자</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">고구마그라탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자그라탕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">피자</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">함박스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">리조또</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">스테이크</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">샐러드</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">햄버거</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">부리또</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">해쉬브라운</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">감자튀김</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">맥앤치즈</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">콘샐러드</span></td>
<td style="text-align: center;"><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">초밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">라멘</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">나가사키짬뽕</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">오니기리</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">연어덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">새우장덮밥</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">메밀소바</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">돈카츠</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">야키니쿠</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">낫또</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">볶음우동</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">카레우동</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">가츠동</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">규동</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">쌀국수</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">팟타이</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';">타코</span><br><span style="font-family: 'Noto Sans Demilight', 'Noto Sans KR';"><br></span></td>
</tr>
</tbody>
</table>"""
    data_dict6 = parse_table(html6)

    # 결과 출력 (또는 Firestore에 저장)
    print(data_dict1)
    print(data_dict2)
    print(data_dict3)
    print(data_dict4)
    print(data_dict5)
    print(data_dict6)

else:
    print("Error:", response.status_code)


# Firebase Admin SDK 초기화
load_dotenv()
api_key = os.environ.get("MY_API_KEY")
cred = credentials.Certificate(api_key) # 서비스 계정 키의 경로를 지정해주세요.
firebase_admin.initialize_app(cred)

db = firestore.client()


# Firestore에 데이터 저장
collection_ref = db.collection('menu')  # 적절한 컬렉션 이름으로 변경해주세요.

# 데이터 저장
combined_data_dict = {
    "data1": data_dict1,
    "data2": data_dict2,
    "data3": data_dict3,
    "data4": data_dict4,
    "data5": data_dict5,
    "data6": data_dict6
}

doc_ref = collection_ref.add(combined_data_dict)

