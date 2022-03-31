from game.scripting.action import Action
from constants import *

class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        

    def execute(self, cast, script):

        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT,)
        self._draw_label(cast, SCORE_GROUP, )
        self._draw_label(cast, POWERUP_GROUP,)

    def _draw_label(self, cast, group):
        pass
