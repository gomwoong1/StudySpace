# 정규표현식의 기초

# 문자 클래스, " [ ] "
# [ ] 사이에 작성된 문자들과 매치, 라는 의미를 갖는다.

# 문자 클래스 예시
# 정규표현식 [abc] 일 때, 이는 문자열 중 a, b, c 셋 중 한 개와 매치 라는 의미를 갖는다. 따라서,
# "abc", "bced" 는 모두 매치된다. 단, "defg"와 같이 a, b, c 어느 하나 포함되지 않는 문자열은 매치되지 않는다.

# 정규표현식 [a-z] 일 때, 이는 범위를 표현하는 정규표현식이며, 알파벳 소문자 a~z중 한 개와 매치라는 의미를 갖는다.
# 정규표현식 [a-zA-Z] 일 때, 이는 알파벳 전부 중 한 개와 매치라는 의미를 갖는다.
# 정규표현식 [0-9] 일 때, 이는 숫자 전부 중 한 개와 매치라는 의미를 갖는다.

# 정규표현식 [^0-9] 일 때, 이는 반대(not)을 표현하는 정규표현식이며, 숫자가 아닌 문자만 매치라는 의미를 갖는다.
# 문자 클래스 + ^ = not을 의미한다.

# 자주 사용하는 정규표현식에 대해 별도 표기법이 존재한다.
# [0-9] == \d
# [^0-9] == \D
# [ \t\n\r\f\v] == \s, 공백문자를 나타내는 것으로, 
# 탭, 개행, 캐리지리턴, 폼피드, 수직 탭은 정규표현식에서 공백문자로 취급된다. 따라서 상기 표기법이 일치한다.
# [^ \t\n\r\f\v] == \S
# [a-zA-Z0-9_] == \w, 문자+숫자+언더바를 나타내는 정규식이다.
# [^a-zA-Z0-9_] == \W


# "." (Dot)
# 개행문자를 제외한 모든 문자와 매치됨을 의미한다.
# 단, 옵션 매개변수 설정 시 개행문자까지 매치할 수 있게 변경이 가능하다.

# 정규표현식 a.b 일 때, 이는 a로 시작하고 b로 끝나며 이 사이에 어떠한 문자 하나가 포함되어야 매치됨을 의미한다.
# "aab", "a0b" 모두 매치되나, "abc"는 a와 b 사이에 문자 하나가 없으므로 매치되지 않는다.
# 정규표현식 a[.]b일 때, 이는 a로 시작하고 b로 끝나며 이 사이에 문자 "."이 포함되어야 매치됨을 의미한다.


# 반복 (*)
# 문자가 0번 이상 반복될 수 있다는 의미를 갖는다. 즉, 반복되지 않아도 매치된다.

# 정규표현식 ca*t 일 때, "ct", "cat", "caaaat" 모두 매치된다.


# 반복 (+)
# 문자가 1번 이상 반복될 수 있다는 의미를 갖는다. 즉, 최소 1번 이상 반복되어야 매치된다.

# 정규표현식 ca+t 일 때, "cat", "caaat" 모두 매치된다. "ct"는 매치되지 않는다.


# 반복 {min, max}?
# 문자(?)가 min부터 max까지 반복될 수 있다는 의미를 갖는다. 즉, 특정 반복 회수 지정이 가능하다.

# 정규표현식 ca{2}t 일 때, a가 2번만 반복되어야 매치됨을 의미한다.
# 정규표현식 ca{2, 5}t 일 때, a가 2번 이상 5번 이하 반복되어야 매치됨을 의미한다.
# {0,}은 "*" 반복과 동일하고, {1,}는 "+" 반복과 동일하다.

# 반복 (?)
# 문자가 0번 이상 1번 이하 반복될 수 있다는 의미를 갖는다. 즉, 있어도 되고 없어도 된다는 뜻과 같다.

# 정규표현식 ab?c 일 때, "ac", "abc" 모두 매치된다.


# -------------------------------------------------------------------------------------------------
# 파이썬에서 정규표현식 사용하기

# 파이썬에서 정규표현식을 지원하는 내장 모듈(re) import
import re

# 정규표현식 a로 시작하고 b가 0번 이상 반복되는 문자열을 매치하는 컴파일된 패턴 객체 생성
RegStr = 'ab*'
ex = re.compile(RegStr)

# 검사할 문자열을 exStr 변수에 저장 후, 정규표현식 'ab*' 패턴이 컴파일 된 객체의 match 함수 호출하여 검사
# match( ) 함수는 문자열의 처음을 정규식과 매치되는지를 조사하는 함수
exStr = "abc"
result = ex.match(exStr)
print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))

exStr = "3abc"
result = ex.match(exStr)
print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))

# MEMO: match( ) 함수는 문자열 첫 부분과 정규식이 맞지 않는다면 매치되지 않는다고 본다.

# 입력받은 값의 유효성 검사를 실시하는 간단한 예제 코드
# 비밀번호를 입력받는 상황을 가정, 반드시 특수문자 느낌표로 시작하며 8~16자 사이의 비밀번호를 입력받기

# 정규표현식 !로 시작하고 문자,숫자,'_'가 7~15자인 문자열을 매치하는 컴파일된 패턴 객체 생성
ex = re.compile('!\w{7,15}')

val = input("느낌표로 시작하는 비밀번호를 8자 이상, 16자 이하로 입력해주세요: ")

# 만약 입력받은 값이 매치가 안된다면 무한루프, 매치된다면 무시 혹은 탈출
while not ex.match(val):
    print("비밀번호를 다시 입력해주세요.")
    val = input("느낌표로 시작하는 비밀번호를 8자 이상, 16자 이하로 입력해주세요: ")

print("안전한 비밀번호 입니다.")



# search( ) 함수 사용하기
# search( ) 함수는 문자열 전체를 탐색하여 정규식과 매치되는 첫 번째 부분 문자열을 찾는 함수

# 정규표현식 알파벳이 최소 1번 이상 반복되는 문자열을 매치하는 컴파일된 패턴 객체 생성
RegStr = '[a-zA-Z]+'
ex = re.compile(RegStr)

exStr = "python"
result = ex.search(exStr)
print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))

exStr = "3 python"
result = ex.search(exStr)
print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))

# MEMO: search( ) 함수는 문자열의 첫 부분이 아닌, 문자열 전체 중에서 매치되는 첫 부분을 찾는다.

# 영업용 차량의 번호판은 중간의 글자가 [아,바,사,자] 중 하나로 이루어져 있다.
# 차량 번호판을 입력받고 영업용 차량인지 아닌지를 판별하는 코드 작성하기.

ex = re.compile('[아바사자]')
val = input("차량의 번호판을 입력하세요: ")

if ex.search(val):
    print("영업용 차량입니다.")
else:
    print("영업용 차량이 아닙니다.")


# findall( ) 함수
# findall( ) 함수는 문자열 중 정규표현식과 매칭되는 모든 값들을 리스트로 리턴해주는 함수

ex = re.compile('[a-z]+')
result = ex.findall("life is too short")
print(result)

# 4자 이상의 단어들만 뽑아오는 예제 코드를 작성하기.

# 정규표현식 문자, 숫자, '_'가 최소 4번 이상 반복되는 문자열을 매치하는 컴파일된 패턴 객체 생성
RegStr = '\w{4,}'
exStr = "If you come at four in the afternoon, then at three I shall begin to be happy."
ex = re.compile(RegStr)

result = ex.findall(exStr)
print(result)

# finditer( ) 함수
# finditer( ) 함수는 findall( ) 함수와 결과는 동일하나, 반환값이 반복 가능한 객체(match)로 리턴하는 차이가 있다.

ex = re.compile('[a-z]+')
result = ex.finditer("life is too short")

for res in result:
    print(res)

# MEMO: match 객체로 반환해주기 때문에 후속해서 서술할 match 객체의 함수를 사용할 수 있다.


# match 객체 함수
# match 객체는 어떤 문자열이 매치 됐는지, 매치된 문자열의 시작과 끝 인덱스 정보를 포함하고 있다.

# 1. group( ) 함수
# match 객체의 매치된 문자열을 String으로 반환해준다.

# 2. start( ) 함수
# 매치된 문자열의 시작 인덱스 번호를 반환해준다.

# 3. end( ) 함수
# 매치된 문자열의 마지막 인덱스 번호를 반환해준다.

# 4. span( ) 함수
# 매치된 문자열의 시작, 마짐가 인덱스 번호를 튜플로 반환해준다.

ex = re.compile('[a-z]+')
result = ex.finditer("life is too short")

for res in result:
    print("텍스트:{}, 시작 인덱스:{}, 끝 인덱스:{}, 인덱스 튜플:{}"
            .format(res.group(), res.start(), res.end(), res.span()))



# 컴파일 옵션
# 정규표현식을 compile( ) 함수를 이용해 컴파일 할 때 옵션을 추가할 수 있다.

# 1. DOTALL (S), "." (Dot) 을 개행문자를 포함해 모든 문자와 매치할 수 있게 설정한다.

RegStr = "a.b"
ex = re.compile(RegStr, re.S)  # 혹은 re.DOTALL

exStr = "a\nb"
result = ex.match(exStr)

print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))


# 2. IGNORECASE (I), 대소문자 구분없이 문자열을 매치하도록 설정한다.

RegStr = '[a-z]+'
ex = re.compile(RegStr, re.I) # 혹은 re.IGNORECASE

exStr = "python Python pYTHON"
result = ex.findall(exStr)

print("정규표현식 '{}'에 대해 '{}' 매치 결과: {}".format(RegStr, exStr, result))

# MEMO: 만약 re.I 옵션을 설정하지 않았을 때의 결과 => ['python', 'ython', 'p']


# 3. MULTILINE (M), 여러 줄과 매치할 수 있도록 설정한다.

RegStr = "^python\s\w+"
ex = re.compile(RegStr, re.M) # 혹은 re.MULTILINE

exStr = """python one
life is too short
python two
you need python
python three"""

result = ex.findall(exStr)
print(result)

# MEMO: re.M 옵션을 살장하지 않았을 때의 결과 => ['python one']