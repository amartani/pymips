
from ui import MainFrame
from stages import Pipeline

class Controller(object):
    def __init__(self, main_frame, pipeline):
        self.main_frame = main_frame
        self.pipeline   = pipeline
        
    def run(self):
        self.main_frame.show()
        self.pipeline.clock()

if __name__ == "__main__":
    main_frame = MainFrame()
    pipeline = Pipeline()
    controller = Controller(main_frame, pipeline)
    controller.run()