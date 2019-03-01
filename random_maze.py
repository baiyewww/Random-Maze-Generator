from src.maze import map

import argparse

def get_parser():
	parser = argparse.ArgumentParser(description='parameters to generate maze')
	parser.add_argument('--width', default=30, help='Maze Width')
	parser.add_argument('--height',  default=30, help='Maze Height')
	parser.add_argument('--unitsize',  default=10, help='Maze Unit size')
	parser.add_argument('--start',  default=(0, 0), help='Start Coordinate')
	parser.add_argument('--end',  default=(29, 29), help='Destination Coordinate')
	args = parser.parse_args()
	return args



if __name__ == '__main__':
	args = get_parser()
	m = map(args.width, args.height, args.unitsize, args.start, args.end)
	path = m.generate_random_maze()
	print(path)