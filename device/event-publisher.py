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

def commandCallback(cmd):
	print("Command received: %s" % cmd.data)
	if cmd.command == "reboot":
		if 'delay' not in cmd.data:
			restart(0)
		else:
			restart(cmd.data['delay'])

def restart(time):
	command = "/usr/bin/sudo /sbin/shutdown -r %s" % time
	import subprocess
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print output

try:
	options = ibmiotf.device.ParseConfigFile(configFilePath)
	client = ibmiotf.device.Client(options)
	client.connect()
	client.commandCallback = commandCallback

	while True:
		myData = publishStatus()
		client.publishEvent("device_status", "json", myData)
		time.sleep(intervalTime)

	client.disconnect()
except ibmiotf.ConnectionException  as e:
	print e