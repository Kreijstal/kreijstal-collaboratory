from manimlib.imports import *

class Circuit(Scene):
    def construct(self):
   #     ptvsd.wait_for_attach()
        tex_circuit="""\\begin{circuitikz}[european]
  %\\draw (0,0) to[isource] (0,3) -- (2,3)
  \\draw (3,2) node[npn](Q){};% to[R] (2,0) -- (0,0);
  \\draw (Q.E) -- (3,1) to[R,*-*] ++(0,-2) -- (1,-1);
  \\draw (Q.B) -- (1,2) -- (1,1) to[R,-*] ++ (0,-2);
  \\draw (Q.B) -- (1,2) -- (1,3) to[R, -*] ++ (0, 2) -- (3,5) -- (Q.C);
  \\draw (1,5) node[vcc](VCC){$V_{CC}$};
  \\draw (1,-1) node[ground](GND){};
  \\draw (1,2) to[C, l_=$C_{in}$,*-o]++(-1.5,0) node[left](vin){$Eingang$};
  \\draw (3,1) to[C, -] ++(2,0) ;%node[right](vout){$Ausgang$};
  \\draw (5,1) to[loudspeaker, name=L] (5,-1) -- ++(-2,0);
  \\node [waves, scale=0.7, right] at(L.north) {};
\\end{circuitikz}"""
        circuit=TextMobject(tex_circuit,stroke_width=2,fill_opacity=0)
        color=list(COLOR_MAP.values())
        for i, v in enumerate(circuit.submobjects[0].submobjects):
            v.set_stroke(color[i])

        circuit.scale(0.7)
        self.play(Write(circuit))
        self.wait()

class VerstarkerIntro(Scene):
    def construct(self):
        main = SVGMobject("Twemoji2_1f914.svg")
        radio = SVGMobject("Icon_sound_radio.svg")
        radio.move_to(LEFT*4)
        color=list(COLOR_MAP.values())
        emoji=["#ffcc00","#664500","#664500","#664500","#664500","#664500","#f4900c"]
        radioc=["#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#000000", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
      #  ptvsd.wait_for_attach()
        for i, v in enumerate(main.submobjects):
            v.set_color(color=emoji[i])
        
        for i, v in enumerate(radio.submobjects):
            v.set_color(color=radioc[i])
        
        main.scale(2)
        self.play(FadeIn(main))
        pop = main.copy()
        t=TextMobject("Wie w{\\\"u}rde ich ein Radio machen?").move_to(DOWN*2)
        pop.move_to(RIGHT*5).scale(0.8)
        self.wait(4)
        self.play(Transform(main,pop))
        self.wait(0.2)
        self.play(Write(t))
        self.wait(4)
        self.play(Transform(t,radio))
        self.wait(10)
        self.play()
