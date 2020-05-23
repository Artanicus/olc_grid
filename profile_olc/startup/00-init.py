import olc

c = olc.Coord('H59X')

print('Available objects: c')
print('c: {olc}, x:{x}, y:{y}'.format(olc=c.olc(), x=c.x, y=c.y))
