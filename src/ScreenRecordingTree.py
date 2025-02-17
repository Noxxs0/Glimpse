# importing the required packages
import pyautogui
import cv2
import numpy as np
from interfaces.IScreenRecorder import IScreenRecorder

class ScreenRecorder(IScreenRecorder):
	def __init__ (self):
		print("hello")
		# self.__capture = False
		# self.__record = False
		# self.__grab = False
		# self.videoName = "example.mp4"
		# self.__output = self.videoName 
	
	def getLocations(self):
		print("danny")
	
		# Specify resolution
		resolution = (1920, 1080)

		# Specify video codec
		# codec = cv2.VideoWriter_fourcc(*"XVID")
		codec = cv2.VideoWriter_fourcc(*'mp4v')

		# Specify name of Output file
		filename = "Recording.mp4"

		# Specify frames rate. We can choose any 
		# value and experiment with it
		fps = 60.0


		# Creating a VideoWriter object
		out = cv2.VideoWriter(filename, codec, fps, resolution)

		# img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
		# height, width, channels = img.shape
		# self.out = cv2.VideoWriter(self.__output, fourcc, 10.0, (width, height))

		# Create an Empty window
		cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

		# Resize this window
		cv2.resizeWindow("Live", 480, 270)

		while True:
			# Take screenshot using PyAutoGUI
			img = pyautogui.screenshot()

			# Convert the screenshot to a numpy array
			frame = np.array(img)

			# Convert it from BGR(Blue, Green, Red) to
			# RGB(Red, Green, Blue)
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# Write it to the output file
			out.write(frame)

			# Optional: Display the recording screen
			cv2.imshow('Live', frame)

    	#Stop recording when we press 'q'
			if cv2.waitKey(1) == ord('q'):
				break
		
		# Release the Video writer
		out.release()

		# Destroy all windows
		cv2.destroyAllWindows()
		
		# #---- Second Try
		# img = pyautogui.screenshot()
	
		# img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
		# height, width, channels = img.shape
		# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
		# self.out = cv2.VideoWriter(self.__output, fourcc, 10.0, (width, height))

		# print("starting")
		# while True:
		# 	img = pyautogui.screenshot()

		# 	image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
		# 	self.out.write(image)
		# 	StopIteration(3)
		# 	# Stop recording when we press 'q'
		# 	if cv2.waitKey(1) == ord('q'):
		# 		break

		# 	cv2.imshow('Live', image)
		
		# print("stoped")
	

		# # Release the Video writer
		# 	self.out.release()

		# 	# Destroy all windows
		# 	cv2.destroyAllWindows()

recorder = ScreenRecorder()
recorder.getLocations()