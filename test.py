from manim import *


class AnimatingMethods(Scene):
    def construct(self):
        code1_str = """
        def add(k, x):
            a[k] += x
            while k <= n:
                tree[k] += x
                k += k & ~(k - 1)
            return
        add(5, 1)
"""
        code1 = Code(
            code=code1_str,
            language="python",
            font="Monospace",
            line_spacing=0.35,
            insert_line_no=False,
        ).to_edge(RIGHT)

        code2_str = """
        def add(k, x):
            a[k] += x
            while k < n+1:
                tree[k] += x
                k += k & ~(k - 1)
            return
        add(5, 1)
"""
        code2 = Code(
            code=code2_str,
            language="python",
            font="FiraCode Nerd Font",
            line_spacing=0.35,
            insert_line_no=False,
        ).to_edge(LEFT)

        self.add(code1)
        self.add(code2)
