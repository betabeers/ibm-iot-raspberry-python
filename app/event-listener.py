import ibmiotf.application

configFilePath = 'app.cfg'

def eventCallBack(event):
	print event.data

try:
	options = ibmiotf.application.ParseConfigFile(configFilePath)
	client = ibmiotf.application.Client(options)

	client.connect()
	client.deviceEventCallback = eventCallBack
	client.subscribeToDeviceEvents()

	while True:
		pass

	client.disconnect()

except ibmiotf.ConnectionException  as e:
	print e