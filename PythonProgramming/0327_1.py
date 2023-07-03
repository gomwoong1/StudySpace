##연산자의 우선순위와 종류1##
##산술연산자##
p_a = 7;p_b = 3
print("p_a + p_b의 결과값 :", p_a+p_b)
print("p_a - p_b의 결과값 :", p_a-p_b)
print("p_a * p_b의 결과값 :", p_a*p_b)
print("p_a / p_b의 결과값 :", p_a/p_b)
print("p_a // p_b의 결과값 :", p_a//p_b)
print("p_a % p_b의 결과값 :", p_a%p_b)
print("p_a ** p_b의 결과값 :", p_a**p_b)

##대입연산자##
p_a = 10; print("p_a = 10의 결과값 :", p_a)

p_a=10; p_a += 5; print("p_a += 5의 결과값 :", p_a)

p_a=10; p_a -= 5; print("p_a -= 5의 결과값 :", p_a)

p_a=10; p_a *= 5; print("p_a *= 5의 결과값 :", p_a)

p_a=10; p_a /= 5; print("p_a /= 5의 결과값 :", p_a)

p_a=10; p_a //= 5; print("p_a //= 5의 결과값 :", p_a)

p_a=10; p_a %= 5; print("p_a %= 5의 결과값 :", p_a)

p_a=10; p_a **= 5; print("p_a **= 5의 결과값 :", p_a)

##관계연산자##
p_a = 10
p_b = 20
print("p_a==p_b의 결과값 : ", p_a==p_b)
print("p_a!=p_b의 결과값 : ", p_a!=p_b)
print(" p_a<p_b의 결과값 : ", p_a<p_b)
print(" p_a>p_b의 결과값 : ", p_a>p_b)
print("p_a<=p_b의 결과값 : ", p_a<=p_b)
print("p_a>=p_b의 결과값 : ", p_a>=p_b)

##논리연산자##
p_a=10; p_b=20; 
print("(p_a==p_b)의 결과값 and (p_a<p_b)의 결과값 : ", (p_a==p_b) and (p_a<p_b))
print("(p_a==p_b)의 결과값 or (p_a<p_b)의 결과값 : ", (p_a==p_b) or (p_a<p_b))
print("not (p_a==p_b)의 결과값 : ", not (p_a==p_b))


##비트연산자##
p_a=3; p_b=2
print("(p_a&p_b)의 결과값 : ", (p_a&p_b))
print("(p_a|p_b)의 결과값 : ", (p_a|p_b))
print("(p_a^p_b)의 결과값 : ", (p_a^p_b))
print("(~p_a)의 결과값 : ", (~p_a))
print("(p_a<<p_b)의 결과값 : ", (p_a<<p_b))
print("(p_a>>p_b)의 결과값 : ", (p_a>>p_b))