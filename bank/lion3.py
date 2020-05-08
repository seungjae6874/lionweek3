from bank_account import *

class Bank(Transfer):
    
    #Main은 구성 기능 입력창 1.계좌 개설 2. 입금하기 3. 출금하기 4. 프로그램 종료

    #메인
    def main(self):
        try:
            print("\n======Bank Menu=====")
            print("1. 계좌개설\n2. 입금하기\n3. 출금하기\n4. 전체조회\n5. 계좌이체\n6. 프로그램 종료")
            print("====================")
            first = int(input("입력: "))
            return first

        except:
            print("===잘못된 입력입니다.===")

menu = 0
while True:
    person = Bank()
    menu = person.main()
    if menu == 6: #5번 프로그램종료 입력시 종료
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
    elif menu == 5:
        person.bank_transfer()
        
