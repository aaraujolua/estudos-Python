class BankAccount:
    def __init__ (self, holder, type, agency, account, balance):
        self.holder = holder
        self.type = type
        self.agency = agency
        self.account = account
        self.__balance = balance
        
    def showDataAccount(self):
        print(f'Account holder: {self.holder}')
        print(f'Account type: {self.type}') 
        print(f'Agency: {self.agency}')
        print(f'Account: {self.account}')
        print(f'Balance: ${self.__balance} \n')
        
    def withdraw(self, value):
        if self.__balance < value:
            print("Sorry, you don't have enough balance to make this operation.")
        else:
            self.__balance -= value
            print(f'{self.holder} withdrawal made successfully! Your current balance is ${self.__balance} \n')
            
    def deposit(self, value):
        self.balance += value
        print(f'{self.holder} deposit made successfully! Your current balance is ${self.__balance} \n')
        
        
        

if __name__ == '__main__':
    luana_account = BankAccount("Luana", "Current", "0001", 102030, 300000)
    james_account = BankAccount("James", "Savings", "0001", 203040, 200000)
    
    print(luana_account.type)
    james_account.showDataAccount()
    luana_account.showDataAccount()
    
    value_withdrawn = float(input('Enter the value you want to withdraw: '))
    luana_account.withdraw(value_withdrawn)
    
    value_deposit = float(input('Enter the value you want to deposit: '))
    luana_account.deposit(value_deposit)
    
    
    