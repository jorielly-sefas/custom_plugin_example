from typing import List

from roa.core.models.enhancer import Enhancer
from roa.core.utils.types import FilterRef, ZoneRef

class EnhancerExample(Enhancer):
    inputs = {"x": "int", "y": "int"}

    # All enhancers should take a zone (where the enhancer will be applied), and a list of filters
    # These do not have to be listed in the input property
    def __init__(self, zone: str, filters: List[FilterRef] = None, x: int, y: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.zone = ZoneRef(zone)
        self._x = x
        self._y = y
        self.filters: List[FilterRef] = [FilterRef(x) for x in filters]

    def execute(self):
        # Your code here
        # These first two steps, getting the elements and applying filters will be the same for most enhancers
        zone_objects = self.zone.get_elements()
        for filter_ in self.filters:
            zone_objects = filter_.run(zone_objects)
        for zone_object in zone_objects:
            # This is where you want to apply your enhancement to the individual objects
            zone_object.move(self._x, self._y)