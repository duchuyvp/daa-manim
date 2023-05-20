from manim import *

SCALE = 0.7
FONT = "FiraCode Nerd Font"


class RangeQuery(Scene):
    def construct(self):
        text = Text("Range Update").scale(1.5)
        text_small = Text("Range query").next_to(text, DOWN)
        VGroup(text, text_small).move_to(ORIGIN)
        self.play(Write(text_small), Write(text))
        self.wait()

        self.play(FadeOut(text), FadeOut(text_small))
        self.wait()

        arr = [[5, 8, 6, 3, 2, 7, 2, 6], [13, 9, 9, 8], [22, 17], [39]]
        laz = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0], [0, 0], [0]]
        st = [0, 39, 22, 17, 13, 9, 9, 8, 5, 8, 6, 3, 2, 7, 2, 6]
        nl = len(arr)
        layer = VGroup(
            *[
                VGroup(
                    *[
                        VGroup(Square(side_length=1, color=BLUE), Text(str(arr[i][j])))
                        for j in range(pow(2, nl - i - 1))
                    ]
                ).arrange(RIGHT, buff=pow(2, i) - 1)
                for i in range(nl)
            ]
        ).arrange(UP, buff=1)

        line = VGroup(
            *[
                VGroup(
                    *[
                        Line(
                            layer[i][j].get_edge_center(UP),
                            layer[i + 1][j // 2].get_edge_center(DOWN) + 0.25 * (LEFT if j % 2 == 0 else RIGHT),
                            color=BLUE,
                        )
                        for j in range(len(layer[i]))
                    ]
                )
                for i in range(nl - 1)
            ]
        )

        nn = 1
        for i in range(len(layer) - 1, -1, -1):
            for node in layer[i]:
                text = Text(str(nn), font=FONT).scale(0.4).next_to(node[0], DOWN, buff=0.1)
                node.add(text)
                nn += 1

        tree = VGroup(layer, line).to_edge(DOWN).scale(0.9)

        self.play(FadeIn(tree))
        self.wait()

        self.play(
            *[
                Transform(
                    layer[i][j][2],
                    Text(str(pow(2, i) * j + 1) + "-" + str(pow(2, i) * j + pow(2, i)), font=FONT)
                    .scale(0.3)
                    .next_to(layer[i][j][0], DOWN, buff=0.1),
                )
                for i in range(len(layer))
                for j in range(len(layer[i]))
            ],
        )
        self.wait()

        # region top down

        query = VGroup(MathTex("\\texttt{q}(3, 7)").scale(SCALE).to_edge(UP + RIGHT, buff=2))

        self.play(
            Write(query),
            *[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(2, 7)],
        )
        self.wait()

        self.add_foreground_mobjects(layer)
        self.add_foreground_mobjects(query)

        self.play(
            Transform(query, label_g("\\texttt{q}(3, 7)").next_to(layer[3][0][0], UP + RIGHT, buff=-0.25)),
            layer[3][0][0].animate.set_color(RED),
        )
        self.wait()

        self.play(
            Transform(
                query,
                VGroup(
                    label_g("\\texttt{q}(3, 4)").next_to(layer[2][0][0], UP + RIGHT, buff=-0.25),
                    label_g("\\texttt{q}(5, 7)").next_to(layer[2][1][0], UP + RIGHT, buff=-0.25),
                ),
            ),
            layer[2][0][0].animate.set_color(RED),
            layer[2][1][0].animate.set_color(RED),
            line[2][0].animate.set_color(RED),
            line[2][1].animate.set_color(RED),
        )
        self.wait(0.5)

        self.play(
            Transform(query[0], label_g("\\texttt{q}(3, 4)").next_to(layer[1][1][0], UP + RIGHT, buff=-0.25)),
            Transform(
                query[1],
                VGroup(
                    label_g("\\texttt{q}(5, 6)").next_to(layer[1][2][0], UP + RIGHT, buff=-0.25),
                    label_g("\\texttt{q}(7, 7)").next_to(layer[1][3][0], UP + RIGHT, buff=-0.25),
                ),
            ),
            layer[1][1][0].animate.set_color(RED),
            layer[1][2][0].animate.set_color(RED),
            layer[1][3][0].animate.set_color(RED),
            line[1][1].animate.set_color(RED),
            line[1][2].animate.set_color(RED),
            line[1][3].animate.set_color(RED),
        )
        self.wait(0.5)

        tmp_sq = Square(side_length=1, color=RED).move_to(layer[0][6][0]).scale(0.9)
        self.play(
            Transform(
                query[1][1],
                label_g("\\texttt{q}(7, 7)").next_to(layer[0][6][0], UP + RIGHT, buff=-0.25),
            ),
            layer[0][6][0].animate.set_stroke_color(RED),
            line[0][6].animate.set_color(RED),
            FadeIn(tmp_sq),
        )
        self.add_foreground_mobjects(tmp_sq)
        self.add_foreground_mobjects(query)
        self.wait()

        self.play(
            FadeOut(query),
            FadeOut(layer),
            FadeOut(line),
            FadeOut(tmp_sq),
        )
        self.wait()

        layer[3][0][0].set_color(BLUE)
        layer[2][0][0].set_color(BLUE)
        layer[2][1][0].set_color(BLUE)
        layer[1][1][0].set_color(BLUE)
        layer[1][2][0].set_color(BLUE)
        layer[1][3][0].set_color(BLUE)
        layer[0][6][0].set_stroke_color(BLUE)
        line[2][1].set_color(BLUE)
        line[2][0].set_color(BLUE)
        line[1][1].set_color(BLUE)
        line[1][2].set_color(BLUE)
        line[1][3].set_color(BLUE)
        line[0][6].set_color(BLUE)
        for i in range(2, 7):
            layer[0][i][0].set_fill(color=YELLOW, opacity=0)

        self.remove_foreground_mobjects(layer, tmp_sq, query)

        # endregion

        text = Text("Lazy propagation")

        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

        self.play(FadeIn(tree))
        self.wait()

        self.play(
            *[
                Transform(
                    layer[i][j][1],
                    Text(str(arr[i][j]) + "/" + str(laz[i][j])).scale(0.5).move_to(layer[i][j][0]),
                )
                for i in range(len(layer))
                for j in range(len(layer[i]))
            ],
        )
        self.wait()

        s_explain = Tex("$s$: Sum of range $\\Rightarrow$").scale(0.6).next_to(layer[3][0][0], LEFT, buff=0.2)
        z_explain = Tex("$\\Leftarrow$ $z$: Propagation value").scale(0.6).next_to(layer[3][0][0], RIGHT, buff=0.2)

        self.play(Write(s_explain), Write(z_explain), run_time=0.5)
        self.wait()

        self.play(
            FadeOut(s_explain),
            FadeOut(z_explain),
        )

        # region range update
        add = VGroup(MathTex("\\texttt{a}([2, 8], 2)").scale(SCALE).to_edge(UP + RIGHT, buff=2))
        brace = Brace(VGroup(*[layer[0][i] for i in range(1, 8)]), DOWN, buff=0.1)

        self.play(Write(brace), Write(add))
        self.wait()

        self.add_foreground_mobjects(layer)
        self.add_foreground_mobjects(add)

        self.play(
            Transform(
                add, label_g("\\texttt{a}([2, 8], 2)", scale=0.5).next_to(layer[3][0][0], UP + RIGHT, buff=-0.25)
            ),
            layer[3][0][0].animate.set_color(RED),
        )
        self.wait()

        arr[3][0] += 2 * 7
        self.play(
            Transform(
                add,
                VGroup(
                    label_g("\\texttt{a}([2, 4], 2)", scale=0.5).next_to(layer[2][0][0], UP + RIGHT, buff=-0.25),
                    label_g("\\texttt{a}([5, 8], 2)", scale=0.5).next_to(layer[2][1][0], UP + RIGHT, buff=-0.25),
                ),
            ),
            layer[2][0][0].animate.set_color(RED),
            layer[2][1][0].animate.set_color(RED),
            line[2][0].animate.set_color(RED),
            line[2][1].animate.set_color(RED),
            Transform(
                layer[3][0][1],
                Text(str(arr[3][0]) + "/" + str(laz[3][0]), color=PURPLE).scale(0.5).move_to(layer[3][0][0]),
            ),
        )
        self.wait(0.5)

        arr[2][0] += 2 * 3
        laz[2][1] += 2

        self.play(
            Transform(
                add[0],
                VGroup(
                    label_g("\\texttt{a}([2, 2], 2)", scale=0.5).next_to(layer[1][0][0], UP + RIGHT, buff=-0.25),
                    label_g("\\texttt{a}([3, 4], 2)", scale=0.5).next_to(layer[1][1][0], UP + RIGHT, buff=-0.25),
                ),
            ),
            layer[1][0][0].animate.set_color(RED),
            layer[1][1][0].animate.set_color(RED),
            line[1][0].animate.set_color(RED),
            line[1][1].animate.set_color(RED),
            Transform(
                layer[2][0][1],
                Text(str(arr[2][0]) + "/" + str(laz[2][0]), color=PURPLE).scale(0.5).move_to(layer[2][0][0]),
            ),
            Transform(
                layer[2][1][1],
                Text(str(arr[2][1]) + "/" + str(laz[2][1]), color=PURPLE).scale(0.5).move_to(layer[2][1][0]),
            ),
        )
        self.wait(0.5)

        arr[1][0] += 2 * 1
        laz[1][1] += 2

        tmp_sq = Square(side_length=1, color=RED).move_to(layer[0][1][0]).scale(0.9)
        self.play(
            Transform(
                add[0][0], label_g("\\texttt{a}([2, 2], 2)", scale=0.5).next_to(layer[0][1][0], UP + RIGHT, buff=-0.25)
            ),
            layer[0][1][0].animate.set_color(RED),
            line[0][1].animate.set_color(RED),
            Transform(
                layer[1][0][1],
                Text(str(arr[1][0]) + "/" + str(laz[1][0]), color=PURPLE).scale(0.5).move_to(layer[1][0][0]),
            ),
            Transform(
                layer[1][1][1],
                Text(str(arr[1][1]) + "/" + str(laz[1][1]), color=PURPLE).scale(0.5).move_to(layer[1][1][0]),
            ),
            FadeIn(tmp_sq),
        )
        self.add_foreground_mobjects(tmp_sq)
        self.add_foreground_mobjects(add)
        self.wait(0.5)

        arr[0][1] += 2 * 1
        laz[0][1] += 0

        self.play(
            Transform(
                layer[0][1][1],
                Text(str(arr[0][1]) + "/" + str(laz[0][1]), color=PURPLE).scale(0.5).move_to(layer[0][1][0]),
            )
        )
        self.wait()

        self.play(
            FadeOut(add),
            FadeOut(tmp_sq),
            FadeOut(brace),
            layer[0][1][0].animate.set_color(BLUE),
            layer[0][1][1].animate.set_color(WHITE),
            layer[1][0][0].animate.set_color(BLUE),
            layer[1][0][1].animate.set_color(WHITE),
            layer[1][1][0].animate.set_color(BLUE),
            layer[1][1][1].animate.set_color(WHITE),
            layer[2][0][0].animate.set_color(BLUE),
            layer[2][0][1].animate.set_color(WHITE),
            layer[2][1][0].animate.set_color(BLUE),
            layer[2][1][1].animate.set_color(WHITE),
            layer[3][0][0].animate.set_color(BLUE),
            layer[3][0][1].animate.set_color(WHITE),
            line[0][1].animate.set_color(BLUE),
            line[1][0].animate.set_color(BLUE),
            line[1][1].animate.set_color(BLUE),
            line[2][0].animate.set_color(BLUE),
            line[2][1].animate.set_color(BLUE),
        )
        self.wait()

        self.remove_foreground_mobjects(layer, tmp_sq, add)

        # endregion

        pi_student = SVGMobject("PiCreature/PiCreatures_happy.svg").to_edge(DOWN + LEFT)

        self.play(Transform(pi_student, SVGMobject("PiCreature/PiCreatures_dance_kick.svg").to_edge(DOWN + LEFT)))
        self.wait()

        self.play(FadeOut(pi_student), FadeOut(tree))
        self.wait()

        pi_teacher = SVGMobject("PiCreature/PiCreatures_plain_teacher.svg").to_edge(DOWN + LEFT)
        pi_teacher_speech = text_bubble_speech("Wait...").next_to(pi_teacher, UP + RIGHT, buff=0)
        self.play(FadeIn(pi_teacher), Write(pi_teacher_speech))
        self.wait()


def label_g(s, scale=SCALE):
    label = SVGMobject("left_label.svg").scale(0.5)
    query = MathTex(s).scale(scale).move_to(label).shift(0.1 * UP + 0.15 * RIGHT)

    return VGroup(label, query)


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)
