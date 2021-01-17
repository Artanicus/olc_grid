from openlocationcode import openlocationcode as olclib
from box import Box

class Area:
    def __init__(self, olc=None, coords=None, get_grid=True):
        self.coords = Box()
        if olc:
            self.olc = olc
            decoded = olclib.decode(olc)
            self.coords.lat = decoded.latitudeLo
            self.coords.lon = decoded.longitudeLo
        elif coords:
            if isinstance(coords, Box):
                self.coords = coords
            elif isinstance(coords, str):
                self.coords.lat = float(coords.split(',')[0])
                self.coords.lon = float(coords.split(',')[1])
            else:
                raise ValueError('Invalid coordinates: {}'.format(coords))
            self.olc = olclib.encode(self.coords.lat, self.coords.lon)
        else:
            raise ValueError('Invalid OLC: {code}'.format(code=olc))
        self.increment_lat = 0.0025 # Comes from the grid split by 20: ((1/20)/20)
        self.increment_lon = 0.0025 # grids are symmetrical even if the globe isn't

        if get_grid:
            self.get_grid()

    def get_grid(self):
        self.N = Area(coords=self.shift(1,0), get_grid=False)
        self.NE = Area(coords=self.shift(1,1), get_grid=False)
        self.E = Area(coords=self.shift(0,1), get_grid=False)
        self.SE = Area(coords=self.shift(-1,1), get_grid=False)
        self.S = Area(coords=self.shift(-1,0), get_grid=False)
        self.SW = Area(coords=self.shift(-1,-1), get_grid=False)
        self.W = Area(coords=self.shift(0,-1), get_grid=False)
        self.NW = Area(coords=self.shift(1,-1), get_grid=False)

    def shift(self, lat_delta, lon_delta):
        coords = Box()
        coords.lat = self.coords.lat + (lat_delta * self.increment_lat)
        coords.lon = self.coords.lon + (lon_delta * self.increment_lon)
        return coords

    def __str__(self):
        return self.olc
