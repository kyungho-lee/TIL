#오늘의 점심메뉴를 추천해주는 프로그램
# import 는 사용할 함수를 가져온다.
# dictionary {}를 사용한다. 확장정보관리
import random

menu = ['새마을식당','초원삼겹살','멀캠20층','홍콩반점','순남시래기']
phone_book = {
    '새마을식당':'010-1234-1213',
    '초원삼겹살':'02-22-22222',
    '멀캠20층': '031-111-111',
    '홍콩반점':'033-444-4444',
    '순남시래기':'02-333-3333'
}
# print(phone_book['새마을식당'])
# menu의 요소 중 랜덤으로 골라서 lunch라는 변수에 담아주세요.
lunch = random.choice(menu)
print(lunch, phone_book[lunch])
