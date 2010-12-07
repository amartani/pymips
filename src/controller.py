
from ui import MainFrame
from stages import Pipeline
import re

class Controller(object):
    def __init__(self, main_frame):
        self.main_frame = main_frame
        main_frame.set_controller_observer(self)
        
    def run(self):
        self.main_frame.show()
        #self.pipeline.clock()
    
    def play(self):
        print "Button play pressed"
    def pause(self):
        print "Button pause pressed"
    def forward(self):
        print "Button forward pressed"
    def file(self, f):
        lines = self._get_lines_from_file(f)
        print lines
        
    @staticmethod
    def _get_lines_from_file(f):
        def line_filter(line):
            re = Controller.LINE_RE
            match = re.search(line)
            if match:
                return match.group(1)
        return [line_filter(line) for line in f]
    LINE_RE = re.compile(r"([01]{32})")
        

if __name__ == "__main__":
    main_frame = MainFrame()
    #pipeline = Pipeline()
    controller = Controller(main_frame)
    controller.run()