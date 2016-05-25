---
layout: post
title: ! "Integrating a Python script with Blender, Part 2: Making the operator script into an addon"
---


We start with a script that can be run to register an operator in Blender, that can then be called up by name within the spacebar menu.

[here is an attempt at an internal link to an earlier post where I got to this starting point]({% post_url 2016-02-23-integrating-part-one %})

At the end of this post, the operator can be loaded from a file, using the Preferences pane, and it's loaded up each time Blender is started -- the operator is permanently available from the spacebar menu.

Putting a button or menu item for the operator into the GUI is left for later.

## Steps to make it visible in the add-ons Panel

Concisely put, at
[https://wiki.blender.org/index.php/Dev:Py/Scripts/Guidelines/Addons](https://wiki.blender.org/index.php/Dev:Py/Scripts/Guidelines/Addons):

>"To have your script show up in the Add-Ons panel, it needs to:
>
>    * be in the addons/ directory
>    * contain a dictionary called "bl_info"
>    * define register() / unregister() functions. "

These steps are also illustrated at [https://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html](https://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html).

### bl_info section

Add:

```
bl_info = {
    "name": "Rig Mirror",
    "category": "Rigging",
    "author": "Chris Nicoll",
    "version": (0, 1),
    "blender": (2, 76, 0)
}
```

to the top of the file.

A list of categories is available at https://wiki.blender.org/index.php/Dev:Py/Scripts/Guidelines/Addons.

A lot more items can go into the `bl_info` dict. Before any attempt to submit this add-on, I would check to see what else it needs.

### register/unregister

Add:

```
def register():
    bpy.utils.register_class(RigMirror)


def unregister():
    bpy.utils.unregister_class(RigMirror)
```
to the end of the file.

Often, after the `register()` and `unregister()` functions, example add-ons contain the lines:

```
if __name__ == "__main__":
    register()
```

A clear explanation for this is given at  https://wiki.blender.org/index.php/Dev:Py/Scripts/Cookbook/Code_snippets/Blender_add-ons :

> "The last lines makes it possible to run the script in stand-alone mode from the Text Editor window. Even if the end user will never run the script from the editor, it is useful to have this possibility when debugging."

## Put the python file in the addons directory

If you can find it (not trivial on Mac OSX). Not strictly necessary. I was able to pull my add-on up in the add-ons browser with "Install from file..." (and selecting my python file). I haven't actually moved the file from my development (and git) directory on my local machine.
