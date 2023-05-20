from manim import *

SCALE = 0.7
FONT = "FiraCode Nerd Font"


class DynamicTree(MovingCameraScene):
    def construct(self):
        text = Text("Data structure").scale(1.5)
        self.play(Write(text))
        self.wait()

        self.play(FadeOut(text))
        self.wait()

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

        self.play(FadeOut(code3), FadeOut(pi_teacher))

        x_range = [0, 4, 1]
        y_range = [0, 4, 1]

        # grid_2d_arr = (
        #     VGroup(
        #         *[
        #             VGroup(
        #                 *[
        #                     VGroup(
        #                         Rectangle(
        #                             width=x_range[2],
        #                             height=y_range[2],
        #                             color=BLUE,
        #                             stroke_width=2,
        #                         ),
        #                         Text(str(g[i][j]), font=FONT),
        #                     )
        #                     for i in range(x_range[0], x_range[1], x_range[2])
        #                 ]
        #             ).arrange(RIGHT, buff=0)
        #             for j in range(y_range[0], y_range[1], y_range[2])
        #         ]
        #     )
        #     .arrange(DOWN, buff=0)
        #     .scale(SCALE)
        #     .to_corner(UP + RIGHT)
        # )

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

        self.play(FadeOut(layer), FadeOut(line), FadeOut(arr_v))
        self.wait()

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


def return_node(s):
    square = Square(side_length=1, color=BLUE)
    text = Text(s, font=FONT).scale(0.4).move_to(square)

    return VGroup(square, text)


def text_bubble_speech(text) -> VGroup:
    bubble_speech = SVGMobject("PiCreature/Bubbles_speech.svg")
    text = Paragraph(text, alignment="center").move_to(bubble_speech).shift(UP * 0.25).scale(0.35)
    return VGroup(bubble_speech, text)


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
