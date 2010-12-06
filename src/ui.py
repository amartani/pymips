'''

'''

from javax.swing import JFrame, JPanel, JLabel
from java.awt import BorderLayout


class MainFrame(JFrame):
    def __init__(self):
        self.title = "PyMips"
        self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        self._createPanes()
    
    def _createPanes(self):
        self.mainpanel = panel = JPanel()
        panel.layout = BorderLayout()
        self.add(panel)
        
        self.controlpanel = controlpanel = JPanel()
        controlpanel.layout = BorderLayout()
        panel.add(controlpanel, BorderLayout.EAST)
        
        label = JLabel()
        label.text = "East"
        controlpanel.add(label)
        
        self.left_panel = left_panel = JPanel()
        left_panel.add(JLabel("Center"))
        panel.add(left_panel, BorderLayout.CENTER)
        

if __name__ == "__main__":
    frame = MainFrame()
    frame.show()