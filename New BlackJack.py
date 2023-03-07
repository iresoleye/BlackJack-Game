from BlackJackCardAndDeckClasses import Card
from BlackJackCardAndDeckClasses import Deck
from PlayerClassandComputerClass import Player
from PlayerClassandComputerClass import Computer

##name = input("What is your name")
##bankaccount = int(input("How much money do you have in the bank"))

#You will need to ask for name and bank account prior like above, but it must be like inputs!
d = "saki"
def gameplay():
    #Why,everytime I re run the function,without the redo function, does it seem to remember the previous number of cards
    name = input("What is your name")
    bankaccount = int(input("How much money do you have in the bank"))
    

    s = True
    while s:
        d = Deck()
        p = Player(name,bankaccount)

            
        print(len(d.deckofcards))
        amountplayerbets = p.betmoney()
        print("\n ")

        c = Computer()
        #Draw Two Random Cards for Computer
        c.addrandomcard(d.collectrandomcard())
        c.addrandomcard(d.collectrandomcard())

        #Create the hidden list. Each item in the list must display the name of the card.
        #Without having the '.name' function, the item would just be a card class*
        c.hiddenlist.append(f"{c.clistofcards[0].name} ({c.clistofcards[0].rank})")
        c.hiddenlist.append("Hidden Card")

        #Create a computer display list that's a function of the computer's list of cards
        cdisplaylist = [f"{c.clistofcards[0].name} ({c.clistofcards[0].rank})",f"{c.clistofcards[1].name} ({c.clistofcards[1].rank})"]
        print("The computer has now drawn two cards. Here they partially are: ")
        print(c.hiddenlist)
    ##  print(f"Also, here is the real list which I am displaying as a test {cdisplaylist}")
    ##  print(len(d.deckofcards))


        #Draw Two Random Cards for Player
        p.addrandomcard(d.collectrandomcard())
        p.addrandomcard(d.collectrandomcard())
        print("...\n \n... \n \n... \n ")

        #Create a player display list that's a function of the player's list of cards
        pdisplaylist = [f"{p.plistofcards[0].name} ({p.plistofcards[0].rank})",f"{p.plistofcards[1].name} ({p.plistofcards[1].rank})"]
        print(f"{p.name}, you have now drawn two cards. Here they are: ")
        print(pdisplaylist)
        print(f"Here is your total rank: {p.ptotalrank()}")
        #print(len(d.deckofcards))


        pfinalrank = p.ptotalrank()

    #Player Turn - Take the player through a loop of stands and hits
        if p.ptotalrank()==21:
            #Potentially add code here that stops computer even having a turn?
            playergametime = False
            print("Jackpot already!!")
        elif p.ptotalrank()==11 and (p.plistofcards[0].rank==1 or p.plistofcards[1].rank==1):
            print("Jackpot via initial Ace!")
            pfinalrank = p.ptotalrank()+10
            playergametime = False
        elif p.ptotalrank()<11 and (p.plistofcards[0].rank==1 or p.plistofcards[1].rank==1):
            q = True
            while q:
                w = int(input(f"You have 2 choices.\nChoice 1: Your total becomes {p.ptotalrank()}\nChoice 2: Your total becomes {p.ptotalrank()+10}\n \nEnter '1' for Choice 1 and '2' for Choice '2'"))
                if w == 1:
                    pfinalrank = p.ptotalrank()
                    q = False
                elif w == 2:
                    pfinalrank = p.ptotalrank()+10
                    q = False
                else:
                    print("Invalid input! Try again\n ")

            playergametime = True    
        else:
            playergametime = True
        
        print("\n ")
        plistofranks = []
        for i in p.plistofcards:
            plistofranks.append(i.rank)
        print(f"Here are your list of ranks so far:{plistofranks}")

        clistofranks = []
        for i in c.clistofcards:
            clistofranks.append(i.rank)

        
        while playergametime:
            if pfinalrank==21:
                playergametime = False
            else:
                print("\n ")
                print(f"This is your total rank so far - {pfinalrank}")
                decision = input("Would you like to stand or hit? \nEnter 'S' for stand and 'H' for hit")
                

                if decision.capitalize()=='S':
                    playergametime = False
                    
                elif decision.capitalize()=='H':
                    p.addrandomcard(d.collectrandomcard())
                    plistofranks.append(p.plistofcards[-1].rank)
                    print(f"Here are your list of ranks: {plistofranks}")
                    
                    if p.ptotalrank()>21:
                        print("\n ")
                        print("You've gone BUST!")
                        pfinalrank = p.ptotalrank()
                        playergametime = False

                    elif p.ptotalrank()==21:
                        print("\n ")
                        print("JACKPOT!!!")
                        pfinalrank = p.ptotalrank()
                        playergametime = False

                    elif (1 in plistofranks) and (p.ptotalrank()+10==21):
                        print("\n ")
                        print("JACKPOT!!!")
                        pfinalrank = p.ptotalrank()+10
                        playergametime = False
                    elif (1 in plistofranks) and (p.ptotalrank()+10<=21):
                        j = True
                        while j:
                            t = int(input(f"You have 2 choices.\nChoice 1: Your total becomes {p.ptotalrank()}\nChoice 2: Your total becomes {p.ptotalrank()+10}\n \nEnter '1' for Choice 1 and '2' for Choice '2'"))
                            if t == 1:
                                pfinalrank = p.ptotalrank()
                                j = False
                                print("\n ")
                            elif t == 2:
                                pfinalrank = p.ptotalrank()+10
                                print("\n ")
                                j = False
                            else:
                                print("Invalid input! Try again\n ")
                    else:
                        pfinalrank = p.ptotalrank()
                        

                else:
                    print("You did not enter a valid output lol \n")

        #print(f"This is the ptotal rank - {p.ptotalrank()}")
        print(f"This is the final rank - {pfinalrank}")
        #print(len(d.deckofcards))
        print("\n \n \n")
        print(f"This is the computer's full list:\n{cdisplaylist}")
        print(f"This is the computer's total rank:\n{c.ctotalrank()}")
        print("\n ")
    
        #Computer Turn
        if pfinalrank ==21 and ((c.ctotalrank()==11 and (c.clistofcards[0].rank==1 or c.clistofcards[1].rank==1))):
            print("Both the player and the computer got 21, so its a DRAW")
            print(f"Your final rank is: {pfinalrank}")
            print(f"This is the computer's final rank: {c.ctotalrank()+10}")
                            
        elif pfinalrank ==21:
            print("You won!")

        elif ((c.ctotalrank()==11 and (c.clistofcards[0].rank==1 or c.clistofcards[1].rank==1))):
            print("You lost. Apologies")
            print(f"Your final rank is: {pfinalrank}")
            print(f"This is the computer's final rank: {c.ctotalrank()+10}")

        elif pfinalrank>21:
            print("You've lost since you've gone BUST")

        elif c.ctotalrank()>pfinalrank:
            print("You lost")
            
        #this elif statement is here to make the game more interesting
        elif c.ctotalrank()==17:
            if c.ctotalrank()>pfinalrank:
                print("You lost")
            
            elif c.ctotalrank()==pfinalrank:
                print("You drew with the computer")
            else:
                print("You won")
                
            print(f"Your final rank  is - {pfinalrank}")
            print(f"This is the computer's final rank:\n{c.ctotalrank()}")    

        else:
            print("The computer will now start drawing cards")
            print("\n \n ")
            n = True
            #Need to sort out the Ace card situation.
            while n:
                c.addrandomcard(d.collectrandomcard())
                clistofranks.append(c.clistofcards[-1].rank)
                cdisplaylist.append(f"{c.clistofcards[-1].name} ({c.clistofcards[-1].rank})")
                if c.ctotalrank()>21:
                    print("After the computer has drawn another card, it appears that:")
                    print("You have won!")
                    print(f"This is the computer's final list:\n{cdisplaylist}")
                    print(f"Your final rank is: {pfinalrank}")
                    print(f"This is the computer's final rank: {c.ctotalrank()}")
                    n = False

                elif c.ctotalrank()==11 and (1 in clistofranks):
                    print("The computer got JACKPOT")
                    print(f"This is the computer's final list:\n{cdisplaylist}")
                    print(f"Your final rank is: {pfinalrank}")
                    print(f"This is the computer's final rank: {c.ctotalrank()+10}")
                    n = False
                
                #I added this extra elif statement to make the game more playable
                elif c.ctotalrank()==17:
                    n = False
                    if c.ctotalrank()>pfinalrank:
                        print("You lost!")
                    elif c.ctotalrank()==pfinalrank:
                        print("You drew with the computer")
                    else:
                        print("The computer has now drawn another card and based on this:")
                        print("You have won!")
                        print("\n \n \n ")
                        print(f"Your final rank is: {pfinalrank}")
                        print(f"This is the computer's final rank: {c.ctotalrank()}")
                        print(f"This is the computer's final list:\n{cdisplaylist}")

                elif(1 in clistofranks) and 16<c.ctotalrank()+10<22 and c.ctotalrank()>pfinalrank:
                    print("The computer has now drawn another card and based on this:")
                    print("You have lost!")
                    print("\n \n \n ")
                    print(f"This is the computer's final list:\n{cdisplaylist}")
                    print(f"Your final rank is: {pfinalrank}")
                    print(f"This is the computer's final rank: {c.ctotalrank()+10}")
                    n = False
                    
                    
                elif 16<c.ctotalrank()<22 and c.ctotalrank()>pfinalrank:
                    print("The computer has now drawn another card and based on this:")
                    print("You have lost!")
                    print("\n \n \n ")
                    print(f"This is the computer's final list:\n{cdisplaylist}")
                    print(f"Your final rank is: {pfinalrank}")
                    print(f"This is the computer's final rank: {c.ctotalrank()}")
                    n = False
                else:
                    print(f"After drawing another card,the computer's full list:\n{cdisplaylist}\n ")
                    print("\n \n \n ")


        print(len(d.deckofcards))
        e = True
        while e:
            k = input("Would you like to play another round?\nEnter Y or N.")
            if k.title()=='Y':
                e = False
                #d.redo()
                

            elif k.title()=='N':
                e = False
                s = False
                print("The game has ended mate")

            else:
                print("You did not enter a valid input.\n ")


        # The final ranks are still stored
        # Bank Account doesn't add to account or reduce account
        # Deck Amounts are still stored
        
    

                
        
        
    

    
