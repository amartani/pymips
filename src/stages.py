class IF:
    def __init__(self):
        pass

    def clock(self):
        print "IF clock"

class ID:
    def __init__(self, if_):
        self.if_ = if_

    def clock(self):
        print "ID clock"

class EX:
    def __init__(self, id):
        self.id = id

    def clock(self):
        print "EX clock"

class MEM:
    def __init__(self, ex):
        self.ex = ex

    def clock(self):
        print "MEM clock"

class WB:
    def __init__(self, mem):
        self.mem = mem

    def clock(self):
        print "WB clock"


class Pipeline:
    def __init__(self):
        self.if_ = if_ = IF()
        self.id  = id  = ID(if_)
        self.ex  = ex  = EX(id)
        self.mem = mem = MEM(ex)
        self.wb  = wb  = WB(mem)

    def clock(self):
        self.if_.clock()
        self.id.clock()
        self.ex.clock()
        self.mem.clock()
        self.wb.clock()
