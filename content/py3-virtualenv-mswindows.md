Title: Python-3 Virtual Environments on MS Windows
Date: 2017-05-18 11:01
Category: Python
Tags: virtualenv, pelican, windows, bash, rant
Authors: Mark Mikofski
Summary: Python-3 venv module vs virtualenv package

This is a follow up from my [first post]({filename}/new-blog-announcement.md)
on this new Pelican blog. I should have logged how I set up this, instead of
the glib cliché, "usage is a snap". Here I am posting for the second time, and
I'm wondering, "why didn't I just use the
[built in Jekyll static site generator](https://help.github.com/articles/about-github-pages-and-jekyll/)?"

Anyway, for posterity...

# Publishing to GH Pages

To publish my pages I use the `Makefile` that Pelican generates when you start
your blog using `pelican-quickstart`. I may have editted the `Makefile` to
target my GitHub `master` branch since I'm using
[User Pages](http://docs.getpelican.com/en/stable/tips.html#user-pages) or maybe
Pelican asked me during the quickstart questionnaire, I can't remember. The
`Makefile` uses a handy tool called
[`ghp-import`](https://github.com/davisp/ghp-import) that copies the contents of
the output directory to the target git branch. Then the `Makefile` publishes
the blog by pushing the target branch to GitHub. The `ghp-import`
package is described a bit in the
[Pelican Tips](http://docs.getpelican.com/en/stable/tips.html#publishing-to-github)
on publishing to GitHub pages, but the `Makefile` takes care of calling it. So
all I have to do to publish my posts is execute:

    make publish

# Python-3 Virtual Environment

Okay, I can't remeber exactly the reason, but `ghp-import` worked better in
Python-3 than Python-2, and so I created a virtual environment for Python-3.
This brings me finally to the title of this post. How does one create a virtual
environment for Python-3? Well according to the
[Python Packaging Authority (PyPA)](https://packaging.python.org/installing/#creating-virtual-environments)
since Python-3.3 there is a built in module called
[`venv`](https://docs.python.org/3.5/library/venv.html). However the venerable
[`virtualenv`](https://virtualenv.pypa.io/en/stable/) package also works just
fine for Python-3.

How do these packages differ? There is one major difference that really affects
me. The built in Python-3 `venv` module only activates in MS Windows `CMD`
terminal or PowerShell whereas Ian Bicking's indispensible `virtualenv` package
works in BaSH as well. This is an issue with Python on MS Windows that I
encounter a lot, it's a PITA and breaks the whole concept of a common unified
experience regardless of user's platform. I should be able to use Python exactly
the same on any system with very minor exceptions. Since I tend to mostly
use BaSH, this means that to use the built in `venv` module I have to
switch to a MS Windows `CMD` shell. I guess it's not that big of a deal, but
since `virtualenv` works fine with Python-3, I guess I'll stick with that.

Okay, there's also one other important difference. Python-3 installs all of its
shared objects into the virtual environment, which is different from Python-2
which uses links mostly. This means that when you update your version of
Python-3 you need to _also_ update your virtual environment.

For the `virtualenv` package you'll have to create a new virtual environment on
top of the old one. But for the built in `venv` module you can just run:

    py -3 -m venv --upgrade <my-py3-venv>

where `<my-py3-venv>` is the name of your Python-3 virtual environment. I think
the source code for both are nearly the same, and I also think that under the
hood the `--upgrade` option is really doing exactly the same thing as
`virtualenv`, the difference is that if you try to create a virtual environment
on top of an existing one with the Python-3 `venv` module is will raise an
exception.

>Changed in version 3.4: In earlier versions, if the target directory already
existed, an error was raised, unless the `--clear` or `--upgrade` option was
provided. Now, if an existing directory is specified, its contents are removed
and the directory is processed as if it had been newly created.

In conclusion, I don't see much difference between the two methods. So if you
want to use BaSH on MS Windows, stick with the original, otherwise try the new.
