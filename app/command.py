import ibmiotf.application

configFilePath = 'app.cfg'

def messageReboot(delay):
	commandData={'delay' : delay}
	client.publishCommand("raspi-demo", "raspi-demo", "reboot", "json", commandData)

try:
	options = ibmiotf.application.ParseConfigFile(configFilePath)
	client = ibmiotf.application.Client(options)

	client.connect()

	messageReboot(1)

	client.disconnect()

except ibmiotf.ConnectionException  as e:
	print e