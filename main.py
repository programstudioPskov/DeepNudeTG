import sys
import cv2

from run import process

"""
main.py

 How to run:
 python3 main.py

"""

# ------------------------------------------------- main()
def maini(img):

	#Read input image
	dress = cv2.imread(img)
	#Process
	watermark = process(dress)

	# Write output image
	cv2.imwrite(f"output{img}", watermark)

	#Exit
	#process.kill()

if __name__ == '__main__':
	maini()