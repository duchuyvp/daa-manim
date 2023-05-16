from manim import *

SCALE = 0.7


class Main(Scene):
    def construct(self):
        text = Text("Range queries").scale(1.5)

        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

        arr = [1, 3, 8, 4, 6, 1, 3, 4]
        arr_v = VGroup(
            *[
                VGroup(
                    Square(side_length=1, color=BLUE),
                    Text(str(arr[i])),
                )
                for i in range(len(arr))
            ]
        ).arrange(RIGHT, buff=0)

        index_v = VGroup(
            *[
                Text(str(i)).scale(0.5).next_to(arr_v[i][1], DOWN)
                for i in range(len(arr))
            ]
        )

        arr_vgroup = (
            VGroup(arr_v, index_v).arrange(DOWN, buff=0.5).scale(SCALE).to_edge(UP)
        )
        arr_vgroup.to_edge(UP)
        self.play(Write(arr_vgroup))
        self.wait()

        l = 3
        r = 6

        query = VGroup(
            MathTex("\\texttt{sum}_q(l,r) =", "\\sum_{i=l}^{r} a_i").move_to(
                ORIGIN + 1.5 * UP
            ),
            MathTex("\\texttt{min}_q(l,r) =", "\\min_{i=l}^{r} a_i").move_to(ORIGIN),
            MathTex("\\texttt{max}_q(l,r) =", "\\max_{i=l}^{r} a_i").move_to(
                ORIGIN + 1.5 * DOWN
            ),
        )
        result = VGroup(
            MathTex("= " + str(sum(arr[l : r + 1])))
            .set_color(GREEN)
            .next_to(query[0], RIGHT),
            MathTex("= " + str(min(arr[l : r + 1])))
            .set_color(GREEN)
            .next_to(query[1], RIGHT),
            MathTex("= " + str(max(arr[l : r + 1])))
            .set_color(GREEN)
            .next_to(query[2], RIGHT),
        )
        queries = (
            VGroup(
                VGroup(query[0], result[0]),
                VGroup(query[1], result[1]),
                VGroup(query[2], result[2]),
            )
            .to_edge(LEFT)
            .shift(DOWN)
        ).scale(SCALE)

        self.play(Write(query[0]), Write(query[1]), Write(query[2]))
        self.wait()

        range_arr = (
            MathTex("l = " + str(l) + ", " + "r = " + str(r))
            .set_color(GREEN)
            .next_to(queries, UP)
            .align_to(queries, LEFT)
            .scale(SCALE)
        )

        self.play(
            Write(range_arr),
            *[
                arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4)
                for i in range(l, r + 1)
            ],
        )
        self.wait()

        self.play(Write(result[0]), Write(result[1]), Write(result[2]))
        self.wait()
        code_str = """

    s = 0
    for i in range(l, r+1):
        s += a[i]
    print(s)

"""
        for_code = (
            Code(
                code=code_str,
                tab_width=4,
                background="window",
                language="C++",
                font="FiraCode Nerd Font",
                line_spacing=0.35,
                insert_line_no=False,
            )
            .scale(SCALE)
            .to_edge(RIGHT, buff=1)
            .shift(UP * 0.5)
        )

        self.play(
            FadeOut(queries[1]),
            FadeOut(queries[2]),
        )
        self.wait()

        self.play(Write(for_code))

        self.play(
            FadeOut(queries[0]),
            FadeOut(range_arr),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0) for i in range(l, r + 1)],
        )
        self.wait()

        ranges = (
            VGroup(
                MathTex("l_1 = " + str(l) + ", " + "r_1 = " + str(r)),
                MathTex("l_2 = " + str(l) + ", " + "r_2 = " + str(r)),
                MathTex("l_3 = " + str(l) + ", " + "r_3 = " + str(r)),
                MathTex("\\vdots"),
                MathTex("l_q = " + str(l) + ", " + "r_q = " + str(r)),
            )
            .set_color(GREEN)
            .arrange(DOWN, buff=1)
            .to_edge(LEFT)
            .scale(SCALE)
        )

        for i in range(len(ranges)):
            self.play(Write(ranges[i]))
        self.wait()

        code_str = """
for q in range(1, Q+1):
    s = 0
    for i in range(l_q, r_q+1):
        s += a[i]
    print(s)

"""
        self.play(
            Transform(
                for_code,
                Code(
                    code=code_str,
                    tab_width=4,
                    background="window",
                    language="C++",
                    font="FiraCode Nerd Font",
                    line_spacing=0.35,
                    insert_line_no=False,
                )
                .scale(SCALE)
                .to_edge(RIGHT, buff=1)
                .shift(UP * 0.5),
            )
        )

        pi_teacher = (
            SVGMobject("PiCreature/PiCreatures_teacher.svg")
            .scale(0.75)
            .to_edge(DOWN)
            .shift(LEFT * 3)
        )
        bubble_speech = (
            text_bubble_speech("O(nq) time?")
            .scale(0.75)
            .next_to(pi_teacher, UP + RIGHT, buff=0)
        )

        self.play(FadeIn(pi_teacher))
        self.play(Write(bubble_speech))
        self.wait()

        self.play(
            FadeOut(ranges),
            FadeOut(for_code),
            FadeOut(arr_vgroup),
            FadeOut(pi_teacher),
            FadeOut(bubble_speech),
        )
        self.wait()

        text = Text("Static array queries").scale(1.5)

        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

        self.play(FadeIn(arr_vgroup))
        self.wait()

        prefix_arr = arr.copy()
        for i in range(1, len(prefix_arr)):
            prefix_arr[i] += prefix_arr[i - 1]

        prefix_arr_v = (
            VGroup(
                *[
                    VGroup(
                        Square(side_length=1, color=BLUE),
                        Text(str(prefix_arr[i])),
                    )
                    for i in range(len(prefix_arr))
                ]
            )
            .scale(SCALE)
            .arrange(RIGHT, buff=0)
            .next_to(arr_vgroup, DOWN)
        )

        self.play(Write(VGroup(*[prefix_arr_v[i][0] for i in range(len(prefix_arr))])))
        self.wait()

        self.play(ReplacementTransform(arr_v[0][1].copy(), prefix_arr_v[0][1]))
        for i in range(1, len(prefix_arr)):
            self.play(
                ReplacementTransform(
                    VGroup(prefix_arr_v[i - 1][1], arr_v[i][1]).copy(),
                    prefix_arr_v[i][1],
                )
            )
        self.wait()

        formula = MathTex(
            "\\texttt{sum}_q(",  # 0
            "l",  # 1
            ",",  # 2
            "r",  # 3
            ") = ",
            "\\texttt{sum}_q(0,",  # 4
            "r",  # 5
            ") ",
            "- ",
            "\\texttt{sum}_q(0,",
            "l-1",  # 6
            ")",  # 7
        )
        formula_ = MathTex(
            "\\texttt{sum}_q(",  # 0
            str(l),  # 1
            ",",  # 2
            str(r),  # 3
            ") = ",  # 4
            "\\texttt{sum}_q(0,",  # 5
            str(r),  # 6
            ") ",
            "- ",  # 7
            "\\texttt{sum}_q(0,",  # 8
            str(l - 1),  # 9
            ")",  # 10
        )
        formula__ = MathTex(
            "\\texttt{sum}_q(",  # 0
            str(l),  # 1
            ",",  # 2
            str(r),  # 3
            ") = ",  # 4
            str(prefix_arr[r]),
            "- ",  # 7
            str(prefix_arr[l - 1]),  # 10
        )

        self.play(Write(formula))
        self.wait()

        self.play(
            # ReplacementTransform(formula, formula_),
            *[Transform(formula[i], formula_[i]) for i in range(len(formula))],
            *[
                arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4)
                for i in range(l, r + 1)
            ],
        )
        self.wait()

        self.play(
            prefix_arr_v[l - 1][0].animate.set_fill(YELLOW, opacity=0.4),
            prefix_arr_v[r][0].animate.set_fill(YELLOW, opacity=0.4),
        )
        self.wait()

        self.play(
            *[
                Transform(formula[i], formula__[j])
                for i, j in zip([0, 1, 2, 3, 4, 8], [0, 1, 2, 3, 4, 6])
            ],
            *[
                Transform(VGroup(*[formula[i] for i in l]), formula__[j])
                for l, j in zip([[5, 6, 7], [9, 10, 11]], [5, 7])
            ],
        )
        self.wait()

        self.play(FadeOut(formula))

        pi_teacher = SVGMobject("PiCreature/PiCreatures_happy_teacher.svg").to_corner(
            DOWN + LEFT
        )

        teacher_speech_bubble = (
            text_bubble_speech("Query in O(1) time")
            .scale(SCALE)
            .next_to(pi_teacher, UP + RIGHT, buff=0)
        )

        self.play(FadeIn(pi_teacher))
        self.play(Write(teacher_speech_bubble))
        self.wait()

        self.play(
            FadeOut(teacher_speech_bubble),
            FadeOut(arr_vgroup),
            FadeOut(prefix_arr_v),
            FadeOut(index_v),
        )

        pi_teacher_speak = SVGMobject(
            "PiCreature/PiCreatures_speaking_teacher.svg"
        ).to_corner(DOWN + LEFT)
        teacher_speak_bubble = (
            text_bubble_speech("Work in \n 2-D array")
            .scale(SCALE)
            .next_to(pi_teacher_speak, UP + RIGHT, buff=0)
        )

        x_range = [0, 10, 1]
        y_range = [0, 7, 1]

        grid_2d_arr = (
            VGroup(
                *[
                    VGroup(
                        *[
                            Rectangle(
                                width=x_range[2],
                                height=y_range[2],
                                color=BLUE,
                                stroke_width=2,
                            )
                            for i in range(x_range[0], x_range[1], x_range[2])
                        ]
                    ).arrange(RIGHT, buff=0)
                    for j in range(y_range[0], y_range[1], y_range[2])
                ]
            )
            .arrange(DOWN, buff=0)
            .scale(SCALE)
            .to_corner(UP + RIGHT)
        )

        label_2d_arr = VGroup(
            Text("A").move_to(grid_2d_arr[4][6]),
            Text("B").move_to(grid_2d_arr[4][2]),
            Text("C").move_to(grid_2d_arr[1][6]),
            Text("D").move_to(grid_2d_arr[1][2]),
        )

        rec_label = VGroup(
            SurroundingRectangle(
                VGroup(grid_2d_arr[2][3], grid_2d_arr[4][6]),
                fill_opacity=0.4,
                stroke_width=0,
                buff=0,
            ),
            SurroundingRectangle(
                VGroup(grid_2d_arr[2][0], grid_2d_arr[4][2]),
                fill_opacity=0.4,
                stroke_width=0,
                buff=0,
            ),
            SurroundingRectangle(
                VGroup(grid_2d_arr[0][3], grid_2d_arr[1][6]),
                fill_opacity=0.4,
                stroke_width=0,
                buff=0,
            ),
            SurroundingRectangle(
                VGroup(grid_2d_arr[0][0], grid_2d_arr[1][2]),
                fill_opacity=0.4,
                stroke_width=0,
                buff=0,
            ),
        )

        query_rect = SurroundingRectangle(
            VGroup(grid_2d_arr[2][3], grid_2d_arr[4][6]), buff=0, color=RED
        )

        # _2d_arr = VGroup(grid_2d_arr, label_2d_arr).scale(SCALE).to_corner(UP + RIGHT)

        self.play(
            Transform(pi_teacher, pi_teacher_speak),
            Write(teacher_speak_bubble),
            Write(grid_2d_arr),
        )
        self.wait()

        self.play(Write(label_2d_arr[0]), FadeOut(teacher_speak_bubble))
        self.wait()

        self.play(FadeIn(rec_label))
        self.wait()

        self.play(Create(query_rect), Write(label_2d_arr), FadeOut(rec_label))

        formula_2d = MathTex("  S(A)", " -S(B)", " +S(D)", " -S(C)").next_to(
            grid_2d_arr, DOWN, buff=1
        )
        self.play(Write(formula_2d))
        self.wait()

        self.play(Indicate(formula_2d[0]), FadeIn(rec_label))
        self.play(Indicate(formula_2d[1]), FadeOut(rec_label[1]), FadeOut(rec_label[3]))
        self.play(Indicate(formula_2d[2]), FadeIn(rec_label[3]))
        self.play(Indicate(formula_2d[3]), FadeOut(rec_label[3]), FadeOut(rec_label[2]))
        self.wait()

        self.play(
            FadeOut(pi_teacher_speak),
            FadeOut(grid_2d_arr),
            FadeOut(label_2d_arr),
            FadeOut(query_rect),
            FadeOut(rec_label),
            FadeOut(formula_2d),
            FadeOut(pi_teacher),
        )

        pi_student = (
            VGroup(
                SVGMobject("PiCreature/PiCreatures_plain.svg"),
                SVGMobject("PiCreature/PiCreatures_plain.svg"),
                SVGMobject("PiCreature/PiCreatures_plain.svg"),
            )
            .arrange(RIGHT)
            .to_corner(DOWN + LEFT)
        )

        pi_student_confuse = (
            VGroup(
                SVGMobject("PiCreature/PiCreatures_confused.svg"),
                SVGMobject("PiCreature/PiCreatures_confused.svg"),
                SVGMobject("PiCreature/PiCreatures_confused.svg"),
            )
            .arrange(RIGHT)
            .to_corner(DOWN + LEFT)
        )

        student_ask_bubble = text_bubble_speech(
            ' "prefix sum" \n for min query?'
        ).next_to(pi_student_confuse, UP + RIGHT, buff=0)

        self.play(Transform(pi_student, pi_student_confuse), Write(student_ask_bubble))
        self.wait()

        self.play(FadeOut(student_ask_bubble), FadeOut(pi_student))
        self.wait()

        self.play(FadeIn(arr_vgroup))

        # self.add(NumberPlane(x_range=(-8, 8, 1), y_range=(-5, 5, 1), fill_opacity=0.1).scale(SCALE))


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = (
        Paragraph(text, alignment="center")
        .move_to(bubble_speech)
        .shift(UP * 0.25)
        .scale(0.35)
    )
    return VGroup(bubble_speech, text)


def text_bubble_ask(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg").flip(UP)
    text = (
        Paragraph(text, alignment="center")
        .move_to(bubble_speech)
        .shift(UP * 0.25)
        .scale(0.35)
    )
    return VGroup(bubble_speech, text)
