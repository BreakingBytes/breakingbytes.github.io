Title: Python Concurrency Primer
Date: 2019-10-07 10:33
Category: Python
Tags: code, web
Authors: Mark Mikofski
Summary: Asynchronous Python workflows for IO and CPU processes on a single machine versus a cluster.

# Python Threading versus Multiprocessing

Threading works really well with IO, but not CPU bound processes, hence why there's an [asyncio lib](https://docs.python.org/3/library/asyncio.html) for IO and a [MP lib](https://docs.python.org/3/library/multiprocessing.html). Before Py3, you could only manually create threads using the [threading lib](https://docs.python.org/3/library/threading.html) and some people who don't like asyncio still prefer to use the manual threading lib, an external lib like [trio](https://trio.readthedocs.io/en/stable/), or older packages like [gevents](http://www.gevent.org/), etc.

For an example of using threading for an IO bound process see the [`pvlib.iotools.get_ecmwf_macc()` method](https://github.com/pvlib/pvlib-python/blob/master/pvlib/iotools/ecmwf_macc.py#L168) which returns the thread that calls the ECMWF api client because it is soooooo slow!


# Concurrency in the Cloud

Curve ball (⚾) - threading and MP work great for a single computer, but when you are on a cluster, such as web applications, then you have more options!  

In a web app, you usually have a load balancer in front of several workers who answer get requests.

Therefore you can deligate the work for both IO and CPU bound processes differently than by using either threading, MP, asyncio, trio, gevent, etc.

[Celery](http://www.celeryproject.org/) is probably the most popular task queue for distributed resources especially for web applications.

I would guess there are task managers other than Celery, but would have to Google around to find a curated list - and many examples recommend Celery, eg: [Heroku](https://devcenter.heroku.com/articles/celery-heroku).

# Inter-Process Communication
Note a task queue, threading, and MP all require a way to communicate with the thread, this is called [IPC or inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication).

For threads and MP, I typically use a [Queue](https://docs.python.org/3/library/queue.html) but there are other options.

For distributed computing, the recommendation is to use a message queue like [RabbitMQ](https://www.rabbitmq.com/) or a shared memory server like [memcached](https://memcached.org/) or [reddis](https://redis.io/).

Unfortunately, I don't have the expertise to say when to use an MQ verses memcache, but there are lots of articles on the internet discussing the pros/cons of each. I've used memcache and it works, but I believe for Celery they preffer MQ.

# The Difference Between IO and CPU Bound Process

* An IO bound process is like getting data from a URL, or writing a file

* A CPU bound process is like a big calculation like matrix inversion, a search routine, or optimization/minimzation problem

IO bound processes use Threads because threads do not block IO bound processes - IE: you can start an IO process in a thread and execution will continue to the next line unless you tell Python to wait. AsyncIO and Trio probably use threading in the background, IDK for sure.

CPU bound processes use MP, because they need their own core to do their stuff. But unfortunately there is a lot of overhead with MP, and so the calculation needs to be really expensive to make it worthwhile.

There's no limit to the number of threads you can create, but the number of MP processes is limited to the number of cores.

These rules don't apply to distributed computing, and they may not apply in other computing languages either. IE: you can distribute both IO and CPU tasks to a task queue across a cluster. However, there may be task managers that are better suited for different types of tasks. EG: [Dask](https://dask.org/) is probably better for distributed computing of CPU intense processes. But honestly, IDK, I'm at the edge of my personal research and experience here, and so I would probably recommend a little more exploration ...

# Python Global Interpreter Lock

The reason there's this difference between IO/CPU and threads/processes in Python specifically, and perhaps not other languages, is because Python is single threaded by default due to the [Global Interpreter Lock or GIL](https://wiki.python.org/moin/GlobalInterpreterLock). Other languages may or may not have similar design, IDK, however Python C-API does let you explicitly [release the GIL](https://docs.python.org/3/c-api/init.html#thread-state-and-the-global-interpreter-lock) and manage threads manually. This is what packages like [NumPy/SciPy](https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html) and [CPython](https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html) do.