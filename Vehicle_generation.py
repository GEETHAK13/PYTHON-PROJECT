def movement_of_vehicles(self):                                     # controlling the movement of the vehicles w.r.t signals and vehicles ahead.

        if (self.direction == 'right'):
            if (self.crossed == 0 and self.x + self.image.get_rect().width > stoplines[self.direction]):
                self.crossed = 1
            if ((self.x + self.image.get_rect().width <= self.stop or self.crossed == 1 or (currentGreen == 0 and currentYellow == 0)) and (self.index == 0 or self.x + self.image.get_rect().width < (vehicles[self.direction][self.lane][self.index-1].x - movingGap))):
                self.x += self.speed

        elif (self.direction == 'down'):
            if (self.crossed == 0 and self.y + self.image.get_rect().height > stoplines[self.direction]):
                self.crossed = 1
            if ((self.y + self.image.get_rect().height <= self.stop or self.crossed == 1 or (currentGreen == 1 and currentYellow == 0)) and (self.index == 0 or self.y + self.image.get_rect().height < (vehicles[self.direction][self.lane][self.index - 1].y - movingGap))):
                self.y += self.speed

        elif (self.direction == 'left'):
            if (self.crossed == 0 and self.x < stoplines[self.direction]):
                self.crossed = 1
            if ((self.x >= self.stop or self.crossed == 1 or (currentGreen == 2 and currentYellow == 0)) and (self.index == 0 or self.x > (vehicles[self.direction][self.lane][self.index - 1].x + vehicles[self.direction][self.lane][self.index - 1].image.get_rect().width + movingGap))):
                self.x -= self.speed               # from right to left x decreases.

        elif (self.direction == 'up'):
            if (self.crossed == 0 and self.y < stoplines[self.direction]):
                self.crossed = 1
            if ((self.y >= self.stop or self.crossed == 1 or (currentGreen == 3 and currentYellow == 0)) and (self.index == 0 or self.y > (vehicles[self.direction][self.lane][self.index - 1].y + vehicles[self.direction][self.lane][self.index - 1].image.get_rect().height + movingGap))):
                self.y -= self.speed             # from down to up y decreases.

def vehicle_generation():              # generating vehicles randomly in random direction.
    while(True):
        vehicle_type = random.randint(0,3)
        lane_number = random.randint(1,2)
        direction_number = random.randint(0,3)
        Vehicle(lane_number, vehicletypes[vehicle_type], directionnum[direction_number])        # function call of the vehicle class.
        time.sleep(1)
