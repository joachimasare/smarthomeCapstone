import time
import requests
import smarthome

#detected=0
#detected_buffer=0

class Detector:
	def __init__(self):
		self.detected = 0
		self.detected_buffer = 0

detector = Detector()

BASE_URL = "http://dd666c2f.ngrok.io/"

smarthome.GPIO.add_event_detect(smarthome.sound_sensor, smarthome.GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW

# assign function to GPIO PIN, Run function on change
smarthome.GPIO.add_event_callback(
	int(smarthome.sound_sensor), 
	lambda sound_sensor: smarthome.callback(sound_sensor, detector)
)

while True:
	response=requests.get(BASE_URL + "user/status")
	authorizations =  response.json()["status"]
	print (authorizations)
	if response.status_code == 200:
		sensor_data = {}
		if authorizations["temperature"] == "authorized":
			temperature=smarthome.take_temperature()
			sensor_data["temperature"] = temperature

		if authorizations["audio"] =="authorized":
			if detector.detected != detector.detected_buffer:
				sensor_data["audiofilename"] = "Cry detected"
				detector.detected_buffer = detector.detected
			else: 
				sensor_data["audiofilename"] = "No Cry detected"
		if authorizations["image"] == "authorized":
			#smarthome.take_photo()
			files = {'file': open('/home/pi/Desktop/image.jpg', 'rb')}
			sensor_data["imageFilename"] = "image.jpg"

		if authorizations["image"] == "authorized":
			response = requests.post(BASE_URL+ "user/recordings", data=sensor_data, files=files)
		else:
			response=requests.post(BASE_URL + "user/recording", json=sensor_data)
		print (response.status_code)
		print (response.json())
	time.sleep(3)
