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


'''
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