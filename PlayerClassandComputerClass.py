from BlackJackCardAndDeckClasses import Card
from BlackJackCardAndDeckClasses import Deck

class Player(Card):

    def __init__(self,name,bankaccount,plistofcards=[]):

        self.name = name
        self.bankaccount = bankaccount
        self.plistofcards = []

    def betmoney(self):
        print(f"You have {self.bankaccount} in the bank currently")
        betamount = int(input("Enter how much would you like to bet: "))
        self.bankaccount-=betamount
        print(f"You now have {self.bankaccount} in the bank since you bet {betamount}")
        return betamount

    def depositmoney(self,depositamount):
        self.bankaccount+=depositamount
        return self.bankaccount

    def addrandomcard(self,addacard):
        self.plistofcards.append(addacard)

    def ptotalrank(self):
        ignorelist = []
        for i in self.plistofcards:
            ignorelist.append(i.rank)

        return sum(ignorelist)
        

class Computer(Card):

    def __init__(self):

        self.clistofcards = []
        self.hiddenlist = []
        
    def addrandomcard(self,addacard):
        self.clistofcards.append(addacard)
    
    def ctotalrank(self):
        ignorelist = []
        for i in self.clistofcards:
            ignorelist.append(i.rank)

        return sum(ignorelist)
