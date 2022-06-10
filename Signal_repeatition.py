def repeatition_of_signals():
    global currentGreen, currentYellow, nextGreen
    while (signals[currentGreen].green > 0):
        for i in range(0, Signalcount):
            if (i == currentGreen):                              # timer at corresponding signal.
                if (currentYellow == 0):
                    signals[i].green -= 1
                else:
                    signals[i].yellow -= 1
            else:
                signals[i].red -= 1
        time.sleep(1)
    currentYellow = 1
    while (signals[currentGreen].yellow > 0):
        for i in range(0, Signalcount):
            if (i == currentGreen):                             # timer at corresponding signal.
                if (currentYellow == 0):
                    signals[i].green -= 1
                else:
                    signals[i].yellow -= 1
            else:
                signals[i].red -= 1
        time.sleep(1)
    currentYellow = 0

    signals[currentGreen].green = Green          # updating the signal values to default values.
    signals[currentGreen].yellow = Yellow
    signals[currentGreen].red = Red

    currentGreen = nextGreen
    nextGreen = (currentGreen + 1) % Signalcount
    repeatition_of_signals()
