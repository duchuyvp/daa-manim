from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars


class SurroundingCodeLine(Scene):
    def construct(self):
        big_circle = Circle(radius=2, opacity=0.5)

        small_circles = Circle(radius=1, color=RED)
