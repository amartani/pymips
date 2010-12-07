from collections import deque
from array import array
from controller import  

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
        if registers.set_in_use(self.rd)
        		pass
    
    def write_back(self, registers):
				if registers.set_in_use(self.rd)
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
				if registers.set_in_use(self.rt)
        		pass
    
    def write_back(self, registers):
				if registers.set_in_use(self.rt)
						registers[self.rt] = self.vt
        		registers.setFree(self.rt)

class TypeJInstruction(Instruction):
    def __init__(self, tarAdd):
				self.tarAdd = tarAdd

		def register_fetch(self): 
				pass

		def execute(self)
				pass

		def memory_access(self, memory)
				pass

		def write_back(self, registers)
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
        PC += 4

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
        PC += 4
    
class Sw(TypeIInstruction):
    def execute(self):
        PC += 4

class Jmp(TypeJInstruction):
		def __init__ (self, tarAdd):
				self.tarAdd = 0				

    def execute(self):
				if registers.set_in_use(self.rd):
						registers.setFree(self.rd)
				if registers.set_in_use(self.rt):
						registers.setFree(self.rt)
		PC = self.tarAdd
	
       
class Stage(object):
    def __init__(self, prev_stage):
        self.prev_stage = prev_stage
        self.clock_count = 0
        self.instruction = None

    def get_instruction(self):
        if self.prev_stage.instruction_available():
            self.instruction = self.prev_stage.instruction
            if self.instruction is None:
                self.clock_count = 0
            else:
                self.clock_count = self.instruction.clock_delay_for(self)
        else:
            self.instruction = None
            self.clock_count = 0

    def clock(self):
        if self.clock_count > 0:
            self.clock_count -= 1
        print self.to_s() + " clock count:" + str(self.clock_count)

    def instruction_available(self):
        if self.clock_count == 0 and self.instruction is not None and self.instruction.available():
            return True
        return False

    def foward(self):
        if self.clock_count == 0:
            if self.prev_stage.instruction_available():
                self.get_instruction()
                if self.instruction is None:
                    print self.to_s() + " bubble!"
                else:
                    print self.to_s() + " foward: " + self.instruction.to_s()
            else:
                self.instruction = None
                self.clock_count = 0
                print self.to_s() + " bubble!"
        else:
            print self.to_s() + " processing: " + self.instruction.to_s()

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

class Register:
    def __init__(self, value):
        self.inUSe = False
        self.value = value  
        
    def set_in_use(self):
        self.inUse = True #Rever depois!      
    
class Memory:
    def teste(self):
        return""

class PipelineControl:
		def __init__ (self, instructions, main_frame): 
				self.instructions = instructions
				self.main_frame = main_frame

		def execute:
				instLength = instructions.len()
				PC = 0
				while PC != 4*qtde_instLength :
						instruction = instructions(PC)

   
registers = []
PC = 0  #variavel global  

for i in range(32):
  
    registers.append(Register(0)) #iniciar certo depois!

l=[]

if l[0:5] == "000010"
    #eh jump
    tarAdd_value = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11])+str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17])+str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    jmp_obj = Jmp(tarAdd_value)
    jmp_obj.execute() 
    
else if l[0:5] == "000000" and l[-6] = "100000"
    # eh add
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    d_index = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23]), 2)
    add_obj = Add(registers[s_index].value, registers[t_index].value, registers[d_index].value)
    add_obj.execute() 

else if l[0:5] == "001000"
    #eh addi
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    addi_obj = Addi(register[s_index].value, registers[t_index].value, imm_value)
    addi_obj.execute()
    
else if l[0:5] == "000101"
    # eh beq
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    beq_obj = Beq(register[s_index].value, registers[t_index].value, imm_value)
    beq_obj.execute()
    
else if l[0:5] == "000111" 
    # eh ble
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    ble_obj = Ble(register[s_index].value, registers[t_index].value, imm_value)
    ble_obj.execute()
    
else if l[0:5] == "000100" 
    # eh bne
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    bne_obj = Bne(register[s_index].value, registers[t_index].value, imm_value)
    bne_obj.execute()

else if l[0:5] == "100011"
    #eh lw
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    lw_obj = Lw(register[s_index].value, registers[t_index].value, imm_value)
    lw_obj.execute()
   
else if l[0:5] == "000000" and l[-6] = "011000"
    #eh mul
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    d_index = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23]), 2)
    mul_obj = Mul(registers[s_index].value, registers[t_index].value, registers[d_index].value)
    mul_obj.execute()
    
else if l[0:5] == "000000" and l[-6] = "000000"
    #eh nop
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    d_index = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23]), 2)
    nop_obj = Nop(registers[s_index].value, registers[t_index].value, registers[d_index].value)
    nop_obj.execute()
    
else if l[0:5] == "000000" and l[-6] = "100010"
    #eh sub
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    d_index = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23]), 2)
    sub_obj = Sub(registers[s_index].value, registers[t_index].value, registers[d_index].value)
    sub_obj.execute()
    
else if l[0:5] == "101011"
    #eh sw 
    s_index = int(str(l[6])+str(l[7])+str(l[8])+str(l[9])+str(l[10])+str(l[11]), 2)
    t_index = int(str(l[12])+str(l[13])+str(l[14])+str(l[15])+str(l[16])+str(l[17]), 2)
    imm_value = int(str(l[18])+str(l[19])+str(l[20])+str(l[21])+str(l[22])+str(l[23])+str(l[24])+str(l[25])+str(l[26])+str(l[27])+str(l[28])+str(l[29]+str(l[30])+str(l[31])), 2)
    sw_obj = Sw(register[s_index].value, registers[t_index].value, imm_value)
    sw_obj.execute()
 

 









'''
teste = Add(Rx, Ry)
teste.add()
'''










mult_instruction = Instruction('00000000110001100011100000011000')
instruction_deque = deque([mult_instruction])
instruction_buffer = InstructionBuffer(instruction_deque)
pipeline = Pipeline(instruction_buffer)
pipeline.clock()
pipeline.foward()
pipeline.clock()
pipeline.foward()
pipeline.clock()
pipeline.foward()
pipeline.clock()
pipeline.foward()
pipeline.clock()
pipeline.foward()
pipeline.clock()
pipeline.foward()
pipeline.clock()
