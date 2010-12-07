from instructions import *

class Register:
    def __init__(self, value):
        self.inUSe = False
        self.value = value

    def set_in_use(self):
        self.inUse = True #Rever depois!

REGISTERS = []
for i in range(32):
    REGISTERS.append(Register(0))

class PipelineControl:
    def __init__(self, instructions, main_frame):
        self.instructions = instructions
        self.main_frame = main_frame
    
    def set_observer(self, observer):
        self.observer = observer
    
    def clock(self):
        if not self.instructions:
            return False
        instruction = self.instructions.pop()
        print instruction
        self.main_frame.add_memory_info(3, 5)
        return True

    def parse_instructions(self):
        self.parsed_instructions = []
        for line in self.instructions:
            parsed_instruction = self.parse_line(line)
            self.parsed_instructions.append(parsed_instruction)

    def parse_line(self, line):
        if line[0:6] == "000010":
            #eh jump
            tarAdd_value = int(line[6:32], 2)
            return Jmp(tarAdd_value)

        elif line[0:6] == "000000" and line[-6:] == "100000":
            # eh add
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            d_index = int(line[18:24], 2)
            return Add(REGISTERS[s_index], REGISTERS[t_index], REGISTERS[d_index])

        elif line[0:6] == "001000":
            #eh addi
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Addi(REGISTERS[s_index], REGISTERS[t_index], imm_value)

        elif line[0:6] == "000101":
            # eh beq
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Beq(REGISTERS[s_index], REGISTERS[t_index], imm_value)

        elif line[0:6] == "000111":
            # eh ble
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Ble(REGISTERS[s_index], REGISTERS[t_index], imm_value)

        elif line[0:6] == "000100":
            # eh bne
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Bne(REGISTERS[s_index], REGISTERS[t_index], imm_value)

        elif line[0:6] == "100011":
            #eh lw
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Lw(REGISTERS[s_index], REGISTERS[t_index], imm_value)

        elif line[0:6] == "000000" and line[-6:] == "011000":
            #eh mul
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            d_index = int(line[18:24], 2)
            #print str(s_index) + " " + str(t_index) + " " + str(d_index)
            return Mul(REGISTERS[s_index], REGISTERS[t_index], REGISTERS[d_index])

        elif line[0:6] == "000000" and line[-6:] == "000000":
            #eh nop
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            d_index = int(line[18:24], 2)
            return Nop(REGISTERS[s_index], REGISTERS[t_index], REGISTERS[d_index])

        elif line[0:6] == "000000" and line[-6:] == "100010":
            #eh sub
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            d_index = int(line[18:24], 2)
            return Sub(REGISTERS[s_index], REGISTERS[t_index], REGISTERS[d_index])

        elif line[0:6] == "101011":
            #eh sw 
            s_index = int(line[6:12], 2)
            t_index = int(line[12:18], 2)
            imm_value = int(line[18:32], 2)
            return Sw(REGISTERS[s_index], REGISTERS[t_index], imm_value)
