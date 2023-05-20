from manim import *

SCALE = 0.7
FONT = "FiraCode Nerd Font"


class RangeUpdate(Scene):
    def construct(self):
        text = Text("Range Update").scale(1.5)
        text_small = Text("Point query").next_to(text, DOWN)
        self.play(Write(text))
        self.play(Write(text_small), VGroup(text, text_small).animate.move_to(ORIGIN))
        self.wait()

        self.play(FadeOut(text), FadeOut(text_small))
        self.wait()

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

        self.play(Create(d_arr_v), Write(text_d_arr))
        self.wait()

        self.play(arr_v[6][0].animate.set_fill(color=YELLOW, opacity=0.4))
        self.wait()

        self.play(*[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(7)])
        self.wait()

        self.play(
            arr_v[6][0].animate.set_fill(color=YELLOW, opacity=0),
            *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(7)],
        )
        self.wait()

        add_text_1 = MathTex("+ x").scale(0.7).next_to(arr_v, RIGHT, buff=SCALE)
        add_text_2 = MathTex("+ x").scale(0.7).next_to(d_arr_v, RIGHT, buff=SCALE)

        self.play(Create(add_text_1), *[arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in range(2, 6)])
        self.wait()

        self.play(Create(add_text_2), *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0.4) for i in [2, 6]])
        self.wait()

        self.play(
            FadeOut(add_text_1),
            FadeOut(add_text_2),
            *[arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in range(2, 6)],
            *[d_arr_v[i][0].animate.set_fill(color=YELLOW, opacity=0) for i in [2, 6]],
        )
        self.wait()

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

        self.play(Write(mid_text), Write(left_text), Write(right_text), Write(rright_text), FadeOut(pi_bubble_speech))
        self.wait()

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


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)
