from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars


class SurroundingCodeLine(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=0.5)
