from collections import deque

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
    def __init__(self, bits):
        self.bits = bits

    def clock_delay_for(self, stage):
        if self.bits[0:12] == "000000" and self.bits[-6:] == "011000" and isinstance( stage, EX ):
            return 2
        return 1

class Stage(object):
    def __init__(self, prev_stage):
        self.prev_stage = prev_stage
        self.clock_count = 0

    def instruction(self):
        return self.instruction

    def get_instruction(self):
        if self.prev_stage.instruction_available():
            self.instruction = self.prev_stage.instruction()
            self.clock = self.instruction.clock_delay_for(self)

    def clock(self):
        if self.clock_count > 0:
            self.clock_count -= 1
        print self.to_s() + " clock count:" + str(self.clock_count)

    def instruction_available(self):
        if self.clock == 0:
            return True
        return False

    def foward(self):
        if self.prev_stage.instruction_available():
            get_instruction()
        print self.to_s() + " foward:" + str(self.instruction)

class IF(Stage):
    def to_s(self):
        return "IF"

class ID(Stage):
    def to_s(self):
        return "ID"

class EX(Stage):
    def to_s(self):
        return "EX"

class MEM(Stage):
    def to_s(self):
        return "MEM"

class WB(Stage):
    def to_s(self):
        return "WB"


class Pipeline:
    def __init__(self, instruction_buffer):
        self.ib  = ib  = instruction_buffer
        self.if_ = if_ = IF(ib)
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

    def foward(self):
        self.wb.clock()
        self.mem.clock()
        self.ex.clock()
        self.id.clock()
        self.if_.clock()

instruction_deque = deque([Instruction('00000000110001100011100000011000')])
instruction_buffer = InstructionBuffer(instruction_deque)
pipeline = Pipeline(instruction_buffer)
pipeline.clock()
pipeline.foward()
pipeline.clock()