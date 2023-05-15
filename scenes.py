from manim import *


class CodeTrackingAnimation(Scene):
    def construct(self):
        code_str = """
        #include<iostream>
        using namespace std;
        int main(){
            int sum = 0;
            for(int i=0;i<n;i++){
                sum += i;
            }
            return 0;
        }"""
        code = Code(code=code_str, language="C++", background="window", line_spacing=1)
        # code.code = remove_invisible_chars(code.code)  # <---- HERE
        self.add(code)
        # build sliding windows (SurroundingRectangle)
        self.sliding_wins = VGroup()
        height = code.code[0].height
        for line in code.code:
            self.sliding_wins.add(
                SurroundingRectangle(line)
                .set_fill(YELLOW)
                .set_opacity(0)
                .stretch_to_fit_width(code.background_mobject.get_width())
                .align_to(code.background_mobject, LEFT)
            )

        self.add(self.sliding_wins)
        for i in range(len(code.code) - 1):
            self.play(self.sliding_wins[i].animate.set_opacity(0.3))
            self.play(
                ReplacementTransform(self.sliding_wins[i], self.sliding_wins[i + 1])
            )
            self.play(self.sliding_wins[i + 1].animate.set_opacity(0.3))
