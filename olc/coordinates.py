class Coord:
    def east(self):
        kwargs = self._horiz(1)
        return Coord(**kwargs)
    def west(self):
        kwargs = self._horiz(-1)
        return Coord(**kwargs)
    def south(self):
        kwargs = self._vert(-1)
        return Coord(**kwargs)
    def north(self):
        kwargs = self._vert(1)
        return Coord(**kwargs)
    
    def olc(self):
        return self.yH + self.xH + self.yL + self.xL

    def __init__(self, olc = None, xH = None, yH = None, xL = None, yL = None, **kwargs):
        self.chars = "23456789CFGHJMPQRVWX"
        self.space = list(self.chars)
        self.base = len(self.space)
        if olc:
            self.yH = olc[0]
            self.xH = olc[1]
            self.yL = olc[2]
            self.xL = olc[3]
        else:
            self.xH = xH
            self.yH = yH
            self.xL = xL
            self.yL = yL
        self.x = ''.join([self.xH, self.xL])
        self.y = ''.join([self.yH, self.yL])
    
    def __str__(self):
        return self.olc()

    def _increment(self, nH, nL, delta):
        iL = self.space.index(nL) + delta
        iH = self.space.index(nH) + int(iL / self.base)
        iL = iL % self.base

        print('{}{}: {},{} -> {},{}'.format(
            nH, nL,
            self.space.index(nH),
            self.space.index(nL),
            iH, iL
            )
        )
        return [
                self.space[iH], 
                self.space[iL]
                ]

    def _horiz(self, diff):
        xH, xL = self._increment(self.xH, self.xL, diff)
        kwargs = {
                'yH': self.yH,
                'xH': xH,
                'yL': self.yL,
                'xL': xL
                }
        return kwargs


    def _vert(self, diff):
        yH, yL = self._increment(self.yH, self.yL, diff)
        kwargs = {
                'yH': yH,
                'xH': self.xH,
                'yL': yL,
                'xL': self.xL
                }
        return kwargs


