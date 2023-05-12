from manim import *


def create_textbox(color, string):
    result = VGroup()  # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center())  # create text
    result.add(box, text)  # add both objects to the VGroup
    return result


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
            VGroup(arr_v, index_v).arrange(DOWN, buff=0.5).to_edge(UP).scale(0.75)
        )

        self.play(Write(arr_vgroup))
        self.wait(1)

        self.play(arr_vgroup.animate.to_edge(UP))
        self.wait(1)

        l = 3
        r = 6

        query = VGroup(
            MathTex("sum_q(l,r) =", "\\sum_{i=l}^{r} a_i").move_to(ORIGIN + 1.5 * UP),
            MathTex("min_q(l,r) =", "\\min_{i=l}^{r} a_i").move_to(ORIGIN),
            MathTex("max_q(l,r) =", "\\max_{i=l}^{r} a_i").move_to(ORIGIN + 1.5 * DOWN),
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
        ).scale(0.75)

        self.play(Write(query[0]), Write(query[1]), Write(query[2]))
        self.wait(1)

        range_arr = (
            MathTex("l = " + str(l) + ", " + "r = " + str(r))
            .set_color(GREEN)
            .next_to(queries, UP)
            .align_to(queries, LEFT)
            .scale(0.75)
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

        for_code = create_textbox(BLUE, "Code").scale(0.75).to_edge(RIGHT)

        self.play(
            FadeOut(queries[1]),
            FadeOut(queries[2]),
            Create(for_code),
        )
        self.wait(1)

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
            .scale(0.75)
        )

        self.play(Write(ranges[0]))
        self.play(Write(ranges[1]))
        self.play(Write(ranges[2]))
        self.play(Write(ranges[3]))
        self.play(Write(ranges[4]))
        self.wait(1)

        self.play(
            FadeOut(ranges),
            FadeOut(for_code),
            FadeOut(arr_vgroup),
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
            .scale(0.75)
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

        self.add(NumberPlane(x_range=(-8, 8, 1), y_range=(-5, 5, 1)).scale(0.75))
