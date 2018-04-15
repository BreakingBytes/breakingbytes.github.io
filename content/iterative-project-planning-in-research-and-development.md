Title: Iterative Project Planning in Research and Development
Date: 2017-06-16 13:04:39
Category: Productivity
Tags: agile, kanban, scrum, development, research, time-management, project-managment, project-planning
Authors: Mark Mikofski
Summary: Iterative planning is a a successful strategy for research and development.

# Objectives and Scope
The purpose of this document is to outline a successful strategy for the optimal
preparation, execution and measurement of plans for open-ended research and
development projects. In particular this document demonstrates the effective use
of short-term iteration cycle planning commonly known as Agile, Scrum or Kanban
project management. It is important to note that the methods described in this
document are not applicable to projects which have well-known execution times
such as engineering, procurement and construction (EPC). Also while short-term
iteration cycle planning may work well for open-ended research questions, they
may be combined with traditional waterfall techniques in time-limited projects.

# Methods
In a nutshell, an iterative project plan has these major features:

## Mission
All projects should have a big giant overriding mission statement. This is what
you look at when you're really lost and trying to re-inspire your team. In other
words, this is what it's all about. For example a school projects mission might
be the following:

> To empower students to become agents of their own learning

## Goals or Objectives
In order to accomplish the mission, you need a few long-term, broad goals or
objectives that point out what direction you think you need to follow. Don't be
too specific here. Continuing the school environment example, some goals might
be the following:

* Engage students in STEAM
* Reinforce literacy in every interaction
* Create a strong sense of community

## Release Cycle
Pick a long-term time frame to work in, during which you hope to make progress
in the same direction as these goals. This is your "release cycle". For example
in a school setting the release cycle might be every three months.

## Milestones or Epics
Narrow down milestones for each of the broad goals that you think can be
accomplished during each release cycle. These milestones are sometimes called
"epics" or "projects"

## Iteration Cycle
Pick a short-term iteration cycle during which you can meet with your team and
measure progress on your "epics". Iteration cycles vary anywhere from weekly to
monthly, but a good compromise is every two weeks. This time-frame is your
"iteration" or "scrum" because you will often meet your group for a quick tally
kind of like a rugby scrum.

## Tasks
Brainstorm the detailed, small, atomic tasks that you think would be required to
complete the epics and put them on cards in a list called your backlog. There
are many online tools like [Trello](https://trello.com/) that are designed to
make this easy, but a large cork board works just fine. An atomic task is nearly
the smallest discreet unit of work you can think of that would need to be done
in order to accomplish the milestone. Tasks are easily measured, and it should
also be easier to predict the time necessary to complete them.

## Effort
Assign each card or task an effort score. Keep the scale small; think of it as a
rubric, not a linear scale, but it could loosely be proportional to time. A
common effort scale might be the following:

|Effort |Description |Approximate time|
|-------|------------|----------------|
|0 |chore |any known length of time|
|1 |easy  |< 1 day|
|2 |hard  |< 1 week|
|3 |mini-epic |> 1 week|

Usually a chore is a well-defined task that is done all the time so you know
exactly how long it takes. Just mark chores on your schedule and do them. A
mini-epic probably means you should break it into smaller tasks, but you may try
to do it as a single task anyway. Effort is used to measure progress; the data
is used to normalize and prioritize future iteration cycles. Since any data is
useful as long as it is carefully measured and calibrated, you may adjust your
effort scale to fit your needs after several iterations and releases.

### Kanban
Kanban, Scrum and Agile have many similarities. See this
[Smartsheet article for a side-by-side comparison](https://www.smartsheet.com/agile-vs-scrum-vs-waterfall-vs-kanban).
In a nutshell, Agile is a philosophy, while Scrum and Kanban are
implementations of Agile. Scrum introduces the concept of a sprint or interval
while Kanban introduces puts all tasks into lists or swimlanes on a board that
everyone can see and manipulate. IMO forget the names and concentrate of what
works best and is easiest to use. The goal is to be efficient and productive.

The simplest Kanban board can be divided into 3 swimlanes, which is the default
workflow for a new Trello board:

* To do (_aka_ backlog)
* Doing (_aka_ current work)
* Done (_aka_ completed work)

You can add more swimlanes to capture other items such as:

* wishlist, icebox or parking lot - items for a rainy day
* won't do - items ruled out
* in review - almost done
* on deck - in between backlog and current work

### Pomodoro
One aspect of an iterative workflow that can create anxiety is the measurement
of progress and the evaluation or prediction of the time to complete a task or
milestone. The
[Pomodoro Technique](https://cirillocompany.de/pages/pomodoro-technique) is a
time management method from the 1980's that provides a concrete conversion rate
between units of work and units of time. One pomodoro is typically equivalent to
30-minutes. Using the Pomodoro technique is a diagnostic tool that eliminates
the need to normalize burndown rates since converting between pomodoros and time
is not subjective.

#### Trello and Pomello
Trello is an online tool that offers a Kanban-esque board to organize tasks and
iterations. The [Pomello app](http://www.pomelloapp.com/) is a plugin for Trello
that integrates Pomodoro. It logs time on task, measures the number of pomodoros
spent on a task and lets you move completed tasks to their swimlane when done.

## Current Work (Option 1: Kanban)
This is my personal preference because IMO the workflow is much simpler since
there are only 3 swimlanes. I use this with the Pomodoro Technique. At the
beginning of each iteration, pull cards into the current work list and count
the number of pomodoros used on each. When a task is done, move it to the
"completed"  list and pull a new item from the backlog. That's it!

## Current Iteration (Option 2: Scrum)
Note this method won't work with Pomello, it's better to use
[Scrum for Trello](http://scrumfortrello.com/) and
[Burndown for Trello](https://www.burndownfortrello.com/).

At the beginning of each iteration cycle move some cards from the backlog into a
new list called your current iteration. Iterations may be numbered or identified
by date or work-week as long as they are recorded. You should assign individuals
or small teams to tasks and encourage frequent communication and collaboration
between individuals and teams during the iteration. During the iteration teams
and individuals should measure their progress by deducting points from the
initial effort of each task until they are complete and the remaining effort is
zero.

During the iteration communicate with your team frequently and make adjustments
as needed. For example, during an iteration you might do any or all of the
following:

* Take new cards from the back log as needed until the iteration is over.
* Reorder cards on the backlog or current iteration board to reprioritize.
* Choose tasks based on their estimated effort and the remaining time in the iteration.
* Reclassify a tasks as an epic and break it into to subtasks.
* Reassign individuals and teams to tasks.

### Burndown (Scrum)
At the end of the iteration, tally up the effort points completed, add it to the
previous total and divide by the total number of iterations. Plot this data for
everyone, for individuals, for all iterations cumulatively and for each
iteration. These are your burndown rates. Use them to normalize team members and
to determine how much effort can be accomplished per iteration.

#### Table 1: Example Effort per Iteration

|Iteration|Bobby|Sally|Juan|Briana|Effort|
|---------|-----|-----|----|------|------|
|1        |12   |4    |7   |10    |8.25  |
|2        |6    |6    |9   |11    |8     |
|3        |8    |5    |7   |9     |7.25  |
|4        |10   |3    |8   |7     |7     |

#### Table 2: Example Cummulative Effort

|Iteration|Bobby|Sally|Juan|Briana|Cummulative|
|---------|-----|-----|----|------|-----------|
|1        |12   |4    |7   |10    |8.25       |
|2        |18   |10   |16  |21    |16.25      |
|3        |26   |15   |23  |30    |23.5       |
|4        |36   |18   |31  |37    |30.5       |

#### Table 3: Example Burndown Calculation

|Iteration|Bobby|Sally|Juan|Briana|Average|
|---------|-----|-----|----|------|-------|
|1        |12   |4    |7   |10    |8.25   |
|2        |9    |5    |8   |10.5  |8.125  |
|3        |8.67 |5    |7.67|10    |7.83   |
|4        |9    |4.5  |7.75|9.25  |7.625  |

Looking at the burndown rates and cumulative effort you can make several
observations:

* Bobby and Briana are either the team’s top performers or are over estimating
  effort. Use this info to normalize the team by either using your own effort
  scale or pairing teammates together to see their joint effort estimates. For
  example if Briana is high performer, her burndown stands, and if Bobby’s
  performance is more equivalent to the team average then adjust it by a factor
  of around 85% to 7.65 instead of 9. Ditto for Sally if she is sandbagging her
  effort estimates, adjust hers by a factor of 1.7x to 7.65.
* Now that your burndown is normalized, the adjusted team average is around
  8 points of Effort per Iteration. Therefore you should only plan to add tasks
  summing up to around 32 effort points each iteration.
* If your iteration is half over, and Juan’s queue is empty, you can only expect
  him to deliver around 4 effort in the remaining time, so choose tasks summing
  up to this or less.

## Reprioritization
After calculating burndown your team can reprioritize tasks and epics, both in
response to data on progress but also due to a shift in the team mission and
associated objectives. Move incomplete tasks from the current iteration either
to epics because they were just too big to do in a single iteration, back to the
backlog because you over allocated effort or to a board called the “Icebox” or
“Parking Lot” to revisit on a rainy day.

## Release
At the end of the release, publish what you have. Report on it. Re-evaluate your
milestones and compare to your broad long term goals and your mission.  Adjust
your milestones as needed. Then celebrate!

# Examples
Here are some typical workflows and how you can set them up using Trello.

## Kanban
Just take the default Trello layout and start working. Put ideas that come up
into the backlog. Break them up into tasks as needed. Each week move some items
into the current work list. When an item is finished move it to the completed
list. Use the Pomello app to measure how many pomodoros they take, and use that
info to make predictions about when projects will get done. That's it!

## Scrum
One way to use Trello for Scrum is to set up 4 boards:

* Epics
* Backlog
* Current Iteration by date
* Icebox

Each iteration, I archive the old iteration and create a new iteration board
with the date. I move cards around all the time. I only assign effort to tasks
in the backlog which get dragged to the current iteration. I create links from
tasks to epics and vice-versa. I put lots of comments on the cards as I make
progress.

# Rationale
There are many arguments for using short-term iteration cycle planning. I will
list the major salient points here.

## Uncertainty is Hyperbolic
Research and development projects are inherently unknowns. There may be some
data that indicates around doing small isolated tasks, but predicting a string
of tasks and how they will proceed from one another is not possible because as
predictions move out of the data centroid and extrapolate to larger projects and
longer time-frames the uncertainty explodes hyperbolically. Therefore better
predictions can only be made close to the data centroid centered on small atomic
tasks.

## Humans are Meta Cognitively Wired
Meta cognition is understanding about how we think, and we know a lot about how
we think we work.

### We get a rush from checking off tasks. (Dopamine)
Using iterative project planning with shorter term iterations allows
contributors to feel more sense of accomplishment because they complete more
tasks, they receive recognition for completed work and have a clear sense of
expectations because data is explicit and meaningful. The feeling comes from
dopamine released each time we tick off a task.

### We dislike wasted effort. (Endorphins)
Only tasks are S.M.A.R.T.  Milestones, objectives and mission statements are
only loosely structured allowing teams to concentrate on the task at hand. By
spending less time planning out long-term objectives teams feel a strong sense
of purpose. Nothing is more aggravating than spending a long time planning
something only to have it switched around completely halfway through it. This
frustration leads ultimately to burnout and dysfunction. The corollary to this
is the excitement and morale boost of diving into work quickly and quickly
scoring small victories. Even a few small failures here are seen as positive
data toward the correct course of action because there isn’t a lot riding on
them. Working hard releases endorphins, which soothes anxiety and makes us feel
accomplished. A lack of endorphins however leads to anger and stress.

### We are more productive when we feel self-directed and that our work has purpose. (Serotonin)
Iterative project planning allows teams to be more productive with less oversite
since they participate in creating tasks and their current workload by taking
tasks from the backlog. Also by leverage Agile project management software to
organize tasks in iterations and calculate burndown, companies can allow
management to focus on the “Big Picture” giving the entire organization a
stronger sense of unity and focus. This sense of purpose and self-value comes
from serotonin released as we partake in planning our own work.

### We like to work in groups. (Oxytocin)
Iterative project planning is inherently designed for groups. Working together
on a project build trust intimacy and ultimately synergy which multiply
productivity. Understanding and valuing each other’s strengths and weaknesses
makes us closer even in a professional setting. This releases oxytocin which
makes us feel appreciated and loved.

# Conclusion
IMHO iterative project planning is a no brainer for any research and development
group. It increases productivity while reducing costs by leveraging more
individual contributors and sharing leadership.

# Links
Wikipedia Articles and Perspectives:

* [Optimize for tiny victories - Scott Hanselman](http://www.hanselman.com/blog/OptimizeForTinyVictories.aspx)
* [Agile is dead - Pragma Dave](https://pragdave.me/blog/2014/03/04/time-to-kill-agile.html)
* [Agile Mangement](https://en.wikipedia.org/wiki/Agile_management)
* [Agile Software Development](https://en.wikipedia.org/wiki/Agile_software_development)
* [Scrum (software development)](https://en.wikipedia.org/wiki/Agile_software_development)
* [Kanban (development)](https://en.wikipedia.org/wiki/Kanban_(development))

Online Tools:

* [Trello planning tool](https://trello.com/markmikofski/recommend)
* [Pomello app](http://www.pomelloapp.com/)
* [scrumfortrello](http://scrumfortrello.com/)
* [burndownfortrello](https://www.burndownfortrello.com/)
* [ganttify for Trello](https://gantt-chart.com/)
* [Pivotal Tracker](https://www.pivotaltracker.com/)
* [Redbooth](https://redbooth.com/)
