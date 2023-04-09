
busTime = [10, 15, 20, 30]
totalTrips = 15

def minimumBusTime(busTime, totalTrips):

    busTime.sort()
    trips = 0
    timeSum = 0
    time = 0
    unit = busTime[0]
    
    while trips < totalTrips:
        
        time += unit
        trips += sum([bus <= time for bus in busTime])
        
        if time >= busTime[-1]:
            timeSum += time
            time = 0
    
    return timeSum + time
    