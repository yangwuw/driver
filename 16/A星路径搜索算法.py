import numpy as np
import heapq
import matplotlib.pyplot as plt
import time
 
 
# def heuristic(a, b):
#     return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
 
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
 
 
def astar(array, start, goal):
    close_set = set()
    parent_from_dict = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    open_list = []
    heapq.heappush(open_list, (fscore[start], start))
    while open_list:
        current = heapq.heappop(open_list)[1]  # return the smallest value
        if current == goal:
            route_loc = []
            while current in parent_from_dict:
                route_loc.append(current)
                current = parent_from_dict[current]
            # append start point to route and reorder route backward to get correct node sequence
            route_loc = route_loc + [start]
            route_loc = route_loc[::-1]
            return route_loc, close_set, open_list
 
        close_set.add(current)
 
        for i, j in neighbor_direction:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        # print('neighbor %s hit wall' % str(neighbor))
                        continue
                else:
                    # array bound y walls
                    # print('neighbor %s hit y walls' % str(neighbor))
                    continue
            else:
                # array bound x walls
                # print('neighbor %s hit x walls' % str(neighbor))
                continue
 
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
 
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                parent_from_dict[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (fscore[neighbor], neighbor))
    return None, close_set, open_list
 
 
def plot(layout, path=None, close_set=None, open_set=None):
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.imshow(layout, cmap=plt.cm.Dark2)
 
    ax.scatter(start[1], start[0], marker="o", color="red", s=200)
    ax.scatter(goal[1], goal[0], marker="*", color="green", s=200)
 
    if path:
        # extract x and y coordinates from route list
        x_coords = []
        y_coords = []
        for k in (range(0, len(path))):
            x = path[k][0]
            y = path[k][1]
            x_coords.append(x)
            y_coords.append(y)
 
        ax.plot(y_coords, x_coords, color="black")
 
    if close_set:
        for c in close_set:
            ax.scatter(c[1], c[0], marker='o', color='green')
 
    if open_set:
        for p in open_set:
            loc = p[1]
            ax.scatter(loc[1], loc[0], marker='x', color='blue')
 
    ax.xaxis.set_ticks(np.arange(0, layout.shape[1], 1))
    ax.yaxis.set_ticks(np.arange(0, layout.shape[0], 1))
    ax.xaxis.tick_top()
    plt.grid()
    plt.show()
 
 
if __name__ == '__main__':
    # neighbor_direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbor_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
    S = np.array([
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    ])
 
    start = (7, 3)
    goal = (7, 17)
 
    # S[(7, 12)] = 1
    # S[(7, 15)] = 1
 
    t_start = time.perf_counter()
    route, c_set, open_l = astar(S, start, goal)
    t_end = time.perf_counter()
    print(f"astar finished in {t_end - t_start:0.4f} seconds")
    if route:
        print(route)
        plot(S, route, c_set, open_l)
    else:
        plot(S, None, c_set, open_l)