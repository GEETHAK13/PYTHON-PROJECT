pygame.init()           # for blit and font functions.
simulation = pygame.sprite.Group()     # It includes methods for collision detection and makes updating positions and rendering of sprites(vehicles) much easier.

class Signalcolour:
    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.signalText = ""


def signal_num():
    signal1 = Signalcolour(Red, Yellow, Green)
    signals.append(signal1)
    signal2 = Signalcolour(Red, Yellow, Green)
    signals.append(signal2)
    signal3 = Signalcolour(Red, Yellow, Green)
    signals.append(signal3)
    signal4 = Signalcolour(Red, Yellow, Green)
    signals.append(signal4)
