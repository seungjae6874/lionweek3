class Bank():

   #Main은 구성 기능 입력창 1.계좌 개설 2. 입금하기 3. 출금하기 4. 프로그램 종료
    account_list = {} #가지고 있는 계좌와 금액 리스
    #메인
    def main(self):
        print("\n=======메뉴=======")
        print("1. 계좌 개설\n2. 입금하기\n3. 출금하기\n4. 계좌조회\n5. 프로그램 종료")
        print("===================")
        first = int(input("입력: "))
        return first

    def make_account(self):
        
        #계좌번호 정수만 입력
        print("\n계좌 개설을 선택하셨습니다.\n")
        account_num = input("계좌번호 생성 : ") #계좌는 str
        self.account_list[account_num] = 0
        
    def manage(self): #잔액 조회
        print("계좌 목록: ", self.account_list)

        
    def deposit(self):
        #계좌를 입력받고
        #해당 계좌에 돈을 입금 해당 계좌 : +=금액
        print("입금을 선택하셨습니다.")
        checkaccount = input("계좌번호를 입력: ")
        if checkaccount in self.account_list.keys():
            balance = int(input("입금 금액 입력: "))
            #money = self.account_list[checkaccount]+balance
            self.account_list[checkaccount] += balance
            print('\n계좌 :',checkaccount, " 잔액 : ",self.account_list[checkaccount])
        else:
            print(self.account_list)
            print("해당 계좌가 존재하지 않습니다.")

    def withdraw(self):
        #계좌를 입력받고
        #해당 계좌에서 출금할 금액 입력 -= 금액
        #만약 출금 금액이 잔액보다 크면 불가
        print("출금을 선택하셨습니다.")
        checkaccount = input("계좌번호 입력: ")
        if checkaccount in self.account_list.keys():
            withdraw = int(input("출금 금액 입력: "))
            if withdraw > self.account_list[checkaccount]: #출금 초과
                print("잔액 부족")
            else:
                self.account_list[checkaccount] -= withdraw
                print("잔액 " , self.account_list[checkaccount])
        else:
            print("해당 계좌가 존재하지 않습니다.")
        

menu = 0
while True:
    person = Bank()
    menu = person.main()
    if menu == 5: #5번 프로그램종료 입력시 종료
        print("프로그램을 종료합니다.")
        break
    elif menu == 1: #계좌 생성
        person.make_account()
        person.manage()
    elif menu == 2: #입금
        person.deposit()
    elif menu == 3: #출금
        person.withdraw()
    elif menu == 4: #계좌 조회
        person.manage()
