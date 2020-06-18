"""
Hangman game advance version
"""

import random

class Hangman():

    #setting up the original scene of hang env
    hang_env = []
    hang_env.append(' #-----#')
    hang_env.append(' |     |')
    hang_env.append('       |')
    hang_env.append('       |')
    hang_env.append('       |')
    hang_env.append('       |')
    hang_env.append('       |')
    hang_env.append('=========')

    #initialize man (total user can miss 6 times )
    man_stage = {}
    man_stage[0] = [' 0     |'] #miss one time
    man_stage[1] = [' 0     |',' |     |'] #miss two times
    man_stage[2] = [' 0     |','/|     |'] #miss three times 
    man_stage[3] = [' 0     |','/|\    |'] #miss four times 
    man_stage[4] = [' 0     |','/|\    |','/      |'] #miss five times 
    man_stage[5] = [' 0     |','/|\    |','/ \    |'] #miss six times   

    picture = []
    words = ['apple','banana','coconut','pear']
    ans = None
    userguesslist_wrong = []
    userguresslsit_correct = []
    display  = []

    #combine environment(stage) setting with error times(man stage) together
    def __init__(self):
        self.picture.append(self.hang_env[:])#append default hang_env setting list into picture
        for errortimes in self.man_stage.values():
            # print (errortimes)
            tmpenv, enterenvindex = self.hang_env[:], 2
            for errortype in errortimes:
                tmpenv[enterenvindex] = errortype
                enterenvindex += 1
            self.picture.append(tmpenv)
    
    #create pick word function that will randomly select word from words put into list and divided into letters 
    def pickword(self):
        self.ans = list(self.words[random.randint(0,len(self.words)-1)])
        return self.ans
    
    def printpicture(self, index):
        for line in self.picture[index]:
            print(line)
    #set the letter in ans to "_" symbol
    def setdisplay(self,ans):
        self.display.extend(self.ans)
        for i in range (0,len(self.display)):
            self.display[i] = '_'
        return self.display
    #ask for user to input letter and check if the letter is valid
    def enterandevaluate(self):
        guess = input()
        
        #The input is not meet the format of the answer or is already guessed before
        if guess == None or len(guess) != 1 or guess in self.userguesslist_wrong or guess in self.userguresslsit_correct:
            return None,False
        #return True or False from checking if the input letter is in the answer
        #to use in caculate miss_counter
        right = guess in self.ans 
        # users did not guess right
        if guess not in self.ans:    
            self.userguesslist_wrong.append(guess)
        if guess in self.ans:
            self.userguresslsit_correct.append(guess)
            for i in range(len(self.ans)):
                if self.ans[i] == guess:
                    self.display[i] = guess
        
        return guess,right
    #main function that will execute the game
    def startgame(self):
        print ("welcome to hangman game!")
        answer = self.pickword()
        default_display = self.setdisplay(answer)#
        print('The word is: ', default_display)
        miss_counter = 0
        success = False 
        while miss_counter < len(self.picture)-1:
            print("please guess a letter")
            print(len(self.picture))
            print(self.picture)
            userguess,right = self.enterandevaluate() 
            if userguess == None:
                print ('please try another letter')
                continue   
            if default_display == answer:
                print ("you save a life")
                success = True 
                break
            if not right:
                miss_counter+=1
            
            self.printpicture(miss_counter)
            print (" ".join(default_display))
            print ('missed characters', self.userguesslist_wrong)
            

        if not success:
            print ('The word was \''+''.join(answer)+'\' ! You\'ve just killed a man, yo !')
#testing env             
a = Hangman().startgame()