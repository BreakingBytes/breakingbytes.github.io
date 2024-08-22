Effects from shade are complicated, but can be summarized in two orthogonal categories:

1. shade across all modules parallel to strings
2. shade across few modules perpendicular to strings

## shade parallel to rows
Row-to-row shade in fixed-tilt systems, typically in winter, is an example of
shade across all modules that is parallel to strings. When I originally wrote
about [PV electrical mismatch]]({filename}PV-electrical-mismatch.md), I analyzed
this type of shade using [PVMismatch](https://sunpower.github.io/PVMismatch/)
to simulate shade across the bottom row of a single string of 10 modules in a
10 string system. The conclusion of that post was that the string performed as
well as the most shaded cell, so even though only the bottom cells were shaded,
the modules in the string lost most of their power. I shaded the bottom cells
80% to simulate only diffuse light, and the string lost roughly 80% of output.
The other 9 strings operated at full capacity, so the system only lost 8%. The
[NIST ground mount array](https://www.nist.gov/el/energy-and-environment-division-73200/heat-transfer-alternative-energy-systems/photovoltaic-1)
is an example of a system that will have row-to-row shade in winter that will
cause most of the strings to lose almost all of their output even when only
the bottom row of cells is shaded.

![NIST Google](./images/nist-ground-array.png)

This topic is also covered in 

## shade not parallel to rows
However, that post also contained a picture of a rooftop with non-uniform shade
that was not consistent across each module of the string. The shade cast from
the roofline cut diagonally across the modules in the string, which was wrapped
in two rows to fit.

![non uniform shade on a roof](./images/20150923_170418.jpg)

I didn't analyze the shade from this system in that post, so it raises the
question whether the rule of thumb I recommended would still apply?

## shade perpendicular to rows
To simplify the question, the rest of this post analyzes a PV system with a
shade obstacle like a wind turbine tower or a telephone pole that casts shade
perpendicular to the rows.

>TL;DR: When shade cuts perpendicular to strings, cells go into reverse bias,
bypass diodes activate in the shaded submodules, and the other modules operate
at higher voltage to match the voltage of unshaded parallel strings.

01234567890123456789012345678901234567890123456789012345678901234567890123456789