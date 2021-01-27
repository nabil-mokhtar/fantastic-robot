import RPi.GPIO as GPIO
from time import sleep
import pika, sys, os,json

############################################################################################### MQ connection setup.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
       TasksDecoder(json.loads(body))

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
############################################################################################### middleware >_< .

def TasksDecoder(dictTasks):


############################################################################################### motor part.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
class motor():
    def __init__(self,Ena,In1,In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)
    def moveF(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        sleep(t)
    def moveB(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        sleep(t)
    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)