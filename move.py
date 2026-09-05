class Move:
    def __init__(self, xfrom, yfrom, xto, yto):
        self._xfrom = xfrom
        self._yfrom = yfrom
        self._xto = xto
        self._yto = yto
    
    @property
    def xfrom(self):
        return self._xfrom
    
    @property
    def yfrom(self):
        return self._yfrom
    
    @property
    def xto(self):
        return self._xto
    
    @property
    def yto(self):
        return self._yto
    
    def equals(self, other_move):
        return (
            self.xfrom == other_move.xfrom and
            self.yfrom == other_move.yfrom and
            self.xto == other_move.xto and
            self.yto == other_move.yto
        )

    def to_string(self):
        return f"({self.xfrom}, {self.yfrom}) -> ({self.xto}, {self.yto})"
