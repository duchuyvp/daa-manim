from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars
from manim_slides import Slide
from utils import *


class Main(MovingCameraScene, Slide):
    def construct(self):
        text = Text("Range queries").scale(1.5)

        self.play(Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

        # region array
        arr = [1, 3, 4, 8, 6, 1, 4, 2]
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
            *[Text(str(i), font="FiraCode Nerd Font").scale(0.5).next_to(arr_v[i][1], DOWN) for i in range(len(arr))]
        )
        # endregion array

        # region intro
        arr_vgroup = VGroup(arr_v, index_v).arrange(DOWN, buff=0.5).scale(SCALE).to_edge(UP)
        arr_vgroup.to_edge(UP)
        self.play(Write(arr_vgroup))
        self.wait()
        self.next_slide()

        l = 3
        r = 6

        query = VGroup(
            MathTex("\\texttt{sum}_q(l,r) =", "\\sum_{i=l}^{r} a_i").move_to(ORIGIN + 1.5 * UP),
            MathTex("\\texttt{min}_q(l,r) =", "\\min_{i=l}^{r} a_i").move_to(ORIGIN),
            MathTex("\\texttt{max}_q(l,r) =", "\\max_{i=l}^{r} a_i").move_to(ORIGIN + 1.5 * DOWN),
        )
        result = VGroup(
            MathTex("= " + str(sum(arr[l : r + 1]))).set_color(YELLOW).next_to(query[0], RIGHT),
            MathTex("= " + str(min(arr[l : r + 1]))).set_color(YELLOW).next_to(query[1], RIGHT),
            MathTex("= " + str(max(arr[l : r + 1]))).set_color(YELLOW).next_to(query[2], RIGHT),
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
        self.next_slide()

        range_arr = (
            MathTex("l = " + str(l) + ", " + "r = " + str(r))
            .set_color(YELLOW)
            .next_to(queries, UP)
            .align_to(queries, LEFT)
            .scale(SCALE)
        )

        self.play(
            Write(range_arr),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in range(l, r + 1)],
        )
        self.wait()
        self.next_slide()

        self.play(Write(result[0]), Write(result[1]), Write(result[2]))
        self.wait()
        self.next_slide()
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
        self.next_slide()

        self.play(Write(for_code))

        self.play(
            FadeOut(queries[0]),
            FadeOut(range_arr),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0) for i in range(l, r + 1)],
        )
        self.wait()
        self.next_slide()

        ranges = (
            VGroup(
                MathTex("l_1 = " + str(l) + ", " + "r_1 = " + str(r)),
                MathTex("l_2 = " + str(1) + ", " + "r_2 = " + str(6)),
                MathTex("l_3 = " + str(2) + ", " + "r_3 = " + str(5)),
                MathTex("\\vdots"),
                MathTex("l_q = " + "a" + ", " + "r_q = " + "b"),
            )
            .set_color(YELLOW)
            .arrange(DOWN, buff=1)
            .to_edge(LEFT)
            .scale(SCALE)
        )

        for i in range(len(ranges)):
            self.play(Write(ranges[i]))
        self.wait()
        self.next_slide()

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

        pi_teacher = SVGMobject("PiCreature/PiCreatures_teacher.svg").scale(0.75).to_edge(DOWN).shift(LEFT * 3)
        bubble_speech = text_bubble_speech("O(nq) time?").scale(0.75).next_to(pi_teacher, UP + RIGHT, buff=0)

        self.play(FadeIn(pi_teacher))
        self.play(Write(bubble_speech))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(ranges),
            FadeOut(for_code),
            FadeOut(arr_vgroup),
            FadeOut(pi_teacher),
            FadeOut(bubble_speech),
        )
        self.wait()
        self.next_slide()

        text = Text("Static array queries").scale(1.5)

        self.play(Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

        self.play(FadeIn(arr_vgroup))
        self.wait()
        self.next_slide()

        # endregion

        # region sum query
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
        self.next_slide()

        self.play(ReplacementTransform(arr_v[0][1].copy(), prefix_arr_v[0][1]))
        for i in range(1, len(prefix_arr)):
            self.play(
                ReplacementTransform(
                    VGroup(prefix_arr_v[i - 1][1], arr_v[i][1]).copy(),
                    prefix_arr_v[i][1],
                )
            )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(
            # ReplacementTransform(formula, formula_),
            *[Transform(formula[i], formula_[i]) for i in range(len(formula))],
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in range(l, r + 1)],
        )
        self.wait()
        self.next_slide()

        self.play(
            prefix_arr_v[l - 1][0].animate.set_fill(YELLOW, opacity=0.4),
            prefix_arr_v[r][0].animate.set_fill(YELLOW, opacity=0.4),
        )
        self.wait()
        self.next_slide()

        self.play(
            *[Transform(formula[i], formula__[j]) for i, j in zip([0, 1, 2, 3, 4, 8], [0, 1, 2, 3, 4, 6])],
            *[
                Transform(VGroup(*[formula[i] for i in l]), formula__[j])
                for l, j in zip([[5, 6, 7], [9, 10, 11]], [5, 7])
            ],
        )
        self.wait()
        self.next_slide()

        self.play(FadeOut(formula))

        pi_teacher = SVGMobject("PiCreature/PiCreatures_happy_teacher.svg").to_corner(DOWN + LEFT)

        teacher_speech_bubble = (
            text_bubble_speech("Query in O(1) time").scale(SCALE).next_to(pi_teacher, UP + RIGHT, buff=0)
        )

        self.play(FadeIn(pi_teacher))
        self.play(Write(teacher_speech_bubble))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(teacher_speech_bubble),
            FadeOut(arr_vgroup),
            FadeOut(prefix_arr_v),
            prefix_arr_v[l - 1][0].animate.set_fill(YELLOW, opacity=0),
            prefix_arr_v[r][0].animate.set_fill(YELLOW, opacity=0),
            FadeOut(index_v),
        )

        pi_teacher_speak = SVGMobject("PiCreature/PiCreatures_speaking_teacher.svg").to_corner(DOWN + LEFT)
        teacher_speak_bubble = (
            text_bubble_speech("Work in \n 2-D array").scale(SCALE).next_to(pi_teacher_speak, UP + RIGHT, buff=0)
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

        query_rect = SurroundingRectangle(VGroup(grid_2d_arr[2][3], grid_2d_arr[4][6]), buff=0, color=RED)

        # _2d_arr = VGroup(grid_2d_arr, label_2d_arr).scale(SCALE).to_corner(UP + RIGHT)

        self.play(
            Transform(pi_teacher, pi_teacher_speak),
            Write(teacher_speak_bubble),
            Write(grid_2d_arr),
        )
        self.wait()
        self.next_slide()

        self.play(Write(label_2d_arr[0]), FadeOut(teacher_speak_bubble))
        self.wait()
        self.next_slide()

        self.play(FadeIn(rec_label))
        self.wait()
        self.next_slide()

        self.play(Create(query_rect), Write(label_2d_arr), FadeOut(rec_label))

        formula_2d = MathTex("  S(A)", " -S(B)", " +S(D)", " -S(C)").next_to(grid_2d_arr, DOWN, buff=1)
        self.play(Write(formula_2d))
        self.wait()
        self.next_slide()

        self.play(Indicate(formula_2d[0]), FadeIn(rec_label))
        self.play(Indicate(formula_2d[1]), FadeOut(rec_label[1]), FadeOut(rec_label[3]))
        self.play(Indicate(formula_2d[2]), FadeIn(rec_label[3]))
        self.play(Indicate(formula_2d[3]), FadeOut(rec_label[3]), FadeOut(rec_label[2]))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(pi_teacher_speak),
            FadeOut(grid_2d_arr),
            FadeOut(label_2d_arr),
            FadeOut(query_rect),
            FadeOut(rec_label[0]),
            FadeOut(formula_2d),
            FadeOut(pi_teacher),
        )

        # endregion sum query

        # region min query
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

        student_ask_bubble = text_bubble_speech(' "prefix sum" \n for min query?').next_to(
            pi_student_confuse, UP + RIGHT, buff=0
        )

        self.play(Transform(pi_student, pi_student_confuse), Write(student_ask_bubble))
        self.wait()
        self.next_slide()

        self.play(FadeOut(student_ask_bubble), FadeOut(pi_student))
        self.wait()
        self.next_slide()

        for i in range(l, r + 1):
            arr_v[i][0].set_fill(YELLOW, opacity=0)
        prefix_arr_v[l - 1][0].animate.set_fill(YELLOW, opacity=0)
        prefix_arr_v[r][0].animate.set_fill(YELLOW, opacity=0)

        self.play(FadeIn(arr_vgroup))

        d = {}
        for i in range(len(arr)):
            d[(i, i)] = arr[i]
        w = 2
        while w <= len(arr):
            for i in range(len(arr) - w + 1):
                d[(i, i + w - 1)] = min(d[(i, i + w / 2 - 1)], d[(i + w / 2, i + w - 1)])
            w *= 2

        sparse_table = VGroup()
        w = 1
        while w < len(arr):
            temp = MathTable(
                [
                    ["l", "r", "\\texttt{min}_q(l,r)"],
                    *[[str(i), str(i + w - 1), str(d[(i, i + w - 1)])] for i in range(len(arr) - w + 1)],
                ],
                line_config={"stroke_width": 1, "color": YELLOW},
            )
            temp.remove(*temp.get_vertical_lines())
            sparse_table.add(temp.copy())
            w *= 2

        sparse_table.arrange(RIGHT, buff=1).scale(0.5).move_to(ORIGIN)
        for table in sparse_table:
            table.align_to(arr_vgroup, UP).shift(DOWN * (0.3 + arr_vgroup.get_height()))

        self.play(FadeIn(sparse_table))
        self.wait()
        self.next_slide()

        self.play(Circumscribe(sparse_table[2].get_rows()[2], color=RED, buff=0.2))
        self.wait()
        self.next_slide()

        self.play(
            Circumscribe(sparse_table[1].get_rows()[2], color=RED, buff=0.2),
            Circumscribe(sparse_table[1].get_rows()[4], color=RED, buff=0.2),
        )
        self.wait()
        self.next_slide()

        l_m = 1
        r_m = 6
        k = r_m - l_m + 1
        while k & (k - 1) != 0:
            k -= k & ~(k - 1)

        formular_min = (
            MathTex(
                "\\texttt{min}_q(",
                "l",
                ",",
                "r",
                ") = ",
                "\\min(",
                "\\texttt{min}_q(",
                "l",
                ",",
                "l+k-1",
                ")",
                ", ",
                "\\texttt{min}_q(",
                "r-k+1",
                ",",
                "r",
                ")",
                ")",
            )
            .scale(SCALE)
            .to_edge(DOWN, buff=0.5)
        )

        formular_min_ = (
            MathTex(
                "\\texttt{min}_q(",
                str(l_m),
                ",",
                str(r_m),
                ") = ",
                "\\min(",
                "\\texttt{min}_q(",
                str(l_m),
                ",",
                str(l_m + k - 1),
                ")",
                ", ",
                "\\texttt{min}_q(",
                str(r_m - k + 1),
                ",",
                str(r),
                ")",
                ")",
            )
            .scale(SCALE)
            .to_edge(DOWN, buff=0.5)
        )
        formular_min__ = (
            MathTex(
                "\\texttt{min}_q(",
                str(l_m),
                ",",
                str(r_m),
                ") = ",
                "\\min(",
                str(d[(l_m, l_m + k - 1)]),
                ", ",
                str(d[(r_m - k + 1, r_m)]),
                ")",
            )
            .scale(SCALE)
            .to_edge(DOWN, buff=0.5)
        )

        self.play(Write(formular_min))
        self.wait()
        self.next_slide()

        formular_min_l_rect = SurroundingRectangle(sparse_table[2].get_rows()[2], color=RED, buff=0.2)
        formular_min_r_rect = SurroundingRectangle(sparse_table[2].get_rows()[4], color=RED, buff=0.2)

        self.play(
            *[Transform(formular_min[i], formular_min_[i]) for i in range(len(formular_min))],
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in range(l_m, r_m + 1)],
            Create(formular_min_l_rect),
            Create(formular_min_r_rect),
        )
        self.wait()
        self.next_slide()

        self.play(
            *[
                Transform(formular_min[i], formular_min__[j])
                for i, j in zip([0, 1, 2, 3, 4, 5, 11, 17], [0, 1, 2, 3, 4, 5, 7, 9])
            ],
            *[
                Transform(VGroup(*[formular_min[i] for i in l]), formular_min__[j])
                for l, j in zip([[6, 7, 8, 9, 10], [12, 13, 14, 15, 16]], [6, 8])
            ],
        )
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(formular_min_l_rect),
            FadeOut(formular_min_r_rect),
            *[arr_v[i][0].animate.set_fill(YELLOW, opacity=0) for i in range(l_m, r_m + 1)],
            FadeOut(formular_min),
            FadeOut(sparse_table),
        )
        self.wait()
        self.next_slide()
        # endregion

        # region Binary indexed tree

        pi_teacher = SVGMobject("PiCreature/PiCreatures_plain_teacher.svg").to_corner(DOWN + LEFT)
        pi_bubble_ask = text_bubble_speech("What if we update \n an element?").next_to(pi_teacher, UP + RIGHT, buff=0)

        self.play(FadeIn(pi_teacher), Write(pi_bubble_ask))
        self.play(FadeIn(prefix_arr_v))

        u = 3

        self.wait()
        self.next_slide()

        self.play(arr_v[u][0].animate.set_fill(YELLOW, opacity=0.4))
        self.play(*[prefix_arr_v[i][0].animate.set_fill(RED, opacity=0.4) for i in range(u, len(prefix_arr_v))])
        self.wait()
        self.next_slide()

        self.play(
            arr_v[u][0].animate.set_fill(YELLOW, opacity=0),
            *[prefix_arr_v[i][0].animate.set_fill(RED, opacity=0) for i in range(u, len(prefix_arr_v))],
            FadeOut(pi_teacher),
            FadeOut(pi_bubble_ask),
            FadeOut(prefix_arr_v),
            FadeOut(arr_vgroup),
        )
        # endregion

        # self.add(NumberPlane(x_range=(-8, 8, 1), y_range=(-5, 5, 1), fill_opacity=0.1).scale(SCALE))

        text = Text("Binary Indexed Tree").scale(1.5)
        self.play(Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        origin = ORIGIN + DOWN * 2 + RIGHT * 2
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=12).move_to(origin))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        text_pk = MathTex("\ p(k) = 2").next_to(ex_pk[-1], RIGHT, buff=0.5)
        self.play(*[FadeIn(ex_pk[i], target_position=ex_pk[0]) for i in range(1, len(ex_pk))])
        self.wait()
        self.next_slide()

        self.play(Write(text_pk))
        self.wait()
        self.next_slide()

        self.play(FadeOut(ex_pk_v), FadeOut(text_k), FadeOut(text_pk))
        self.wait()
        self.next_slide()

        self.play(Restore(self.camera.frame))
        formula_tree = MathTex("tree[k] = ", "\\texttt{sum}_q(", "k-p(k)+1", ",", "k", ")")
        self.play(Write(formula_tree))
        self.wait()
        self.next_slide()

        self.play(FadeOut(formula_tree))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(*[ReplacementTransform(value_v[i].copy(), bit_v[i][1]) for i in range(len(value_v))])
        self.wait()
        self.next_slide()

        self.play(
            arr_vgroup.animate.shift(LEFT * 2),
            value_v.animate.shift(LEFT * 2),
            bit_vgroup.animate.shift(LEFT),
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(*[Transform(formula_sum[i], formula_sum_[i]) for i in range(len(formula_sum))])
        self.wait()
        self.next_slide()

        self.play(*[Transform(formula_sum[i], formula_sum__[i]) for i in range(len(formula_sum))])
        self.wait()
        self.next_slide()

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
        self.next_slide()

        line_debug = highlight_line_code(sum_code, 7)

        self.play(Create(line_debug))
        self.play(Write(watch[2], run_time=0.2))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(
            FadeOut(line_debug),
            FadeOut(watch),
            FadeOut(sum_code),
        )
        self.wait()
        self.next_slide()

        u = 3

        self.play(arr_v[u - 1][0].animate.set_fill(YELLOW, opacity=0.4))
        self.wait()
        self.next_slide()

        self.play(
            *[bit_v[i][0].animate.set_fill(YELLOW, opacity=0.4) for i in [2, 3, 7]],
            *[value_v[i].animate.set_fill(YELLOW, opacity=0.4) for i in [2, 3, 7]],
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        line_debug = highlight_line_code(add_code, 7)

        self.play(Create(line_debug))
        self.play(Write(watch[2], run_time=0.2))
        self.wait()
        self.next_slide()

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
        self.next_slide()

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
        self.next_slide()

        self.play(Write(teacher_bubble_speech))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(student_bubble_ask),
            FadeOut(teacher_bubble_speech),
            FadeOut(pi_student),
            FadeOut(pi_teacher),
        )
        self.wait()
        self.next_slide()

        text = Text("Segment Tree").scale(1.5)
        self.play(Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        for i in range(1, nl):
            self.play(Write(line[i - 1]), Write(layer[i])),
            self.wait(0.5)

        self.wait()
        self.next_slide()

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
        self.next_slide()

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
        self.next_slide()

        self.play(Restore(self.camera.frame), FadeOut(array), tree.animate.to_edge(LEFT))
        self.wait()
        self.next_slide()

        # region: query
        self.play(*[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(2, 8)])
        self.wait()
        self.next_slide()

        self.play(
            *[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 8)],
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(1, 4)],
        )
        self.play(
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 4)],
            *[layer[2][i][0].animate.set_fill(color=YELLOW, opacity=0.3) for i in range(1, 2)],
        )
        self.wait()
        self.next_slide()

        self.play(
            *[layer[2][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [1]],
            *[layer[1][i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [1]],
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        line_debug = highlight_line_code(sum_code, 15)

        self.play(Create(line_debug))
        self.play(Write(watch[3], run_time=0.2))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        # endregion

        # region: update
        u = 4
        self.play(layer[0][u][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.wait()
        self.next_slide()

        self.play(layer[1][2][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.play(layer[2][1][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.play(layer[3][0][0].animate.set_fill(color=YELLOW, opacity=0.3))
        self.wait()
        self.next_slide()

        pi_teacher = SVGMobject("PiCreature/PiCreatures_connving_teacher.svg").to_corner(DOWN + RIGHT)
        pi_speak = text_bubble_ask("Implement \n your self!").next_to(pi_teacher, UP + LEFT, buff=0)

        self.play(FadeIn(pi_teacher), Write(pi_speak))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(FadeOut(pi_teacher), FadeOut(pi_student), FadeOut(pi_speak), FadeOut(student_speak))
        self.wait()
        self.next_slide()

        text = Text("Range Update").scale(1.5)
        text_small = Text("Point query").next_to(text, DOWN)
        self.play(Write(text))
        self.play(Write(text_small), VGroup(text, text_small).animate.move_to(ORIGIN))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text), FadeOut(text_small))
        self.wait()
        self.next_slide()

        arr = [3, 3, 1, 1, 1, 5, 2, 2]
        d_arr = [3, 0, -2, 0, 0, 4, -3, 0]
        arr_v = (
            VGroup(
                *[
                    VGroup(
                        Square(side_length=1, color=BLUE),
                        Text(str(arr[i])),
                    )
                    for i in range(len(arr))
                ]
            )
            .arrange(RIGHT, buff=0)
            .scale(SCALE)
            .to_edge(UP)
        )

        d_arr_v = (
            VGroup(
                *[
                    VGroup(
                        Square(side_length=1, color=BLUE),
                        Text(str(d_arr[i])),
                    )
                    for i in range(len(d_arr))
                ]
            )
            .arrange(RIGHT, buff=0)
            .scale(SCALE)
            .next_to(arr_v, DOWN, buff=SCALE)
        )
        text_d_arr = Text("D-Array").scale(0.5).next_to(d_arr_v, LEFT)

        self.play(Create(arr_v))
        self.wait()
        self.next_slide()

        self.play(Create(d_arr_v), Write(text_d_arr))
        self.wait()
        self.next_slide()

        self.play(arr_v[6][0].animate.set_fill(color=YELLOW, opacity=0.4))
        self.wait()
        self.next_slide()

        self.play(*[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(7)])
        self.wait()
        self.next_slide()

        self.play(
            arr_v[6][0].animate.set_fill(color=YELLOW, opacity=0),
            *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(7)],
        )
        self.wait()
        self.next_slide()

        add_text_1 = MathTex("+ x").scale(0.7).next_to(arr_v, RIGHT, buff=SCALE)
        add_text_2 = MathTex("+ x").scale(0.7).next_to(d_arr_v, RIGHT, buff=SCALE)

        self.play(Create(add_text_1), *[arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(2, 6)])
        self.wait()
        self.next_slide()

        self.play(Create(add_text_2), *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in [2, 6]])
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(add_text_1),
            FadeOut(add_text_2),
            *[arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 6)],
            *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [2, 6]],
        )
        self.wait()
        self.next_slide()

        pi_teacher = SVGMobject("PiCreature/PiCreatures_raise_right_hand_teacher.svg").to_edge(DOWN + LEFT)
        pi_bubble_speech = text_bubble_speech("Time Complexity?").next_to(pi_teacher, UP + RIGHT)

        mid_text = (
            VGroup(
                Text(" ~ ").scale(0.5),
                Text(" ~ ").scale(0.5),
                Text(" ~ ").scale(0.5),
            )
            .arrange(DOWN, buff=0.5)
            .move_to(ORIGIN)
            .shift(LEFT)
        )
        left_text = VGroup(
            Text("Construct D-Array").scale(0.5).next_to(mid_text[0], LEFT),
            Text("Update a range").scale(0.5).next_to(mid_text[1], LEFT),
            Text("Query an element").scale(0.5).next_to(mid_text[2], LEFT),
        )
        right_text = VGroup(
            Text(" ").scale(0.5).next_to(mid_text[0], RIGHT),
            Text("Update 2 elements in D-Array ~ ").scale(0.5).next_to(mid_text[1], RIGHT),
            Text("Query a range D-Array ~ ").scale(0.5).next_to(mid_text[2], RIGHT),
        )
        rright_text = VGroup(
            MathTex("O(n)").scale(0.5).next_to(mid_text[0], RIGHT),
            MathTex("O(\\log(n))").scale(0.5).next_to(right_text[1], RIGHT),
            MathTex("O(\\log(n))").scale(0.5).next_to(right_text[2], RIGHT),
        )

        self.play(FadeIn(pi_teacher), Write(pi_bubble_speech))
        self.wait()
        self.next_slide()

        self.play(Write(mid_text), Write(left_text), Write(right_text), Write(rright_text), FadeOut(pi_bubble_speech))
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(pi_teacher),
            FadeOut(mid_text),
            FadeOut(left_text),
            FadeOut(right_text),
            FadeOut(rright_text),
            FadeOut(arr_v),
            FadeOut(d_arr_v),
            FadeOut(text_d_arr),
        )
        self.wait()
        self.next_slide()

        text = Text("Range Update").scale(1.5)
        text_small = Text("Range query").next_to(text, DOWN)
        VGroup(text, text_small).move_to(ORIGIN)
        self.play(Write(text_small), Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text), FadeOut(text_small))
        self.wait()
        self.next_slide()

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
        self.next_slide()

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
        self.next_slide()

        # region top down

        query = VGroup(MathTex("\\texttt{q}(3, 7)").scale(SCALE).to_edge(UP + RIGHT, buff=2))

        self.play(
            Write(query),
            *[layer[0][i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(2, 7)],
        )
        self.wait()
        self.next_slide()

        self.add_foreground_mobjects(layer)
        self.add_foreground_mobjects(query)

        self.play(
            Transform(query, label_g("\\texttt{q}(3, 7)").next_to(layer[3][0][0], UP + RIGHT, buff=-0.25)),
            layer[3][0][0].animate.set_color(RED),
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(
            FadeOut(query),
            FadeOut(layer),
            FadeOut(line),
            FadeOut(tmp_sq),
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

        self.play(FadeIn(tree))
        self.wait()
        self.next_slide()

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
        self.next_slide()

        s_explain = Tex("$s$: Sum of range $\\Rightarrow$").scale(0.6).next_to(layer[3][0][0], LEFT, buff=0.2)
        z_explain = Tex("$\\Leftarrow$ $z$: Propagation value").scale(0.6).next_to(layer[3][0][0], RIGHT, buff=0.2)

        self.play(Write(s_explain), Write(z_explain), run_time=0.5)
        self.wait()
        self.next_slide()

        self.play(
            FadeOut(s_explain),
            FadeOut(z_explain),
        )

        # region range update
        add = VGroup(MathTex("\\texttt{a}([2, 8], 2)").scale(SCALE).to_edge(UP + RIGHT, buff=2))
        brace = Brace(VGroup(*[layer[0][i] for i in range(1, 8)]), DOWN, buff=0.1)

        self.play(Write(brace), Write(add))
        self.wait()
        self.next_slide()

        self.add_foreground_mobjects(layer)
        self.add_foreground_mobjects(add)

        self.play(
            Transform(
                add, label_g("\\texttt{a}([2, 8], 2)", scale=0.5).next_to(layer[3][0][0], UP + RIGHT, buff=-0.25)
            ),
            layer[3][0][0].animate.set_color(RED),
        )
        self.wait()
        self.next_slide()

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
        self.next_slide()

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
        self.next_slide()

        self.remove_foreground_mobjects(layer, tmp_sq, add)

        # endregion

        pi_student = SVGMobject("PiCreature/PiCreatures_happy.svg").to_edge(DOWN + LEFT)

        self.play(Transform(pi_student, SVGMobject("PiCreature/PiCreatures_dance_kick.svg").to_edge(DOWN + LEFT)))
        self.wait()
        self.next_slide()

        self.play(FadeOut(pi_student), FadeOut(tree))
        self.wait()
        self.next_slide()

        pi_teacher = SVGMobject("PiCreature/PiCreatures_plain_teacher.svg").to_edge(DOWN + LEFT)
        pi_teacher_speech = text_bubble_speech("Wait...").next_to(pi_teacher, UP + RIGHT, buff=0)
        self.play(FadeIn(pi_teacher), Write(pi_teacher_speech))
        self.wait()
        self.next_slide()

        text = Text("Data structure").scale(1.5)
        self.play(Write(text))
        self.wait()
        self.next_slide()

        self.play(FadeOut(text))
        self.wait()
        self.next_slide()

        struct_code = """
        class Node:
            value: int
            left: Node
            right: Node

            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        """

        code = (
            Code(
                code=struct_code,
                tab_width=4,
                background="window",
                language="Python",
                line_spacing=0.35,
                insert_line_no=False,
                font=FONT,
            )
            .scale(SCALE)
            .to_edge(LEFT)
            .shift(UP * 2)
        )

        pi_teacher = SVGMobject("PiCreature/PiCreatures_plain_teacher.svg").to_corner(DOWN + LEFT)
        pi_bubble_speech = text_bubble_speech("update 10").next_to(pi_teacher, UP + RIGHT).shift(DOWN)

        node1 = return_node("0-15")
        node2 = return_node("8-15").move_to(node1).shift(DOWN * 2 + RIGHT * 4)
        node3 = return_node("8-11").move_to(node2).shift(DOWN * 2 + LEFT * 2)
        node4 = return_node("10-11").move_to(node3).shift(DOWN * 2 + RIGHT * 1)
        node5 = return_node("10-10").move_to(node4).shift(DOWN * 2 + LEFT * 0.5)
        line1 = Line(
            node1.get_critical_point(DOWN + RIGHT) + 0.25 * LEFT,
            node2.get_critical_point(UP + LEFT) + 0.5 * RIGHT,
            color=BLUE,
        )
        line2 = Line(
            node2.get_critical_point(DOWN + LEFT) + 0.25 * RIGHT,
            node3.get_critical_point(UP + RIGHT) + 0.5 * LEFT,
            color=BLUE,
        )
        line3 = Line(
            node3.get_critical_point(DOWN + RIGHT) + 0.25 * LEFT,
            node4.get_critical_point(UP + LEFT) + 0.5 * RIGHT,
            color=BLUE,
        )
        line4 = Line(
            node4.get_critical_point(DOWN + LEFT) + 0.25 * RIGHT,
            node5.get_critical_point(UP + RIGHT) + 0.5 * LEFT,
            color=BLUE,
        )

        tree = (
            VGroup(node1, node2, node3, node4, node5, line1, line2, line3, line4)
            .to_edge(RIGHT + UP)
            .scale(SCALE)
            .shift(UP)
        )

        self.play(Write(node1), Create(pi_teacher), Write(code))
        self.wait()
        self.next_slide()

        self.play(
            Write(pi_bubble_speech),
            Write(line1),
            Write(node2),
            Write(line2),
            Write(node3),
            Write(line3),
            Write(node4),
            Write(line4),
            Write(node5),
        )
        self.wait()
        self.next_slide()

        self.play(FadeOut(tree), FadeOut(pi_bubble_speech))

        struct_code2 = """
        class Node:
            value: int | t.List
            left: Node
            right: Node

            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        """
        struct_code3 = """
        class Node:
            value: int | t.List | t.Dict | Mobject | None
            left: Node
            right: Node

            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        """

        code2 = (
            Code(
                code=struct_code2,
                tab_width=4,
                background="window",
                language="Python",
                line_spacing=0.35,
                insert_line_no=False,
                font=FONT,
            )
            .scale(SCALE)
            .move_to(code)
            .align_to(code, LEFT)
        )
        code3 = (
            Code(
                code=struct_code3,
                tab_width=4,
                background="window",
                language="Python",
                line_spacing=0.35,
                insert_line_no=False,
                font=FONT,
            )
            .scale(SCALE)
            .move_to(code)
            .align_to(code, LEFT)
        )

        self.play(FadeOut(code), FadeIn(code2))
        self.play(FadeOut(code2), FadeIn(code3))
        self.wait()
        self.next_slide()

        self.play(FadeOut(code3), FadeOut(pi_teacher))

        arr = [3, 1, 2, 3, 1, 1, 1, 2]

        layer = VGroup()

        layer.add(VGroup(*[node_map([arr[i]], [1]) for i in range(len(arr))]).arrange(RIGHT, buff=0.4))
        layer.add(
            VGroup(
                node_map([1, 3], [1, 1]).next_to(VGroup(layer[0][0], layer[0][1]), UP, buff=0.5),
                node_map([2, 3], [1, 1]).next_to(VGroup(layer[0][2], layer[0][3]), UP, buff=0.5),
                node_map([1], [2]).next_to(VGroup(layer[0][4], layer[0][5]), UP, buff=0.5),
                node_map([1, 2], [1, 1]).next_to(VGroup(layer[0][6], layer[0][7]), UP, buff=0.5),
            )
        )
        layer.add(
            VGroup(
                node_map([1, 2, 3], [1, 1, 2]).next_to(VGroup(layer[1][0], layer[1][1]), UP, buff=0.5),
                node_map([1, 2], [3, 1]).next_to(VGroup(layer[1][2], layer[1][3]), UP, buff=0.5),
            )
        )
        layer.add(VGroup(node_map([1, 2, 3], [4, 2, 2]).next_to(VGroup(layer[2][0], layer[2][1]), UP, buff=0.5)))

        layer.scale(0.7).to_edge(DOWN)

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
                for i in range(3)
            ]
        )
        arr_v = (
            VGroup(
                *[
                    VGroup(
                        Square(side_length=1, color=BLUE),
                        Text(str(arr[i])),
                    )
                    for i in range(len(arr))
                ]
            )
            .arrange(RIGHT, buff=0)
            .scale(0.7)
            .next_to(layer, UP, buff=0.5)
        )

        self.play(FadeIn(layer), FadeIn(line), FadeIn(arr_v))
        self.wait()
        self.next_slide()

        self.play(FadeOut(layer), FadeOut(line), FadeOut(arr_v))
        self.wait()
        self.next_slide()

        _2d_arr = [[7, 6, 1, 6], [8, 7, 5, 2], [3, 9, 7, 1], [8, 5, 3, 8]]
        _2d_arr_v = (
            VGroup(
                *[
                    VGroup(
                        *[
                            VGroup(
                                Square(side_length=1, color=BLUE),
                                Text(str(_1d_arr[i])),
                            )
                            for i in range(len(_1d_arr))
                        ]
                    ).arrange(RIGHT, buff=0)
                    for _1d_arr in _2d_arr
                ]
            )
            .arrange(DOWN, buff=0)
            .scale(0.7)
            .to_edge(UP)
        )

        self.play(FadeIn(_2d_arr_v))

        st_2d = VGroup(
            VGroup(
                build_segment_tree([[7, 6, 1, 6], [13, 7], [20]]),
                build_segment_tree([[8, 7, 5, 2], [15, 7], [22]]),
                build_segment_tree([[3, 9, 7, 1], [12, 8], [20]]),
                build_segment_tree([[8, 5, 3, 8], [13, 11], [24]]),
            ),
            VGroup(
                build_segment_tree([[15, 13, 6, 8], [28, 14], [42]]),
                build_segment_tree([[11, 14, 10, 9], [25, 19], [44]]),
            ),
            VGroup(
                build_segment_tree([[26, 27, 16, 17], [53, 33], [86]]),
            ),
        )

        st_2d[0].arrange(RIGHT, buff=2)
        st_2d[1][0].next_to(VGroup(st_2d[0][0], st_2d[0][1]), UP, buff=3)
        st_2d[1][1].next_to(VGroup(st_2d[0][2], st_2d[0][3]), UP, buff=3)
        st_2d[2][0].next_to(VGroup(st_2d[1][0], st_2d[1][1]), UP, buff=3)

        line_2d = VGroup(
            VGroup(
                Line(st_2d[0][0].get_critical_point(UP), get_semi_down_corner(st_2d[1][0], LEFT), color=BLUE),
                Line(st_2d[0][1].get_critical_point(UP), get_semi_down_corner(st_2d[1][0], RIGHT), color=BLUE),
                Line(st_2d[0][2].get_critical_point(UP), get_semi_down_corner(st_2d[1][1], LEFT), color=BLUE),
                Line(st_2d[0][3].get_critical_point(UP), get_semi_down_corner(st_2d[1][1], RIGHT), color=BLUE),
            ),
            VGroup(
                Line(st_2d[1][0].get_critical_point(UP), get_semi_down_corner(st_2d[2][0], LEFT), color=BLUE),
                Line(st_2d[1][1].get_critical_point(UP), get_semi_down_corner(st_2d[2][0], RIGHT), color=BLUE),
            ),
        )

        tree_2d = VGroup(st_2d, line_2d).scale(0.7).to_edge(DOWN)

        self.play(*[Transform(_2d_arr_v[i], st_2d[0][i][0][0]) for i in range(len(_2d_arr_v))])
        self.play(Write(tree_2d), self.camera.frame.animate(run_time=2).scale(2.5).move_to(tree_2d))
        self.wait()
        self.next_slide()
