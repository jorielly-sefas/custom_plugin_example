from roa.core.models.filter import Filter


class FilterExample(Filter):
    inputs = {"param": "int"}

    def __init__(self, param: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def run(self, objects):
        # Your code here
        # Objects is the list of objects recieved by the filter
        # Return the list of objects that are selected by the filter
        try:
            return [obj for obj in objects]
        except:
            return []