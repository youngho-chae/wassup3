import random

def 로또_번호생성():
    return random.sample(range(1, 46), 6)

for i in range(5):
    번호생성 = 로또_번호생성()
    print(f"Set {i + 1}: {번호생성}")
print('~.~ 1등 당첨 가즈앙!! ~.~')