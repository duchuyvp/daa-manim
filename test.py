from manim import *


class CodeFromString(Scene):
    def construct(self):
        bubble = SVGMobject("PiCreature/Bubbles_speech.svg")
        self.add(bubble)
        dot = Dot().shift(UP*0.25)
        self.add(dot)
