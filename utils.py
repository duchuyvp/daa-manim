from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars

SCALE = 0.7
FONT = "FiraCode Nerd Font"


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)


def text_bubble_ask(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg").flip(UP)
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)


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


def label_g(s, scale=SCALE):
    label = SVGMobject("left_label.svg").scale(0.5)
    query = MathTex(s).scale(scale).move_to(label).shift(0.1 * UP + 0.15 * RIGHT)

    return VGroup(label, query)


def return_node(s):
    square = Square(side_length=1, color=BLUE)
    text = Text(s, font=FONT).scale(0.4).move_to(square)

    return VGroup(square, text)


def node_map(a, b):
    text_a = VGroup(*[Tex(str(a[i])) for i in range(len(a))]).arrange(RIGHT, buff=0.4)
    text_b = VGroup(*[Tex(str(b[i])).next_to(text_a[i], DOWN, buff=0.3) for i in range(len(b))])
    line = Line(
        text_a.get_critical_point(DOWN + LEFT) + 0.1 * LEFT, text_a.get_critical_point(DOWN + RIGHT) + 0.1 * RIGHT
    ).next_to(text_a, DOWN, buff=0.15)

    sr = SurroundingRectangle(VGroup(text_a, text_b, line), buff=0.15, color=BLUE)

    return VGroup(text_a, text_b, line, sr)


def build_segment_tree(arr):
    # arr = [[5, 8, 6, 3, 2, 7, 2, 6], [13, 9, 9, 8], [22, 17], [39]]
    st = [0]
    for i in range(len(arr) - 1, -1, -1):
        st.extend(arr[i])
    nl = len(arr)
    layer = VGroup(
        *[
            VGroup(
                *[VGroup(Square(side_length=1, color=BLUE), Text(str(arr[i][j]))) for j in range(pow(2, nl - i - 1))]
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

    sr = SurroundingRectangle(VGroup(layer, line), buff=1, color=BLUE)

    return VGroup(layer, line, sr)


def get_semi_down_corner(mobject, direction):
    return (mobject.get_critical_point(DOWN) + mobject.get_critical_point(DOWN + direction)) / 2
