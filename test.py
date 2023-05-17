from manim import *


class AnimatingMethods(Scene):
    def construct(self):
        i = 3
        a = MathTex("tree[k] = ", "\\sum_", "{i=k-p(k) + 1}", "^", "k", " a_i")
        b = MathTex(
            "tree[k] = ", "\\texttt{sum}_q(", "k-p(k)+1", ",", "k", ")"
        ).next_to(a, DOWN)
        self.add(a)
        self.wait()
        # da = index_labels(a)
        # self.add(da)

        self.play(
            *[
                Transform(a[i], b[j])
                for i, j in zip([0, 1, 2, 3, 4, 5], [0, 4, 1, 3, 2, 5])
            ]
        )
        # self.add(b)
        db = index_labels(b)
        # self.add(db)
        self.wait()
