print('Welcome to CrossZero!')
print('Its a game for 2 players')
print('First player need to choose place for cross X')
print('Second player need to choose place for zero 0')
print("Let's start!")
print('#############################################')
print('We have a battle field, P1 choose X position first!')
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
print('\n', *lst1, '\n', *lst2, '\n', *lst3, '\n')
def inpt1():
	x1 = input('P1: Enter the position for X\n')
	if int(x1) == lst1[0]:
		lst1[0] = ('X')
	elif int(x1) == lst1[1]:
		lst1[1] = ('X')
	elif int(x1) == lst1[2]:
		lst1[2] = ('X')
	elif int(x1) == lst2[0]:
		lst2[0] = ('X')
	elif int(x1) == lst2[1]:
		lst2[1] = ('X')
	elif int(x1) == lst2[2]:
		lst2[2] = ('X')
	elif int(x1) == lst3[0]:
		lst3[0] = ('X')
	elif int(x1) == lst3[1]:
		lst3[1] = ('X')
	elif int(x1) == lst3[2]:
		lst3[2] = ('X')
	else:
		print('Incorrect number, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt1()

def inpt2():
	o1 = input('P2: Enter the position for 0\n')
	if int(o1) == lst1[0]:
		lst1[0] = ('O')
	elif int(o1) == lst1[1]:
		lst1[1] = ('O')
	elif int(o1) == lst1[2]:
		lst1[2] = ('O')
	elif int(o1) == lst2[0]:
		lst2[0] = ('O')
	elif int(o1) == lst2[1]:
		lst2[1] = ('O')
	elif int(o1) == lst2[2]:
		lst2[2] = ('O')
	elif int(o1) == lst3[0]:
		lst3[0] = ('O')
	elif int(o1) == lst3[1]:
		lst3[1] = ('O')
	elif int(o1) == lst3[2]:
		lst3[2] = ('O')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt2()

def inpt3():
	x2 = input('P1: Enter the position for X\n')
	if int(x2) == lst1[0]:
		lst1[0] = ('X')
	elif int(x2) == lst1[1]:
		lst1[1] = ('X')
	elif int(x2) == lst1[2]:
		lst1[2] = ('X')
	elif int(x2) == lst2[0]:
		lst2[0] = ('X')
	elif int(x2) == lst2[1]:
		lst2[1] = ('X')
	elif int(x2) == lst2[2]:
		lst2[2] = ('X')
	elif int(x2) == lst3[0]:
		lst3[0] = ('X')
	elif int(x2) == lst3[1]:
		lst3[1] = ('X')
	elif int(x2) == lst3[2]:
		lst3[2] = ('X')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt3()

def inpt4():
	o2 = input('P2: Enter the position for 0\n')
	if int(o2) == lst1[0]:
		lst1[0] = ('O')
	elif int(o2) == lst1[1]:
		lst1[1] = ('O')
	elif int(o2) == lst1[2]:
		lst1[2] = ('O')
	elif int(o2) == lst2[0]:
		lst2[0] = ('O')
	elif int(o2) == lst2[1]:
		lst2[1] = ('O')
	elif int(o2) == lst2[2]:
		lst2[2] = ('O')
	elif int(o2) == lst3[0]:
		lst3[0] = ('O')
	elif int(o2) == lst3[1]:
		lst3[1] = ('O')
	elif int(o2) == lst3[2]:
		lst3[2] = ('O')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt4()

def inpt5():
	x3 = input('P1: Enter the position for X\n')
	if int(x3) == lst1[0]:
		lst1[0] = ('X')
	elif int(x3) == lst1[1]:
		lst1[1] = ('X')
	elif int(x3) == lst1[2]:
		lst1[2] = ('X')
	elif int(x3) == lst2[0]:
		lst2[0] = ('X')
	elif int(x3) == lst2[1]:
		lst2[1] = ('X')
	elif int(x3) == lst2[2]:
		lst2[2] = ('X')
	elif int(x3) == lst3[0]:
		lst3[0] = ('X')
	elif int(x3) == lst3[1]:
		lst3[1] = ('X')
	elif int(x3) == lst3[2]:
		lst3[2] = ('X')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt5()

CongratsX = ('Congratulations! Player 1 WINS for X!!')
def win1():
	if lst1[0] == ('X') and lst1[1] == ('X') and lst1[2] == ('X'):
		print(CongratsX)
	elif lst2[0] == ('X') and lst2[1] == ('X') and lst2[2] == ('X'):
		print(CongratsX)
	elif lst3[0] == ('X') and lst3[1] == ('X') and lst3[2] == ('X'):
		print(CongratsX)
	elif lst1[0] == ('X') and lst2[0] == ('X') and lst3[0] == ('X'):
		print(CongratsX)
	elif lst1[0] == ('X') and lst2[1] == ('X') and lst3[2] == ('X'):
		print(CongratsX)
	elif lst1[1] == ('X') and lst2[1] == ('X') and lst3[1] == ('X'):
		print(CongratsX)
	elif lst1[2] == ('X') and lst2[2] == ('X') and lst3[2] == ('X'):
		print(CongratsX)
	elif lst1[2] == ('X') and lst2[1] == ('X') and lst3[0] == ('X'):
		print(CongratsX)

win1()

def inpt6():
	o3 = input('P2: Enter the position for 0\n')
	if int(o3) == lst1[0]:
		lst1[0] = ('O')
	elif int(o3) == lst1[1]:
		lst1[1] = ('O')
	elif int(o3) == lst1[2]:
		lst1[2] = ('O')
	elif int(o3) == lst2[0]:
		lst2[0] = ('O')
	elif int(o3) == lst2[1]:
		lst2[1] = ('O')
	elif int(o3) == lst2[2]:
		lst2[2] = ('O')
	elif int(o3) == lst3[0]:
		lst3[0] = ('O')
	elif int(o3) == lst3[1]:
		lst3[1] = ('O')
	elif int(o3) == lst3[2]:
		lst3[2] = ('O')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt6()

CongratsO = ('Congratulations! Player 2 WINS for O!!')
def win2():
	if lst1[0] == ('O') and lst1[1] == ('O') and lst1[2] == ('O'):
		print(CongratsO)
	elif lst2[0] == ('O') and lst2[1] == ('O') and lst2[2] == ('O'):
		print(CongratsO)
	elif lst3[0] == ('O') and lst3[1] == ('O') and lst3[2] == ('O'):
		print(CongratsO)
	elif lst1[0] == ('O') and lst2[0] == ('O') and lst3[0] == ('O'):
		print(CongratsO)
	elif lst1[0] == ('O') and lst2[1] == ('O') and lst3[2] == ('O'):
		print(CongratsO)
	elif lst1[1] == ('O') and lst2[1] == ('O') and lst3[1] == ('O'):
		print(CongratsO)
	elif lst1[2] == ('O') and lst2[2] == ('O') and lst3[2] == ('O'):
		print(CongratsO)
	elif lst1[2] == ('O') and lst2[1] == ('O') and lst3[0] == ('O'):
		print(CongratsO)
win2()

def inpt7():
	x4 = input('P1: Enter the position for X\n')
	if int(x4) == lst1[0]:
		lst1[0] = ('X')
	elif int(x4) == lst1[1]:
		lst1[1] = ('X')
	elif int(x4) == lst1[2]:
		lst1[2] = ('X')
	elif int(x4) == lst2[0]:
		lst2[0] = ('X')
	elif int(x4) == lst2[1]:
		lst2[1] = ('X')
	elif int(x4) == lst2[2]:
		lst2[2] = ('X')
	elif int(x4) == lst3[0]:
		lst3[0] = ('X')
	elif int(x4) == lst3[1]:
		lst3[1] = ('X')
	elif int(x4) == lst3[2]:
		lst3[2] = ('X')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt7()
win1()

def inpt8():
	o4 = input('P2: Enter the position for 0\n')
	if int(o4) == lst1[0]:
		lst1[0] = ('O')
	elif int(o4) == lst1[1]:
		lst1[1] = ('O')
	elif int(o4) == lst1[2]:
		lst1[2] = ('O')
	elif int(o4) == lst2[0]:
		lst2[0] = ('O')
	elif int(o4) == lst2[1]:
		lst2[1] = ('O')
	elif int(o4) == lst2[2]:
		lst2[2] = ('O')
	elif int(o4) == lst3[0]:
		lst3[0] = ('O')
	elif int(o4) == lst3[1]:
		lst3[1] = ('O')
	elif int(o4) == lst3[2]:
		lst3[2] = ('O')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt8()
win2()

def inpt9():
	x5 = input('P1: Enter the position for X\n')
	if int(x5) == lst1[0]:
		lst1[0] = ('X')
	elif int(x5) == lst1[1]:
		lst1[1] = ('X')
	elif int(x5) == lst1[2]:
		lst1[2] = ('X')
	elif int(x5) == lst2[0]:
		lst2[0] = ('X')
	elif int(x5) == lst2[1]:
		lst2[1] = ('X')
	elif int(x5) == lst2[2]:
		lst2[2] = ('X')
	elif int(x5) == lst3[0]:
		lst3[0] = ('X')
	elif int(x5) == lst3[1]:
		lst3[1] = ('X')
	elif int(x5) == lst3[2]:
		lst3[2] = ('X')
	else:
		print('Incorrect number or busy place, next turn!')
	print('\n',*lst1,'\n',*lst2,'\n',*lst3,'\n')
inpt9()
win1()

def draw():
	if not win2() and not win1():
		print('This is a DRAW!')
draw()
