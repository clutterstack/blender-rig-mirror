---
layout: post
title: Background
---

# Motivation

While exploring armature building in Blender, I searched for an easy way to mirror bone constraints from one side of the rig to the other. There are two easy-to-find candidates.

The first I hit upon was the response by prolific Stack Exchange user TLousky to [this question](http://blender.stackexchange.com/questions/41709/how-to-copy-constraints-from-one-bone-to-another) about copying constraints on bones used to control facial shape keys. The script ran all right on my armature, but some of the constraint parameters were not as I'd expect for my humanoid body rig and constraints.

The other result was a Blender add-on called [Pose Mirror](https://developer.blender.org/T36334) dating from 2013 by Connor Simpson. It looks as though it copies all the constraints and parameters, making no changes, unless the constraint has a target, in which case it does switch the target to the corresponding bone on the correct side. I haven't tested this aspect.

Neither of the above scripts takes the pain out of mirroring the Limit Rotation constraints that my human rig is full of, so I decided to look into writing something myself.

# First steps

## Reading
With some rusty Python at my disposal, my main concern was getting a foothold on the Blender/Python API. Luckily there's a lot of information in the [API docs](https://www.blender.org/api/blender_python_api_current/). The [Quickstart Introduction](https://www.blender.org/api/blender_python_api_current/info_quickstart.html) and the [Python API Overview](https://www.blender.org/api/blender_python_api_current/info_overview.html) are well worth skimming before starting, and referring back to after playing with some commands.

There is quite an illuminating [Gotchas](https://www.blender.org/api/blender_python_api_current/info_gotcha.html) section in the API docs, with [essential reading](https://www.blender.org/api/blender_python_api_current/info_gotcha.html?highlight=gotcha#editbones-posebones-bone-bones) on dealing with armatures and their properties.

## Scripting within Blender


Blender's developers have given a lot of effort and thought into making scripting accessible through features of the interface:

* There are **Text Editor** and **Python Console** modes available for the window panels ("[Areas](https://www.blender.org/manual/interface/window_system/arranging_areas.html)").

* The default **Info** mode of the top area, if expanded a little, shows recent commands executed through the GUI.

* Hovering over buttons in the GUI pops up not only a standard tooltip, but also the relevant Python operator or attributes.

* Where appropriate, options **Copy Data Path**, **Edit Source**, **Online Manual**, and **Online Python Reference** (targeted to the relevant entries) are available through the button's right-click context menu.

Commands can be entered directly into the Python console (which I placed in the top area of the default layout, in place of the **Info** panel). Scripts can be run from a text editor panel within Blender, but I find it more comfortable to use a standalone text editor like GitHub's [Atom](atom.github.io) (or see the [Wikipedia entry](https://en.wikipedia.org/wiki/Atom_(text_editor)). In this case it's convenient to enter the following in the console:
```
filename = "/full/path/to/myscript.py"
exec(compile(open(filename).read(), filename, 'exec'))
```

The above is found in the [Tips and Tricks](https://www.blender.org/api/blender_python_api_current/info_tips_and_tricks.html) section of the current docs; it's perhaps worth looking into every doc linked under the [**Blender/Python Documentation**](https://www.blender.org/api/blender_python_api_current/contents.html#blender-python-documentation) heading!

To re-run the script, the second line can be accessed from the console's history using the up arrow.

## Getting going on my script

I began by building a simple one-sided partial armature to test my code on: a spine, a detached clavicle, and a left arm. The chain of bones begins at the base of the spine, which is in the default orientation (*y* up, *z* forward, *x* to the right). I saved the .blend file so the original can be recovered after the script messes around with it.

Then I put the line
```
import bpy
```
at the top of an empty text file (which I saved with a .py extension), and started playing around with commands, in a combination of one-liners in the console and cumulative actions in the script file.
