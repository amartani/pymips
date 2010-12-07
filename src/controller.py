from ui import MainFrame
from mocks import PipelineControl
import re
import threading
import time

class PipelineThread(threading.Thread):
    def __init__(self, pipeline):
        super(PipelineThread, self).__init__()
        self.pipeline = pipeline
        self.started = False
        self.stopped = False
        self.paused = False

    def run(self):
        self.started = True
        pipeline_end = False
        while not self.stopped and not pipeline_end:
            if not self.paused:
                pipeline_end = not self.pipeline.clock()
            time.sleep(2.0)

class Controller(object):
    def __init__(self, main_frame):
        self.main_frame = main_frame
        main_frame.set_controller_observer(self)
        self.thread = None

    def run(self):
        self.main_frame.show()
        #self.pipeline.clock()

    def play(self):
        print "Button play pressed"
        if self.thread is None:
            return
        if not self.thread.started:
            self.thread.start()
        if self.thread.paused:
            self.thread.paused = False

    def pause(self):
        print "Button pause pressed"
        if self.thread is None:
            return
        if self.thread.paused == False:
            self.thread.paused = True

    def forward(self):
        print "Button forward pressed"

    def file(self, f):
        self._kill_current_thread()
        instructions = self._get_lines_from_file(f)
        pipeline = self._create_pipeline(instructions)
        self.thread = PipelineThread(pipeline)
        print "File loaded"

    @staticmethod
    def _get_lines_from_file(f):
        def line_filter(line):
            re = Controller.LINE_RE
            match = re.search(line)
            if match:
                return match.group(1)
        return [line_filter(line) for line in f]
    LINE_RE = re.compile(r"([01]{32})")

    def _create_pipeline(self, instructions):
        pipeline = PipelineControl(instructions, self.main_frame)
        pipeline.set_observer(self)
        return pipeline

    def _kill_current_thread(self):
        if self.thread is not None:
            self.thread.stopped = True
            self.thread = None

if __name__ == "__main__":
    main_frame = MainFrame()
    controller = Controller(main_frame)
    controller.run()