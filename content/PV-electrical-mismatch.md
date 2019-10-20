Title: Electric Mismatch in Silicon-Cell PV is Not Intuitive
Date: 2019-10-18 15:23
Category: Solar
Tags: solar, modeling, code
Authors: Mark Mikofski
Summary: Why does shade just across the bottom row of cells cause 90% power loss?

# Uniform Versus Non-Uniform Shade

Photovoltaic solar energy panels, _aka_ PV, have a very unintuitive resonse to
shade, that surprises most people.

> Shade across a relatively small portion of the panel can cause a
disproportionately much larger power loss.

_IE_ Shade across just the bottom row of cells, only 6 cells out of 60, only
10% of the PV panel, will cause 90% power loss! Why does this happen? Did you
think it would cause only 10% power loss? Why isn't power loss _linear_ with
shade?

OK, to be fair, if the entire array is uniformly shaded or merely illuminated
with a less intense light, then the decrease in power _would_ be proportional
to the decrease in light intensity. For example if a giant rain cloud passed
over the sun, or the sun slowly sank behind a mountain, so that the same light
was cast everywhere, but just lower intensity, say 50%, then the power would be
50% lower as well.

So just to be _completely clear_, in this post we are **not** going to talk about
the effects of changes in light intensity that are totally uniform everywhere,
but instead we're going to focus on what happens when there are non-uniform
differences in light intensity across the PV system. Here's an example of a PV
system with non-uniform shade.

![non uniform shade on a roof](./images/20150923_170418.jpg)

# PV Primer

In PV lingo a panel is called a "module" which is made up of smaller solar
"cells" which are connected in series in most silicon PV modules. Modules are
most often connected in series to form "strings" of modules, which are in
parallel and connected to an "inverter" which converts DC current to AC which
is sent to the grid.

Here's a typical PV system at the National Institute of Standards and Technology:

![NIST Google](./images/NIST_Google.png)
![NIST ground mount racks](./images/ground-mount-racks.jpg)

## PV Cells and Modulea

The cells in a PV module can be considered roughly as diodes, which are
semiconductor, or a material that conducts current in one direction, called
forward bias. When a negative voltage, or reverse bias is applied to the cell,
it won't 

# Electric Circuit Theory

So why does non-uniform shade cause this non-linear effect? If we consider the
PV system as an electric circuit, then it must obey the following two laws:

* [Ohm's Law](https://en.wikipedia.org/wiki/Ohm%27s_law)
* [Kirchhoff's Law](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws)

## Ohms Law

According to Ohm's law because the cells and modules in a PV system are all in
series, then they must all carry the same current, `I`, the total votlage of
each module, `Vmod`, is the sum of the cell voltages in that module, and the
total string voltage, `Vstr`, is the sum of the modules voltages in the string.
In the equation below, `Z` represents the impedance of each cell in a module or
each module in a string.

![Ohm's Law](https://latex.codecogs.com/png.latex?V%20%3D%20%5Csum%7BV%7D%20%3D%20I%20%5Csum%7BZ%7D)

_LaTeX provided by [CodeCogs Equation Editor](https://www.codecogs.com/latex/eqneditor.php)_

The actual relation in a cell is actually a bit more complicated than `V=IZ`,
but hopefully this will do to explain electrical mismatch for now. The relation
between the flux of charge and solar cell voltage is described by
[Poisson Energy Transport Equation](https://en.wikipedia.org/wiki/Poisson%E2%80%93Boltzmann_equation) but in practice a 1-diode circuit is a
useful analog. See this post on
[examples of implicit vs. explicit solutions for PV systems](./examples-of-implicit-versus-explicit-solutions-for-photovoltaic-solar-energy-systems.html)
for more info.

## Kirchhoff's Law

Kirchhoff's law requires the voltage across all of the parallel strings to be
the same as the voltage across the inverter, and the total current at the
inverter nodes to be the sum of the currents from all parallel strings
connected to it.

![Kirchhoff's Law](https://latex.codecogs.com/png.latex?I%20%3D%20%5Csum%7BI%7D)

_LaTeX provided by [CodeCogs Equation Editor](https://www.codecogs.com/latex/eqneditor.php)_

# Electrical Mismatch 

The combined effect of enforcing Ohm's and Kirchhoff's laws on a PV system that
is partially shaded can cause what's called _electrical mismatch_. In other
words, the shaded cells can't match the current being carried by the rest of
the module, or the string with shaded modules can't carry the same voltage as
the PV system, and therefore the entire system has to find a new operating
condition to satisfy Ohm's and Kirchhoff's laws.

## The Single Diode Model

How 