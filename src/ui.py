'''

'''

from javax.swing import JFrame

class MainFrame(JFrame):
    def __init__(self):
        self.title = "PyMips"
        self.defaultCloseOperation = JFrame.EXIT_ON_CLOSE

if __name__ == "__main__":
    frame = MainFrame()
    frame.show()