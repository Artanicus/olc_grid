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
    def ne(self):
        kwargs = self._mutate(1, 1)
        return Area(**kwargs)
    def se(self):
        kwargs = self._mutate(-1, 1)
        return Area(**kwargs)
    def sw(self):
        kwargs = self._mutate(-1, -1)
        return Area(**kwargs)
    def nw(self):
        kwargs = self._mutate(1, -1)
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
            raise ValueError('Invalid OLC: {}{}{}{}'.format(self.yH, self.xH, self.yL, self.xL))

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
    
    def _mutate(self, yD, xD):
        yH, yL = self._increment(self.yH, self.yL, yD)
        xH, xL = self._increment(self.xH, self.xL, xD)
        kwargs = {
                'yH': yH,
                'xH': xH,
                'yL': yL,
                'xL': xL
                }
        return kwargs


    def _horiz(self, delta):
        return self._mutate(0, delta)


    def _vert(self, delta):
        return self._mutate(delta, 0)
