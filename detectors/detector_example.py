from roa.core.models.detector import Detector, DetectResult

class DetectorExample(Detector):
    inputs = {"param": "int"}

    def __init__(self, param: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = int(param)

    def detect_start(self) -> bool:
        # Your code here
        # If your start condition is met, return DetectResult(detected=True)
        # Otherwise, return DetectResult(detected=False)
        self.counter = 0
        return DetectResult(detected=True)

    def detect_end(self) -> bool:
        # Your code here
        # If your end condition is met, return DetectResult(detected=True)
        # Otherwise, return DetectResult(detected=False)
        self.counter += 1
        if self.counter == self.param:
            return DetectResult(detected=True)
        return DetectResult(detected=False)