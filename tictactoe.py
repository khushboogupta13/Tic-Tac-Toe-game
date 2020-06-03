board=["-","-","-",
       "-","-","-",
       "-","-","-"]
gameon=True
winner=None
player="X"

def display(board):
	print board[0]+"|"+board[1]+"|"+board[2]
    	print board[3]+"|"+board[4]+"|"+board[5]
	print board[6]+"|"+board[7]+"|"+board[8]
	

def playgame():
    	display(board)
    	while gameon:
        	turns(player)
        	gameover()
        	changeplayer()

    	if winner=="X" or winner=="0":
        	print winner + " won"
    	elif winner==None:
        	print "the game was a tie."

def turns(player):

    	print player + "'s turn"
    	position=input("Choose any number from 1-9: ")

      	position=int(position)-1
    	board[position]=player
    	display(board)
    	return


def gameover():
  	checkwin()
    	checktie()
	return

def checktie():

    	global gameon
    	if "-" not in board:
        	gameon=False
    	return


def checkwin():

    	global winner

     	row_winner=checkrow()
     	column_winner=checkcolumn()
     	diagnol_winner=checkdiagnol()

     	if row_winner:
        	winner=row_winner
     	elif column_winner:
        	winner=column_winner
     	elif diagnol_winner:
        	winner=diagnol_winner
     	else:
        	winner=None

     	return


def checkrow():
    	global gameon

    	row1 = board[0]==board[1]==board[2]!="-"
    	row2 = board[3]==board[4]==board[5]!="-"
    	row3 = board[6]==board[7]==board[8]!="-"

    	if row1 or row2 or row3:
        	gameon=False

    	if row1:
        	return board[0]
    	elif row2:
        	return board[3]
    	elif row3:
        	return board[6]
    	return

def checkcolumn():
    	global gameon

    	col1 = board[0]==board[3]==board[6]!="-"
    	col2 = board[1]==board[4]==board[7]!="-"
    	col3 = board[2]==board[5]==board[8]!="-"

    	if col1 or col2 or col3:
        	gameon=False

    	if col1:
        	return board[0]
    	elif col2:
        	return board[1]
    	elif col3:
        	return board[2]
    	return

def checkdiagnol():
    	d1 = board[0]==board[4]==board[8]!="-"
    	d2 = board[2]==board[4]==board[6]!="-"

    	if d1 or d2:
        	gameon=False

    	if d1:
        	return board[0]
    	elif d2:
        	return board[2]
    	return

def changeplayer():

    	global player
    
	if player=="X":
        	player="0"
    	elif player=="0":
        	player="X"
    	return

playgame()

