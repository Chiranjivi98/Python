from random import randint

class Sports:

        def __init__(self,matches,player1score,player2score):

                self.matches=matches

                self.player1score=player1score

                self.player2score=player2score

                

        def match(self):

                self.m=int(input('Number of matches you want to play ='))

                while self.matches<self.m+1:

                        print('Match number=>',self.matches)

                        self.i=randint(1,100)

                        if self.i<50:

                                self.player1score=self.player1score+6

                                print('Player 1 won and scored=>',self.player1score)

                                

                        else:

                                self.player2score=self.player2score+6

                                print('Player 2 won and scored=>',self.player2score)

                                

                        self.matches=self.matches+1

                print('Match Finished')

                        

    

        def result(self):

                print('The Final total is given below:-')

                if self.player1score>self.player2score:

                        print('Player 1 won with points=',self.player1score)

                else:

                        print('Player 2 won with points=',self.player2score)

                

                

def xyz():

        s=Sports(1,1,1)

        s.match()

        s.result()
