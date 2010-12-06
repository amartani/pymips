'''

'''

from javax.swing import JFrame, JPanel, JLabel, BoxLayout, ImageIcon
from java.awt import BorderLayout, Dimension

class MainFrame(JFrame):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.title = "PyMips"
        self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        self._createPanes()
        self.size = Dimension(1000, 800)
    
    def _createPanes(self):
        self.mainpanel = panel = JPanel()
        panel.layout = BoxLayout(panel, BoxLayout.X_AXIS)
        self.add(panel)
        
        self.left_panel = left_panel = LeftPanel()
        panel.add(left_panel)
        
        self.right_panel = right_panel = RightPanel()
        panel.add(right_panel)
        
class LeftPanel(JPanel):
    def __init__(self):
        super(LeftPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.stages_info_panel = stages_info_panel = StagesInfoPanel()
        self.add(stages_info_panel)
        
        self.stages_image_panel = stages_image_panel = StagesImagePanel()
        self.add(stages_image_panel)

class StagesInfoPanel(JPanel):
    def __init__(self):
        super(StagesInfoPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.if_panel = if_panel = StageInfoPanel()
        self.add(if_panel)
        if_panel.text = "IF"
        
        self.id_panel = id_panel = StageInfoPanel()
        self.add(id_panel)
        id_panel.text = "ID"
        
        self.ex_panel = ex_panel = StageInfoPanel()
        self.add(ex_panel)
        ex_panel.text = "EX"
        
        self.mem_panel = mem_panel = StageInfoPanel()
        self.add(mem_panel)
        mem_panel.text = "MEM"
        
        self.wb_panel = wb_panel = StageInfoPanel()
        self.add(wb_panel)
        wb_panel.text = "WB"

class StageInfoPanel(JPanel):
    def __init__(self):
        super(StageInfoPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.label = label = JLabel()
        self.add(label)
    
    def set_text(self, text):
        self.label.text = text
    
    def get_text(self):
        return self.label.text
    
    text = property(get_text, set_text)
        

class StagesImagePanel(JPanel):
    def __init__(self):
        super(StagesImagePanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.add(JLabel(ImageIcon("../static/mips.png")))


class RightPanel(JPanel):
    def __init__(self):
        super(RightPanel, self).__init__()

        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.control_panel = control_panel = ControlPanel()
        self.add(control_panel)
        
        self.mem_info_panel = mem_info_panel = MemInfoPanel()
        self.add(mem_info_panel)
        
        self.clock_info_panel = clock_info_panel = ClockInfoPanel()
        self.add(clock_info_panel)

        self.registers_info_panel = registers_info_panel = RegistersInfoPanel()
        self.add(registers_info_panel)

class ControlPanel(JPanel):
    def __init__(self):
        super(ControlPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.button_play = button_play = JLabel(">")
        self.add(button_play)
        
        self.button_ff = button_ff = JLabel(">>")
        self.add(button_ff)
        
        self.button_pause = button_pause = JLabel("||")
        self.add(button_pause)
        
        self.button_load = button_load = JLabel("L")
        self.add(button_load)

class MemInfoPanel(JPanel):
    def __init__(self):
        super(MemInfoPanel, self).__init__()

class ClockInfoPanel(JPanel):
    def __init__(self):
        super(ClockInfoPanel, self).__init__()
        
class RegistersInfoPanel(JPanel):
    def __init__(self):
        super(RegistersInfoPanel, self).__init__()

if __name__ == "__main__":
    frame = MainFrame()
    frame.show()