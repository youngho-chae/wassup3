import random
print('======Lotto 1등 가즈앙!!======')
def 로또_번호생성():
    return random.sample(range(1, 46), 6)

for i in range(5):
    번호생성 = 로또_번호생성()
    print(f"Set {i + 1}: {번호생성}")
print('~'*30)
print('======연금 1등 가즈앙!!======')
import random
def 연금_번호생성():
    return random.sample(range(0, 10), 6)
연금번호 = 연금_번호생성()
print(f"각조 : {연금번호}")
print('='*30)
print('~.~ 1등 당첨 기원 ~.~')