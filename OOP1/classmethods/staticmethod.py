class Account:



    @staticmethod
    def cal_interest(p,r,t):
        return p*r*t/100

print(Account.cal_interest(100000,2,3))