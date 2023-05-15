from manim import *


class CodeFromString(Scene):
    def construct(self):
        code = """from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
"""
        rendered_code = Code(
            code=code,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            line_spacing=0.25,
        )
        self.play(Write(rendered_code))

        line_num = rendered_code.line_numbers

        h = line_num[0].height
        w = rendered_code.background_mobject.width

        debug_line = VGroup(
            *[
                SurroundingRectangle(line)
                .set_fill(YELLOW)
                .set_opacity(0.3)
                .stretch_to_fit_width(w)
                .align_to(rendered_code.background_mobject, LEFT)
                for line in rendered_code.code
            ]
        )

        self.play(Write(debug_line[0]))
        for i in range(len(rendered_code.code) - 1):
            self.play(ReplacementTransform(debug_line[i], debug_line[i + 1]))
        self.wait()
