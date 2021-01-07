from roa.core.models.modifier import Modifier


class ModifierExample(Modifier):
    inputs = {"param": "int"}

    def __init__(self, param: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.param = param

    def run(self, text):
        # Your code here
        # Text is the value recieved by the modifier
        # Return value will be output of the modifier
        try:
            return text
        except:
            return None
