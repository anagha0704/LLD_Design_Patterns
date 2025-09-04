import time
from IntersectionState import IntersectionState
from States.EastWestGreenState import EastWestGreenState
from Direction import Direction
from Signal import Signal

class NorthSouthGreenState(IntersectionState):

    def handle(self, context: "IntersectionController")->None:
        print(f"***Intersection {context.get_id()}: Cycle Start -> North-South GREEN***")

        context.get_light(Direction.NORTH).start_green()
        context.get_light(Direction.SOUTH).start_green()
        context.get_light(Direction.EAST).set_color(Signal.RED)
        context.get_light(Direction.WEST).set_color(Signal.RED)

        time.sleep(context.get_green_duration()/1000.0)

        context.get_light(Direction.NORTH).transition()
        context.get_light(Direction.SOUTH).transition()

        time.sleep(context.get_yellow_duration()/1000.0)

        context.get_light(Direction.NORTH).transition()
        context.get_light(Direction.SOUTH).transition()

        context.set_state(EastWestGreenState())