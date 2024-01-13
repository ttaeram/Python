#04 문자열
'''
type() : ()안에 확인하고 싶은 데이터를 넣어 출력하면 데이터가 어떤 형태인지 보여줌
나는 소년입니다 -> <class 'str'>
'''

#인덱스
'''
index : 여러 문자로 구성된 문자열의 n번째 문자 -> n번째 인덱스
-> 인덱스는 데이터의 순서 혹은 위치를 나타냄
jumin = '990229-1234567'
jumin[7] : 1
인덱스는 0부터 시작
'''

#슬라이싱
'''
[]안에 인덱스를 넣고 필요 범위를 :(콜론)으로 구분해 표시함
jumin[0:2] : 0부터 2직전까지 -> 0, 1
jumin[2:4] : 2부터 4직전까지 -> 2, 3

-변수명[:종료 인덱스] : 처음부터 종료 인덱스까지 슬라이싱
-변수명[시작 인덱스:] : 시작 인덱스부터 끝까지 슬라이싱
-변수명[:] : 처음부터 끝까지 슬라이싱
jumin[:6] : 처음부터 6직전까지 = jumin[0:6]
jumin[7:] : 7부터 끝까지 = jumin[7:14]

뒤에서부터 슬라이싱 할 경우 음수 인덱스를 사용
양수 인덱스는 0부터지만 음수 인덱스는 -1부터 시작
jumin[-7:] : 뒤에서 7번째 위치부터 끝까지 슬라이싱
'''

#함수로 문자열 처리하기
'''
lower() : 문자열을 소문자로 변환
upper() : 문자열을 대문자로 변환
islower() : 문자열이 소문자인지 확인
isupper() : 문자열이 대문자인지 확인
replace() : 문자열 바꾸기
index() : 찾는 문자열의 인덱스 (없으면 오류 발생)
find() : 찾는 문자열의 인덱스 (없으면 -1 반환)
count() : 문자열이 나온 횟수
-> 문자열 처리 함수는 문자열과 함수를 .(점)으로 연결하여 사용
len() : 문자열의 길이 정보 (공백까지 포함)
len()는 len(문자열 또는 변수)의 형태로 사용함
'''

#문자열 포매팅
'''
문자열을 연결할 때는 + 연산자나 ,(쉼표)를 사용
+를 사용하면 문자열 사이를 띄어쓰지 않지만 ,(쉼표)를 사용하면 한칸 띄어 쓴 채 연결함
문자열과 다른 자료형을 연결하려면 형변환을 해야함
하지만 형변환 없이 가능한 방법 존재
'''

#서식 지정자
'''
%d : 정수(decimal)
%f : 실수(floating-point)
%c : 문자(character)
%s : 문자열(string)
-> print("문자열 서식지정자 문자열" % 값) 의 형태로 사용
    ex) "나는 %d살입니다." % 20
        "나는 %s를 좋아합니다." % "파이썬"
-> 문자열 안에 값을 2개 이상 넣고 싶다면 서식 지정자를 넣고 싶은만큼 넣은 후
    값들을 쉼표로 구분후 소괄호로 감까 %뒤에 넣음
    ex) "나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")
'''

#format() 함수
'''
문자열에 넣을 값을 format()의 소괄호 안에 넣어 사용
    ex) "나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")
중괄호 안에 인덱스 값 뿐 아니라 이름을 넣고 사용도 가능
    ex) "나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간")
'''

#f-문자열 사용하기
'''
print(f"문자열{변수명1}문자열{변수2}...") 형식으로 사용
    ex) age = 20
        color = "빨간"
        print(f"나는 {age}살이며, {color}색을 좋아해요.")
'''

#탈출문자
'''
\n : 문자열 안에서 줄 바꿈할 때 사용하는 탈출 문자
\", \' : 문자열 안에서 따옴표를 사용할 때 사용하는 탈출 문자
\\ : 문자열 안에 역슬래시를 사용하고 싶은 경우 사용
r : 문자열 앞에 r을 붙이면 문자열 내에 어떤 값이 있던 출력 가능
\r : \r뒤의 문자열을 맨 앞으로 이동시킨 후 원래 값에 덮어씌움
\b : \b앞의 글자 하나를 삭제함
\t : tab키와 통일한 역할을 함
'''

#실습 문제 : 비밀번호 만들기
'''
사이트 별로 비밀번호를 생성하는 프로그램을 작성하세요.
http://naver.com
http://daum.net
http://google.com
http://youtube.com
'''
#조건
'''
1. http:// 부분은 제외한다.
2. 처음 만나는 점(.) 이후 부분도 제외한다.
남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e'의 개수 + !로 구성한다.
프로그램을 실행했을 때 실행 결과는 다음 형태로 나와야 한다.
http://naver.com의 비밀번호는 nav51!입니다.
'''

addres = input()
addres1 = addres[7:-4]
pw = addres1[:3] + str(len(addres1)) + str(addres1.count('e')) + '!'
print("http://naver.com의 비밀번호는", pw + "입니다.")