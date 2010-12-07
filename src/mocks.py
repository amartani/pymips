class Pipeline:
    def __init__(self, instructions):
        self.instructions = instructions
    
    def set_observer(self, observer):
        self.observer = observer
    
    def clock(self):
        if not self.instructions:
            return False
        instruction = self.instructions.pop()
        print instruction
        return True
