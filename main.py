from manim import *


class Main(Scene):
    def construct(self):
        text = Text("Range queries").scale(1.5)

        self.play(Write(text))
        self.wait(1)

        self.play(FadeOut(text))
        self.wait(1)

        arr = [1, 3, 8, 4, 6, 1, 3, 4]
        arr_vgroup = VGroup(
            *[VGroup(Square(side_length=1, color=BLUE), Text(str(i))) for i in arr]
        ).arrange(RIGHT, buff=0).scale(0.75)

        self.play(Write(arr_vgroup))
        self.wait(1)

        self.play(arr_vgroup.animate.to_edge(UP))
        self.wait(1)

        query = [
            MathTex("sum_q(l,r) =", "\\sum_{i=l}^{r} a_i").move_to(ORIGIN+ 1.5* UP),
            MathTex("min_q(l,r) =", "\\min_{i=l}^{r} a_i").move_to(ORIGIN),
            MathTex("max_q(l,r) =", "\\max_{i=l}^{r} a_i").move_to(ORIGIN+ 1.5*DOWN),
        ]
        result = [
            MathTex("= 14").next_to(query[0], RIGHT),
            MathTex("= 1").next_to(query[1], RIGHT),
            MathTex("= 6").next_to(query[2], RIGHT),
        ]
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

        l = 3
        r = 6

        range_arr = MathTex(
            "l = " + str(l),
            ", ",
            "r = " + str(r),
        ).next_to(queries, UP).scale(0.75)

        self.play(
            Write(range_arr),
            *[arr_vgroup[i][0].animate.set_fill(YELLOW, opacity=0.2) for i in range(l, r + 1)],
        )
        self.wait(1)


        self.play(Write(result[0]), Write(result[1]), Write(result[2]))
        self.wait(1)



        # self.add(NumberPlane(x_range=(-5, 5, 1), y_range=(-5, 5, 1)))
