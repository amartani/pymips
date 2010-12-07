'''

'''

from javax.swing import JFrame, JPanel, JLabel, JButton, BoxLayout, Box, ImageIcon, BorderFactory
from java.awt import BorderLayout, Dimension

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
        self.size = Dimension(1000, 800)
    
    def _createPanes(self):
        self.mainpanel = panel = JPanel()
        panel.layout = BoxLayout(panel, BoxLayout.X_AXIS) 
        self.add(panel)
        
        self.left_panel = left_panel = LeftPanel()
        panel.add(left_panel)
        
        self.right_panel = right_panel = RightPanel()
        panel.add(right_panel)
        
class LeftPanel(BorderPanel):
    def __init__(self):
        super(LeftPanel, self).__init__("Stages")
        
        self.layout = BoxLayout(self, BoxLayout.Y_AXIS)
        
        self.stages_info_panel = stages_info_panel = StagesInfoPanel()
        self.add(stages_info_panel)
        
        self.stages_image_panel = stages_image_panel = StagesImagePanel()
        self.add(stages_image_panel)
        
        self.add(Box.createVerticalGlue())

class StagesInfoPanel(JPanel):
    def __init__(self):
        super(StagesInfoPanel, self).__init__()
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.if_panel = if_panel = StageInfoPanel("IF")
        self.add(if_panel)
        if_panel.text = "IF"
        
        self.id_panel = id_panel = StageInfoPanel("ID")
        self.add(id_panel)
        id_panel.text = "ID"
        
        self.ex_panel = ex_panel = StageInfoPanel("EX")
        self.add(ex_panel)
        ex_panel.text = "EX"
        
        self.mem_panel = mem_panel = StageInfoPanel("MEM")
        self.add(mem_panel)
        mem_panel.text = "MEM"
        
        self.wb_panel = wb_panel = StageInfoPanel("WB")
        self.add(wb_panel)
        wb_panel.text = "WB"

class StageInfoPanel(BorderPanel):
    def __init__(self, name):
        super(StageInfoPanel, self).__init__(name)
        
        self.layout = BoxLayout(self, BoxLayout.X_AXIS)
        
        self.add(Box.createHorizontalGlue())
        
        self.label = label = JLabel()
        self.add(label)
        
        self.add(Box.createHorizontalGlue())
    
    def set_text(self, text):
        self.label.text = text
    
    def get_text(self):
        return self.label.text
    
    text = property(get_text, set_text)
        

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
        
        self.clock_info_panel = clock_info_panel = ClockInfoPanel()
        self.add(clock_info_panel)

        self.registers_info_panel = registers_info_panel = RegistersInfoPanel()
        self.add(registers_info_panel)

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
        super(MemInfoPanel, self).__init__("Memory")

class ClockInfoPanel(BorderPanel):
    def __init__(self):
        super(ClockInfoPanel, self).__init__("Clock")
        
class RegistersInfoPanel(BorderPanel):
    def __init__(self):
        super(RegistersInfoPanel, self).__init__("Registers")

if __name__ == "__main__":
    frame = MainFrame()
    frame.show()