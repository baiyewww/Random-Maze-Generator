import BasicOperation as bo 
import cv2
import random

class map:
	def __init__(self, width_units, height_units, unit_width, start_point, end_point):
		self.width_units = width_units
		self.height_units = height_units
		self.unit_width  = unit_width

		self.maze = bo.create_new_img(width_units*unit_width, height_units*unit_width)
		self.start = start_point
		self.end   = end_point
		self.path  = []

	def generate_random_path(self):
		graph = [[False for i in range(self.width_units)] for j in range(self.height_units)]
		path  = [[[-1, -1] for i in range(self.width_units)] for j in range(self.height_units)]
		ans   = []
		stack = []
		now = self.start
		ans.append(now)
		stack.append(now)
		while len(stack) != 0:
			now = stack[len(stack) - 1]
			stack.pop(len(stack) - 1)
			
			if now == self.end:
				break

			graph[now[0]][now[1]] = True
			direction = random.randint(0, 3)
			if direction == 0:
				if now[0] - 1 >= 0 and graph[now[0] - 1][now[1]] == False:
					path[now[0] - 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] - 1, now[1]]))
				if now[0] + 1 <= self.height_units - 1 and graph[now[0] + 1][now[1]] == False:
					path[now[0] + 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] + 1, now[1]]))
				if now[1] - 1 >= 0 and graph[now[0]][now[1] - 1] == False:
					path[now[0]][now[1] - 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] - 1]))
				if now[1] + 1 <= self.width_units - 1 and graph[now[0]][now[1] + 1] == False:
					path[now[0]][now[1] + 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] + 1]))
			elif direction == 1:
				if now[0] + 1 <= self.height_units - 1 and graph[now[0] + 1][now[1]] == False:
					path[now[0] + 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] + 1, now[1]]))
				if now[0] - 1 >= 0 and graph[now[0] - 1][now[1]] == False:
					path[now[0] - 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] - 1, now[1]]))
				if now[1] - 1 >= 0 and graph[now[0]][now[1] - 1] == False:
					path[now[0]][now[1] - 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] - 1]))
				if now[1] + 1 <= self.width_units - 1 and graph[now[0]][now[1] + 1] == False:
					path[now[0]][now[1] + 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] + 1]))
			elif direction == 2:
				if now[1] - 1 >= 0 and graph[now[0]][now[1] - 1] == False:
					path[now[0]][now[1] - 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] - 1]))
				if now[0] - 1 >= 0 and graph[now[0] - 1][now[1]] == False:
					path[now[0] - 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] - 1, now[1]]))
				if now[0] + 1 <= self.height_units - 1 and graph[now[0] + 1][now[1]] == False:
					path[now[0] + 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] + 1, now[1]]))
				if now[1] + 1 <= self.width_units - 1 and graph[now[0]][now[1] + 1] == False:
					path[now[0]][now[1] + 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] + 1]))
			elif direction == 3:
				if now[1] + 1 <= self.width_units - 1 and graph[now[0]][now[1] + 1] == False:
					path[now[0]][now[1] + 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] + 1]))
				if now[0] - 1 >= 0 and graph[now[0] - 1][now[1]] == False:
					path[now[0] - 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] - 1, now[1]]))
				if now[0] + 1 <= self.height_units - 1 and graph[now[0] + 1][now[1]] == False:
					path[now[0] + 1][now[1]] = [now[0], now[1]]
					stack.append(tuple([now[0] + 1, now[1]]))
				if now[1] - 1 >= 0 and graph[now[0]][now[1] - 1] == False:
					path[now[0]][now[1] - 1] = [now[0], now[1]]
					stack.append(tuple([now[0], now[1] - 1]))

		e = path[self.end[0]][self.end[1]]
		ans.insert(0, self.end)
		while e[0] != self.start[0] or e[1] != self.start[1]:
			e = path[e[0]][e[1]]
			ans.insert(0, e)
		return ans[:len(ans)-1]

	def draw_path(self, interval=100):
		path = self.generate_random_path()
		dir_path = []
		cannot_list = []
		for i in range(len(path) - 1):
			now = path[i]
			nex = path[i + 1]
			if now[0] == nex[0] and now[1] + 1 == nex[1]:
				dir_path.append([[now[0], now[1]], 0])    # Long Right    | -|- |
			elif now[0] == nex[0] and now[1] - 1 == nex[1]:
				dir_path.append([[now[0], now[1]], 1])    # Long Left  | -|- |
			elif now[0] + 1 == nex[0] and now[1] == nex[1]:  #   Down
				dir_path.append([[now[0], now[1]], 2])
			elif now[0] - 1 == nex[0] and now[1] == nex[1]:
				dir_path.append([[now[0], now[1]], 3])
			else:
				dir_path.append('#')

		for i in dir_path:
			cv2.imshow('Image', self.maze)
			cv2.waitKey(interval)
			if isinstance(i, type('#')):
				break
			if i[1] == 0:
				now_center = (i[0][1] * self.unit_width + int(self.unit_width/2), i[0][0] * self.unit_width + int(self.unit_width/2))
				nex_center = (now_center[0] + self.unit_width, now_center[1])
				cannot_start = (i[0][1] * self.unit_width + self.unit_width, i[0][0] * self.unit_width)
				cannot_end   = (i[0][1] * self.unit_width + self.unit_width, i[0][0] * self.unit_width + self.unit_width)
				cannot_list.append([cannot_start, cannot_end])
				bo.draw_line(self.maze, now_center, nex_center, (0,0,255), 1)
			elif i[1] == 1:
				now_center = (i[0][1] * self.unit_width + int(self.unit_width/2), i[0][0] * self.unit_width + int(self.unit_width/2))
				nex_center = (now_center[0] - self.unit_width, now_center[1])
				cannot_start = (i[0][1] * self.unit_width, i[0][0] * self.unit_width)
				cannot_end   = (i[0][1] * self.unit_width, i[0][0] * self.unit_width + self.unit_width)
				cannot_list.append([cannot_start, cannot_end])
				bo.draw_line(self.maze, now_center, nex_center, (0,0,255), 1)
			elif i[1] == 2:
				now_center = (i[0][1] * self.unit_width + int(self.unit_width/2), i[0][0] * self.unit_width + int(self.unit_width/2))
				nex_center = (now_center[0], now_center[1] + self.unit_width)
				cannot_start = (i[0][1] * self.unit_width, i[0][0] * self.unit_width + self.unit_width)
				cannot_end   = (i[0][1] * self.unit_width + self.unit_width, i[0][0] * self.unit_width + self.unit_width)
				cannot_list.append([cannot_start, cannot_end])
				bo.draw_line(self.maze, now_center, nex_center, (0,0,255), 1)
			elif i[1] == 3:
				now_center = (i[0][1] * self.unit_width + int(self.unit_width/2), i[0][0] * self.unit_width + int(self.unit_width/2))
				nex_center = (now_center[0], now_center[1] - self.unit_width)
				cannot_start = (i[0][1] * self.unit_width, i[0][0] * self.unit_width)
				cannot_end   = (i[0][1] * self.unit_width + self.unit_width, i[0][0] * self.unit_width)
				cannot_list.append([cannot_start, cannot_end])
				bo.draw_line(self.maze, now_center, nex_center, (0,0,255), 1)
		return cannot_list
		# bo.show_img_obj(self.maze)


	def generate_random_maze(self, interval=100):
		path = self.generate_random_path()
		print(path)
		cannot_list = self.draw_path(interval=interval)

		for i in range(self.height_units):
			cv2.imshow('Image', self.maze)
			cv2.waitKey(interval)
			for j in range(self.width_units):
				random_up   = random.randint(0, 1)
				random_down = random.randint(0, 1)
				random_left = random.randint(0, 1)
				random_right= random.randint(0, 1)

				if random_up == 1:  # Left_Down
					s = (i*self.unit_width, j*self.unit_width)
					e = (i*self.unit_width, j*self.unit_width + self.unit_width)
					if [s, e] not in cannot_list:
						bo.draw_line(self.maze, s, e, (255, 255, 255), 2)
				if random_down == 1: # Right_down
					s = (i*self.unit_width + self.unit_width, j*self.unit_width)
					e = (i*self.unit_width + self.unit_width, j*self.unit_width + self.unit_width)
					if [s, e] not in cannot_list:
						bo.draw_line(self.maze, s, e, (255, 255, 255), 2)
				if random_left == 1: # UP_Left
					s = (i*self.unit_width, j*self.unit_width)
					e = (i*self.unit_width + self.unit_width, j*self.unit_width)
					if [s, e] not in cannot_list:
						bo.draw_line(self.maze, s, e, (255, 255, 255), 2)
				if random_right == 1: # Down_Right
					s = (i*self.unit_width, j*self.unit_width + self.unit_width)
					e = (i*self.unit_width + self.unit_width, j*self.unit_width + self.unit_width)
					if [s, e] not in cannot_list:
						bo.draw_line(self.maze, s, e, (255, 255, 255), 2)
		bo.show_img_obj(self.maze)


if __name__ == '__main__':
	m = map(30, 30, 10, (0, 0), (29, 29))
	path = m.generate_random_maze()
	print(path)