import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Carts(Actor):
    """
    A cart which strangely has a plumber in it that is scrambling
    to avoid a green, egg laying, dinosaur
    
    The responsibility of the cart is to move itself.

    """
    
    def __init__(self):
        
        # TODO eventually Create 4 Carts
        
        super().__init__()
        self._segments = []
        self._prepare_cart()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()

        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    # TODO change to get_bike
    def get_cart(self):
        return self._segments[0]

    # # TODO change to grow_trail
    # def grow_tail(self, number_of_segments):
    #     for i in range(self._number_of_segments):
    #         tail = self._segments[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("O")
    #         segment.set_color(constants.GREEN)
    #         self._segments.append(segment)

    def turn_cart(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_cart(self):
        
        x, y = self._place_cart() 

        cart_color = self._select_color()

        # for i in range(constants.BIKE_LENGTH):
        # TODO figure position constants.BIKE_LENGTH added in place of i
        position = Point(x - constants.BIKE_LENGTH * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "O"
        color = cart_color
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)

    def _select_color(self):
        # Assign blue color, then red, yellow, green.
        pass


    def _place_cart(self):
        # Place bike in upper left quadrant if first iteration
        # Place bike in upper right and so on until 4

        return int(constants.MAX_X / 2), int(constants.MAX_Y / 2)

    def buff(self):
        pass
