import RPi.GPIO as GPIO
import sys

def inicializaBoard():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
def definePinoSaida(numeroPino):
    GPIO.setup(numeroPino, GPIO.OUT)
    
def definePinoEntrada(numeroPino):
    GPIO.setup(numeroPino,GPIO.IN)
    
def escrevePorta(numeroPino, estadoPorta):
    GPIO.output(numeroPino, estadoPorta)
