import cv2
import numpy as np 


# ------------------------------Read/Show/Write Image-------------------------
def read_img(img_path):
	'''
	Input : img_path
	Output: img_obj
	'''
	try:
		img = cv2.imread(img_path)
	except:
		print("*** Error: Img read error!", img_path)
		return None
	if isinstance(img, type(None)):
		print("*** Error: Cannot find img:", img_path)
		return None
	return img

def show_img(img_path, name='Image', waitKey=0):
	'''
	It will new a window with auto size and print the img.
	WaitKey means the window will wait for the keyboard to input. If there are some inputs in the time, it will return the ascii code. Either it will return -1.
	If the value == 0, means it will continuous wait.
	'''
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	img = read_img(img_path)
	cv2.imshow(name, img)
	cv2.waitKey(waitKey)
	cv2.destroyAllWindows()

def show_img_obj(img_obj, name='Image', waitKey=0):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	cv2.imshow(name, img_obj)
	cv2.waitKey(waitKey)
	cv2.destroyAllWindows()

def write_img(img_path, img_obj):
	cv2.imwrite(img_path, img_obj)
# ----------------------------------------------------------------------------

# --------------------------Draw pictures-------------------------------------
''' Example to draw a line and show
img = create_new_img(300, 400)
draw_line(img, (0, 0), (100, 100), (255,255,0), 7)
show_img_obj(img)
'''

def create_new_img(width, height):
	'''
	Create a new RGB [black] picture.
	'''
	img = np.zeros((width, height, 3), np.uint8)
	return img

def draw_line(img, start_coord, end_coord, color, pix_width):
	'''
	cv2.line(img, (0, 0), (511, 511), (255,255,0), 7)
	'''
	cv2.line(img, start_coord, end_coord, color, pix_width)

def draw_rect(img, vertex_left, vertex_right, color, pix_width):
	'''
	cv2.rectangle(img, (0, 0), (100, 100), (255, 255, 0), 7)
	'''
	cv2.rectangle(img, vertex_left, vertex_right, color, pix_width)

def draw_circle(img, center, radius, color, pix_width):
	'''
	cv2.circle(img, (200, 200), 50, (255, 255, 0), 1)
	If pix_width == -1, full painted.
	'''
	cv2.circle(img, center, radius, color, pix_width)

def draw_polylines(img, pts, is_closed, color, pix_width):
	'''
	pts = np.array([[0, 20], [20, 30], [70, 80]], np.int32)
	Polylines consists of many points.
	'''
	cv2.polylines(img, [pts], is_closed, color, pix_width)

# ----------------------------------------------------------------------------
def cvtColor(img, flag=cv2.COLOR_BGR2HSV):
	img = cv2.cvtColor(img, flag)
	return img

def resize(img, re_size, interpolation=cv2.INTER_CUBIC):
	return cv2.resize(img, re_size, interpolation)

if __name__ == '__main__':
	img = read_img('111.jpeg')
	img = resize(img, (2*img.shape[0], 2*img.shape[1]))
	show_img_obj(img)


# ----------------------------------------------------------------------------
# def draw_text(img, text, font=cv2.FONT_HERSHEY_SIMPLEX, pixel_size=4, )
