Title: Blast Wall Optimisation

Overview: This project was completed as a learning exercise during my time at The University of Sheffield. It models the dynamic response of a cantilevered blast wall subjected to a time-varying blast load. The program implements a bisector root finding algorithm to evaluate combinations of structural stiffness, mass, and stand-off distance to identify the lowest-cost design that satisfies a maximum allowable displacement.

Technologies: Python, Numpy, Matplotlib

Assumptions:
-    The wall behaves as a linear elastic system throughout loading.
-    Mass and stiffness are represented by equivalent lumped parameters.
-    Structural damping is neglected.
-    The blast load is applied uniformly across the wall face.
-    Peak blast force  varies with stand-off distance according to:
  
          Fpeak(x) = 1000 + 9x² − 183x
     where Fpeak (kN), x(m).
-    Load duration varies with stand-off distance according to:

          td(x) = 20 − 0.12x² + 4.2x
     where td(ms), x(m).
-    Displacement is calculated using the analytical solution for an undamped SDOF system subjected to a linearly decaying load pulse:

            z(t) = Fpeak/k [1 − cos(ωt)] + Fpeak/(k·td) [sin(ωt)/ω − t] for t ≤ td
            z(t) = Fpeak/(kωtd) [sin(ωt) − sin(ω(t − td))] − Fpeak/k cos(ωt) for t > td
     where z(m), Fpeak(N), k(N/m), td(s), t(s), ω = √(k/m)(rad/s).
-    The wall is considered to fail if peak displacement exceeds 100 mm.
-    Material non-linearity, cracking, yielding, permanent deformation and soil-structure interaction are not considered.
-    The optimum solution is obtained within a discretised design space of stiffness and mass values.
-    The optimisation considers three sources of cost: additional stiffness, additional mass, and additional distance. Governed by the following equations respectively:

          Ck = 900 + 825k² − 1725k
          Cm = 10m − 2000
          Cx = 2400(x²/4)
          C = Ck + Cm + Cx
     where k(MN/m), m(kg), x(m).
