# -*- coding: utf-8 -*-
'''

'''

from javax.swing import JFrame, JPanel, JLabel, JButton, JTable, JScrollPane, JTextField, BoxLayout, Box, ImageIcon, BorderFactory
from javax.swing.table import DefaultTableModel
from java.awt import BorderLayout, GridLayout, Dimension

class BorderPanel(JPanel):
    def __init__(self, name):
        super(BorderPanel, self).__init__()
        self.border = BorderFactory.createTitledBorder(name)
        

# --- Program Frames ----

class MainFrame(JFrame):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.title = "PyMips"
        self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        self._createPanes()
        self.size = Dimension(1200, 750)
    
    def _createPanes(self):
        self.mainpanel = panel = JPanel()
        panel.layout = BoxLayout(panel, BoxLayout.X_AXIS) 
        self.add(panel)
        
        self.left_panel = left_panel = LeftPanel()
        panel.add(left_panel)
        
        self.right_panel = right_panel = RightPanel()
        panel.add(right_panel)
    
    @property
    def add_memory_info(self):
        return self.right_panel.add_memory_info
    
    @property
    def update_statistics(self):
        return self.right_panel.update_statistics
    
    @property
    def set_registers(self):
        return self.right_panel.set_registers
    
    @property
    def update_stages(self):
        return self.left_panel.update_stages
        
class LeftPanel(BorderPanel):
    def __init__(self):
        super(LeftPanel, self).__init__("Stages")
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.stages_info_panel = stages_info_panel = StagesInfoPanel()
        self.add(stages_info_panel)
        
        self.stages_image_panel = stages_image_panel = StagesImagePanel()
        self.add(stages_image_panel)
        
        self.add(Box.createVerticalGlue())
    
    @property
    def update_stages(self):
        return self.stages_info_panel.update_stages

class StagesInfoPanel(JPanel):
    def __init__(self):
        super(StagesInfoPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.if_panel = if_panel = StageInfoPanel("IF")
        self.add(if_panel)
        
        self.id_panel = id_panel = StageInfoPanel("ID")
        self.add(id_panel)
        
        self.ex_panel = ex_panel = StageInfoPanel("EX")
        self.add(ex_panel)
        
        self.mem_panel = mem_panel = StageInfoPanel("MEM")
        self.add(mem_panel)
        
        self.wb_panel = wb_panel = StageInfoPanel("WB")
        self.add(wb_panel)
    
    def update_stages(self, pipeline):
        self.if_panel.update_stage(pipeline.if_)
        self.id_panel.update_stage(pipeline.id)
        self.ex_panel.update_stage(pipeline.ex)
        self.mem_panel.update_stage(pipeline.mem)
        self.wb_panel.update_stage(pipeline.wb)

class StageInfoPanel(BorderPanel):
    def __init__(self, name):
        super(StageInfoPanel, self).__init__(name)
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        #self.add(Box.createHorizontalGlue())
        
        self.instruction_txtfield = txtfield = JTextField(editable=False)
        self.add(txtfield)
        self.signals_txtfield = txtfield = JTextField(editable=False)
        self.add(txtfield)
        
        #self.add(Box.createHorizontalGlue())
        
    def update_stage(self, stage):
        self.instruction_txtfield.text = str(stage.instruction)
        self.signals_txtfield.text = str(stage.signals)
    
class StagesImagePanel(JPanel):
    def __init__(self):
        super(StagesImagePanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.add(JLabel(ImageIcon("../static/mips.png")))


class RightPanel(JPanel):
    def __init__(self):
        super(RightPanel, self).__init__()

        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.control_panel = control_panel = ControlPanel()
        self.add(control_panel)
        
        self.mem_info_panel = mem_info_panel = MemInfoPanel()
        self.add(mem_info_panel)
        
        self.statistics_panel = statistics_panel = StatisticsPanel()
        self.add(statistics_panel)

        self.registers_info_panel = registers_info_panel = RegistersInfoPanel()
        self.add(registers_info_panel)

    @property
    def add_memory_info(self):
        return self.mem_info_panel.add_memory_info
    
    @property
    def update_statistics(self):
        return self.statistics_panel.update_statistics
    
    @property
    def set_registers(self):
        return self.registers_info_panel.set_registers

class ControlPanel(BorderPanel):
    def __init__(self):
        super(ControlPanel, self).__init__("Control")
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.add(Box.createHorizontalGlue())
        
        self.button_play = button_play = JButton(ImageIcon("../static/media-playback-start.png"))
        self.add(button_play)
        
        self.button_ff = button_ff = JButton(ImageIcon("../static/media-seek-forward.png"))
        self.add(button_ff)
        
        self.button_pause = button_pause = JButton(ImageIcon("../static/media-playback-pause.png"))
        self.add(button_pause)
        
        self.button_load = button_load = JButton(ImageIcon("../static/document-open.png"))
        self.add(button_load)
        
        self.add(Box.createHorizontalGlue())

class MemInfoPanel(BorderPanel):
    def __init__(self):
        super(MemInfoPanel, self).__init__("Recently Used Memory")
        
        headers = ["Address", "Value"]
        self.table_model    = table_model   = DefaultTableModel(headers, 0)
        self.table          = table         = JTable(table_model)
        table.fillsViewportHeight = True
        
        scrollpane = JScrollPane(table)
        
        self.add(scrollpane)
        
    def add_memory_info(self, address, value):
        self.table_model.insertRow(0, [address, value])

class StatisticsPanel(BorderPanel):
    def __init__(self):
        
        super(StatisticsPanel, self).__init__("Statistics")
        
        self.layout = GridLayout(4, 2)
        
        self.add(JLabel("Clock corrente"))
        
        self.current_clock_txtfield = textfield = JTextField()
        textfield.editable = False
        self.add(textfield)
        
        self.add(JLabel("PC"))
        
        self.pc_txtfield = textfield = JTextField()
        textfield.editable = False
        self.add(textfield)
        
        self.add(JLabel("Numero de instrucoes concluidas"))
        
        self.no_instructions_txtfield = textfield = JTextField()
        textfield.editable = False
        self.add(textfield)
        
        self.add(JLabel("Produtividade"))
        
        self.productivity_txtfield = textfield = JTextField()
        textfield.editable = False
        self.add(textfield)
        
    def update_statistics(self, current_clock, pc, no_instructions, productivity):
        self.current_clock_txtfield.text    = str(current_clock)
        self.pc_txtfield.text               = str(pc)
        self.no_instructions_txtfield.text  = str(no_instructions)
        self.productivity_txtfield.text     = str(productivity)
        
class RegistersInfoPanel(BorderPanel):
    def __init__(self):
        super(RegistersInfoPanel, self).__init__("Registers")
        
        self.layout = GridLayout(8, 8)
        self.txtfields = txtfields = []
        
        for i in range(32):
            self.add(JLabel("R%d" % i))
            txtfield = JTextField()
            txtfield.editable = False
            txtfields.append(txtfield)
            self.add(txtfield)

    def set_registers(self, registers):
        for i, value in enumerate(registers):
            self.txtfields[i].text = str(value)


if __name__ == "__main__":
    frame = MainFrame()
    
    frame.add_memory_info(1, 10)
    frame.add_memory_info(2, 50)
    frame.add_memory_info(3, 60)
    
    frame.update_statistics(60, 21, 41, 0.21)
    
    frame.set_registers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
    
    class StageMock:
        class InstructionMock:
            def __str__(self):
                return "I1: ADD R10, R0, R2"
        class SignalsMock:
            def __str__(self):
                return "Sinais de controle"
        instruction = InstructionMock()
        signals = SignalsMock()
    
    class PipelineMock:
        if_ = StageMock()
        id  = StageMock()
        ex  = StageMock()
        mem = StageMock()
        wb  = StageMock()
    
    pipeline = PipelineMock()
    
    frame.update_stages(pipeline)
    
    frame.show()