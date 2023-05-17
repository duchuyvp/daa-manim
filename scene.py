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
            insert_line_no=False,
        )
        # code.code = remove_invisible_chars(code.code)
        self.play(Write(code))

        h = code.code[0].height + 0.05
        w = code.background_mobject.width

        a = index_labels(code.code)
        self.add(a)

        for line in [0, 2, 3, 4, 5, 6, 7]:
            # surround_line = (
            #     Rectangle(width=w, height=h, fill_opacity=0.3, stroke_width=0)
            #     .move_to(code.code[line])
            #     .align_to(code, LEFT)
            # )
            self.add(highlight_line_code(code, line))
            self.wait()


def highlight_line_code(code: Code, line) -> Rectangle:
    code.code = remove_invisible_chars(code.code)
    h = code.code[0].height + 0.05
    w = code.background_mobject.width
    surround_line = (
        Rectangle(width=w, height=h, fill_opacity=0.3, stroke_width=0, color=YELLOW_D)
        .move_to(code.code[line])
        .align_to(code, LEFT)
    )
    return surround_line
