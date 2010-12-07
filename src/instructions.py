from mocks  import *
from stages import *

class Instruction(object):
    def __init__(self, pc):
        self.pc = pc

    def clock_delay_for(self, stage):
        return 1

    # Must handle jumps and locks
    def available(self):
        return True

    def to_s(self):
        return self.bits

    def instruction_fetch(self):
        PC.value += 4

    def register_fetch(self):
        pass

    def execute(self):
        pass

    def memory_access(self):
        pass

    def write_back(self):
        pass

class TypeRInstruction(Instruction):
    def __init__(self, rs, rt, rd):
        self.rs = rs
        self.rt = rt
        self.rd = rd

    def register_fetch(self):
        self.rd.set_in_use()
        self.vt = self.rt.value
        self.vd = self.rd.value

    def write_back(self):
        self.rd.value = self.vd
        self.rd.set_free()

class TypeIInstruction(Instruction):
    def __init__(self, rs, rt, imm):
        self.rs = rs
        self.rt = rt
        self.imm = imm

    def register_fetch(self):
        self.rt.set_in_use()
        self.vs = self.rs.value

    def write_back(self):
        self.rt.value = self.vt
        self.rt.set_free()

# class TypeJInstruction(Instruction):
#     def __init__(self, tarAdd):
#         self.tarAdd = tarAdd
# 
#     def decode_instruction(self):
#         PC.set_in_use()
# 
#     def write_back(self):
#         PC.set_free()

class Add(TypeRInstruction):
    def execute(self):
        self.vd = self.vs + self.vt

class Sub(TypeRInstruction):
    def execute(self):
        self.vd = self.vs - self.vt

class Mul(TypeRInstruction):
    def clock_delay_for(self, stage):
        if isinstance( stage, EX ):
            return 2
        return 1

    def execute(self):
        self.vd = self.vs*self.vt

class Nop(TypeRInstruction):
    def __init__(self):
        pass 

class Addi(TypeIInstruction):
    def execute(self):
        self.vt = self.vs + self.imm

class Beq(TypeIInstruction):
    def execute(self):
        if self.vs == self.vt:
            PC += self.imm

class Ble(TypeIInstruction):
    def execute(self):
        if self.vs <= self.vt:
            PC = self.imm

class Bne(TypeIInstruction):
    def execute(self):
        if self.vs != self.vt:
            PC += self.imm

class Lw(TypeIInstruction):
    def execute(self):
        pass

class Sw(TypeIInstruction):
    def execute(self):
        pass

class Jmp(Instruction):
    def __init__(self, tarAdd):
        self.tarAdd = tarAdd

    def instruction_fetch(self):
        PC.set_in_use()

    def write_back(self):
        PC.value = self.tarAdd
        PC.set_free()