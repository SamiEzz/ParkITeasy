import math

def getDistance(p1,p2):
    lat1deg=p1.lat
    lat2deg=p2.lat
    lon1deg=p1.lon
    lon2deg=p2.lon
    R = 6373.0 # radius of the Earth

    # coordinates
    lat1 = math.radians(lat1deg)
    lon1 = math.radians(lon1deg)
    lat2 = math.radians(lat2deg)
    lon2 = math.radians(lon2deg)

    #change in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    # Haversine formula
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
