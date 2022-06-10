import time
import pygame
import threading
import random

signalCoods = [(530, 230), (810, 230), (810, 570), (530, 570)]
TimerCoods = [(530, 210), (810, 210), (810, 550), (530, 550)]

Signalcount = 4
currentGreen = 0
currentYellow = 0
Green = 5
Red = 120
Yellow = 5
signals = []
nextGreen = (currentGreen + 1) % Signalcount
