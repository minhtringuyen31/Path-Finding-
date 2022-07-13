from queue import PriorityQueue
import BackGround
 

# Search Algorithms - find path 

Graph=BackGround.Graph
path= BackGround.path




def BFS(start, goal):
    cost_path = 0
    cost_expand=0
    queue = [start]
    #queue.append(start)  # Thêm đỉnh bắt đầu vào queue
    #expand=[]
    #expand.append(start)
    start.expanded = True  
    while queue:
        x = queue.pop(0)  # Xóa phần tử đầu khỏi queue
        x.expanded = True  # đặt lại vị trí đã đi qua
        cost_expand +=1
        if x == goal:
            #expand.append(goal)  
            while x.priority != start:  
                path.append(x.priority)  
                #expand.append(x)
                x = x.priority  
                x.path = True  # đặt lại path
                cost_path += 1
            # cost_expand=len(x.expanded)
            print("Cost expand: " ,cost_expand)
            print("Cost path: " ,cost_path)  # print cost
            return
        else:
            for neighbour_node in x.neighbour_nodes:
                if not neighbour_node.queue and not neighbour_node.wall and not neighbour_node.wall1 and not neighbour_node.wall2:  # kiểm tra
                    neighbour_node.priority = x  
                    neighbour_node.queue = True 
                    queue.append(neighbour_node)  # Thêm vào queue 
        BackGround.draw()  
    
    print("Not Path")  # In ra cmd nếu không tìm thấy đường đi




def UCS(start, goal): 
    cost_path=0
    cost_UCS = 0
    cost_expand=0
    frontier = PriorityQueue()  
    #expand=[]
    #expand.append(start)
    frontier.put((0, cost_UCS, start))  # thêm start vào queue
    start.expanded = True  
    weighted_graph = {game: float("inf") for row in Graph for game in row} 
    weighted_graph[start] = 0  
    while frontier and not frontier.empty(): 
        node = frontier.get()
        x=node[-1]
        x.expanded = True  
        cost_expand +=1
        if x == goal:
            #expand.append(goal)  
            while x.priority != start: 
                path.append(x.priority)  # Thêm vào path
                #expand.append(x)
                x = x.priority  # đi đến priority
                x.path = True  
                cost_path += 1  
            #cost_expand = len(expand)
            print("Cost expand: " ,cost_expand)
            print("Cost path: " ,cost_path)
            return
        else:
            for neighbour_node in x.neighbour_nodes:
                if not neighbour_node.queue and not neighbour_node.wall:  
                    neighbour_node.priority = x  # đặt priority bằng x
                    neighbour_node.queue = True  
                    weighted_graph[neighbour_node] = weighted_graph[x] + 1  # tính giá trị trọng số 
                    frontier.put((weighted_graph[neighbour_node], cost_UCS, neighbour_node)) # thêm vào queue 
                    cost_UCS += 1 # tăng cost +1 
        BackGround.draw()  
    print("Not Path") # In ra cmd nếu không tìm thấy đường đi




def IDS(start, goal, max_depth): 
    cost_path = 0
    cost_expand=0
    stack = []
    stack.append(start)  # Thêm start vào stack
    #expand=[]
    #expand.append(start)
    start.expanded = True  
    while len(stack) > 0:  # while stack không rỗng
        x = stack.pop()  # Xóa phần tử cuối ra khỏi stack
        x.expanded = True 
        cost_expand +=1
        #expand.append(x)
        if x == goal:  
            #expand.append(goal)
            while x.priority != start:  
                path.append(x.priority)  # Thêm vào path
                #expand.append(x)
                x = x.priority  # đi đến priority
                x.path = True 
                cost_path += 1 
            #cost_expand=len(expand)
            print("Cost expand: " , cost_expand)
            print("Cost path: " , cost_path)  
            return
        if max_depth <= 0 :
            print ("No Path")
            return 
        if x.level > max_depth: 
            continue  
        for neighbour_node in x.neighbour_nodes:
            if not neighbour_node.expanded and not neighbour_node.wall: 
                neighbour_node.priority = x # cài đặt priority 
                neighbour_node.queue = True  # cài đặt queue
                neighbour_node.level = x.level + 1  # cài đặt level 
                stack.append(neighbour_node)  
        BackGround.draw()   
    print("Not Path") # In ra cmd nếu không tìm thấy đường đi






def GBFS(start, goal):
    cost_path = 0
    cost_GBFS = 0
    cost_expand=0
    #expand=[]
    #expand.append(start)
    frontier = PriorityQueue()
    frontier.put((0, cost_GBFS, start))  # Thêm start vao queue
    start.expanded = True  
    hueris = {game: float("inf") for row in Graph for game in row}  
    hueris[start] = Heuristic((start.x, start.y),(goal.x, goal.y))  # Gán heuristic cho start
    while frontier and not frontier.empty():  
        node = frontier.get()  # lấy điểm node
        x=node[-1]
        x.expanded = True  
        cost_expand += 1
        if x == goal: 
            #expand.append(goal)
            while x.priority != start: 
                path.append(x.priority) 
                #expand.append(x)
                x = x.priority  
                x.path = True  
                cost_path += 1 
            #cost_expand = len(expand)
            print("Cost expand: " ,cost_expand)
            print("Cost path: " ,cost_path)
            return
        else:
            for neighbour_node in x.neighbour_nodes:
                if not neighbour_node.queue and not neighbour_node.wall:  
                    neighbour_node.priority = x 
                    neighbour_node.queue = True  
                    hueris[neighbour_node] = Heuristic((neighbour_node.x, neighbour_node.y),(goal.x, goal.y))  # Tính toán giá trị trọng số mới 
                    frontier.put((hueris[neighbour_node], cost_GBFS, neighbour_node)) 
                    cost_GBFS += 1  
        BackGround.draw()   
    print("Not Path") # In ra cmd nếu không tìm thấy đường đi





def AStar(start, goal):  
    cost_path = 0
    cost_expand=0
    cost_AStar = 0
    #expand=[]
    #expand.append(start)
    frontier = PriorityQueue()
    frontier.put((0, cost_AStar, start))  
    start.expanded = True  
    weighted_graph = {game: float("inf") for row in Graph for game in row}  # gán giá trị trọng số cho weighted_graph
    weighted_graph[start] = 0  
    hueris = {game: float("inf") for row in Graph for game in row}  
    hueris[start] = Heuristic((start.x, start.y), (goal.x, goal.y))  # Gán gía trị hue cho start
    while frontier and not frontier.empty(): 
        node = frontier.get() 
        x = node[-1]
        x.expanded = True 
        cost_expand += 1 
        if x == goal:  
            #expand.append(goal)
            while x.priority != start:
                path.append(x.priority)  
                #expand.append(x)
                x = x.priority 
                x.path = True  
                cost_path += 1  
            #cost_expand = len(expand)
            print("Cost expand: " ,cost_expand)
            print("Cost path: " ,cost_path)
            return
        else:
            for neighbour_node in x.neighbour_nodes:
                if not neighbour_node.queue and not neighbour_node.wall: 
                    neighbour_node.priority = x  # set priority
                    neighbour_node.queue = True  # cài đặt queue
                    weighted_graph[neighbour_node] = weighted_graph[x] + 1  # set g của neighbour_node đến g của node trước +1 
                    hueris[neighbour_node] = weighted_graph[neighbour_node] + Heuristic((neighbour_node.x, neighbour_node.y), (goal.x, goal.y))  # tính giá trị hue mới 
                    frontier.put((hueris[neighbour_node], cost_AStar, neighbour_node))  
                    cost_AStar += 1  
        BackGround.draw()  
    print("Not Path") # In ra nếu không tìm thấy 



def Heuristic(p1, p2):  
    x1, y1 = p1  # Điểm bắt đầu
    x2, y2 = p2  # điểm kết thúc
    return abs(x1 - x2) + abs(y1 - y2) #Khoảng cách