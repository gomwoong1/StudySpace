a = ['one', 2, 3.0]
print("a의 첫번째 원소:", a[0])
print("a의 1, 2번째 원소 더하기 결과값:", a[1] + a[2])
print("a의 마지막 요소:", a[-1])

a = [1, 2, 3, ['One', 'Two', 'Three']]
print("a의 첫번째 원소:", a[0])
print("a의 마지막 요소:", a[-1])
print("a의 마지막 요소 중 첫번째 요소", a[-1][0])
print("a의 마지막 요소 중 마지막 요소", a[-1][-1])

a = [101, 102, ['a', 'b', ['Spring', 'Summer']]]
print("3차원 리스트중, 마지막 요소의 첫번째 요소", a[2][2][0])
print("3차원 리스트중, 마지막 요소의 마지막 요소", a[-1][-1][-1])
print("3차원 리스트중, 1차원 리스트의 마지막 요소의 첫번째 요소", a[-1][0][0])

a = [101, 102, 103, 104, 105]
print("a의 0~2번 요소를 출력:", a[0:3])

a = "101, 102, 103, 104, 105"
# print("a의 세번째 요소까지 슬라이싱:", a[0:13])
print("a의 3번 인덱스까지 슬라이싱:", a[0:3])

a = [101, 102, ['One', 'Two', 'Three'], 103, 104, 105]
print("a의 2~4번째 요소 출력:", a[1:4])
print("a의 두번째 요소중 1~2번째 요소 출력:", a[2][:2])

a = [101, 102, 103]
b = [201, 202, 203]
print("리스트 a와 b의 더하기 연산결과:", a+b)

c = ['one', 'two']
d = ['three']
print("리스트 c와 d의 더하기 연산결과", c+d)

a = ['one', 'two', 'three']
print("리스트 a의 곱하기 3 연산결과:", a*3)

a = [11, 12, 13]
# print("에러발생:", a[2] + "회")
print("리스트를 문자열로 형변환하고 문자열과 더하기 연산결과:", str(a[2]) + "회")

a = [101, 102, 103]
a[2] = 201
print("a의 세번째 요소값 변경 결과:", a)

a = [201, 202, 203]
a[1:2] = ['one', 'two', 'three']
print("a의 두번째 요소값 변경 결과:", a)
print("a의 두번째 요소:", a[1])
a[1] = ['하나', '둘', '셋']
print("a의 두번째 요소를 리스트로 수정:", a)

print("요소 삭제 전 리스트 출력:", a)
print("리스트 a의 2~3번째 요소 출력:", a[1:3])
a[1:3] = []
print("2~3번째 요소 삭제 후 리스트 출력:", a)

print("함수 이용해 원소 삭제 전 리스트 출력:", a)
del a[1]
print("두번째 요소를 삭제 후 리스트 출력:", a)

a = [301, 302, 303]
print("리스트 a중 302의 인덱스 번호:", a.index(302))
print("리스트 a중 303의 인덱스 번호:", a.index(303))

a = [101, 102, 103]
a.extend([201, 202])
print("리스트 a에 요소를 확장한 결과:", a)
b = [301, 302, 303]
a.extend(b)
print("리스트 a에 리스트 b를 확장한 결과:", a)

a = ['one', 'two']
a.append('three')
print("리스트 a에 마지막 요소 추가:", a)
a.append([5, 10])
print("리스트 a에 리스트 추가:", a)

a = [101, 102, 103]
a.insert(1, 201)
print("리스트 a의 두번째 요소 위치에 요소 추가:", a)
a.insert(2, 'three')
print("리스트 a의 세번째 요소 위치에 요소 추가:", a)
a.insert(3, [301, 302])
print("리스트 a의 세번째 요소 위치에 요소 추가:", a)

a = [88, 35, 97, 35, 88]
a.remove(35)
print("리스트 중 35를 삭제한 결과:", a)
a.remove(88)
print("리스트 중 88를 삭제한 결과:", a)

a = ['one', 'two', 'three']
a.remove('two')
print("리스트 중 'two'를 삭제한 결과:", a)

a = ['one', 'two', 'three']
print("리스트 a의 맨 마지막 요소를 반환:", a.pop())
print("pop 함수 이후 리스트 출력:", a)

a = [33, 85, 33, 96, 33]
print("리스트 중 33이 몇 개인지 출력:", a.count(33))

a = [356, 123, 509, 25, 808]
a.sort()
print("리스트 a를 오름차순으로 정렬:", a)
b = ['three', 'two', 'one']
b.sort()
print("리스트 b를 오름차순으로 정렬:", b)
# c = ['홍길동', '강감찬', '이순신']
# c.sort()
# print("리스트 c를 오름차순으로 정렬:", c)

# a = [56, 13, 7, 25, 88]
# a.reverse()
# print("리스트 a를 뒤집은 결과:", a)

# tp = (101, 102, 'one', 'two')
# print("튜플 tp의 첫번째 요소:", tp[0])
# print("튜플 tp의 세번째 요소:", tp[2])

# tp = (101, 102, 'one', 'two')
# print("튜플 tp의 3번째부터 마지막요소까지 출력:", tp[2:])
# print("튜플 tp의 2번째 요소 출력:", tp[1:2])

# tp = (101, 102)
# tp2 = ('one', 'two')
# print("튜블끼리 더하기 연산 결과:", tp + tp2)

# tp = ('space', 'zone')
# print("튜플에 곱하기 2 연산한 결과:", tp * 2)
# tp = ('Good',)
# print("튜플에 곱하기 5 연산한 결과:", tp * 5)




# ---------------------------
# 집합형 데이터 타입 예제 소스
# ---------------------------

a = {101:'smart'}
a[201] = 'graphic'
print("딕셔너리 a 출력:", a)
a['id'] = 'cskisa'
print("딕셔너리 a 출력:", a)
a['one'] = [101, 102, 103]
print("딕셔너리 a 출력:", a)

print("딕셔너리 a 삭제 전 출력:", a)
del a['one']
print("키 one을 가진 쌍 삭제:", a)
del a[201]
print("키 201을 가진 쌍 삭제:", a)

print("딕셔너리 a에서 요소 추출전 출력:", a)
print("키가 id인 값 출력:", a['id'])
print("키가 id인 값 출력:", a[101])

a = {101:'space', 101:'zone'}
print("중복된 키 101을 만든 결과:", a[101])
print("중복된 키 101을 만든 결과:", a)

# a = {[1,2]:'space'}
# print("에러발생:", a)
a = {(1,2):'speed'}
print("a(1,2) 키를 이용해 값 출력:", a[(1,2)])

a = {'id':'jwkim', 'pw':945018, 'email':'gomwoong0619@naver.com'}
print("딕셔너리 a의 키 모두 출력:", a.keys())
print("딕셔너리 a의 키를 리스트로 모두 출력:", list(a.keys()))

print("딕셔너리 a의 값 모두 출력:", a.values())
print("딕셔너리 a의 값을 리스트로 모두 출력:", list(a.values()))

print("딕셔너리의 키,값을 쌍으로 출력:", a.items())
print("딕셔너리의 키,값을 리스트로 출력:", list(a.items()))

print("딕셔너리의 키 'id'로 값 출력하기", a.get('id'))
print("딕셔너리의 키 'pw'로 값 출력하기", a.get('pw'))
# print("딕셔너리에 없는 키로 값 찾을 경우 에러발생", a.get('name'))
print("get 함수의 에러를 방지하는 방법:", a.get('name', 'non-name'))

print("키 'name'이 딕셔너리 a에 있는지 여부:", 'name' in a)
print("키 'pw'가 딕셔너리 a에 있는지 여부:", 'pw' in a)

a.clear()
print("clear 함수 호출 후 딕셔너리 a 출력:", a)








# s1 = set([1, 'two', 3])
# print("집합 s1 출력:", s1)
# s2 = set(['one', 2, 'three'])
# print("집합 s2 출력:", s2)

# s3 = set('speed')
# print("집합 s3 출력:", s3)

# s1 = set([1, 'two', 3])
# s2 = set(['one', 'two', 'three', 4, 5])
# print("집합 s1과 s2의 교집합 결과:", s1&s2)

# print("집합 s1과 s2의 합집합 결과:", s1|s2)

# print("집합 s1에서 s2의 차집합 결과:", s1-s2)
# print("집합 s2에서 s1의 차집합 결과:", s2-s1)
# print("집합 s1에서 s2의 차집합 결과:", s1.difference(s2))
# print("집합 s2에서 s1의 차집합 결과:", s2.difference(s1))

# sd = set([101, 102, 103])
# sd.add(105)
# print("집합 sd에 원소를 추가하고 출력:", sd)

# sd = set([201, 203, 205])
# sd.update([202, 204])
# print("집합 sd에 여러 원소를 추가하고 출력:", sd)

# sd = set([501, 502, 503])
# sd.remove(502)
# print("집합 sd에서 502 요소를 삭제하고 출력:", sd)