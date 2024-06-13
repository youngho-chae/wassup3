contacts = {}

while True:
    print("\n기능을 선택하세요:")
    print("1: 연락처 추가")
    print("2: 연락처 전체 보기")
    print("3: 검색")
    print("4: 수정")
    print("5: 삭제")
    print("6: 프로그램 종료")
    choice = input("선택: ")

    if choice == '1':
        name = input("이름: ")
        num = input("전화번호: ")
        contacts[name] = num
        print(f'연락처 추가: {name} : {num}')
    
    elif choice == '2':
        if contacts:
            for name, num in contacts.items():
                print(f'이름: {name}, 전화번호: {num}')
        else:
            print('연락처가 없습니다.')
    
    elif choice == '3':
        name = input('이름: ')
        num = contacts.get(name)
        if num:
            print(f'{name}의 전화번호는 {num}입니다.')
        else:
            print(f'{name}의 전화번호가 없습니다.')
    
    elif choice == '4':
        name = input('이름: ')
        if name in contacts:
            num = input(f'{name}의 수정할 번호: ')
            contacts.update({name: num})
            print(f'{name}의 연락처가 수정되었습니다.')
        else:
            print(f'{name}의 전화번호가 없습니다.')
    
    elif choice == '5':
        name = input('이름: ')
        if name in contacts:
            del contacts[name]
            print(f'{name}의 연락처가 삭제되었습니다.')
        else:
            print(f'{name}의 전화번호가 없습니다.')
    
    elif choice == '6':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("다시 입력하세요.")
