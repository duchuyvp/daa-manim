from manim import *


class TabularVGroup(VGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arrange(DOWN, aligned_edge=LEFT)


class TikzToManim(Scene):
    def construct(self):
        a = [1, 2, 3]
        b = [1, 1, 1]
        self.add(node_map(a, b))


def node_map(a, b):
    text_a = VGroup(*[Tex(str(a[i])) for i in range(len(a))]).arrange(RIGHT, buff=0.4)
    text_b = VGroup(*[Tex(str(b[i])).next_to(text_a[i], DOWN, buff=0.3) for i in range(len(b))])
    line = Line(
        text_a.get_critical_point(DOWN + LEFT) + 0.1 * LEFT, text_a.get_critical_point(DOWN + RIGHT) + 0.1 * RIGHT
    ).next_to(text_a, DOWN, buff=0.15)

    sr = SurroundingRectangle(VGroup(text_a, text_b, line), buff=0.15, color=BLUE)

    return VGroup(text_a, text_b, line, sr)
