# 로또 번호 랜덤 추출기
import random

numbers = range(1,46)
# 이것의 결과는 배열 [1,2,3,...,45] 과 비슷
# random.choice 를 사용해 6개의 번호를 뽑아 출력하세요 - choice는 중복허용
# random.sample 은 중복제거
lotto = random.sample(numbers,6)
print(sorted(lotto))
# sorted 함수는 자동정렬
# 단축키 : alt + shift + 위 or 아래 방향키 이전라인 복사
# 단축키 : alt + 위 or 아래 라인 이동