
class Instruction(object):
    def register_fetch(self, registers):
        pass
    def execute(self):
        pass
    def memory_access(self, memory):
        pass
    def write_back(self, registers):
        pass

class TypeRInstruction(Instruction):
    def __init__(self, rs, rt, rd):
        self.rs = rs
        self.rt = rt
        self.rd = rd
    
    def register_fetch(self, registers):
        self.vs = registers[self.rs]
        self.vt = registers[self.rt]
        registers.set_in_use(self.rd)
    
    def execute(self):
        pass
       
    def memory_access(self, memory):
        pass
    
    def write_back(self, registers):
        registers[self.rd] = self.vt

class Add(TypeRInstruction):
    def execute(self):
        self.vd = self.vs + self.vt

