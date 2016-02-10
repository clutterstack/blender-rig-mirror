---
layout: post
title: Background
---

# Motivation

While exploring armature building in Blender, I searched for an easy way to mirror bone constraints from one side of the rig to the other. There are two easy-to-find candidates.

The first I hit upon was the response by prolific Stack Exchange user TLousky to [this question] (http://blender.stackexchange.com/questions/41709/how-to-copy-constraints-from-one-bone-to-another). The script ran all right on my armature, but some of the constraint parameters were not as I'd expect for my rig and my constraints. This script was posted in response to a question about constraints on bones used to control shape keys, so it's worth checking out for that use case.

The other result was a Blender add-on called [Pose Mirror](https://developer.blender.org/T36334) dating from 2013 by Connor Simpson. It looks as though it copies all the constraints and parameters, making no changes, unless the constraint has a target, in which case it does switch the target to the corresponding bone on the correct side. I haven't tested this aspect.

Neither of the above scripts takes the pain out of mirroring the Limit Rotation constraints that my human rig is full of, so I decided to look into writing something myself.

# First steps

## Reading
With some rusty Python at my disposal, my main concern was getting a foothold on the Blender/Python API. Luckily there's a lot of information in the [API docs](https://www.blender.org/api/blender_python_api_current/). The [Quickstart Introduction](https://www.blender.org/api/blender_python_api_current/info_quickstart.html) and the [Python API Overview](https://www.blender.org/api/blender_python_api_current/info_overview.html) are well worth skimming before starting, and referring back to after playing with some commands.

There is quite an illuminating [Gotchas](https://www.blender.org/api/blender_python_api_current/info_gotcha.html) section in the API docs, with [essential reading](https://www.blender.org/api/blender_python_api_current/info_gotcha.html?highlight=gotcha#editbones-posebones-bone-bones) on dealing with armatures and their properties.

## Scripting within Blender


Blender's interface makes a lot of effort to be friendly to those wanting to try scripting:

* There are text editor and Python console modes available for the window panels ("[Areas](https://www.blender.org/manual/interface/window_system/arranging_areas.html)").

* The default "Info" mode of the top area, if expanded a little, shows recent commands executed through the GUI.

* Hovering over buttons in the GUI pops up not only the usual explanation of the button's action, but also the relevant Python operator or attributes.

* Where appropriate, the context-aware options `Copy Data Path`, `Edit Source`, `Online Manual`, and `Online Python Reference` (targeted to the relevant entries) are available through the button's right-click context menu.

Where appropriate, it gives the option to the option of copying the text of the attribute, and also of opening (and editing if you wish) the source code for the relevant module!



In the default Blender layout, the top panel shows

I began by building a one-sided partial armature: just a spine, a detached clavicle and an arm. I saved this as a .blend file for easy access.
