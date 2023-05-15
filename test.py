from manim import *


class AnimatingMethods(Scene):
    def construct(self):
        self.play(Create(Rectangle(color=RED, fill_opacity=0.5)))
