
from manim import *
import numpy as np


TRANSFORM_FORMURA = {
'TF_T' : r"ct' = \gamma (ct - \beta x)",
'TF_X' : r"x' = \gamma (-\beta ct + x)",
'TF_Y' : r"y' = y",
'TF_Z' : r"z' = z"
}
C = 6

BETA = r"\beta = \frac{V}{c}"
GAMMA = r"\gamma = \frac{1}{\sqrt{1 - (\frac{V}{c})^2}}"


class Formura1Slide(Scene):
    '''
    Lorentz transformation formura
    '''
    def construct(self):
        formula_cursor = MathTex(r"-")
        formula_cursor.to_edge(UP)
        for formula in TRANSFORM_FORMURA.values():
            eq = MathTex(formula)
            eq.next_to(formula_cursor, DOWN)
            formula_cursor = eq
            self.play(Write(eq))
        self.wait(1)
        
        formula_beta = MathTex(f"{BETA} \quad {GAMMA}").next_to(formula_cursor, DOWN)
        self.play(Write(formula_beta))

class Formura2Slide(Scene):
    XDASH = r"x' = a_1 x + a_2 t"
    TDASH = ["t'", "=", "a_3 x", "+", "a_4 t"]
    XDASH_1 = r"x' = A x - Av t"
    XDASH_2 = r"x' = A (x - vt)"
    SPHERE_EQ = r"x^2 + y^2 + z^2 = (ct)^2"
    SPHERE_EQ_DASH = r"x'^2 + y'^2 + z'^2 = (ct')^2"
    TDASH_1 = r"t' = B x + D t"
    SPHERE_EQ_DASH2 = r"A^2 (x - vt)^2 + y^2 + z^2 = c^2 (Bx + Dt)^2"
    SPHERE_EQ_DASH3 = [
        "(A^2 - c^2 B^2)", "x^2", 
        "+", "y^2", "+", "z^2",
        "=",
        "(c^2 D^2 - v^2 A^2)", "t^2",
        "+", "(2vA^2 + 2c^2BD)", "xt",
    ]
    SPHERE_EQ_DASH3_COEFF_X_INDEX = 0
    SPHERE_EQ_DASH3_COEFF_T_INDEX = 7
    SPHERE_EQ_DASH3_COEFF_XT_INDEX = 10
    SIM_EQ = r"""
    A^2 - c^2 B^2 = 1 \\
    c^2 D^2 - v^2 A^2 = c^2 \\
    2vA^2 + 2c^2BD = 0
    """
    
    

    CONST_LIGHT = r"Principle of constancy of light velocity"
    RELATIVITY = r"Principle of relativity"

    def construct(self):
        formula_cursor = MathTex(r"-")
        formula_cursor.to_edge(UP)
        xdash = MathTex(self.XDASH)
        xdash.next_to(formula_cursor, DOWN)
        self.add(xdash)

        tdash = MathTex(*self.TDASH)
        tdash.next_to(xdash, DOWN)
        self.add(tdash)
        self.wait(1)
        
        xdash2 = MathTex(self.XDASH_2)
        xdash2.move_to(xdash.get_center())
        self.play(ReplacementTransform(xdash, xdash2))
        self.wait(1)
        

        tdash_1 = MathTex(self.TDASH_1)
        tdash_1.move_to(tdash.get_center())
        self.play(ReplacementTransform(tdash, tdash_1))
        self.wait(1)
        
        
        princ_const_text = Text(self.CONST_LIGHT, font_size=24)
        princ_const_text.move_to(ORIGIN)
        sp = MathTex(self.SPHERE_EQ)
        sp.next_to(princ_const_text, DOWN)
        spdash = MathTex(self.SPHERE_EQ_DASH)
        spdash.next_to(sp, DOWN)
        self.play(AnimationGroup(
            Write(princ_const_text),
            Write(sp),
            Write(spdash)
        ))
        self.wait(1)
        

        self.play(
            AnimationGroup(
                FadeOut(sp),
                FadeOut(princ_const_text),
                spdash.animate.move_to(ORIGIN),
            )
        )
        self.wait(1)
        

        self.play(AnimationGroup(
            TransformMatchingTex(xdash2.copy(), spdash),
            TransformMatchingTex(tdash_1.copy(), spdash),
        ))
        spdash2 = MathTex(self.SPHERE_EQ_DASH2)
        self.play(
            ReplacementTransform(spdash, spdash2)
        )
        
        self.play(
                TransformMatchingTex(
                    spdash,
                    spdash2,
                ),
        )
        # self.wait(1)

        FONT_SZ_SPD3 = 40
        spdash3 = MathTex(*self.SPHERE_EQ_DASH3, font_size=FONT_SZ_SPD3)
        self.play(
            ReplacementTransform(spdash2, spdash3)
        )
        
        # self.wait(1)

        underline_x = Underline(spdash3[self.SPHERE_EQ_DASH3_COEFF_X_INDEX])
        underline_t = Underline(spdash3[self.SPHERE_EQ_DASH3_COEFF_T_INDEX])
        underline_xt = Underline(spdash3[self.SPHERE_EQ_DASH3_COEFF_XT_INDEX])
        self.play(AnimationGroup(
            Write(underline_x),
            Write(underline_t),
            Write(underline_xt),
        ))

        # Show original sphere equation (without dash symbol)
        sp = MathTex(self.SPHERE_EQ).next_to(spdash3)
        sp.move_to([0, -2, 0])
        self.play(Write(sp))
        
        # font size is aligned with spdash3 equation
        ul_label_x = Text("1", font_size=FONT_SZ_SPD3).next_to(underline_x, DOWN)
        ul_label_t = MathTex("c^2", font_size=FONT_SZ_SPD3).next_to(underline_t, DOWN)
        ul_label_xt = Text("0", font_size=FONT_SZ_SPD3).next_to(underline_xt, DOWN)
        self.play(AnimationGroup(
            Write(ul_label_x),
            Write(ul_label_t),
            Write(ul_label_xt),
        ))
        # self.wait(1)

        sim_eq = MathTex(SIM_EQ)

        

class LightSpreadScene(Scene):
    def construct(self):
        
        for i in range(3):
            sphere = Sphere(radius=0.2, fill_opacity=0.1)
            self.add(sphere)
            self.play(
                sphere.animate.scale(6),
                run_time=0.5
            )
            self.play(FadeOut(sphere))
        self.wait()

        

class RocketAndHumanScene(Scene):
    ROCKET_START_POS = 0
    ROCKET_STOP_POS = 3
    def construct(self):
        nm_line = NumberLine(
            x_range=[-1, 5, 1],
            length=10,
            color=BLUE,
            include_numbers=False,
            label_direction=DOWN
        )
        nm_line.add_tip()
        coord_label = MathTex(r"x").next_to(nm_line, RIGHT)
        point_0_label = MathTex(r"0").next_to(nm_line.n2p(0), DOWN)
        
        # Draw 1D numerical line
        self.play(AnimationGroup(
            Create(nm_line),
            Write(coord_label),
            Write(point_0_label),
        ))
        self.wait(1)

        # Draw and animate a rocket
        rocket_half = [
            [-2, 0, 0],
            [-2, 1.5, 0],
            [-1, 1, 0],
            [3, 1, 0],
            [4, 0, 0],
        ]
        mirror_rockert_half = [[point[0], -point[1], point[2]] for point in reversed(rocket_half)]

        rocket = Polygon(
            *rocket_half,
            *mirror_rockert_half,
            color=WHITE,
            fill_opacity=1
        )
        rocket.scale(0.3)
        rocket.next_to(nm_line.n2p(self.ROCKET_START_POS), UP)  
        
        self.play(FadeIn(rocket)) 
        self.play(rocket.animate.next_to(nm_line.n2p(self.ROCKET_STOP_POS), UP))
        
        # Show label at x = vt
        point_label = MathTex(r"""
            \begin{aligned}
            t = t_1 \\
            x = V t_1
            \end{aligned}
        """).next_to(nm_line.n2p(self.ROCKET_STOP_POS), DOWN)        
        
        # Velocity allow
        vect_v = Arrow(
            color=RED,
            buff=0,
        )
        vect_v.next_to(rocket, UP)
        vect_v_label = MathTex(r"V").next_to(vect_v, UP)
        self.play(AnimationGroup(
                GrowArrow(vect_v),
                FadeIn(vect_v_label),
                FadeIn(point_label),
         ))
        self.wait(1)


        human_half = [
            [0, 0, 0],
            [0.1, 0, 0], 
            [0.1, -2, 0], # foot
            [0.5, -2, 0], # foot
            [0.5, 0.2, 0],
            [0.7, 0.2, 0],
            [0.7, 0, 0],
            [1, 0, 0],
            [1, 2, 0],
            [0.5, 2, 0], # head
            [0.5, 2.8, 0], # head
            [0, 2.8, 0], # head
        ]
        mirror_human_half = [[-point[0], point[1], point[2]] for point in reversed(human_half)]

        human = Polygon(
            *human_half,
            *mirror_human_half,
            fill_opacity=1
        )
        human.scale(0.2)
        human.next_to(nm_line.n2p(self.ROCKET_START_POS), UP)
        self.play(Write(human))
    



class XTGraphAnimSlide(Scene):
    def construct(self):
        ax = NumberPlane(
            x_range=[-C, C, 1],
            y_range=[-C, C, 1],
        )
        x_values = np.linspace(0, C, 10)
        light_y_values = x_values
        light_graph = ax.plot_line_graph(x_values, light_y_values, line_color=GOLD_E)
        
        sdash_y_values = x_values *2
        sdash_graph = ax.plot_line_graph(x_values, sdash_y_values)
        ax.add_coordinates()

        label_x = MathTex("x").next_to(ax.x_axis, RIGHT)
        label_y = MathTex("ct").next_to(ax.y_axis, UP)

        self.add(ax)
        self.add(label_x, label_y)
        self.play(Create(light_graph, run_time=2))
        self.play(Create(sdash_graph, run_time=2))

class LinearTransformation(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            leave_ghost_vectors=False,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        v = C / 3
        beta = v / C
        gamma = np.sqrt(1 / (1  - (v / C) ** 2 ))

        matrix = [[gamma, -beta * gamma], [-beta * gamma, gamma]] 
        light_vect = self.add_vector([3, 3], color=GOLD_A, animate=False)
        rocket_vect = self.add_vector([1, 3], color=GOLD_B, animate=False)
        

        # obj = Line(start = [1, 0, 0], end = [2, 2, 0], stroke_color=YELLOW).add_tip()
        x_label = MathTex(r"x")
        x_label.to_edge(RIGHT).shift(UP * 0.3)
        y_label = MathTex(r"ct")
        y_label.to_edge(UP).shift(LEFT * 0.3)
        self.add(x_label, y_label)
        
        self.add_transformable_label(light_vect, "Light", at_tip=True, new_label="Light'")
        self.add_transformable_label(rocket_vect, "Rocket", at_tip=True, new_label="Rocket'")
        self.add_transformable_mobject(light_vect, rocket_vect)

        self.apply_matrix(matrix)
        
        
        tf_x_label = MathTex(r"x'")
        tf_y_label = MathTex(r"ct'")

        tf_x_label.move_to(x_label.get_center())
        tf_y_label.move_to(y_label.get_center())
        self.play(AnimationGroup(
            ReplacementTransform(x_label, tf_x_label),
            ReplacementTransform(y_label, tf_y_label)
            )
        )
        self.wait()
