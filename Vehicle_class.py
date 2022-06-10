class Vehicle(pygame.sprite.Sprite):
    def __init__(self, lane, vehicletype, direction):
        pygame.sprite.Sprite.__init__(self)                 # runs the built-in Sprite classes initializer.
        self.lane = lane
        self.vehicletype = vehicletype
        self.speed = speeds[vehicletype]
        self.direction = direction
        self.x = x[direction][lane]    # current x coordinate.
        self.y = y[direction][lane]    # current y coordinate.
        self.crossed = 0
        vehicles[direction][lane].append(self)
        self.index = len(vehicles[direction][lane])-1     #position of the vehicle among the vehicles moving in the same direction,same lane.
        path = "images/" + direction + "/" + vehicletype + ".png"
        self.image = pygame.image.load(path)
        self.stop = defaultstop[direction]        # vehicles to stop by default

        if (direction == 'right'):                       #sets x to position after the vehicle
            const = self.image.get_rect().width + stoppingGap
            self.x -= const
        elif (direction == 'left'):
            const = self.image.get_rect().width + stoppingGap
            self.x += const
        elif (direction == 'down'):
            const = self.image.get_rect().height + stoppingGap
            self.y -= const
        elif (direction == 'up'):
            const = self.image.get_rect().height + stoppingGap
            self.y += const
        simulation.add(self)                   # adding the vehicles in a group from random directions.

    def render(self, display_surface):
        display_surface.blit(self.image, (self.x, self.y))         # displaying the image onto the screen.
