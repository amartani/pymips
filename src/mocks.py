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
