from manim import *

class Reuleaux(Scene):
    def construct(self):
        shape = Triangle(stroke_color = PINK).scale(1.5).move_to(ORIGIN)
        def update_point1_1(dot):
            dot.become(Dot(shape.get_top(), fill_opacity = 0).shift(LEFT*6))
        def update_point1_2(dot):
            dot.become(Dot(shape.get_top(), fill_opacity = 0).shift(RIGHT*4))
        def update_point2_1(dot):
            dot.become(Dot(shape.get_bottom(), fill_opacity = 0).shift(LEFT*6))
        def update_point2_2(dot):
            dot.become(Dot(shape.get_bottom(), fill_opacity = 0).shift(RIGHT*4))
        point1_1 = Dot().add_updater(update_point1_1)
        point1_2 = Dot().add_updater(update_point1_2)
        point2_1 = Dot().add_updater(update_point2_1)
        point2_2 = Dot().add_updater(update_point2_2)
        line1 = Line(stroke_color=YELLOW).add_updater(lambda line: line.become(Line(point1_1.get_center(), point1_2.get_center(), stroke_color=YELLOW)))
        line2 = Line(stroke_color=YELLOW).add_updater(lambda line: line.become(Line(point2_1.get_center(), point2_2.get_center(), stroke_color=YELLOW)))
        widthLine = DoubleArrow().add_updater(lambda x: x.become(DoubleArrow(point1_1.copy().shift(RIGHT/2).get_center(), point2_1.copy().shift(RIGHT/2).get_center(), buff=0, stroke_width=3)))
        widthTex = Tex(r"width =", font_size=40).add_updater(lambda t: t.next_to(widthLine, RIGHT, buff=0.05))
        widthNum = DecimalNumber((point1_1.get_center()-point2_1.get_center())[1], num_decimal_places=3, font_size=40).next_to(widthTex, RIGHT).add_updater(lambda n: n.set_value((point1_1.get_center()-point2_1.get_center())[1]).next_to(widthTex, RIGHT))
        widthRect = SurroundingRectangle(widthNum, stroke_color = YELLOW).add_updater(lambda x: x.become(SurroundingRectangle(widthNum, stroke_color = YELLOW)))
        self.add(point1_1, point1_2, point2_1, point2_2)
        self.play(Create(shape))
        self.play(shape.animate.set_fill(PINK, opacity=0.5))
        self.wait(1)
        self.play(Create(line1), Create(line2))
        self.play(FadeIn(widthLine))
        self.play(Write(widthTex), Write(widthNum))
        self.play(Create(widthRect))
        

        self.wait(2)
        self.play(Uncreate(widthRect))
        self.play(Uncreate(line1), Uncreate(line2), FadeOut(widthLine), FadeOut(widthTex), FadeOut(widthNum))

        self.play(RotateCenter(shape, PI/6), run_time=1)
        self.wait(0.5)
        self.play(Create(line1), Create(line2))
        self.play(FadeIn(widthLine))
        self.play(Write(widthTex), Write(widthNum))
        self.play(Create(widthRect))
        self.wait(2)
        self.play(Uncreate(widthRect))
        self.play(RotateCenter(shape, 1.5*PI), run_time = 6)

        self.wait(1)
        self.play(Uncreate(line1), Uncreate(line2), FadeOut(widthLine), FadeOut(widthTex), FadeOut(widthNum))
        self.wait(1)


        square = RegularPolygon(n=4, stroke_color = BLUE, fill_color = BLUE, fill_opacity=0.5).scale(1.5).move_to(ORIGIN)
        self.play(Transform(shape, square))
        self.play(Create(line1), Create(line2))
        self.play(FadeIn(widthLine))
        self.play(Write(widthTex), Write(widthNum))
        self.wait(0.5)
        self.play(RotateCenter(shape, 1.5*PI), run_time = 6)
        self.wait(1)

        color = [GREEN, PURPLE, ORANGE]
        for i in range(5, 8):
            polygon = RegularPolygon(n = i, stroke_color = color[i-5], fill_color = color[i-5], fill_opacity=0.5).scale(1.5).move_to(ORIGIN)
            self.play(Transform(shape, polygon))
            self.wait(0.5)
            self.play(RotateCenter(shape, PI), run_time = 4)
            self.wait(0.5)

        textHeadingCircle = Tex(r"Circle", color=BLUE).to_edge(UP).shift(LEFT*2.5)
        textHeadingWidth = MathTex(r"\Rightarrow   width = constant ").to_edge(UP).shift(RIGHT)
        textWhat = Tex(r"?").to_edge(UP).shift(LEFT*2)
        textWhatElse = Tex(r"What else?").to_edge(UP, buff=1.5)
        textReuleauxTriangle = Tex(r"Reuleaux triangle", color=RED).to_edge(UP).shift(LEFT*4)
        textConst = Tex(r"constant", font_size=40, color=YELLOW).next_to(widthRect, DOWN).add_updater(lambda x: x.next_to(widthRect, DOWN))

        self.play(Write(textHeadingWidth), Write(textWhat))
        self.wait(1.5)
        self.play(ReplacementTransform(textWhat, textHeadingCircle))

        circle = Circle(stroke_color = BLUE, fill_color = BLUE, fill_opacity=0.5).scale(1.5)
        self.play(Transform(shape, circle))
        self.wait(2)
        self.play(Create(widthRect))
        self.play(Write(textConst))
        self.wait(1.5)
        self.play(Unwrite(textConst), run_time=0.5)
        self.play(Uncreate(widthRect))
        self.wait(1)
        self.play(Write(textWhatElse))
        self.play(ReplacementTransform(textHeadingCircle, textReuleauxTriangle))

        textConst = Tex(r"constant", font_size=40, color=YELLOW).next_to(widthRect, DOWN).add_updater(lambda x: x.next_to(widthRect, DOWN))
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        arc0 = ArcBetweenPoints(a, b, radius=2)
        arc1 = ArcBetweenPoints(b, c, radius=2)
        arc2 = ArcBetweenPoints(c, a, radius=2)
        reuleaux = ArcPolygonFromArcs(arc0, arc1, arc2, stroke_color=RED, fill_color=RED, fill_opacity=0.5).scale(1.5).move_to(ORIGIN)

        self.play(FadeOut(textWhatElse), Transform(shape, reuleaux))
        point1_1.remove_updater(update_point1_1)
        point1_2.remove_updater(update_point1_2)
        point2_1.remove_updater(update_point2_1)
        point2_2.remove_updater(update_point2_2)
        self.play(RotateCenter(shape, 2*PI), run_time = 8)
        self.play(Create(widthRect))
        self.play(Write(textConst))
        self.wait(1.5)
        self.play(Unwrite(textConst), run_time=0.5)
        self.play(Uncreate(widthRect))
        self.wait(3)
        self.clear()
        a = [-1, 0, 0]
        b = [1, 0, 0]
        c = [0, np.sqrt(3), 0]
        triangle = Polygon(a, b, c, stroke_color=YELLOW, stroke_width = 3)

        arc0 = ArcBetweenPoints(a, b, radius=2, stroke_width=5)
        point0 = Dot(a, fill_color=RED, radius=0.05)
        circle0 = Circle(radius=2, stroke_color=RED, stroke_width = 3, fill_opacity=0).move_to(a)

        arc1 = ArcBetweenPoints(b, c, radius=2, stroke_width=5)
        circle1 = Circle(radius=2, stroke_color=BLUE, stroke_width = 3, fill_opacity=0).move_to(b)
        point1 = Dot(b, fill_color=BLUE, radius=0.05)

        arc2 = ArcBetweenPoints(c, a, radius=2, stroke_width=5)
        circle2 = Circle(radius=2, stroke_color=GREEN, stroke_width = 3, fill_opacity=0).move_to(c)
        point2 = Dot(c, fill_color=GREEN, radius=0.05)

        reuleaux = ArcPolygonFromArcs(arc0, arc1, arc2, fill_opacity=0)
        group = VGroup(triangle, circle0, circle1, circle2, point0, point1, point2)
        group_all = VGroup(group, reuleaux).scale(2).move_to(ORIGIN)

        self.play(Create(triangle))
        self.wait(0.5)

        self.play(FadeIn(point0))
        self.play(Create(circle0))
        self.wait(0.5)

        self.play(FadeIn(point1))
        self.play(Create(circle1))
        self.wait(0.5)

        self.play(FadeIn(point2))
        self.play(Create(circle2))
        self.wait(0.5)

        self.play(Create(arc1))
        self.play(Create(arc2))
        self.play(Create(arc0))
        self.wait(1)

        self.play(FadeOut(group), reuleaux.animate.set_fill(RED, opacity=1))
        self.wait(5)
        



class RotateCenter(Animation):
    def __init__(self, shape, angle, **kwargs):
        super().__init__(shape,  **kwargs)
        self.angle = angle
        self.shapeCopy = shape.copy()

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = alpha * self.angle
        self.mobject.become(self.shapeCopy.copy().rotate(value))
        self.mobject.move_to(ORIGIN)

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

