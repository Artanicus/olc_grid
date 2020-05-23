class Area:
    def east(self):
        kwargs = self._horiz(1)
        return Area(**kwargs)
    def west(self):
        kwargs = self._horiz(-1)
        return Area(**kwargs)
    def south(self):
        kwargs = self._vert(-1)
        return Area(**kwargs)
    def north(self):
        kwargs = self._vert(1)
        return Area(**kwargs)
    
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
            self.yH = yH
            self.xH = xH
            self.yL = yL
            self.xL = xL
        if not (self.xH in self.space and self.yH in self.space and self.xL in self.space and self.yL in self.space):
            raise ValueError('Invalid OLC: {}{}{}{}'.format(yH, xH, yL, xL))

        self.x = ''.join([self.xH, self.xL])
        self.y = ''.join([self.yH, self.yL])
    
    def __str__(self):
        return self.olc()

    def _increment(self, nH, nL, delta):
        iL = self.space.index(nL) + delta
        iH = self.space.index(nH) + int(iL / self.base)
        iL = iL % self.base

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


