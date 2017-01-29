# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
from photobioreactor_sm import PhotobioreactorSM, LED
import json


clientId = "myClientId"
# For certificate based connection
myMQTTClient = AWSIoTMQTTClient(clientId)

# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
endpoint = "a3smi5m5yuwmr8.iot.us-west-2.amazonaws.com"
myMQTTClient.configureEndpoint(endpoint, 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
caPath = "/home/pi/aws_certs/newRootCa.pem"
privateKey = "/home/pi/aws_certs/7e543ab190-private.pem.key"
certificate = "/home/pi/aws_certs/7e543ab190-certificate.pem.crt"
myMQTTClient.configureCredentials(caPath, privateKey, certificate)
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect() 

# Setup the photobioreactor state machine
power_led = LED()
pbr = PhotobioreactorSM(power_led)

def callback(client, userdata, message): 
    print("Received a new message: ", message.payload)
    print("From topic: ", message.topic)
    data = json.loads(message.payload)
    pbr.trigger(data['power'])

topic = "codys/Autoreactor"

myMQTTClient.subscribe(topic+'/power/', 1, callback)

while True: 
	print "publishing to ", topic
        pbr_state = pbr.state
	myMQTTClient.publish(topic, pbr.state, 0)
	time.sleep(1)

