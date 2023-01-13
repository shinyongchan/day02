#chap 4 : if

limits = 20
tweets = 'pass'*6
diff =limits-len(tweets)
#if diff := limits-len(tweets) >=0:
if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)} 초과 ')

a = []
vowels = 'aeiou'
letter = 'x'
if letter not in vowels:
    print("실행 안됨!")

print(bool(a))
a.append(5)
print(bool(a))
print(bool(set()))
print(bool(dict()))