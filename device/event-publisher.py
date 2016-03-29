import ibmiotf.device
import psutil
import time

configFilePath = 'device.cfg'
intervalTime = 1

def publishStatus():
	cpu_percent = psutil.cpu_percent(interval=None)
	virtual_memory_percent = psutil.virtual_memory().percent
	disk_usage = psutil.disk_usage('/').percent

	myData={'cpu_percent' : cpu_percent, 'virtual_memory_percent' : virtual_memory_percent, 'disk_usage' : disk_usage}

	return myData

try:
	options = ibmiotf.device.ParseConfigFile(configFilePath)
	client = ibmiotf.device.Client(options)
	client.connect()

	while True:
		myData = publishStatus()
		client.publishEvent("device_status", "json", myData)
		time.sleep(intervalTime)

	client.disconnect()
except ibmiotf.ConnectionException  as e:
	print e