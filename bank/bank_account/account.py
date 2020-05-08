class Account():
    account_list = {} #가지고 있는 계좌와 금액 리스트
    name_list = {}
    def make_account(self):
            
        #계좌번호 정수만 입력
        print("\n======계좌개설======\n")
        try:
            account_num = int(input("계좌번호: ")) #계좌는 str->int로 모두 수정
            if account_num < 0:
                raise NotImplementedError #계좌번호, 입금, 출금에서 전부 음수 입력X
            name = input("이름: ")
            if name.isdigit() == False: #이름에 숫자X
                self.name_list[account_num] = name
                try:
                    first_deposit = int(input("예금: "))
                    if first_deposit < 0:
                        raise NotImplementedError
                    self.account_list[account_num] = first_deposit
                    print("##계좌개설을 완료하였습니다##")
                    print("====================")
                except:
                    print("금액 입력이 올바르지 않습니다.")
            else:
                print("이름 입력이 올바르지 않습니다.")
        except:
            print("계좌번호 입력이 올바르지 않습니다.")
               
    def manage(self): #잔액 조회
        print("======전체조회======")
        for i in self.account_list :
            print("계좌번호:", i, "/ 이름:", self.name_list[i], "/ 잔액:", self.account_list[i], "원")
        print("====================")
            
    def deposit(self):
        #계좌를 입력받고
        #해당 계좌에 돈을 입금 해당 계좌 : +=금액
        print("======입금하기======")
        checkaccount = int(input("입금하실 계좌번호를 입력해주세요: "))
        if checkaccount in self.account_list.keys():
            print("계좌이름:", self.name_list[checkaccount])
            print("계좌잔고:", self.account_list[checkaccount], "원")
            balance = int(input("입금하실 금액을 입력해주세요: "))
            #money = self.account_list[checkaccount]+balance
            if balance >= 0:
                self.account_list[checkaccount] += balance
                print('\n##계좌잔고: ', self.account_list[checkaccount], "원##")
                print("##입금이 완료되었습니다##")
                print("====================")
            else:
                print("금액 입력이 올바르지 않습니다.") #음수 입력X
        else:
            print(self.account_list)
            print("해당 계좌가 존재하지 않습니다.")

    def withdraw(self):
        #계좌를 입력받고
        #해당 계좌에서 출금할 금액 입력 -= 금액
        #만약 출금 금액이 잔액보다 크면 불가
        print("======출금하기======")
        try:
            checkaccount = int(input("출금하실 계좌번호를 입력해주세요: "))
            if checkaccount in self.account_list.keys():
                print("계좌이름:", self.name_list[checkaccount])
                print("계좌잔고:", self.account_list[checkaccount], "원")
                withdraw = int(input("출금하실 금액을 입력해주세요: "))
                if withdraw > self.account_list[checkaccount]: #출금 초과
                    print("잔액 부족")
                elif withdraw < 0:
                    print("금액 입력이 올바르지 않습니다.") #음수 입력X
                else:
                    self.account_list[checkaccount] -= withdraw
                    print('\n##계좌잔고: ', self.account_list[checkaccount], "원##")
                    print("##출금이 완료되었습니다##")
                    print("====================")
            else:
                print("해당 계좌가 존재하지 않습니다.")
        except:
            print("\n===잘못된 계좌번호 입니다.===")
        
class Transfer(Account):
    findaccount = 0
    def bank_transfer(self):
        print("======계좌 이체=====")
        #내 계좌 선택
        try:
            sender = int(input("사용하실 계좌를 입력해주세요: "))
        except:
            print("잘못된 입력입니다.")
        for j in self.account_list:
            if j == sender:
                sendindex = j #보내는 사람의 계좌 인덱스
        if sender in self.account_list:
            try:
                getter = int(input("이체하실 계좌번호를 입력해주세요: "))                      
                for i in self.account_list:
                    if i == getter:
                        if getter == sender:
                            #보내는 계좌와 받는계좌가 같을 경우는 예외
                            print("받는 이가 보내는이와 동일한 계좌입니다.")
                            
                        else:
                            index = i #받는 사람의 계좌 인덱스

                
                if getter in self.account_list:
                    print("예금주: ",self.name_list[index],"가 맞습니까?")
                    check = input("Y/N: ")
                    if check == 'y' or check == 'Y': #일치
                        #입금 진행
                        money = int(input("입금 금액을 입력: "))
                        
                        #금액이 잔액보다 크면 잔액부족
                        if money > self.account_list[sender]:
                            print("잔액이 부족합니다.")
                        else:
                            #입금 처리, -> getter의 계좌에 money를 더해준다.
                            #sender의 계좌에서 money를 빼준다. -> sender의 잔액을 표시해준다.
                            # 예금주, 보낸금액, 보내는 계좌에 대한 출력 후 완료
                            self.account_list[index] = self.account_list[index] + money
                            self.account_list[sendindex] = self.account_list[sendindex] - money
                            print("받는 사람 : ",self.name_list[index])
                            print("출금 계좌 : ", sender)
                            print("이체 금액 :  ", self.account_list[sendindex],"원")
                            print('출금 계좌 잔액 : ', self.account_list[sendindex],"원")

                    elif check == 'n' or check == 'N':#불일치
                        print("거래가 취소되었습니다.")
                    else:
                        print("잘못된 입력입니다.")
                else:
                    print("존재하지 않는 계좌입니다.")
            except:
                print("잘못된 입력입니다.")
        