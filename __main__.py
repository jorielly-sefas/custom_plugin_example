from roa.core.plugin_manager import RoaPlugin
from roa.core.toolset import Toolset

from plugin_example.detectors.detector_example import DetectorExample
from plugin_example.enhancers.enhancer_example import EnhancerExample
from plugin_example.filters.filter_example import FilterExample
from plugin_example.modifiers.modifier_example import ModifierExample


class ExampleLibrary(RoaPlugin):
    name = 'PluginExample'
    toolset = Toolset(
        detectors=[DetectorExample],
        enhancers=[EnhancerExample],
        filters=[FilterExample],
        modifiers=[ModifierExample],
        objects=[],
    )

def get_library():
    return ExampleLibrary

if __name__ == "__main__":
    print(get_library())
