import pygame
import math 
from pygame.locals import *
Graph=[]
path=[]
# expanded=[]

def ReadFile(mode):
    f = open(mode,"r")  # Mở file
    columns, rows = [int(x) for x in f.readline().split()]  # Đọc số hàng và cột
    for i in range(columns):  # Tạo Graph
        Graph.append([])  # Thêm hàng
        for j in range(rows):  # Thêm cột
            Graph[i].append(game(i, j, columns, rows)) 
    for i in range(columns):
        for j in range(rows):
            Graph[i][j].set_neighbour_nodes()
    Pointss = []  # Danh sách điểm
    Obstacle = []  # Danh sách số trở ngại phải đi qua
    start_x, start_y, goal_x, goal_y = [int(x) for x in f.readline().split()]  # Đọc điểm start và goal
    PointssCount = eval(f.readline())  # Đọc số trở ngại
    for i in range(PointssCount):
        Pointss = f.readline()  # read Pointssgon
        Pointss = [int(x) for x in Pointss.split()]  # Chuyển đổi qua list
        temp = []  # temporary list
        for j in range(0, int(len(Pointss) / 2)):  
            temp.append((Pointss[j * 2], Pointss[j * 2 + 1]))  
        Obstacle = temp  
        for j in range(0, len( Obstacle)):
            if (j == len( Obstacle) - 1):  
                Bresenham_Alg( Obstacle[j],  Obstacle[0]) 
            else:
                Bresenham_Alg( Obstacle[j],  Obstacle[j + 1])  
    f.close()
    return  columns, rows, start_x, start_y, goal_x, goal_y

# Hàm lấy điểm start goal để tạo đường đi
def Start_Goal_Point():
    start = Graph[start_x][start_y]  
    start.start = True  
    goal = Graph[goal_x][goal_y]  
    goal.goal = True 
    return start, goal 


# Sử dụng pygame để tạo nên màn hình path finding
class game: 
    def __init__(self, i, j, col, row):  
        self.x = i
        self.y = j  
        self.col=col
        self.row= row
        self.start = False  
        self.wall = False 
        self.wall1 = False 
        self.wall2 = False 
        self.goal = False   
        self.queue = False  
        self.expanded = False 
        self.neighbour_nodes = []  
        self.priority = None  
        self.level = 0  
    
    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * game_width, self.y * game_height, game_width, game_height))

    def set_neighbour_nodes(self):
        if self.y > 0:  
            self.neighbour_nodes.append(Graph[self.x][self.y - 1])  # Thêm neighbour_node vào trên
        if self.x < self.col - 1:  
            self.neighbour_nodes.append(Graph[self.x + 1][self.y])  # Thêm neighbour_node vào phải
        if self.y < self.row - 1: 
            self.neighbour_nodes.append(Graph[self.x][self.y + 1])  # Thêm neighbour_node vào dưới
        if self.x > 0: 
            self.neighbour_nodes.append(Graph[self.x - 1][self.y])  # Thêm neighbour_node vào trái

    def __lt__(self, other):
        return False


def Bresenham_Alg(p0, p1):  # Giải thuật Bresenham đường thẳng đa giác
    x0, y0 = p0  # Điểm bắt đầu
    x1, y1 = p1  # Điểm kết thúc 
    dx = abs(x1 - x0) 
    dy = abs(y1 - y0)  
    x_point, y_point = x0, y0  # Điểm
    sx = -1 if x0 > x1 else 1  
    sy = -1 if y0 > y1 else 1  
    if dx > dy:  
        temp = dx / 2.0
        while x_point != x1:
            Graph[x_point][y_point].wall = True
              
            temp -= dy  
            if temp < 0:
                y_point += sy 
                temp += dx  
            x_point += sx  
    else:
        temp = dy / 2.0
        while y_point != y1:
            Graph[x_point][y_point].wall = True  
            temp -= dx  
            if temp < 0:
                x_point += sx  
                temp += dy  
            y_point += sy  
    Graph[x_point][y_point].wall = True 


columns, rows, start_x, start_y, goal_x, goal_y=ReadFile("input.txt")



#Kích thước màn hình trò chơi
window = pygame.display.set_mode((790,640),0,32)  # Tạo cửa sổ 
pygame.display.set_caption('Path_Finding')


YELLOW = (255,215,0)   #goal 
GRAY = (169,169,169)  #path
RED = (255, 0, 0)  #start
WHILE = (255, 255, 255)  #block
GREEN = (43, 167, 107) #wall
WHITE_COLOR = (76, 173, 162)  #grip
PINK = (255,182,193)  #unexpand
BLUE = (135,206,250)  #expand
GREEN1 = (255,182,193)
GREEN2 = (255,215,0)

game_width = 35
game_height = 35



window_width = columns * game_width
window_height = rows * game_height
def draw_Graph(win):
    for j in range(columns):
        pygame.draw.line(win, WHITE_COLOR, (j * game_width, 0), (j * game_width, window_height))
        for i in range(rows):
            pygame.draw.line(win, WHITE_COLOR, (0, i * game_height), (window_width, i * game_height))

def draw():  
    window.fill(WHILE)  # Tô màu 
    for i in range(columns):
        for j in range(rows):
            game = Graph[i][j]  
            game.draw(window, WHILE)  
            if game.queue:
                game.draw(window, PINK) 
            if game.expanded:  
                game.draw(window, BLUE)  
            if game in path:  
                game.draw(window, GRAY)
            if game.start:  
                game.draw(window, RED)  
            if game.wall: 
                game.draw(window, GREEN) 
            if game.wall1: 
                game.draw(window, GREEN1) 
            if game.wall2: 
                game.draw(window, GREEN2)    
            if game.goal:  
                game.draw(window, YELLOW) 
            # if game in expanded:  
            #     game.draw(window, EXPAND) 
    draw_Graph(window)  
    window.blit(pygame.transform.flip(window, False, True), (0, 0))  
    pygame.display.flip()  




mainClock = pygame.time.Clock()
from pygame.locals import*

pygame.init()
pygame.display.set_caption('Path Finding')

font= pygame.font.SysFont('Helvetica',35)



#Hàm tạo văn bản trên màn pygame window
def drawtext(text, font, color,surface ,x,y):
	textobj= font.render(text,1,color)
	textrect=textobj.get_rect()
	textrect.topleft= (x,y)
	surface.blit(textobj,textrect)

#Hàm tạo nút button trên màn pygame window
def drawButtonOut(screen, x, y, width, height, text, color):
        pygame.draw.rect(
            screen,
            color,
            (x-5, y-5, width+10, height+10)            
        )
        pygame.draw.line(screen, "white", (x,y), (x+width, y), 2)
        pygame.draw.line(screen, "white", (x,y), (x, y+height), 2)
        pygame.draw.line(screen, "white", (x,y+height), (x+width, y+height), 2)
        pygame.draw.line(screen, "white", (x+width,y), (x+width, y+height), 2)

        label = font.render(text, True, 'white')
        text_rect = label.get_rect(center = (x + width/2, y + height/2))
        screen.blit(label, text_rect)
        return pygame.Rect(x-5, y-5, width+10, height+10)