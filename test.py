from manim import *


class CodeFromString(Scene):
    def construct(self):
        text1 = MathTex("a")
        text2 = MathTex("+")
        text3 = MathTex("b")
        left_group = VGroup(text1, text2, text3).arrange(RIGHT)
        text4 = MathTex("=")
        text5 = MathTex("c")
        right_group = VGroup(text5).arrange(RIGHT)

        equation = VGroup(left_group, text4, right_group).arrange(RIGHT)

        self.play(Write(left_group))
        self.play(Write(text4))
        self.play(Transform(left_group.copy(), right_group))
        self.wait(1)
