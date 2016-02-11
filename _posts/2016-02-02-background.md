---
layout: post
title: Background
---

## Motivation

While exploring armature building in Blender, I wondered whether there was an easy way to mirror bone constraints from one side of my human rig to the other. I did find two scripts that contained clues.

The first was the response by prolific Stack Exchange user TLousky to [this question](http://blender.stackexchange.com/questions/41709/how-to-copy-constraints-from-one-bone-to-another) about copying constraints on bones used to control facial shape keys. The script ran all right on my armature, but doesn't adjust the constraint parameters in the way I need for a body rig.

The other result was a Blender add-on called [Pose Mirror](https://developer.blender.org/T36334) by Connor Simpson. It looks as though it copies all the constraints and parameters, making no changes, unless the constraint has a target, in which case it does switch the target to the corresponding object on the correct side.

Neither of the above scripts properly mirrors the Limit Rotation constraints that my human rig is full of, so I decided to look into writing something myself. This work-in-progress is called [blender-rig-mirror](https://github.com/clutterstack/blender-rig-mirror). Check the README for its current state; as of this writing it's not a polished product.

## First steps

### Reading
With some rusty Python at my disposal, my main concern was getting a foothold on the Blender/Python API. Luckily there's a lot of information in the [API docs](https://www.blender.org/api/blender_python_api_current/). The [Quickstart Introduction](https://www.blender.org/api/blender_python_api_current/info_quickstart.html) and the [Python API Overview](https://www.blender.org/api/blender_python_api_current/info_overview.html) are well worth skimming before starting, and referring back to after playing with some commands.

There is quite an illuminating [Gotchas](https://www.blender.org/api/blender_python_api_current/info_gotcha.html) section in the API docs, with [essential reading](https://www.blender.org/api/blender_python_api_current/info_gotcha.html?highlight=gotcha#editbones-posebones-bone-bones) on dealing with armatures and their properties.

### Scripting within Blender

Blender's developers have given a lot of effort and thought into making scripting accessible through features of the interface:

* There are **Text Editor** and **Python Console** modes available for the window panels ("[Areas](https://www.blender.org/manual/interface/window_system/arranging_areas.html)").

* The default **Info** mode of the top area, if expanded a little, shows recent commands executed through the GUI.

* Hovering over buttons in the GUI pops up not only a standard tooltip, but also the relevant Python operator or attributes.

* Where appropriate, options **Copy Data Path**, **Edit Source**, **Online Manual**, and **Online Python Reference** (targeted to the relevant entries) are available through the button's right-click context menu.

Commands can be entered directly into the Python console (which I placed in the top area of the default layout, in place of the **Info** panel). Scripts can be run from a text editor panel within Blender, but I find it more comfortable to use a standalone text editor like GitHub's [Atom](atom.github.io) (or see the [Wikipedia entry](https://en.wikipedia.org/wiki/Atom_(text_editor)). In this case it's convenient to enter the following in the console:

```
filename = "/full/path/to/myscript.py"
```

```
exec(compile(open(filename).read(), filename, 'exec'))
```

The above is found in the [Tips and Tricks](https://www.blender.org/api/blender_python_api_current/info_tips_and_tricks.html) section of the current docs; it's worth looking into every link under the [Blender/Python Documentation](https://www.blender.org/api/blender_python_api_current/contents.html#blender-python-documentation) heading!

To re-run the script, the `exec ...` line is run again (the console keeps a history, so you can up-arrow to get it quickly).

One final technical note: The [`dir([object])`](https://docs.python.org/3/library/functions.html#dir) Python command is really useful to see what attributes an object has, when you're navigating what you can and can't do in the API.

### Finally starting a script

I began by building a simple one-sided partial armature to test my code on: a spine, a detached clavicle, and a left arm. I saved the .blend file so the original can be recovered after the script messes with it. **Tip:** Save the file after entering the `filename ...` and `exec` line into the Python console (you may have to undo some changes made by the script if there's anything in it already), and these commands will be available in the console history when you reload.

Once the Python script imports Blender's [`bpy`](https://www.blender.org/api/blender_python_api_current/bpy.data.html) module:

```
import bpy
```

it's ready to go. Commands that can be entered into the console can just as easily be run from the .py file. Because I was still feeling my way around, I played around with commands, in a combination of one-liners in the console and cumulative actions in the script file. It's quite satisfying watching even the simplest changes happening to an object in the 3D view as a result of a typed command.

Soon, the script began doing some of the things I want my add-on to do. At the time of writing, it doesn't do everything, and it's not in add-on format yet.

### Licensing

Once I seemed to be making some progress, I wanted version control. GitHub provides this as well as a way to share the project, so I put the script up, after getting side-tracked researching the [GNU Public License (GPL)](https://en.wikipedia.org/wiki/GNU_General_Public_License). I've used a variety of GPLed software for years, but have never been in the position of deciding on a license for something I've written and want to share. In this case, if I want to distribute an add-on to work with Blender, it [has to be released under the GPL](https://www.blender.org/support/faq/), so I don't have a decision to make in this case.

Incidentally, from my reading on the topic of licensing and copyright, it appears to me that there's some scope to define best practices
around attributing portions of code written by different authors. Currently it looks pretty difficult and inconsistent.
