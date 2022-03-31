import constants

from game.Casting.cast import Cast
from game.Casting.food import Food
from game.Casting.score import Score
from game.Casting.carts import Cart
from game.Scripting.script import Script
from game.Scripting.control_actors_action import ControlActorsAction
from game.Scripting.move_actors_action import MoveActorsAction
from game.Scripting.handle_collisions_action import HandleCollisionsAction
from game.Scripting.draw_actors_action import DrawActorsAction
from game.Directing.director import Director
from game.Services.keyboard_service import KeyboardService
from game.Services.video_service import VideoService
from game.Shared.color import Color
from game.Shared.point import Point


def main():
    
    """
    The goal is to create a second playable character.
    """

    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("cart", Cart())
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()