from manim import *
from colour import Color


class SegmentTree(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=0.5)

        self.add(sq, index_labels(sq))
