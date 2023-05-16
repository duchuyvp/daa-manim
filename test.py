from manim import *


class AnimatingMethods(Scene):
    def construct(self):
        text = Text("Hello World").shift(UP)
        self.play(Write(text))
        self.wait()

        self.play(text.animate.set_text("Hello Manim"))
