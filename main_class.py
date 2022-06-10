class main:

    black = (0, 0, 0)
    white = (255, 255, 255)
    FONT = pygame.font.Font(None, 30)

    thread1 = threading.Thread(name="signalnumber", target=signal_num, args=())
    thread1.daemon = True                                                             # runs in background simultaneously
    thread1.start()                                                                   # calling the thread.

    background = pygame.image.load('images/intersection.png')
    pygame.display.set_caption("TRAFFIC LIGHT SIMULATION")
    redsignal = pygame.image.load('images/signals/red.png')
    yellowsignal = pygame.image.load('images/signals/yellow.png')
    greensignal = pygame.image.load('images/signals/green.png')

    display_surface = pygame.display.set_mode((1400, 922))

    thread2 = threading.Thread(name="vehiclegeneration", target=vehicle_generation, args=())
    thread2.daemon = True
    thread2.start()

    running = True
    while running:
        for event in pygame.event.get():                    # doesn't quit untill we press the close button.
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background, (0, 0))

        for i in range(0, Signalcount):                                               # display of signals according to the timer.
            if (i == currentGreen):
                if (currentYellow == 0):
                    signals[i].signalText = signals[i].green
                    display_surface.blit(greensignal, signalCoods[i])
                else:
                    signals[i].signalText = signals[i].yellow
                    display_surface.blit(yellowsignal, signalCoods[i])

            else:
                if (signals[i].red <= 10):
                    signals[i].signalText = signals[i].red
                else:
                    signals[i].signalText = "---"
                display_surface.blit(redsignal, signalCoods[i])


            signalTexts = ["", "", "", ""]
            for i in range(0, Signalcount):                                                  # display of the timer.
                signalTexts[i] = FONT.render(str(signals[i].signalText), True, white, black)
                display_surface.blit(signalTexts[i], TimerCoods[i])


            for vehicle in simulation:
                display_surface.blit(vehicle.image, [vehicle.x, vehicle.y])
                vehicle.movement_of_vehicles()

        pygame.display.update()
