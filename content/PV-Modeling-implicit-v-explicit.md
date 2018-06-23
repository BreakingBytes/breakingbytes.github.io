Title: Examples of implicit versus explicit solutions for photovoltaic solar energy systems
Date: 2018-06-22 20:55
Category: Modeling
Tags: code, solar
Authors: Mark Mikofski
Summary: Using a numerical solver to model solar power.

# Full Scale PV Modeling

I want to explore different ways to find the operating conditions for max power
of a PV system. I'm going to assume that we're using a single diode model (SDM)
which is an analog curcuit of a solar cell composed from a current source, a
diode, and a resistance in parallel, in series with another resistance.

![single diode model](https://pvpmc.sandia.gov/wp-content/uploads/2012/04/Single-Diode-EC2.png)

_source: [Sandia National Labs: PV Performance Modeling Collaborative](https://pvpmc.sandia.gov/)_

The cell current in the SDM can't be solved explicitly as a function of cell
voltage without using the Lambert-W function. It can be solved implicitly by
using an iterative solver such as a gradient descent method. And there is an
explicit method that can be used to solve for cell current as a function of an
intermediate parameter, the diode voltage, which can then be used to calculate
the cell current. To get a specific voltage using this explicit parameterized
approach, requires solving for several diode voltages and interpolating.

A common use of the SDM is to solve for the ideal operating condition of an
entire PV system by assuming all of the cells are identical. Another proposed
usage of the SDM is to model all of the cells in an entire system to account
for their differences either due to variance in manufacturing, ambient
conditions, or degradation. This second problem poses some challenges
computationally for very large systems.

What is the best method to do full scale PV system modeling? I'm going to skip
the Lambert-W function and focus on implict and explicit methods.

# Conclusions

* The implicit approach is efficient at finding a single operating condition,
even or especially when most of the cells are different, but it's slow at
tracing the entire IV curve.

* The implicit approach is also efficient at determining the max power point.

* Nesting search methods is less efficient than a single closed solution.

* The explicit method is most efficient at tracing the entire IV curve, even
when every cell is different.

# Gist

The following Gist contains examples for a full scale implicit approach and the
explicit parameterized approach described. The Gist are best viewed on
[nbviewer](http://nbviewer.jupyter.org/gist/mikofski/df318d1f892767ac7c762e732fecaa7f).

<script src="https://gist.github.com/mikofski/df318d1f892767ac7c762e732fecaa7f.js"></script>
