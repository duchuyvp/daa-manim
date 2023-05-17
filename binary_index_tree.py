from manim import *

SCALE = 0.7


class BinaryIndexedTree(MovingCameraScene):
    def construct(self):
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
                Text(str(i)).scale(0.5).next_to(arr_v[i - 1][1], DOWN)
                for i in range(1, len(arr))
            ]
        )

        arr_vgroup = (
            VGroup(arr_v, index_arr_v).arrange(DOWN, buff=0.5).scale(SCALE).to_edge(UP)
        )
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

        index_bit_v = VGroup(
            *[
                Text(str(i)).scale(0.5).next_to(bit_v[i - 1][1], LEFT)
                for i in range(1, len(arr))
            ]
        )
        bit_vgroup = (
            VGroup(bit_v, index_bit_v)
            .arrange(LEFT, buff=0.5)
            .scale(SCALE)
            .next_to(arr_vgroup, DOWN)
            .to_edge(LEFT, buff=1.5)
        )

        bit_label = Tex("tree").scale(SCALE).next_to(bit_v, UP)
        self.play(Write(bit_label))

        self.play(
            *[Create(bit_v[i][0]) for i in range(len(bit_v))], Create(index_bit_v)
        )
        self.wait()

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=8))
        self.wait()

        # self.play(Restore(self.camera.frame))
        # formula_tree = MathTex("tree[k] = \\sum_{i=k-p(k) + 1}^{k} a_i")
        # self.play(Write(formula_tree))
        # self.wait()
