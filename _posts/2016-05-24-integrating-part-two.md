---
layout: post
title: ! "Integrating a Python script with Blender, Part 2: Making the operator script into an add-on"
---

I'm picking up where I left off after [this post](http://clutterstack.github.io/blender-rig-mirror/2016/02/23/integrating-part-one.html): with a script that can be run to register an operator in Blender, that can then be called up by name ("Rig Mirror") within the spacebar menu.

At the end of this post, the script will be in basic add-on form.
It will be installed from a file, using the User Preferences Add-ons pane, and it's loaded up each time Blender is started -- the operator is permanently available from the spacebar menu.

## Steps to make the add-on visible in the add-ons panel

From
[the Blender wiki add-on guidelines](https://wiki.blender.org/index.php/Dev:Py/Scripts/Guidelines/Addons):

>"To have your script show up in the Add-Ons panel, it needs to:
>
>    * be in the addons/ directory
>    * contain a dictionary called "bl_info"
>    * define register() / unregister() functions. "

These steps are also illustrated in a [tutorial in the Blender Python API docs](https://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html), which is more of a demonstration than a reference, though useful.

### bl_info dictionary

Add the dict:

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

The [guidelines](https://wiki.blender.org/index.php/Dev:Py/Scripts/Guidelines/Addons) contain a useful reference for the possible contents of `bl_info`, as well as more on preparing an add-on for submission to the Blender Foundation.


### register()/unregister() functions

Add:

```
def register():
    bpy.utils.register_class(RigMirror)


def unregister():
    bpy.utils.unregister_class(RigMirror)
```
to the end of the file. `RigMirror` is the name of my operator class.

Often, after the `register()` and `unregister()` functions, example add-ons contain the lines:

```
if __name__ == "__main__":
    register()
```

A clear explanation for this is given at  https://wiki.blender.org/index.php/Dev:Py/Scripts/Cookbook/Code_snippets/Blender_add-ons :

> "The last lines makes it possible to run the script in stand-alone mode from the Text Editor window. Even if the end user will never run the script from the editor, it is useful to have this possibility when debugging."

## Put the python file in the addons directory

The addons directory is a bit hard to find on my OSX (Yosemite) machine, since it's at `/Users/chris/Library/Application Support/Blender/2.76/scripts/addons`, and for some reason the Library folder is hidden from users by default.

Although it's not too hard to unhide the Library (see, *e.g.* [this thread at Blender Artists](http://blenderartists.org/forum/showthread.php?331685-Adding-Addons-To-Mac)), it's not strictly necessary here. In the add-ons browser, I used "Install from file..." (selecting my python file from my development directory) and Blender put a copy of it into the addons folder.

That's it; my script has been converted to an installable operator. An obvious next step would be to add a button or menu item for the operator to Blender's GUI.
