class InstructionBuffer(object):
    def __init__(self, bits_buffer):
        self.bits_buffer = bits_buffer

    def instruction_available(self):
        if self.bits_buffer.__len__() > 0:
            return True
        return False

    def instruction(self):
        return self.bits_buffer.popleft()

class Instruction(object):
    def __init__(self, bits, pc):
        self.bits = bits
        self.pc = pc

    def clock_delay_for(self, stage):
        if self.bits[0:5] == "000000" and self.bits[-6] == "011000" and isinstance( stage, EX ):
            return 2
        return 1

    # Must handle jumps and locks
    def available(self):
        return True

    def to_s(self):
        return self.bits

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
        if registers.set_in_use(self.rd):
            pass

    def write_back(self, registers):
        if registers.set_in_use(self.rd):
            registers[self.rd] = self.vd
            registers.setFree(self.rd)

class TypeIInstruction(Instruction):
    def __init__(self, rs, rt, imm):
        self.rs = rs
        self.rt = rt
        self.imm = imm

    def register_fetch(self, registers):
        self.vs = registers[self.rs]
        self.vt = registers[self.rt]
        registers.set_in_use(self.rt)

    def execute(self):
        pass

    def memory_access(self, memory):
        if registers.set_in_use(self.rt):
            pass

    def write_back(self, registers):
        if registers.set_in_use(self.rt):
            registers[self.rt] = self.vt
            registers.setFree(self.rt)

class TypeJInstruction(Instruction):
    def __init__(self, tarAdd):
        self.tarAdd = tarAdd

    def register_fetch(self):
        pass

    def execute(self):
        pass

    def memory_access(self, memory):
        pass

    def write_back(self, registers):
        pass

class Add(TypeRInstruction):
    def execute(self):
        self.vd = self.vs + self.vt
        PC += 4

class Sub(TypeRInstruction):
    def execute(self):
        self.vd = self.vs - self.vt
        PC += 4

class Mul(TypeRInstruction):
    def execute(self):
        self.vd = self.vs * self.vt
        PC += 4

class Nop(TypeRInstruction):
    def execute(self):
        pass 

class Addi(TypeIInstruction):
    def execute(self):
        self.vt = self.vs + self.imm
        PC += 4

class Beq(TypeIInstruction):
    def execute(self):
        if self.vs == self.vt
            PC += imm
        PC += 4

class Ble(TypeIInstruction):
    def execute(self):
        if self.vs <= self.vt
            PC = imm
        else
            PC += 4

class Bne(TypeIInstruction):
    def execute(self):
        if self.vs != self.vt
            PC += imm
        PC += 4

class Lw(TypeIInstruction):
    def execute(self):
        pass

class Sw(TypeIInstruction):
    def execute(self):
        pass

class Jmp(TypeJInstruction):
    def __init__ (self, tarAdd):
        self.tarAdd = 0

    def execute(self):
        if registers.set_in_use(self.rd):
            registers.setFree(self.rd)
        if registers.set_in_use(self.rt):
            registers.setFree(self.rt)
        PC = self.tarAdd

# class Instruction(object):
#     def register_fetch(self, registers):
#         pass
#     def execute(self):
#         pass
#     def memory_access(self, memory):
#         pass
#     def write_back(self, registers):
#         pass
# 
# class TypeRInstruction(Instruction):
#     def __init__(self, rs, rt, rd):
#         self.rs = rs
#         self.rt = rt
#         self.rd = rd
#     
#     def register_fetch(self, registers):
#         self.vs = registers[self.rs]
#         self.vt = registers[self.rt]
#         registers.set_in_use(self.rd)
#     
#     def execute(self):
#         pass
#        
#     def memory_access(self, memory):
#         pass
#     
#     def write_back(self, registers):
#         registers[self.rd] = self.vt
# 
# class Add(TypeRInstruction):
#     def execute(self):
#         self.vd = self.vs + self.vt
# 
