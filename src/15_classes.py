# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return 'Waypoint { name = '+self.name+', lat = '+str(self.lat)+', lon = '+str(self.lon)+' }'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# # YOUR CODE HERE
class Geocache(Waypoint):

# YOUR CODE HERE
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return 'Geocache { name = '+self.name+', difficulty = '+str(self.difficulty)+', size = '+str(self.size)+', lat = '+str(self.lat)+', lon = '+str(self.lon)+' }'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521).__str__()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556).__str__()

# Print it--also make this print more nicely
print(geocache)
