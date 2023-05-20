from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars

SCALE = 0.7


class BinaryIndexedTree(MovingCameraScene):
    def construct(self):
        text = Text("Binary Indexed Tree").scale(1.5)
        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

        arr = [0, 1, 3, 4, 8, 6, 1, 4, 2]
        prefix_arr = arr.copy()
        for i in range(1, len(prefix_arr)):
            prefix_arr[i] += prefix_arr[i - 1]

        bit = arr.copy()
        for k in range(1, len(bit)):
            pk = k & ~(k - 1)
            bit[k] = prefix_arr[k] - prefix_arr[k - pk]

        arr_v = VGroup(
            *[
                VGroup(
                    Square(side_length=1, color=BLUE),
                    Text(str(arr[i])),
                )
                for i in range(1, len(arr))
            ]
        ).arrange(RIGHT, buff=0)

        index_arr_v = VGroup(
            *[
                Text(str(i), font="FiraCode Nerd Font").scale(0.5).next_to(arr_v[i - 1][1], DOWN)
                for i in range(1, len(arr))
            ]
        )

        arr_vgroup = VGroup(arr_v, index_arr_v).arrange(DOWN, buff=0.5).scale(SCALE).to_edge(UP)
        arr_vgroup.to_edge(UP)
        self.play(Write(arr_vgroup))

        bit_v = VGroup(
            *[
                VGroup(
                    Square(side_length=1, color=BLUE),
                    Text(str(bit[i])),
                )
                for i in range(1, len(arr))
            ]
        ).arrange(DOWN, buff=0)

        index_bit_v = VGroup(*[Text(str(i)).scale(0.5).next_to(bit_v[i - 1][1], LEFT) for i in range(1, len(arr))])

        bit_vgroup = (
            VGroup(bit_v, index_bit_v)
            .arrange(LEFT, buff=0.5)
            .scale(SCALE)
            .next_to(arr_vgroup, DOWN)
            .to_edge(LEFT, buff=1.5)
        )

        bit_label = Tex("tree").scale(SCALE).next_to(bit_v, UP)
        bit_vgroup.add(bit_label)
        self.play(Write(bit_label))

        self.play(*[Create(bit_v[i][0]) for i in range(len(bit_v))], Create(index_bit_v))
        self.wait()

        origin = ORIGIN + DOWN * 2 + RIGHT * 2
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=12).move_to(origin))
        self.wait()

        ex_pk = VGroup(
            MathTex("1110_2"),
            MathTex("1000_2"),
            MathTex("\ 100_2"),
            MathTex("\ \ 10_2"),
        ).arrange(DOWN, buff=0.2)
        line = Line(ORIGIN, RIGHT * ex_pk[0].get_width()).next_to(ex_pk[0], DOWN, buff=0.1)
        for i in range(1, len(ex_pk)):
            ex_pk[i].align_to(ex_pk[0], RIGHT)
        ex_pk_v = VGroup(ex_pk, line).move_to(origin)
        text_k = MathTex("\ k = 14").next_to(ex_pk[0], RIGHT, buff=0.5)
        self.play(Write(ex_pk[0]), Create(line), Write(text_k))
        self.wait()

        text_pk = MathTex("\ p(k) = 2").next_to(ex_pk[-1], RIGHT, buff=0.5)
        self.play(*[FadeIn(ex_pk[i], target_position=ex_pk[0]) for i in range(1, len(ex_pk))])
        self.wait()

        self.play(Write(text_pk))
        self.wait()

        self.play(FadeOut(ex_pk_v), FadeOut(text_k), FadeOut(text_pk))
        self.wait()

        self.play(Restore(self.camera.frame))
        formula_tree = MathTex("tree[k] = ", "\\texttt{sum}_q(", "k-p(k)+1", ",", "k", ")")
        self.play(Write(formula_tree))
        self.wait()

        self.play(FadeOut(formula_tree))
        self.wait()

        value_v = VGroup(
            *[
                Rectangle(
                    height=0.5,
                    width=(i & ~(i - 1)),
                    color=GOLD,
                    stroke_width=0,
                    fill_opacity=0.3,
                )
                .scale(SCALE)
                .move_to(bit_v[i - 1][0])
                .align_to(arr_v[i - 1][0], RIGHT)
                for i in range(1, len(arr))
            ]
        )

        self.play(Create(value_v))
        self.wait()

        self.play(*[ReplacementTransform(value_v[i].copy(), bit_v[i][1]) for i in range(len(value_v))])
        self.wait()

        self.play(
            arr_vgroup.animate.shift(LEFT * 2),
            value_v.animate.shift(LEFT * 2),
            bit_vgroup.animate.shift(LEFT),
        )
        self.wait()

        formula_sum = (
            MathTex(
                "\\texttt{sum}_q(1,6) ",
                "=",
                "\\texttt{sum}_q(1,4) ",
                "+",
                "\\texttt{sum}_q(5,6)",
            )
            .scale(SCALE)
            .next_to(value_v, RIGHT, buff=0.5)
            .shift(UP)
        )

        formula_sum_ = (
            MathTex(
                "\\texttt{sum}_q(1,6) ",
                "=",
                "tree[4] ",
                "+",
                "tree[6] ",
            )
            .scale(SCALE)
            .next_to(value_v, RIGHT, buff=0.5)
            .shift(UP)
        )

        formula_sum__ = (
            MathTex(
                "\\texttt{sum}_q(1,6) ",
                "=",
                "16 ",
                "+",
                "7 ",
            )
            .scale(SCALE)
            .next_to(value_v, RIGHT, buff=0.5)
            .shift(UP)
        )

        self.play(
            Write(formula_sum[0]),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in range(6)],
        )
        self.play(
            *[Write(formula_sum[i]) for i in range(1, len(formula_sum))],
            *[bit_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in [3, 5]],
            *[value_v[i].animate.set_fill(YELLOW, opacity=0.4) for i in [3, 5]],
        )
        self.wait()

        self.play(*[Transform(formula_sum[i], formula_sum_[i]) for i in range(len(formula_sum))])
        self.wait()

        self.play(*[Transform(formula_sum[i], formula_sum__[i]) for i in range(len(formula_sum))])
        self.wait()

        self.play(
            FadeOut(formula_sum),
            *[arr_v[i][0].animate.set_fill(WHITE, opacity=0) for i in range(6)],
            *[bit_v[i][0].animate.set_fill(WHITE, opacity=0) for i in [3, 5]],
            *[value_v[i].animate.set_fill(GOLD, opacity=0.3) for i in [3, 5]],
        )

        sum_func = """
        def sum(k):
            s = 0
            while k > 0:
                s += tree[k]
                k -= k & ~(k - 1)
            return s

        sum(7)
"""
        sum_code = (
            Code(
                code=sum_func,
                tab_width=4,
                background="window",
                language="C++",
                font="FiraCode Nerd Font",
                line_spacing=0.35,
                insert_line_no=False,
            )
            .scale(SCALE)
            .to_edge(RIGHT, buff=1.5)
            .shift(DOWN)
        )

        watch = (
            VGroup(
                VGroup(
                    Text("k:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("7  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("s:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("0  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("n:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("8  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
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

        line_debug = highlight_line_code(sum_code, 7)

        self.play(Create(line_debug))
        self.play(Write(watch[2], run_time=0.2))
        self.wait()

        k = 7
        s = 0

        self.play(
            Transform(line_debug, highlight_line_code(sum_code, 1)),
            Write(watch[0], run_time=0.2),
        )
        self.wait(0.5)
        self.play(
            Transform(line_debug, highlight_line_code(sum_code, 2)),
            Write(watch[1], run_time=0.2),
        )
        self.wait(0.5)
        while k > 0:
            self.play(Transform(line_debug, highlight_line_code(sum_code, 3)))
            self.wait(0.5)
            s += bit[k]

            self.play(
                Transform(line_debug, highlight_line_code(sum_code, 4)),
                Transform(
                    watch[1][1],
                    Text(str(s) + "  ", font="FiraCode Nerd Font", color=PINK).scale(0.5).move_to(watch[1][1]),
                    run_time=0.2,
                ),
                Indicate(bit_v[k - 1][1]),
            )
            self.wait(0.5)

            k -= k & ~(k - 1)
            self.play(
                Transform(line_debug, highlight_line_code(sum_code, 2)),
                Transform(
                    watch[0][1],
                    Text(str(k) + "  ", font="FiraCode Nerd Font", color=PINK).scale(0.5).move_to(watch[0][1]),
                    run_time=0.2,
                ),
            )
            self.wait(0.5)

        self.play(Transform(line_debug, highlight_line_code(sum_code, 5)))
        self.wait()

        self.play(
            FadeOut(line_debug),
            FadeOut(watch),
            FadeOut(sum_code),
        )
        self.wait()

        u = 3

        self.play(arr_v[u - 1][0].animate.set_fill(YELLOW, opacity=0.4))
        self.wait()

        self.play(
            *[bit_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in [2, 3, 7]],
            *[value_v[i].animate.set_fill(YELLOW, opacity=0.4) for i in [2, 3, 7]],
        )
        self.wait()

        self.play(
            arr_v[u - 1][0].animate.set_fill(YELLOW, opacity=0),
            *[bit_v[i][0].animate.set_fill(YELLOW, opacity=0) for i in [2, 3, 7]],
            *[value_v[i].animate.set_fill(GOLD, opacity=0.3) for i in [2, 3, 7]],
        )

        add_func = """
        def add(k, x):
            a[k] += x
            while k < n+1:
                tree[k] += x
                k += k & ~(k - 1)
            return

        add(5, 1)
"""
        add_code = (
            Code(
                code=add_func,
                tab_width=4,
                background="window",
                language="C++",
                font="FiraCode Nerd Font",
                line_spacing=0.35,
                insert_line_no=False,
            )
            .scale(SCALE)
            .to_edge(RIGHT, buff=1.5)
            .shift(DOWN)
        )

        k = 5
        x = 1

        watch = (
            VGroup(
                VGroup(
                    Text("k:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("5  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("x:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("1  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Text("n:  ", font="FiraCode Nerd Font", color=GRAY_B).scale(0.5),
                    Text("8  ", font="FiraCode Nerd Font", color=PINK).scale(0.5),
                ).arrange(RIGHT, buff=0.1),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(add_code, UP, buff=0.2)
            .align_to(add_code, LEFT)
            .shift(RIGHT * 0.5)
        )

        for text in watch:
            text[1].align_to(text[0], DOWN)

        self.play(Write(add_code))
        self.wait()

        line_debug = highlight_line_code(add_code, 7)

        self.play(Create(line_debug))
        self.play(Write(watch[2], run_time=0.2))
        self.wait()

        self.play(
            Transform(line_debug, highlight_line_code(add_code, 1)),
            Write(watch[0], run_time=0.2),
            Write(watch[1], run_time=0.2),
        )
        self.wait(0.5)

        arr[k] += x
        self.play(
            Transform(line_debug, highlight_line_code(add_code, 2)),
            Transform(
                arr_v[k - 1][1],
                Text(str(arr[k]), color=PINK).scale(SCALE).move_to(arr_v[k - 1][1]),
                run_time=0.2,
            ),
        )
        self.wait(0.5)

        while k <= 8:
            self.play(Transform(line_debug, highlight_line_code(add_code, 3)))
            self.wait(0.5)
            bit[k] += x

            self.play(
                Transform(line_debug, highlight_line_code(add_code, 4)),
                Transform(
                    bit_v[k - 1][1],
                    Text(str(bit[k]), color=PINK).scale(SCALE).move_to(bit_v[k - 1][1]),
                    run_time=0.2,
                ),
                Indicate(value_v[k - 1]),
            )
            self.wait(0.5)

            k += k & ~(k - 1)
            self.play(
                Transform(line_debug, highlight_line_code(add_code, 2)),
                Transform(
                    watch[0][1],
                    Text(str(k) + "  ", font="FiraCode Nerd Font", color=PINK).scale(0.5).move_to(watch[0][1]),
                    run_time=0.2,
                ),
            )
            self.wait(0.5)

        self.wait()

        self.play(
            FadeOut(line_debug),
            FadeOut(watch),
            *[FadeOut(i) for i in [add_code, arr_vgroup, bit_vgroup, value_v]],
        )

        pi_student = SVGMobject("PiCreature/PiCreatures_hesitant.svg").to_corner(DOWN + RIGHT).shift(LEFT)
        pi_teacher = SVGMobject("PiCreature/PiCreatures_plain_teacher.svg").to_corner(DOWN + LEFT).shift(RIGHT)
        self.play(FadeIn(pi_student), FadeIn(pi_teacher))

        student_bubble_ask = text_bubble_ask("Fenwick Tree works with \n min/max query?").next_to(pi_student, UP + LEFT)

        teacher_bubble_speech = text_bubble_speech("No!").next_to(pi_teacher, UP + RIGHT)

        self.play(
            Write(student_bubble_ask),
            Transform(
                pi_student,
                SVGMobject("PiCreature/PiCreatures_pondering.svg").move_to(pi_student),
            ),
        )
        self.wait()

        self.play(Write(teacher_bubble_speech))
        self.wait()

        self.play(
            FadeOut(student_bubble_ask),
            FadeOut(teacher_bubble_speech),
            FadeOut(pi_student),
            FadeOut(pi_teacher),
        )
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


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)


def text_bubble_ask(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg").flip(UP)
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.3)
    return VGroup(bubble_speech, text)
