import math
import sys, os
import random
import pygame
from pygame.locals import *

DEFAULT = 325
x = 425
y = 375
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = 	(245,252,131)
PINK = (255,128,255)
GREEN_LEAF = (128,255,0)
GRAY = (182,182,182)
GRAY_FADING = (223,223,223)
GREEN_FADING = (131,254,192)
BLUE = (112,146,190)
RED = (226,55,22)	
PRUNE = (196,0,0)
MY_COLOUR=[GREEN_FADING,RED,GRAY_FADING,PRUNE,BLUE,PINK,YELLOW,GREEN_LEAF]
WIDTH = 1649
HEIGHT = 1001
MIN_WIDTH = 249
MIN_HEIGHT = 99
board = ((WIDTH-MIN_WIDTH + 2)/50) * ((HEIGHT-MIN_HEIGHT)/50) 
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("HoaTrongCamQuan.mp3") 
#os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the screen 
sound = pygame.mixer.Sound('click.wav')
menu_image = pygame.image.load("background.png")
ingame_image = pygame.image.load("ingame.png")
board_image = pygame.image.load("board.png")
pygame.init()
FPS = 240
# <-- DISPLAY --> #
DISPLAY= pygame.display.set_mode((WIDTH+270,HEIGHT+80))
pygame.display.set_caption("Caro Game ~ by @Restudy - HCMUS")
Music_mode = 3
choose = 0 
player_text = pygame.font.Font(None,50)	
menu_text = pygame.font.Font(None,200)
# <-- Menu --> #
def menu(music = 0):	
	text = menu_text.render("CARO" ,10 , GREEN_FADING)	
	DISPLAY.blit(menu_image,(0,0))
	if music == 1:
		pygame.draw.line(DISPLAY, RED, [1150,37], [1117,80],10)

def display_fading():
	for i in range(2, int(WIDTH/50+1)):
		pygame.draw.line(DISPLAY, GRAY_FADING, (50*i,100),(50*i,HEIGHT),3)
	for i in range(2,int(HEIGHT/50+1)):
		pygame.draw.line(DISPLAY, GRAY_FADING, (100,50*i),(WIDTH,50*i),3)

def display():
	DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))


def invisible_player(count,color):
	if count%2 ==0:
		pygame.draw.circle(DISPLAY,color, [x,y], 20)  
	else:
		pygame.draw.line(DISPLAY, color, [x-15,y-15], [x+15, y+15],5)
		pygame.draw.line(DISPLAY, color, [x-15,y+15], [x+15, y-15],5)
 
def check(player):
	for i in range(len(player)):  
		collums= []
		rows = []
		
		for j in range(len(player)):			
			# <-- Rows --> #
			if (player[i][1] == player[j][1]):
				rows.append(player[j][0])
				wining_holding_y[0] = player[i][1]
			# <-- Collums --> #			
			if (player[i][0] == player[j][0]):
				collums.append(player[j][1])
				wining_holding_x[0] = player [j][0]
		# <-- Primary diagonal --> #
		if [player[i][0]+50,player[i][1]+50] in player:
			if [player[i][0]+100,player[i][1]+100] in player:
				if [player[i][0]+150,player[i][1]+150] in player:
					if [player[i][0]+200,player[i][1]+200] in player:
						wining_diag.append([player[i][0]+50,player[i][1]+50])
						wining_diag.append([player[i][0]+100,player[i][1]+100])
						wining_diag.append([player[i][0]+150,player[i][1]+150])
						wining_diag.append([player[i][0]+200,player[i][1]+200])
						wining_diag.append([player[i][0],player[i][1]])
						return True	

		# <-- Secondary diagonal --> #
		if [player[i][0]-50,player[i][1]+50] in player:
			if [player[i][0]-100,player[i][1]+100] in player:
				if [player[i][0]-150,player[i][1]+150] in player:
					if [player[i][0]-200,player[i][1]+200] in player:
						wining_diag.append([player[i][0]-50,player[i][1]+50])
						wining_diag.append([player[i][0]-100,player[i][1]+100])
						wining_diag.append([player[i][0]-150,player[i][1]+150])
						wining_diag.append([player[i][0]-200,player[i][1]+200])
						wining_diag.append([player[i][0],player[i][1]])
						return True

		collums.sort(reverse = False)  
		rows.sort(reverse = False)
		for z in range(0,len(rows)-4):
			if rows[z] == rows[z+1] - 50 == rows[z+2] - 100 == rows[z+3] - 150 == rows[z+4] - 200:
				wining_x.append([rows[z],rows[z+1],rows[z+2],rows[z+3],rows[z+4]])
				return True
		for z in range(0,len(collums)-4):
			if collums[z] == collums[z+1] - 50 == collums[z+2] - 100 == collums[z+3] - 150 == collums[z+4] - 200:
				wining_y.append([collums[z],collums[z+1],collums[z+2],collums[z+3],collums[z+4]])
				return True
	return False

# <-- Chặn 2 đầu --> #
def check_win(player,player2):
	for i in range(len(player)):  
		collums= []
		rows = []
		
		for j in range(len(player)):			
			# <-- Rows --> #
			if (player[i][1] == player[j][1]):
				rows.append(player[j][0])
				wining_holding_y[0] = player[i][1]
			# <-- Collums --> #			
			if (player[i][0] == player[j][0]):
				collums.append(player[j][1])
				wining_holding_x[0] = player [j][0]
		# <-- Primary diagonal --> #
		if [player[i][0]+50,player[i][1]+50] in player:
			if [player[i][0]+100,player[i][1]+100] in player:
				if [player[i][0]+150,player[i][1]+150] in player:
					if [player[i][0]+200,player[i][1]+200] in player:
						if [player[i][0]+250, player[i][1]+250] in player2 and [player[i][0]-50,player[i][1]-50] in player2:
							return False
						wining_diag.append([player[i][0]+50,player[i][1]+50])
						wining_diag.append([player[i][0]+100,player[i][1]+100])
						wining_diag.append([player[i][0]+150,player[i][1]+150])
						wining_diag.append([player[i][0]+200,player[i][1]+200])
						wining_diag.append([player[i][0],player[i][1]])

						return True	

		# <-- Secondary diagonal --> #
		if [player[i][0]-50,player[i][1]+50] in player:
			if [player[i][0]-100,player[i][1]+100] in player:
				if [player[i][0]-150,player[i][1]+150] in player:
					if [player[i][0]-200,player[i][1]+200] in player:
						if [player[i][0]+50,player[i][1]-50] in player2 and [player[i][0]-250, player[i][1]+250] in player2:
							return False 				
						wining_diag.append([player[i][0]-50,player[i][1]+50])
						wining_diag.append([player[i][0]-100,player[i][1]+100])
						wining_diag.append([player[i][0]-150,player[i][1]+150])
						wining_diag.append([player[i][0]-200,player[i][1]+200])
						wining_diag.append([player[i][0],player[i][1]])
						return True

		collums.sort(reverse = False)  
		rows.sort(reverse = False)
		for z in range(0,len(rows)-4):
			if rows[z] == rows[z+1] - 50 == rows[z+2] - 100 == rows[z+3] - 150 == rows[z+4] - 200:
				print(rows)
				print(rows[z])
				if [rows[z] -50 , wining_holding_y[0]] in player2 and [rows[z]+250, wining_holding_y[0]] in player2:

					return False
				wining_x.append([rows[z],rows[z+1],rows[z+2],rows[z+3],rows[z+4]])
				return True
		for z in range(0,len(collums)-4):
			if collums[z] == collums[z+1] - 50 == collums[z+2] - 100 == collums[z+3] - 150 == collums[z+4] - 200:
				if [wining_holding_x[0], collums[z] - 50] in player2 and [wining_holding_x[0], collums[0]+ 250] in player2:
					return False
				wining_y.append([collums[z],collums[z+1],collums[z+2],collums[z+3],collums[z+4]])
				return True
	return False
# <-- Bot --> #

# <-- Attention --> #
Attack = [0,8,72,648,5832,52488,472392]
Defense =  [0,3,27,99,729,6561,59049]
# <-- Attack --> #
def AttRows(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1, 7):
		if x_ + dem*50 > WIDTH:
			break
		if [x_ + dem*50, y_] in player1:
			Enemy +=1
			break
		elif [x_ + dem*50, y_] in bot1:
			Bot +=1
		#Blank Space
		else:
			break
	for dem in range(1, 6):
		if x_ - dem*50 < MIN_WIDTH+26:
			break
		if [x_ - dem*50, y_] in player1:
			Enemy +=1
			break
		elif [x_ - dem*50, y_] in bot1:
			Bot +=1
		#Blank Space
		else:
			break
	if Enemy == 2:
		if Bot <= 3:
			return 1;
	Point -= Defense[Enemy] * 3
	Point += Attack[Bot]
	return Point
def AttCollums(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if y_ +dem*50 > HEIGHT:
			break
		if [x_ , y_ + dem*50] in player1:
			Enemy += 1
			break
		elif [x_ , y_ + dem*50] in bot1:
			Bot += 1
		#Blank Space
		else:
			break
	for dem in range(1, 7):
		if y_ - dem*50 < MIN_HEIGHT+26:
			break
		if [x_, y_ - dem*50] in player1:
			Enemy +=1
			break
		elif [x_ , y_ - dem*50] in bot1:
			Bot +=1
		#Blank Space
		else:
			break
	if Enemy == 2:
		if Bot <= 3:
			return 1;
	Point -= Defense[Enemy] * 3
	Point += Attack[Bot]
	return Point
def AttSecDiag(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if x_ + dem*50 > WIDTH or y_ - dem*50 < MIN_HEIGHT+26:
			break
		if [x_ + dem*50, y_ - dem*50] in player1:
			Enemy += 1
			break
		elif [x_ + dem*50, y_ - dem*50] in bot1:
			Bot +=1
		#Blank Space
		else:
			break

	for dem in range(1, 7):
		if x_ - dem*50 < 125 or  y_ + dem*50 > HEIGHT:
			break
		if [x_ - dem*50, y_ + dem*50] in player1:
			Enemy +=1
			break
		elif [x_ - dem*50 , y_ + dem*50] in bot1:
			Bot +=1
		#Blank Space
		else:
			break
	if Enemy == 2:
		if Bot <= 3:
			return 1;
	Point -= Defense[Enemy] * 3
	Point += Attack[Bot]
	return Point
def AttPrDiag(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if x_ + dem*50 > WIDTH or y_ + dem*50 > HEIGHT:
			break
		if [x_ + dem*50, y_ + dem*50] in player1:
			Enemy += 1
			break
		elif [x_ + dem*50, y_ + dem*50] in bot1:
			Bot +=1
		#Blank Space
		else:
			break

	for dem in range(1, 7):
		if x_ - dem*50 < MIN_HEIGHT+26 or  y_ - dem*50 < MIN_WIDTH+26:
			break
		if [x_ - dem*50, y_ - dem*50] in player1:
			Enemy +=1
			break
		elif [x_ - dem*50 , y_ - dem*50] in bot1:
			Bot +=1
		#Blank Space
		else:
			break
	if Enemy == 2:
		if Bot <= 3:
			return 1
	Point -= Defense[Enemy+1] * 3
	Point += Attack[Bot]
	return Point
# <-- Defense --> #
def DefRows(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1, 7):
		if x_ + dem*50 >= WIDTH:
			break
		if [x_ + dem*50, y_] in player1:
			Enemy +=1		
			
		elif [x_ + dem*50, y_] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	for dem in range(1, 7):
		if x_ - dem*50 < MIN_WIDTH+26:
			break
		if [x_ - dem*50, y_] in player1:
			Enemy +=1
			
		elif [x_ - dem*50, y_] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	if Bot == 2:
		return 1
	Point += Defense[Enemy]
	#print(Point)
	return Point
def DefCollums(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if y_+ dem*50 >= HEIGHT:
			break
		if [x_ , y_ + dem*50] in player1:
			Enemy += 1
			
		elif [x_ , y_ + dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	for dem in range(1, 7):
		if y_ - dem*50 < MIN_HEIGHT+26:
			break
		if [x_, y_ - dem*50] in player1:
			Enemy +=1
			
		elif [x_ , y_ - dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	if Bot == 2:
		return 1	 
	Point += Defense[Enemy]
	return Point
def DefSecDiag(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if x_ + dem*50 > WIDTH or y_ - dem*50 < MIN_HEIGHT+26:
		 	break
		if [x_ + dem*50, y_ - dem*50] in player1:
			Enemy += 1
			
		elif [x_ + dem*50, y_ - dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break

	for dem in range(1, 7):
		if x_ - dem*50 < MIN_WIDTH+26 or  y_ + dem*50 >= HEIGHT:
			break
		if [x_ - dem*50, y_ + dem*50] in player1:
			Enemy +=1
			
		elif [x_ - dem*50 , y_ + dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	if Bot == 2:
		return 1
	Point += Defense[Enemy]
	return Point
def DefPrDiag(x_, y_):
	Point = 0
	Enemy = 0
	Bot = 0 
	for dem in range(1,7):
		if x_ + dem*50 > WIDTH or y_ + dem*50 >= HEIGHT:
			break
		if [x_ + dem*50, y_ + dem*50] in player1:
			Enemy += 1			
		elif [x_ + dem*50, y_ + dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break

	for dem in range(1, 7):
		if x_ - dem*50 < 125 or  y_ - dem*50 < 125:
			break
		if [x_ - dem*50, y_ - dem*50] in player1:
			Enemy +=1

		elif [x_ - dem*50 , y_ - dem*50] in bot1:
			Bot +=1
			break
		#Blank Space
		else:
			break
	if Bot == 2:
		return 1
	Point += Defense[Enemy]
	return Point
# <-- Counting points for bot --> #
def bot_ways():
	Point_max = 0
	count = 0
	result = [375,125]
	for i in range(MIN_WIDTH + 26, WIDTH, 50):
		for j in range(MIN_HEIGHT+26, HEIGHT, 50):
			if [i, j] not in player1 and [i, j] not in bot1:
				Attack_Point = AttCollums(i, j) + AttRows(i, j) + AttPrDiag(i, j) + AttSecDiag(i, j)
				Defense_Point = DefCollums(i, j) + DefRows(i, j) + DefPrDiag(i, j) + DefSecDiag(i , j)
				Temp_Point = max(Attack_Point,Defense_Point)				
				if Point_max < Temp_Point:			
					Point_max = Temp_Point
					result[0] = i
					result[1] = j
			else:
				continue

	return result
def bot():
	pos = []
	pos = bot_ways()
	bot1.append( [pos[0],pos[1]])

font = pygame.font.Font(None, 40)

# <-- Players --> #
score_1 = 0
score_2 = 0
score_bot = 0
player1= []
player2 = []
bot1 =[]
wining_x= []
wining_y= []
wining_holding_x = [0]
wining_holding_y = [0]
wining_diag = []
win = 0
count = 0
count_save = 0 
redo_save  = 0
redo_list1 = []
redo_list2 = []
replay_list = []
def undo(count):
	global redo_save
	if count > redo_save:
		redo_save = count 
	count -= 1
	if choose == 1:
		if count%2 == 0:
			if len(player1)> 0:
				redo_list1.append(player1[len(player1)-1])
				player1.pop()
			else:
				return count + 1
		else:
			if len(player2) > 0:
				redo_list2.append(player2[len(player2)-1])
				player2.pop()
			else:
				return count + 1
		return count
	else:
		if len(player1 ) > 0:
			redo_list1.append(player1[len(player1)-1])
			redo_list2.append(bot1[len(bot1)-1])
			player1.pop()
			bot1.pop()
			return count - 1
		return count + 1

def replay():
	display()
	time = 500
	pygame.draw.rect(DISPLAY, BLACK,(50,25,50,50))
	for event in pygame.event.get():
		if pygame.type == QUIT:
			sys.exit()
			pygame.quit()
	if choose == 1:
		if count_save % 2 == 0:
			for i in range(0,len(replay_list)):
				# <-- SKIP REPLAY --> #
				for event in pygame.event.get():
					if pygame.Rect((50,25),(50, 50)).collidepoint(pygame.mouse.get_pos()):
						if event.type == pygame.MOUSEBUTTONDOWN:
							time = 1
				if (i %2 == 0):
					pygame.time.wait(time)
					pygame.draw.circle(DISPLAY,BLUE, [replay_list[i][0],replay_list[i][1]], 20,5) 
					pygame.draw.circle(DISPLAY,WHITE,[replay_list[i][0],replay_list[i][1]] , 17)	 	
					pygame.display.update()
				else:
					pygame.time.wait(time)
					pygame.draw.line(DISPLAY, PRUNE, [replay_list[i][0]-15,replay_list[i][1]-15], [replay_list[i][0]+15, replay_list[i][1]+15],5)
					pygame.draw.line(DISPLAY, PRUNE, [replay_list[i][0]-15,replay_list[i][1]+15], [replay_list[i][0]+15, replay_list[i][1]-15],5)		
				pygame.display.update()
		else:
			for i in range(0,len(replay_list)):
				# <-- SKIP REPLAY --> #
				for event in pygame.event.get():
					if pygame.Rect((50,25),(50, 50)).collidepoint(pygame.mouse.get_pos()):
						if event.type == pygame.MOUSEBUTTONDOWN:
							time= 0
				if (i % 2 ==  0):
					pygame.time.delay(time)
					pygame.draw.line(DISPLAY, PRUNE, [replay_list[i][0]-15,replay_list[i][1]-15], [replay_list[i][0]+15, replay_list[i][1]+15],5)
					pygame.draw.line(DISPLAY, PRUNE, [replay_list[i][0]-15,replay_list[i][1]+15], [replay_list[i][0]+15, replay_list[i][1]-15],5)	
					pygame.display.update()
				else:
					pygame.time.delay(time)
					pygame.draw.circle(DISPLAY,BLUE, [replay_list[i][0],replay_list[i][1]], 20,5) 
					pygame.draw.circle(DISPLAY,WHITE,[replay_list[i][0],replay_list[i][1]] , 17)	 		
				pygame.display.update()
	pygame.display.flip()
# <-- Text --> #
win_text1 = font.render('CLICK ANYWHEHRE TO CONINUE', 0, BLACK)
win_text2 = font.render('PRESS \'X\' TO EXIT ', 0, BLACK)
# <-- Game play --> #
while True:
		#pygame.draw.rect(DISPLAY,BLACK,(50,50, 80, 25))
# <-- Menu --> #
	if choose == 0:
		redo_list1.clear()
		redo_list2.clear()
		count = 0
		score_1 =0 
		score_2 = 0
		score_bot = 0
		count_save = 0
		player1.clear()
		player2.clear()
		bot1.clear()

		if Music_mode % 2 == 0:
			menu()
			if pygame.mixer.get_busy() == True: 
				pygame.mixer.music.play()					
		else:
			menu(1)
			pygame.mixer.music.stop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# <-- Music ON/OFF --> #	

			if pygame.Rect((1100,30),(56,62)).collidepoint(pygame.mouse.get_pos()):
				if event.type == pygame.MOUSEBUTTONDOWN:
					sound.play()
					Music_mode += 1

		#pygame.draw.rect(DISPLAY,BLACK,(330,490,520,100))
		# <-- When the cursor is near multi mode --> #
			if pygame.Rect((330,490),( 520, 100)).collidepoint(pygame.mouse.get_pos()):		
				if event.type == pygame.MOUSEBUTTONDOWN:
					sound.play()
					choose = 1
					print("HELLO")
		# <-- When the cursor is near single mode --> #
			if pygame.Rect((330,355),(520, 100)).collidepoint(pygame.mouse.get_pos()):	
				if event.type == pygame.MOUSEBUTTONDOWN:
					sound.play()
					choose = 2
					print("HI")
		# <-- IMAGE LOADING MUST BE OUT OF "FOR LOOPS" ABOVE. OTHEWISE, THE RESPONDING OF IMAGES WILL BE INTERRUPTED --> #
		if pygame.Rect((330,490),( 520, 100)).collidepoint(pygame.mouse.get_pos()):		
			PVP = pygame.image.load("Multiplayer.png")
			DISPLAY.blit(PVP,(330,490))
		if pygame.Rect((330,355),(520, 100)).collidepoint(pygame.mouse.get_pos()):
			PVB = pygame.image.load("Singleplayer.png")
			DISPLAY.blit(PVB,(330,350))		
		if choose != 0:
			DISPLAY.blit(ingame_image,(0,0))
		clock.tick(240)
		pygame.display.flip()

# <-- Player VS Player -->
	if choose == 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			# <-- Get position of mouse --> #
			position = pygame.mouse.get_pos()
			#pygame.draw.rect(DISPLAY,RED,(50,HEIGHT+20, 220, 30))
			# <-- Test save game --> #
			if pygame.Rect((350,25),(100, 60)).collidepoint(pygame.mouse.get_pos()):
				if event.type == pygame.MOUSEBUTTONDOWN:
					sound.play()
					print("GAME SAVED!")
					if (os.path.isfile('./SAVE.txt')):
						os.remove("SAVE.txt")
					file = open("SAVE.txt","a")
					for i in range(0,len(player1)):
						file.write( str(player1[i][0]) + " " + str( player1[i][1])+ " ")
					file.write("\n")
					for i in range(0,len(player2)):
						file.write( str(player2[i][0]) + " " + str( player2[i][1])+ " ")
					file.close()
					DISPLAY.fill(WHITE)
					text = font.render("GAME SAVED! GAME WILL BE CLOSED!",20,BLACK)
					DISPLAY.blit(text, (350,300))
					pygame.display.update()
					pygame.time.delay(1000)
					pygame.quit()
					sys.exit()
					
			else:
				pygame.draw.rect(DISPLAY,BLACK,(50,HEIGHT+20, 220, 30))
			# <-- Test load game --> #
			if pygame.Rect((460,25),(100, 50)).collidepoint(pygame.mouse.get_pos()):
				if event.type == pygame.MOUSEBUTTONDOWN:
					if (os.path.isfile('./SAVE.txt')):
						f = open("SAVE.txt","r+")				
						p1 = f.readline().split()
						p2 = f.readline().split()
						player1 = [[int(p1[i]) , int(p1[i+1])] for i in range(0,len(p1)-1,2)]
						player2 = [[int(p2[i]) , int(p2[i+1])] for i in range(0,len(p2)-1,2)]
						f.close()
						if (len(p1)>len(p2)):
							count = 1
					else:
						text = font.render("NO GAME SAVED FOUND!",5,PINK)
						DISPLAY.blit(text, (300,HEIGHT+20))				
						pygame.display.update()
						pygame.time.wait(100)
					DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))
			else: 
				pygame.draw.rect(DISPLAY,BLACK,(WIDTH-200,HEIGHT+20, 220, 30))
			
			# <-- Back to menu -->
			if pygame.Rect((15,15),(250, 50)).collidepoint(pygame.mouse.get_pos()):
				if event.type == pygame.MOUSEBUTTONUP:				
					sound.play()					
					choose = 0
			# <-- Undo --> #
			if pygame.Rect((1500,40),(80, 60)).collidepoint(pygame.mouse.get_pos()):
				undo_text = font.render('UNDO',0,RED)
				if event.type == pygame.MOUSEBUTTONDOWN:								
					display()								
					count = undo(count)
					if (count < count_save):
						count = count_save
			else:
				undo_text = font.render('UNDO',0,BLACK)		
			# <-- Redo ?? :D ?? --> #
			if pygame.Rect((1575,40),(80, 60)).collidepoint(pygame.mouse.get_pos()):					
				if event.type == pygame.MOUSEBUTTONDOWN:	
					display()		
					if (redo_save  <=  count):
						redo_list1.clear()
						redo_list2.clear() 
					if count % 2 == 0:
						if (len(redo_list1) > 0):						
							player1.append(redo_list1[len(redo_list1)-1])
							redo_list1.pop()		
							count+=1

					else:
						if (len(redo_list2) > 0):
							player2.append(redo_list2[len(redo_list2)-1])
							redo_list2.pop()
							count+=1			
			else:
				redo_text = font.render('REDO', 0 , BLACK)
			if win == 0:
				if  position[0] < 100 or position[1] < 100 or position[0] >= WIDTH or position[1] >= HEIGHT:
					continue
				if 	[ 25* int(position[0]/25+1),25* int(position[1]/25+1)] in player1 or [ 25* int(position[0]/25+1), 25* int(position[1] /25 )] in player1 or [25* int(position[0]/25),25* int(position[1]/25+1)] in player1 or  [25* int(position[0]/25),25* int(position[1]/25)] in player1 :
					continue
				if 	[ 25* int(position[0]/25+1),25* int(position[1]/25+1)] in player2 or [ 25* int(position[0]/25+1), 25* int(position[1] /25 )] in player2 or [25* int(position[0]/25),25* int(position[1]/25+1)] in player2 or  [25* int(position[0]/25),25* int(position[1]/25)] in player2 :
					continue
				if (int(position[0]/25))%2 ==0:		
					DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))
					x = 25* int(position[0]/25+1)
					invisible_player(count,GRAY)
				else:				
					DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))
					x = 25* int(position[0]/25) 
					invisible_player(count,GRAY)
				if (int(position[1]/25))%2 ==0:			
					DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))
					y = 25* int(position[1]/25+1)
					invisible_player(count,GRAY)
				else : 			
					DISPLAY.blit(board_image,(MIN_WIDTH,MIN_HEIGHT))
					y = 25* int((position[1] /25))
					invisible_player(count,GRAY)
				pygame.display.update()
			# <-- MOVE --> #
			if event.type == pygame.MOUSEBUTTONDOWN and win == 0:
				redo_save = count # When you make a new move, you can't redo what you last undo 
				sound.play()
				if [x,y] in player1 or [x,y] in player2 or x < 125 or y < 125 or x >= WIDTH or y >= HEIGHT:
					continue					
				if count %2 ==0:
					player1.append([x,y])
					replay_list.append([x,y])
				else:
					player2.append([x,y])
					replay_list.append([x,y])
				count+=1
	
			# <-- When wins --> 
			if win == 1:
				if event.type == pygame.KEYDOWN:		
					if event.key == pygame.K_x:
						pygame.quit()
						sys.exit()
				# <-- Test reply --> #
			
				if pygame.Rect((150,20),(100, 35)).collidepoint(pygame.mouse.get_pos()):				
					pygame.draw.rect(DISPLAY,RED,(150,20, 100, 35))
					if event.type == pygame.MOUSEBUTTONDOWN:
						replay()

				else:
					pygame.draw.rect(DISPLAY,BLACK,(150,20, 100, 35))
					if event.type == pygame.MOUSEBUTTONDOWN:
						sound.play()
						win = 0
						replay_list.clear()
						wining_diag.clear()
						wining_x.clear()
						wining_y.clear()
						player1.clear()
						player2.clear()
						redo_list1.clear()
						redo_list2.clear()					
						display()		
						count_save = count

		# <-- Drawing --> #
		if win == 0:
			score1 = player_text.render("%d" %score_1,10,BLACK)
			score2 = player_text.render("%d" %score_2,10,BLACK)
			DISPLAY.blit(score1,(50, HEIGHT/2))
			DISPLAY.blit(score2,(WIDTH + 50, HEIGHT/2))
			for i in player1:
				pygame.draw.circle(DISPLAY,BLUE, i, 20,5)  
				pygame.draw.circle(DISPLAY,WHITE,i , 17)		
			for i in range(0,len(player2)) :
				pygame.draw.line(DISPLAY, PRUNE, [player2[i][0]-15,player2[i][1]-15], [player2[i][0]+15, player2[i][1]+15],5)
				pygame.draw.line(DISPLAY, PRUNE, [player2[i][0]-15,player2[i][1]+15], [player2[i][0]+15, player2[i][1]-15],5)
		# <-- Refill when game ended --> #
		else:
			for i in player1:
				pygame.draw.circle(DISPLAY,GRAY_FADING, i, 20,5) 
				pygame.draw.circle(DISPLAY,WHITE, i , 17)	 	
			for i in range(0,len(player2)) :
				pygame.draw.line(DISPLAY, GRAY, [player2[i][0]-15,player2[i][1]-15], [player2[i][0]+15, player2[i][1]+15],5)
				pygame.draw.line(DISPLAY, GRAY, [player2[i][0]-15,player2[i][1]+15], [player2[i][0]+15, player2[i][1]-15],5)			
			DISPLAY.blit(win_text1, (WIDTH/3+20,HEIGHT+20))
			DISPLAY.blit(win_text2, (WIDTH/3+60,HEIGHT+60))	

		# <-- Check wining --> #
		if check_win(player1,player2) == True and win == 0:
			if len(wining_x) > 0:
				for i in wining_x[0]:
					player1.remove([i,wining_holding_y[0]])
			elif (len(wining_y) > 0):
				for i in wining_y[0]:
					player1.remove([wining_holding_x[0],i])
			else:
				for i in wining_diag:
					player1.remove(i)
			text = font.render('PLAYER 1 WON!', 10, BLACK)
			DISPLAY.blit(text, (WIDTH/2-50,50))
			win = 1 
			score_1 += 1
		if check_win(player2,player1) == True and win == 0:
			if len(wining_x) > 0:
				for i in wining_x[0]:
					player2.remove([i,wining_holding_y[0]])
			elif (len(wining_y) > 0):
				for i in wining_y[0]:
					player2.remove([wining_holding_x[0],i])
			else :
				for i in wining_diag:
					player2.remove(i)

			text = font.render('PLAYER 2 WON!', 10, BLACK)
			DISPLAY.blit(text, (WIDTH/2-50,50))		
			win = 1
			score_2 += 1
		# <-- Out of moves --> #
		if len(player1) + len(player2) >= board:
			win = 1
			text = font.render('OUT OF MOVES',10,BLACK)
			DISPLAY.blit(text, (WIDTH/2-50,50))
		# <-- Music ends --> #
		if pygame.mixer.music.get_busy() == False and Music_mode%2 == 0:

			pygame.mixer.music.load("HoaTrongCamQuan.mp3")
			pygame.mixer.music.play()

# <-- Player VS Bot -->
	if choose == 2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				#sys.exit()
			# <-- Get position of mouse --> #
			position = pygame.mouse.get_pos()

			# <-- Undo -->
			if pygame.Rect((WIDTH,50),(90, 25)).collidepoint(pygame.mouse.get_pos()):
				undo_text = font.render('UNDO',0,RED)
				if event.type == pygame.MOUSEBUTTONUP:
					print( redo_save, count)
					sound.play()
					display()
					count = undo(count)
			else:
				undo_text = font.render('UNDO',0,BLACK)	

			# <-- Redo --> #
			if pygame.Rect((WIDTH,75),(220, 35)).collidepoint(pygame.mouse.get_pos()):				
				redo_text = font.render('REDO', 0 , PRUNE)			
				if event.type == pygame.MOUSEBUTTONDOWN:	
					print( redo_save, count)
					display()		
					if (redo_save  <=  count):
						redo_list1.clear()
						redo_list2.clear() 
					if (len(redo_list1) > 0):						
						player1.append(redo_list1[len(redo_list1)-1])
						redo_list1.pop()								
						bot1.append(redo_list2[len(redo_list2)-1])
						redo_list2.pop()
						count+=2
		
			else:
				redo_text = font.render('REDO', 0 , BLACK)
			# <-- Back to menu -->
			if pygame.Rect((48,48),(220, 35)).collidepoint(pygame.mouse.get_pos()):
				back_text = font.render('BACK TO MENU', 0 , PRUNE)
				if event.type == pygame.MOUSEBUTTONUP:
					sound.play()
					choose = 0
			else:
				back_text = font.render('BACK TO MENU', 0 , BLACK)
			DISPLAY.blit(back_text,(50,50))
			DISPLAY.blit(undo_text,(WIDTH,50))
			DISPLAY.blit(redo_text,(WIDTH,75))
			if win == 0:
				if  position[0] < 100 or position[1] < 100 or position[0] >= WIDTH or position[1] >= HEIGHT:
					continue				
				if 	[ 25* int(position[0]/25+1),25* int(position[1]/25+1)] in player1 or [ 25* int(position[0]/25+1), 25* int(position[1] /25 )] in player1 or [25* int(position[0]/25),25* int(position[1]/25+1)] in player1 or  [25* int(position[0]/25),25* int(position[1]/25)] in player1 :
					continue
				if 	[ 25* int(position[0]/25+1),25* int(position[1]/25+1)] in bot1 or [ 25* int(position[0]/25+1), 25* int(position[1] /25 )] in bot1 or [25* int(position[0]/25),25* int(position[1]/25+1)] in bot1 or  [25* int(position[0]/25),25* int(position[1]/25)] in bot1 :
					continue
				if (int(position[0]/25))%2 ==0:
					invisible_player(0,WHITE)
					x = 25* int(position[0]/25+1)
					invisible_player(0,GRAY)
				else:
					invisible_player(0,WHITE)
					x = 25* int(position[0]/25) 
					invisible_player(0,GRAY)
				if (int(position[1]/25))%2 ==0:
					invisible_player(0,WHITE)
					y = 25* int(position[1]/25+1)
					invisible_player(0,GRAY)
				else : 
					invisible_player(0,WHITE)
					y = 25* int((position[1] /25 ))
					invisible_player(0,GRAY)
			# <-- MOVE --> #
			if event.type == pygame.MOUSEBUTTONDOWN and win == 0:
				
				if [x,y] in player1 or [x,y] in bot1 or x < 75 or y < 75 or x > WIDTH or y > HEIGHT:
					continue	
				sound.play()
				player1.append([x,y])
				bot()
				count +=  2
				redo_save = 0
			# <-- When wins --> 
			if event.type == pygame.KEYDOWN and win == 1:		
				if event.key == pygame.K_x:
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and win == 1:
				sound.play()
				win = 0
				wining_diag.clear()
				wining_x.clear()
				wining_y.clear()
				player1.clear()
				bot1.clear()
				display()		

		# <-- Refill --> #
		if win == 0:
			score1 = player_text.render("%d" %score_1,10,BLACK)
			score2 = player_text.render("%d" %score_bot,10,BLACK)
			DISPLAY.blit(score1,(50, HEIGHT/2))
			DISPLAY.blit(score2,(WIDTH + 50, HEIGHT/2))
			for i in player1:
				pygame.draw.circle(DISPLAY,BLUE, i, 20,5)  
				pygame.draw.circle(DISPLAY,WHITE,i , 17)	
			for i in range(0,len(bot1)) :
				pygame.draw.line(DISPLAY, RED, [bot1[i][0]-15,bot1[i][1]-15], [bot1[i][0]+15, bot1[i][1]+15],5)
				pygame.draw.line(DISPLAY, RED, [bot1[i][0]-15,bot1[i][1]+15], [bot1[i][0]+15, bot1[i][1]-15],5)
			if len(bot1) > 0:
				pygame.draw.line(DISPLAY, PINK, [bot1[len(bot1)-1][0]-15,bot1[len(bot1)-1][1]-15], [bot1[len(bot1)-1][0]+15, bot1[len(bot1)-1][1]+15],5)
				pygame.draw.line(DISPLAY, PINK, [bot1[len(bot1)-1][0]-15,bot1[len(bot1)-1][1]+15], [bot1[len(bot1)-1][0]+15, bot1[len(bot1)-1][1]-15],5)
		else:
			for i in player1:
				pygame.draw.circle(DISPLAY,GRAY_FADING, i, 20,5) 
				pygame.draw.circle(DISPLAY,WHITE,i , 17)
			for i in range(0,len(bot1)):
				pygame.draw.line(DISPLAY, GRAY_FADING, [bot1[i][0]-15,bot1[i][1]-15], [bot1[i][0]+15, bot1[i][1]+15],5)
				pygame.draw.line(DISPLAY, GRAY_FADING, [bot1[i][0]-15,bot1[i][1]+15], [bot1[i][0]+15, bot1[i][1]-15],5)		
			DISPLAY.blit(win_text1, (WIDTH/3+20,HEIGHT+20))
			DISPLAY.blit(win_text2, (WIDTH/3+20,HEIGHT+60))	
		# <-- Check wining --> #
		if check(player1) == True and win == 0:
			if len(wining_x) > 0:
				for i in wining_x[0]:
					player1.remove([i,wining_holding_y[0]])
			elif (len(wining_y) > 0):
				for i in wining_y[0]:
					player1.remove([wining_holding_x[0],i])
			else:
				for i in wining_diag:
					player1.remove(i)
			score_1 +=1
			display_fading()
			text = font.render('YOU WON!', 10, BLACK)
			DISPLAY.blit(text, (WIDTH/2-50,50))
			win = 1 

		if check(bot1) == True and win == 0:
			if len(wining_x) > 0:
				for i in wining_x[0]:
					bot1.remove([i,wining_holding_y[0]])
			elif (len(wining_y) > 0):
				for i in wining_y[0]:
					bot1.remove([wining_holding_x[0],i])
			else:
				for i in wining_diag:
					bot1.remove(i)
			display_fading()
			text = font.render('YOU LOSE!', 10, BLACK)
			score_bot +=1
			DISPLAY.blit(text, (WIDTH/2-50,50))
			win = 1
		# <-- Out of moves --> #
		if len(player1) + len(bot1) >= board:
			win =1
			text = font.render('OUT OF MOVES',10,BLACK)
			DISPLAY.blit(text, (WIDTH/2-50,50))

		# <-- Music ends --> #
		if pygame.mixer.music.get_busy() == False and Music_mode%2 ==0 :
			pygame.mixer.music.load("HoaTrongCamQuan.mp3")
			pygame.mixer.music.play()
		pygame.display.flip()
	clock.tick(FPS)
	pygame.display.flip()


# 5:0 PM - 03/03/2019 #
# --Chưa:
# Làm game Mới
# Chế độ chặn 2 đầu
# Đổi 2 bên players
# Background trong bàn bờ
# Đổi ký tự người chơi

# -- Mới:
# Reply trong phần 2 người chơi
# Menu mới
# Back to menu
# Sửa nút ấn vào
# Redo thơm ngon
# Save - Load game
# Chặn 2 đầu (Chưa sửa code vô luôn phần check để cho gọn!)