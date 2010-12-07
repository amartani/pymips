from controller   import *
from instructions import *

class InstructionProxy(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.instruction_available = True

    def get_instruction(self):
        return self.instructions[PC/4]

class Stage(object):
    def __init__(self, prev_stage):
        self.prev_stage = prev_stage
        self.busy = False
        self.instruction_available = False
        self.instruction = Nop(REGISTERS[0], REGISTERS[0], REGISTERS[0])
        self.clock_count = self.instruction.clock_delay_for(self)

    def get_instruction(self):
        self.instruction_available = False
        return self.instruction

    def clock(self):
        # print self.to_s() + " clock count: " + str(self.clock_count)
        if self.clock_count > 0:
            self.clock_count -= 1
            if self.clock_count == 0:
                self.stage_step()()
                self.instruction_available = True
                self.busy = False

    def foward(self):
        if not self.busy and not self.instruction_available:
            if self.prev_stage.instruction_available:
                self.instruction = self.prev_stage.get_instruction()
            else:
                self.instruction = Nop(REGISTERS[0], REGISTERS[0], REGISTERS[0])
            self.clock_count = self.instruction.clock_delay_for(self)

class IF(Stage):
    def get_instruction(self):
        if self.prev_stage.instruction_available():
            self.instruction = self.prev_stage.instruction()
            self.clock_count = self.instruction.clock_delay_for(self)
        else:
            self.instruction = None
            self.clock_count = 0

    def to_s(self):
        return "IF"

    def stage_step(self):
        return self.instruction.decode_instruction

    def decode_instruction(self):
        pass

class ID(Stage):
    def to_s(self):
        return "ID"

    def stage_step(self):
        return self.instruction.register_fetch

    def clock(self):
        if self.instruction.available():
            super( Stage, self ).clock()

class EX(Stage):
    def to_s(self):
        return "EX"

    def stage_step(self):
        return self.instruction.execute

class MEM(Stage):
    def to_s(self):
        return "MEM"

    def stage_step(self):
        return self.instruction.memory_access

class WB(Stage):
    def to_s(self):
        return "WB"

    def stage_step(self):
        return self.instruction.write_back

class Pipeline:
    def __init__(self, instruction_proxy):
        self.ip  = ip  = instruction_proxy
        self.if_ = if_ = IF(ip)
        self.id  = id  = ID(if_)
        self.ex  = ex  = EX(id)
        self.mem = mem = MEM(ex)
        self.wb  = wb  = WB(mem)

    def clock(self):
        self.wb.clock()
        self.mem.clock()
        self.ex.clock()
        self.id.clock()
        self.if_.clock()

    def foward(self):
        self.wb.foward()
        self.mem.foward()
        self.ex.foward()
        self.id.foward()
        self.if_.foward()
