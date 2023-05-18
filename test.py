from manim import *


class Test(MovingCameraScene):
    def construct(self):
        n = 7
        layer = VGroup(
            *[
                VGroup(*[Square(1) for _ in range(pow(2, n - i - 1))]).arrange(
                    RIGHT, buff=pow(2, i) - 1
                )
                for i in range(n)
            ]
        ).arrange(UP, buff=1)

        line = VGroup(
            *[
                VGroup(
                    *[
                        Line(
                            layer[i][j].get_edge_center(UP),
                            layer[i + 1][j // 2].get_edge_center(DOWN)
                            + 0.25 * (LEFT if j % 2 == 0 else RIGHT),
                        )
                        for j in range(len(layer[i]))
                    ]
                )
                for i in range(n - 1)
            ]
        )

        tree = VGroup(layer, line).to_edge(DOWN)
        self.play(Write(tree, run_time=3), self.camera.frame.animate.scale(10))
        self.wait(2)
