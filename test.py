from olc.olc.coordinates import Area
from pprint import pprint

def grid(a):
    g = [
            [str(a.NW), str(a.N), str(a.NE)],
            [str(a.W), str(a), str(a.E)],
            [str(a.SW), str(a.S), str(a.SE)]
            ]
    pprint(g)

a = Area(coords='60.62995351908941, 24.858076623722912')
b = Area(olc='9GG6JVH5+X6')

grid(a)
grid(b)
