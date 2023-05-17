from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars


class SurroundingCodeLine(Scene):
    def construct(self):
        code = """from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
"""
        code = Code(
            code=code,
            tab_width=4,
            background="window",
            language="C++",
            font="FiraCode Nerd Font",
            line_spacing=0.35,
        )
        self.play(Write(code))

        code_label = index_labels(code.code, color=BLUE)
        self.add(code_label)

        number_label = index_labels(code[1], color=RED)
        self.add(number_label)
