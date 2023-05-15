from manim import *

SCALE = 0.7


class Main(Scene):
    def construct(self):
        text = Text("Range queries").scale(1.5)

        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))
        self.wait(1)

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
            VGroup(arr_v, index_v).arrange(DOWN, buff=0.5).to_edge(UP).scale(SCALE)
        )
        arr_vgroup.to_edge(UP)
        self.play(Write(arr_vgroup))
        self.wait(1)

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
        self.wait(1)

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
        self.wait(1)

        self.play(Write(result[0]), Write(result[1]), Write(result[2]))
        self.wait(1)
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
            .to_edge(RIGHT, buff=1)
            .shift(UP * 0.5)
            .scale(SCALE)
        )

        self.play(
            FadeOut(queries[1]),
            FadeOut(queries[2]),
        )
        self.wait(1)

        self.play(Write(for_code))

        self.play(
            FadeOut(queries[0]),
            FadeOut(range_arr),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0) for i in range(l, r + 1)],
        )
        self.wait(1)

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
        self.wait(1)

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
                .to_edge(RIGHT, buff=1)
                .shift(UP * 0.5)
                .scale(SCALE),
            )
        )

        pi_teacher = (
            SVGMobject("PiCreature/PiCreatures_teacher.svg")
            .scale(0.75)
            .to_edge(DOWN)
            .shift(LEFT * 2)
        )
        bubble_speech = (
            SVGMobject("PiCreature/Bubbles_speech.svg")
            .scale(0.75)
            .next_to(pi_teacher, UP + RIGHT, buff=0)
        )
        text = text_chat_speech("O(nq) time?", bubble_speech).scale(0.35)
        pi_teacher_chat = VGroup(bubble_speech, text)

        self.play(FadeIn(pi_teacher))
        self.play(Write(pi_teacher_chat))
        self.wait(1)

        self.play(
            FadeOut(ranges),
            FadeOut(for_code),
            FadeOut(arr_vgroup),
            FadeOut(pi_teacher),
            FadeOut(pi_teacher_chat),
        )
        self.wait(1)

        text = Text("Static array queries").scale(1.5)

        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))
        self.wait(1)

        self.play(FadeIn(arr_vgroup))
        self.wait(1)

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
            .arrange(RIGHT, buff=0)
            .next_to(arr_vgroup, DOWN)
            .scale(SCALE)
        )

        self.play(Write(VGroup(*[prefix_arr_v[i][0] for i in range(len(prefix_arr))])))
        self.wait(1)

        self.play(Transform(arr_v[0][1].copy(), prefix_arr_v[0][1]))
        for i in range(1, len(prefix_arr)):
            self.play(
                Transform(
                    VGroup(prefix_arr_v[i - 1][1], arr_v[i][1]).copy(),
                    prefix_arr_v[i][1],
                )
            )
        self.wait(1)

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
        # self.play(Write(formula_))
        # self.play(Write(formula__))
        self.wait(1)

        # indices = index_labels(formula)
        # self.add(indices)
        # indices = index_labels(formula_)
        # self.add(indices)
        # indices = index_labels(formula__)
        # self.add(indices)

        self.play(
            # ReplacementTransform(formula, formula_),
            *[
                Transform(formula[i], formula_[i])
                for i in range(len(formula))
            ],
            *[
                arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4)
                for i in range(l, r + 1)
            ],
        )
        self.wait(1)

        self.play(
            prefix_arr_v[l - 1][0].animate.set_fill(YELLOW, opacity=0.4),
            prefix_arr_v[r][0].animate.set_fill(YELLOW, opacity=0.4),
        )
        self.wait(1)

        self.play(
            *[
                Transform(formula[i], formula__[j])
                for i, j in zip([0,1,2,3,4,8], [0,1,2,3,4,6])
            ],
            *[
                Transform(VGroup(*[formula[i] for i in l]), formula__[j])
                for l, j in zip([[5, 6, 7], [9, 10, 11]], [5, 7])
            ],
        )
        self.wait(1)

        self.play(FadeOut(formula))


        pi_student = SVGMobject("PiCreature/PiCreatures_happy.svg").to_corner(DOWN+LEFT)

        bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg").next_to(pi_student, UP + RIGHT, buff=0)
        text = Text("Query in O(1) time").scale(0.35).move_to(bubble_speech).shift(UP * 0.2)
        pi_student_chat = VGroup(bubble_speech, text)

        self.play(FadeIn(pi_student))
        self.play(Write(pi_student_chat))


        pi_student_confuse = SVGMobject("PiCreature/PiCreatures_confused.svg").to_edge(DOWN).shift(RIGHT * 2).move_to(pi_student)
        self.play(Transform(pi_student, pi_student_confuse), FadeOut(text))
        self.wait(1)

        text = text_chat_speech("How about \"prefix sum\" \n for min query?", bubble_speech).scale(0.8)
        self.play(Write(text))
        self.wait(1)

        self.play(
            FadeOut(pi_student_chat),
            FadeOut(pi_student),
            FadeOut(prefix_arr_v),
        )

        # self.add(NumberPlane(x_range=(-8, 8, 1), y_range=(-5, 5, 1), fill_opacity=0.1).scale(SCALE))


def text_chat_speech(text, bubble_speech) -> Text:
    return Text(text).move_to(bubble_speech).shift(UP * 0.25)