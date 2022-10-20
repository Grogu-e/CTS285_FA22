# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:23:57 2022

@author: anacs
"""

#DataMan _ui --user interface for project
import Program as logic
import random
import re
#import dataman_logic as logic
#import dataman_data as data


class Dataman_UI:
    def __init__(self):
        
        self.logic = logic.Dataman_Logic()
        self.data = logic.Dataman_Data()
    
    def displayMenu(self):
        
        print("Dataman Main Menu")
        print("1.Answer Checker")
        print("2.Memory Bank Pending")
        print("3.Number Guesser Pending")
        print("5.Exit")
    
    def menu(self):
        
        QUIT_CHOICE = 5
        choice = 0
        
        while choice != QUIT_CHOICE: 
            
            self.displayMenu()
            
            choice = int(input("Make A Selection: "))
            if choice == 5: # Exit
                return False # UI is finished
            if choice == 1 :
                self.answerChecker()
            elif choice == 2 :
                self.MemoryBankMenu()
            else:
                print("Please make another selection.")
                return True 
    
    
    #Anwer Checker Function
    def answerChecker(self):
        #Show player the format of the problem
        print("Format is: 1 + 2 = 3")
        issueBreed = input("Enter math problem: ")
        issuesBits = issueBreed.split(" ")
        
        
        numberOne = int(issuesBits[0])
        operator = issuesBits[1]
        numberTwo = issuesBits[2]
        responsed = int(issuesBits[4])
        issue = logic.Issue(numberOne,operator, numberTwo,responsed)
        
        
        if(operator == "+"):
            realAnswer = int(numberOne) + int( numberTwo)
            if(realAnswer == responsed):
                print("Your problem was: ", str(issue))
                print("This is correct!")
            elif(realAnswer != responsed):
                print("Your problem was incorrect: ", str(issue))
            #1if operator 
                print("The correct answer is: ", realAnswer)
        elif(operator == "-"):
            realAnswer = int(numberOne) - int( numberTwo)
            if(realAnswer == responsed):
                print("Your problem was: ", str(issue))
                print("This is correct!")
            elif(realAnswer != responsed):
                print("Your problem was incorrect: ", str(issue))
                print("The correct answer is: ", realAnswer)
        elif(operator == "*"):
            realAnswer = int(numberOne) * int( numberTwo)
            if(realAnswer == responsed):
                print("Your problem was: ", str(issue))
                print("This is correct!")
            elif(realAnswer != responsed):
                print("Your problem was incorrect: ", str(issue))
                print("The correct answer is: ", realAnswer)
        elif(operator == "/"):
            realAnswer = int(numberOne) / int( numberTwo)
            if(realAnswer == responsed):
                print("Your problem was: ", str(issue))
                print("This is correct!")
            elif(realAnswer != responsed):
                print("Your problem was incorrect: ", str(issue))
                print("The correct answer is: ", realAnswer)
        else:
            print("Not a valid input.")
            
    #Get input from user to continue or end the game
    def ContinueGame(self,contLoop,checkLoop):
        while contLoop == False:
            cont = input("Continue Y/N -->")
            if cont.lower() == "y":
                contLoop = True
                print("")
            elif cont.lower() == "n":
                return False
            else:
                print("Invalid Input!")
    
    
    # Memory Bank Menue Fucntion--     
    def MemoryBankMenu(self):
        
        menuLoop = False #Declare and initialize game memu sentinel

        while menuLoop == False: #Continues loop until boolean equals true
          #Display functional menu to user
          print("1. Play Memory Bank")
          print("2. Add Problems to Memory")
          print("3. Clear Memory Bank")
          choice = input("Select from the Menu --> ") #Get input from user
          if choice == "1":
              self.PlayMemoryBank() #Execute function (Play memory bank game)
          elif choice == "2":
                self.AddToBank() #Execute function (Add to gamebank file)          
          elif choice == "3":
                self.ClearBank() #Execute function (Clear gamebank file)           
          elif choice == "4":
                menuLoop = True
        else:
            print("Invalid Selction!")

    #play memory bank game function------------------
    def PlayMemoryBank(self):
        #Read from text doc bank and display to user
        #Store what was read from the doc in list
        #perform calculations to determine answer and store in variable
        #Get input from the user to verify input to the answer
        #Display to user if the answer is correct or not
        auth_operators={
            "+": self.logic.operator.add,
            "-": self.logic.operator.sub,
            "*": self.logic.operator.mul,
            "/": self.logic.operator.truediv}
        count =0
        score = 0

        #Count number of lines in GameBank file to ensure math problems exist
        with open("GameBank.txt", mode="r") as gameFile:              
            for count, line in enumerate(gameFile):    
                
                pass    
        
        if count + 1 > 0:  
            with open("GameBank.txt", mode="r") as gameFile:
                #gameDoc = gameFile.readline()
             
                count +=1
                while count != 0:                    
                        problem = gameFile.readline()#Read each line in text document                   
                        problem = ''.join(problem.split())#Join string at locations that are white space
                        letter = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list

                        print(letter)#THIS IS FOR DEBUGGING PURPOSES ONLY. WILL BE REMOVED WHEN ALL BUGS ARE FIXED.
                        #Declare and initialize variables with appropriate subscipt
                        num1 = int(letter[0])
                        num2 = int(letter[2])
                        operator = (letter[1])

                        #totalFromDoc = int(letter[4])
                        total = auth_operators[operator](num1,num2)#Calculate total
                        print(total)#THIS IS FOR DEBUGGING PURPOSES ONLY. WILL BE REMOVED WHEN ALL BUGS ARE FIXED.
                        answer = input(f"{num1} {operator} {num2} = ?  ")#Get input from user

                        if answer == str(total):#Verify answer is correct or incorrect
                            print("Great Job!")
                            score += 1
                        else:
                            print("Sorry! Incorrect Answer.")
                            count -= 1  

                        print(f"\n*****GAMEOVER*****\n\nPLAYER SCORE: {score}\n\n******************\n")#Display players score when game is finished
                        gameFile.close()
        else:
            print("Memory Bank Empty...")#Display if file is empty
            gameFile.close()#Close file

        #ADD TO GAMEBANK FILE FUNCTION----------------------------------------------------------------------------------------------
    def AddToBank(self):
        count = 0
        #Get admin authentication by verifying password from txt doc
        #Get admin to enter problems and use the split/join and regex function to create proper format
        #Write to txt doc

        #Get user to input admin password and verify that the inputted password matches the stored admin password in doc.
        password = input("Enter Admin Password --> ")
        with open("DatamanPassword.txt",mode = "r") as readDoc:
            #adminPass = readDoc.readline()
            password2 = readDoc.readline()
        readDoc.close()
    
        #Allow user to write to document if password matches admin password
        if password == password2:            
            with open("GameBank.txt", mode="r") as gameFile:              
                for count, line in enumerate(gameFile):    
                
                    pass
            #Determines if lines are equal to zero. If lines are equal to zero a new document or current document is refreshed/cleared
            #Condition statement to determine if there is space available to add math problems to document
            if count + 1 == 0:
                problem = input("Enter Problem --> ")#Get user to enter problem to store in document
                problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
             
                if self.VerifyMemoryBankProblem(problem) == True:#Verifies that inputted problem is indeed a correct problem (ex. 1+1=2)
                    with open("GameBank.txt", mode = "w") as gameFile:
                        gameFile.write(problem)#Writes problem to document
                        print("Problem Added Successfully")
                        gameFile.close()
                else:
                    self.DisplayMemoryBankInputError()
       #If lines are greater than 1 and less than 10. Allow user to enter/add a new problem
        elif count +1 < 10 and count +1 > 0:
            print("Format should be 4 + 4 = 8")
            print("Can use +, -, *, or / ")
            problem = input("Enter Problem --> ")
            problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
            if self.VerifyMemoryBankProblem(problem) == True:#Verifies that inputted problem is indeed a correct problem (ex. 1+1=2)
                with open("GameBank.txt", mode = "a") as gameFile:
                     gameFile.write(f"\n{problem}")#Writes problem to document
                     print("Problem Added Successfully")
                     gameFile.close()
            else:
                self.DisplayMemoryBankInputError()#Displays error to user
                gameFile.close()
        elif count == 10:#If count is equal to 10 display memory bank full to user
            print("Memory Bank Full! Clear bank!")   
            gameFile.close()        
        else:
           print("Invalid Password!")

     #CLEAR GAMEBANK FILE FUNCTION----------------------------------------------------------------------------------------------       
    def ClearBank(self):
         #Clear txt doc
         password = input("Enter Admin Password --> ")
         with open("DatamanPass.txt",mode = "r") as readDoc:
             #adminPass = readDoc.readline()
             password2 = readDoc.readline()
         readDoc.close()
         if password == password2: 
                with open("GameBank.txt", mode = "w") as f:#Opens gamebank document and overwrites and clears the document
                     pass
                print("Memory Bank Cleared....")
    
    
    
    
    def VerifyMemoryBankProblem(self,problem):
        auth_operators={
            "+": logic.operator.add,
            "-": logic.operator.sub,
            "*": logic.operator.mul,
            "/": logic.operator.truediv}
    
        subscriptDivide = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list
        total=0
        if self.CheckCharArrayForSpecificCharacters(subscriptDivide) == True:
            num1 = int(subscriptDivide[0])
            num2 = int(subscriptDivide[2])
            operator = subscriptDivide[1]
            usersInputTotal = int(subscriptDivide[4])

            total = auth_operators[operator](num1,num2)
         
            if total == usersInputTotal:
                return True
            else:
               return False
        else:       
           return False

    
    
    
    
    
    def GuessNumberMenu():
        #Display guess number menu to user
        print("Number Guesser\n"+
              "1. 1-10\n"+
              "2. 1-20\n"+
             "3. 1-50\n"+
             "4. 1-100\n"+
             "5. Exit\n")
    
    def GuessNumber(self):  
     
       menuLoop = False

       while menuLoop == False:
            #Display functional menu to user
            self.GuessNumberMenu()
            choice = input("Select from the Menu --> ")
            if choice == "1":
                self.GuessTheNumber(1,10)#Random number 1-10           
            elif choice == "2":
                self.GuessTheNumber(1,20)#Random number 1-20  
             
            elif choice == "3":
                self.GuessTheNumber(1,50)#Random number 1-30  
            elif choice == "4":
                self.GuessTheNumber(1,100)#Random number 1-100
            elif choice == "5":
                menuLoop = True
            else:
                print("Invalid Selction!")
     


    def GuessTheNumber(self,num1,num2):
        increment = 0
        loop = False
        randNum = random.randint(num1,num2)
        correctNum = str(randNum)
        print(correctNum)
        while loop == False:
            userInput = input("Guess a number between " + str(num1) + " and " + str(num2) + " --> ")
            if userInput == correctNum:
                print("\n*************\nGreat Job!\n\n*************\n")
                loop = True
            elif increment > 1:
                print("You ran out of chances! The random number was: ", correctNum, "\n")
                loop = True
            elif userInput != correctNum:
                if int(userInput) > int(correctNum):
                    print("To High! Try a lower number.\n")
                elif int(userInput) < int(correctNum):
                    print("To Low! Try a higher number.\n")
                    #print("Try Again!")
                    increment += 1
         
        
            else:
                print("Invalid Input!")    
                
                
                
                
                
                

# just set up and launch the UI 

def main():
    app = Dataman_UI()
    app.menu()
        
        
if __name__ == "__main__":
    main()