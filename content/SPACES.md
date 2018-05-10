Title: SPACES: Mnemonic for core values of good modeling software
Date: 2018-05-10 00:14
Category: Python, Modeling, Code
Tags: rant, code
Authors: Mark Mikofski
Summary: What makes good modeling software? Repeat this three times out loud.

# Modeling
Mathematical models of scientific phenomena are essential in engineering. We
use them to design experiments and select instruments based on estimates of the
sensitivities of relationships between factors. We derive models from the
experimental results and use them to develop more predictive models. Sometimes
we can use models to reorganize experimental results to fit into the context of
our understanding of the physical world, and sometimes this leads to the
discovery of new factors and new relationships. When we are confident in our
models ability to explain physical phenomena and describe relationships, we use
them to predict. We can use predictive models to find solutions by optimizing
our objectives. Good models are powerful, and they are the very essense of
science.

# Software
Computers have revolutionalized the derivation and use of mathematical models
to understand, describe, and predict our universe. We use code to interpret
mathematics and science into a language that computers can use to perform
calculations that would have taken us years to do by hand. But just like pencil
and paper work there are ways to organize code to accomplish objectives. Good
modeling software is based on a set core values.

# SPACES
SPACES is a mnemonic for the core values of good modeling software.

* **S**imple
* **P**erfomant
* **A**ccurate
* **C**ollaborative
* **E**xtensible
* **S**table

## Simplicity
Good modeling software is simple. It doesn't do more or less than what it needs
to do. It doesn't create more problems than it solves. It isn't convoluted or
difficult to explain. It may contain complex algorithms, but the art and beauty
of good code is that it makes the complex elegant. Document your code well. Use
autodocumentation so that there isn't double documentation. Keep as much of the
documenation in the source code as possible. Make comments that explain the
intent of your code and read like a human being wrote them. Write comments to
yourself. Use `TODO` and `FIXME` frequently in your code as reminders of
changes you still need or want. Break up your documentation into sections based
on the target audience.

>Always include a **Quickstart Tutorial** that is one page and has simple but
>realistic examples!

Include a detailed but simple user guide, a comprehensive API, and a developer
guide that explains things like how to build the documentation, how the CI is
set up, how the server is configured, how to deploy the software, and what
conventions were used. Be detailed. Consider adding a cookbook of examples, a
gallery, tutorials, or HOWTO sections. Your API should be 100% covered.

## Performance
It just has to be fast enough. Usually there is a trade off between speed and
accuracy, so finding the balance is tricky. But in order to be useful, modeling
software must not be slow. Efficiency where possible should always be a
priority. Maybe not in the first draft, but in revisions inefficiency should be
removed wherever it's found. Don't repeat yourself. However, don't create overly complicated code. Efficienty code should still be simple. Strive for elegance.

## Accuracy
It just has to be accurate enough. Understand your uncertainties. Regardless,
modeling software that is inaccurate is useless. Make sure it works the way
it's expected.

## Collaboration
Work together. Science is consensus. Others have already solved your problems.
Others can find new problems. Use what is out there already. Don't reinvent the
wheel. Ask for help. Get opinions. Listen. Consider alternatives. Collaborate.

## Extensibility
Things change. Our understanding of the physical world changes. New
technologies evolve. Build in the capacity for change in your modeling
software. Anticipate that your code will need to adapt. Make it easy to
maintain and update. Make it extensible to customization. Modularize. Break
down your model into units that can be reused, so that intermediate values
can be interrogated easily, and so contributions can be made at different entry
points. Consider making your application a stack with a common object that is
passed from unit to unit, and can be serialized and deserialized when needed.
This will make it easier to save and load state, and to scale and parallelize.
It will also make it easier to test.

## Stability
Good modeling software isn't fragile. It should be bomb proof. Test it. Use a
unitest framework as well as some end-to-end tests. Strive for 100% coverage.
Set up a CI server to test on every push to the master branch and on pulls.
Don't use polynomial fits over 3rd order unless they are physical. Set limits
on arguments, and handle exceptions gracefully. Make sure that equations don't
blow up unexpectedly and return `NaN` or `Inf` everywhere. Make sure that units
are explained in the documentation or user interface. Scale big numbers and
watch out for overflows. Watch for interger division. It's okay to follow the
practice of "easier to ask for forgiveness than permission" but errors have to
be handled eventually, and users deserve meaningful feedback. Just make sure it
always works as expected.

## Spaces
Put spaces in your code. Don't be terse. Follow the coding guidelines common
for the codebase.
