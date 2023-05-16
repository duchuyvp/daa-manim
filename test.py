from manim import *


class AnimatingMethods(Scene):
    def construct(self):
        bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
        self.add(bubble_speech)
