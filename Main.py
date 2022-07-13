
# Class 20CLC01 - Term III/2021-2022
# Course: CSC14003 - Artificial Intelligence
# PROJECT 01: SERCH
# PATH FINDING

# Hoang Huu Minh An  - 20127102
# Nguyen Vo Minh Tri - 20127364
# Phan Minh Xuan     - 20127395




from Search import BFS
from Search import UCS
from Search import IDS
from Search import GBFS
from Search import AStar
from BackGround import draw
from BackGround import Start_Goal_Point
from BackGround import drawtext
from BackGround import drawButtonOut
import pygame 
import sys



mainClock = pygame.time.Clock()
from pygame.locals import*
font= pygame.font.SysFont('Helvetica',35)
screen = pygame.display.set_mode((785,635),0,32)
screen.fill((135,206,250))


# Create buttons
button_1=drawButtonOut(screen,350,100,100,50,"BFS",(255,0,0))
button_2=drawButtonOut(screen,350,200,100,50,"UCS",(255,0,0))
button_3=drawButtonOut(screen,350,300,100,50,"IDS",(255,0,0))
button_4=drawButtonOut(screen,350,400,100,50,"GBFS",(255,0,0))
button_5=drawButtonOut(screen,350,500,100,50,"A*",(255,0,0))
drawtext("SEARCH  ALGORITHMS",font,(255,0,0),screen, 20,50)
drawtext("ENTER ESC TO EXIT",font,(255,0,0),screen, 490,550)

#Hàm gọi BFS , vẽ đường đi trên pygame 
def BFS_1(): 
    start, goal=Start_Goal_Point()
    Search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()   
        pygame.display.update()
        if Search :
                print("Breadth First Search (BFS) Algorithm")
                BFS(start, goal)
        Search = False
       
#Hàm gọi UCS , vẽ đường đi trên pygame 
def UCS_1():
    start, goal=Start_Goal_Point()
    Search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        if Search :
                print("Uniform Cost Search (UCS) Algorithm")
                UCS(start, goal)
        Search = False



#Hàm gọi IDS , vẽ đường đi trên pygame 
def IDS_1(): 
    start, goal=Start_Goal_Point()
    Search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        if Search :
                print("Iterative Deepening Search (IDS) Algorithm")
                IDS(start, goal,50)
        Search = False


#Hàm gọi GBFS , vẽ đường đi trên pygame 
def GBFS_1(): 
    start, goal=Start_Goal_Point()
    Search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        if Search :
                print("Greedy Best First Search (GBFS) Algorithm")
                GBFS(start, goal)
        Search = False


#Hàm gọi A* , vẽ đường đi trên pygame 
def AStar_1(): 
    start, goal=Start_Goal_Point()
    Search = True
    while True:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        if Search :
                print("Graph Search A* (AStar) Algorithm")
                AStar(start, goal)
        Search = False






def main():
	click= False
	while True:
		mx,my=pygame.mouse.get_pos()

		if button_1.collidepoint(mx,my):
			if click:
				BFS_1()
		if button_2.collidepoint(mx,my):
			if click:
				UCS_1()
		if button_3.collidepoint(mx,my):
			if click:
				IDS_1()
		if button_4.collidepoint(mx,my):
			if click:
				GBFS_1()

		if button_5.collidepoint(mx,my):
			if click:
				AStar_1()
		click=False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				if event.button ==1:
					click=True
		pygame.display.update()
		mainClock.tick(60)
main()

		
