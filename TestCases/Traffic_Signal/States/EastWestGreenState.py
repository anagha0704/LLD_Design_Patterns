import time
from IntersectionState import IntersectionState
from Direction import Direction
from Signal import Signal

class EastWestGreenState(IntersectionState):

    def handle(self,  context:'IntersectionController')->None:
        print(f"***Intersection {context.get_id()}: Cycle Start -> East-West GREEN***")

        context.get_light(Direction.EAST).start_green()
        context.get_light(Direction.WEST).start_green()
        context.get_light(Direction.NORTH).set_color(Signal.RED)
        context.get_light(Direction.SOUTH).set_color(Signal.RED)

        time.sleep(context.get_green_duration()/1000.0)

        context.get_light(Direction.EAST).transition()
        context.get_light(Direction.WEST).transition()

        time.sleep(context.get_yellow_duration()/1000.0)

        context.get_light(Direction.EAST).transition()
        context.get_light(Direction.WEST).transition()

        from States.NorthSouthGreenState import NorthSouthGreenState
        context.set_state(NorthSouthGreenState())