speeds = {'car':2, 'bus':1, 'truck':0.5, 'bike':2.5}

x = {"right":[0,0,0], "down":[755,727,697], "left":[1400,1400,1400], "up":[602,627,657]}
y = {"right":[348,370,398], "down":[0,0,0], "left":[498,466,436], "up":[800,800,800]}

vehicles = {"right": {1:[], 2:[]}, "down": {1:[], 2:[]}, "left": {1:[], 2:[]}, "up": {1:[], 2:[]}}
vehicletypes = {0:"car", 1:"bus", 2:"truck", 3:"bike"}
directionnum = {0:"right", 1:"down", 2:"left", 3:"up"}

# Coordinates of stop lines
stoplines = {"right": 590, "down": 330, "left": 800, "up": 535}
defaultstop = {"right": 580, "down": 320, "left": 810, "up": 545}

# Gap between vehicles
stoppingGap = 15    # stopping gap
movingGap = 15   # moving gap
