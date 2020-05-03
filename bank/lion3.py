from bank_account import *

class Bank(Account):

    #Main은 구성 기능 입력창 1.계좌 개설 2. 입금하기 3. 출금하기 4. 프로그램 종료

    #메인
    def main(self):
        print("\n======Bank Menu=====")
        print("1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 프로그램 종료")
        print("====================")
        first = int(input("입력: "))
        return first

 

menu = 0
while True:
    person = Bank()
    menu = person.main()
    if menu == 5: #5번 프로그램종료 입력시 종료
        print("##프로그램을 종료합니다##")
        break
    elif menu == 1: #계좌 생성
        person.make_account()
    elif menu == 2: #입금
        person.deposit()
    elif menu == 3: #출금
        person.withdraw()
    elif menu == 4: #계좌 조회
        person.manage()
