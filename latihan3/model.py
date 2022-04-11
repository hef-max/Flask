import cv2.cv2 as cv2
import cv2.data as cvd

face_cascade = cv2.CascadeClassifier(cvd.haarcascades + 'haarcascade_frontalface_default.xml')
ds_factor = 1

class VideoCamera(object):
	"""docstring for VideoCamera"""
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		ret, frame = self.video.read()

		frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation = cv2.INTER_AREA)
		gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in face_rects:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

		frame = cv2.putText(frame, 'Adit', (0, 35), 1, 3, (0, 255, 0), 2, cv2.FONT_HERSHEY_SIMPLEX)
		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tobytes()