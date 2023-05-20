from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars

SCALE = 0.7
FONT = "FiraCode Nerd Font"


class SegmentTree(MovingCameraScene):
    def construct(self):
        text = Text("Segment Tree").scale(1.5)
        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

        # region: segment tree
        arr = [[5, 8, 6, 3, 2, 7, 2, 6], [13, 9, 9, 8], [22, 17], [39]]
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

        tree = VGroup(layer, line).to_edge(DOWN)

        # endregion

        self.play(FadeIn(layer[0], target_position=ORIGIN))
        self.wait()

        for i in range(1, nl):
            self.play(Write(line[i - 1]), Write(layer[i])),
            self.wait(0.5)

        self.wait()

        node_label = VGroup()
        nn = 1
        for i in range(len(layer) - 1, -1, -1):
            for node in layer[i]:
                text = Text(str(nn), font=FONT).scale(0.4).next_to(node[0], DOWN, buff=0.1)
                node_label.add(text)
                node.add(text)
                nn += 1

        self.play(Write(node_label))
        self.wait()

        array = (
            VGroup(*[node.copy() for i in range(len(layer) - 1, -1, -1) for node in layer[i]])
            .arrange(RIGHT, buff=0)
            .next_to(tree, DOWN, buff=1.5)
        )

        self.camera.frame.save_state()
        self.play(
            *[Transform(layer[3][i - 0].copy(), array[i]) for i in [0]],
            *[Transform(layer[2][i - 1].copy(), array[i]) for i in [1, 2]],
            *[Transform(layer[1][i - 3].copy(), array[i]) for i in [3, 4, 5, 6]],
            *[Transform(layer[0][i - 7].copy(), array[i]) for i in [7, 8, 9, 10, 11, 12, 13, 14]],
            self.camera.frame.animate.scale(1.5).shift(DOWN),
        )
        self.wait()

        self.play(Restore(self.camera.frame), FadeOut(array), tree.animate.to_edge(LEFT))
        self.wait()

        # region: query
        self.play(*[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(2, 8)])
        self.wait()

        self.play(
            *[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 8)],
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(1, 4)],
        )
        self.play(
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 4)],
            *[layer[2][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(1, 2)],
        )
        self.wait()

        self.play(
            *[layer[2][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [1]],
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [1]],
        )
        self.wait()

        sum_func = """
        def sum(l, r):
            l += n
            r += n
            s = 0
            while l <= r:
                if l % 2 == 1:
                    s += tree[l]
                    l += 1
                if r % 2 == 0:
                    s += tree[r]
                    r -= 1
                l //= 2
                r //= 2
            return s

        sum(1, 7)
        """
        sum_code = (
            Code(
                code=sum_func,
                tab_width=4,
                background="window",
                language="Python",
                line_spacing=0.35,
                insert_line_no=False,
            )
            .scale(SCALE)
            .to_edge(RIGHT)
            .shift(DOWN)
        )
        watch = (
            VGroup(
                VGroup(
                    Text("s:  ", font=FONT, color=GRAY_B).scale(0.5),
                    Text("0  ", font=FONT, color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("l:  ", font=FONT, color=GRAY_B).scale(0.5),
                    Text("1  ", font=FONT, color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("r:  ", font=FONT, color=GRAY_B).scale(0.5),
                    Text("7  ", font=FONT, color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("n:  ", font=FONT, color=GRAY_B).scale(0.5),
                    Text("8  ", font=FONT, color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(sum_code, UP, buff=0.2)
            .align_to(sum_code, LEFT)
            .shift(RIGHT * 0.5)
        )

        for text in watch:
            text[1].align_to(text[0], DOWN)

        self.play(Write(sum_code))
        self.wait()

        line_debug = highlight_line_code(sum_code, 15)

        self.play(Create(line_debug))
        self.play(Write(watch[3], run_time=0.2))
        self.wait()

        n = 8
        l = 1
        r = 7
        s = 0

        self.play(
            Transform(line_debug, highlight_line_code(sum_code, 1)),
            Write(watch[1], run_time=0.2),
            Write(watch[2], run_time=0.2),
        )
        self.wait(0.5)

        label_l = label("l").move_to(node_label[l - 1]).shift(UP + LEFT)
        label_r = label("r").move_to(node_label[r - 1]).shift(UP + LEFT)

        l += n
        self.play(
            Transform(line_debug, highlight_line_code(sum_code, 2)),
            Transform(watch[1][1], Text(str(l) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[1][1])),
            Transform(label_l, label("l").move_to(node_label[l - 1]).shift(UP + LEFT)),
        )
        self.wait(0.5)

        r += n
        self.play(
            Transform(line_debug, highlight_line_code(sum_code, 3)),
            Transform(watch[2][1], Text(str(r) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[2][1])),
            Transform(label_r, label("r").move_to(node_label[r - 1]).shift(UP + LEFT)),
        )
        self.wait(0.5)

        self.play(Transform(line_debug, highlight_line_code(sum_code, 4)), Write(watch[0], run_time=0.2))
        self.wait(0.5)

        while l <= r:
            self.play(Transform(line_debug, highlight_line_code(sum_code, 5)))
            self.wait(0.5)

            if l % 2 == 1:
                self.play(Transform(line_debug, highlight_line_code(sum_code, 6)))
                self.wait(0.5)

                s += st[l]
                self.play(
                    Transform(line_debug, highlight_line_code(sum_code, 7)),
                    Transform(watch[0][1], Text(str(s) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[0][1])),
                )
                self.wait(0.5)

                l += 1
                self.play(
                    Transform(watch[1][1], Text(str(l) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[1][1])),
                    Transform(label_l, label("l").move_to(node_label[l - 1]).shift(UP + LEFT)),
                )

            self.play(Transform(line_debug, highlight_line_code(sum_code, 8)))
            self.wait(0.5)

            if r % 2 == 0:
                self.play(Transform(line_debug, highlight_line_code(sum_code, 9)))
                self.wait(0.5)

                s += st[r]
                self.play(
                    Transform(line_debug, highlight_line_code(sum_code, 10)),
                    Transform(watch[0][1], Text(str(s) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[0][1])),
                )
                self.wait(0.5)

                r -= 1
                self.play(
                    Transform(watch[2][1], Text(str(r) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[2][1])),
                    Transform(label_r, label("r").move_to(node_label[r - 1]).shift(UP + LEFT)),
                )

            self.play(Transform(line_debug, highlight_line_code(sum_code, 11)))
            self.wait(0.5)

            l //= 2
            self.play(
                Transform(line_debug, highlight_line_code(sum_code, 12)),
                Transform(watch[1][1], Text(str(l) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[1][1])),
                Transform(label_l, label("l").move_to(node_label[l - 1]).shift(UP + LEFT)),
            )
            self.wait(0.5)

            r //= 2
            self.play(
                Transform(line_debug, highlight_line_code(sum_code, 4)),
                Transform(watch[2][1], Text(str(r) + "  ", font=FONT, color=PINK).scale(0.5).move_to(watch[2][1])),
                Transform(label_r, label("r").move_to(node_label[r - 1]).shift(UP + LEFT)),
            )
            self.wait(0.5)

        self.play(Transform(line_debug, highlight_line_code(sum_code, 13)))
        self.wait(2)

        self.play(FadeOut(line_debug), FadeOut(watch), FadeOut(label_l), FadeOut(label_r), FadeOut(sum_code))
        self.wait()

        # endregion

        # region: update
        u = 4
        self.play(layer[0][u][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.wait()

        self.play(layer[1][2][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.play(layer[2][1][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.play(layer[3][0][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.wait()

        pi_teacher = SVGMobject("PiCreature/PiCreatures_connving_teacher.svg").to_corner(DOWN + RIGHT)
        pi_speak = text_bubble_ask("Implement \n your self!").next_to(pi_teacher, UP + LEFT, buff=0)

        self.play(FadeIn(pi_teacher), Write(pi_speak))
        self.wait()

        self.play(
            FadeOut(pi_speak),
            FadeOut(tree),
            Transform(pi_teacher, SVGMobject("PiCreature/PiCreatures_tease_teacher.svg").move_to(pi_teacher)),
        )

        layer[0][u][0].set_fill(color=YELLOW, opacity=0)
        layer[1][2][0].set_fill(color=YELLOW, opacity=0)
        layer[2][1][0].set_fill(color=YELLOW, opacity=0)
        layer[3][0][0].set_fill(color=YELLOW, opacity=0)

        pi_speak = (
            text_bubble_ask("How about .... \n update a range").next_to(pi_teacher, UP + LEFT, buff=0).shift(LEFT)
        )

        self.play(
            Write(pi_speak),
            Transform(
                pi_teacher,
                SVGMobject("PiCreature/PiCreatures_pondering_teacher.svg").move_to(pi_teacher).shift(LEFT),
            ),
        )
        pi_student = (
            VGroup(
                SVGMobject("PiCreature/PiCreatures_gracious.svg"),
                SVGMobject("PiCreature/PiCreatures_gracious.svg"),
                SVGMobject("PiCreature/PiCreatures_gracious.svg"),
            )
            .arrange(RIGHT)
            .to_corner(DOWN + LEFT)
        )
        student_speak = text_bubble_speech("W...What?").next_to(pi_student, UP + RIGHT, buff=0)
        self.play(
            ReplacementTransform(
                VGroup(
                    SVGMobject("PiCreature/PiCreatures_plain.svg"),
                    SVGMobject("PiCreature/PiCreatures_plain.svg"),
                    SVGMobject("PiCreature/PiCreatures_plain.svg"),
                )
                .arrange(RIGHT)
                .to_corner(DOWN + LEFT),
                pi_student,
            ),
            Write(student_speak),
        )
        # endregion

        self.wait()

        self.play(FadeOut(pi_teacher), FadeOut(pi_student), FadeOut(pi_speak), FadeOut(student_speak))
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


def label(s):
    label = SVGMobject("label.svg")
    font = "FiraCode Nerd Font"
    text = Text(s, font=font).move_to(label.get_center()).shift(0.25 * UP + 0.4 * LEFT)

    return VGroup(label, text).scale(0.5)


def text_bubble_ask(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg").flip(UP)
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.3)
    return VGroup(bubble_speech, text)


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)
