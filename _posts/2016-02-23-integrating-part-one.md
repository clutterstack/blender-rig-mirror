---
layout: post
title: Integrating a Python script with Blender, Part 1
---

Some exploration of the Blender Python API has left me with a working (though not fully-featured) script. Rather than carry on building and debugging as it is, I want to make sure my code is structured in such a way that it won't be a mess to convert to a Blender Add-on.

At this point I'm going through the minimal process for writing and registering an operator that can be called from within Blender. Creating a proper add-on requires a few more steps, which will be addressed at another time.

Most of the information in this post comes from the [Operator(bpy_struct)](https://www.blender.org/api/blender_python_api_current/bpy.types.Operator.html) page of the API docs.

### Defining a subclass of `bpy.types.Operator`:

After `import bpy`, everything that was in the original Python script now goes into the definition of a new class inheriting from `bpy.types.Operator`. Some rearrangement will be needed, which is described below.

```
class RigMirror(bpy.types.Operator):
```

The parent class `bpy.types.Operator` takes care of providing variables and methods to allow operator subclasses like my new `RigMirror` class to interface with Blender.

Next some class properties are needed:


~~~
  bl_idname = "object.rig_mirror"

  bl_label = "Rig Mirror" # Human friendly name

  bl_options = {'REGISTER', 'UNDO'} # Enables undo.
~~~


`bl_idname` sets the name that can be used in code to call the operator -- its "real" name. It's an object operator so its `bl_idname` starts with `object.`.

`bl_label` sets the human-friendly name we can find, for example, in the spacebar search dropdown once the operator is registered with Blender.

`bl_options`: by default this is a set containing only `'REGISTER'` ([docs](https://www.blender.org/api/blender_python_api_current/bpy.types.Operator.html?highlight=bl_options#bpy.types.Operator.bl_options)), so we don't absolutely need this line. I'll throw the `'UNDO'` straight in there, having come across it in the [Addon Tutorial](https://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html).

More properties can be set here, but these are all we need for the moment.

In my script, I had a dictionary (`suffixes`) containing suffix mappings for bone names, as well as a `main()` function and several helper functions. All this stuff goes inside the class definition.

To fit them into the form of an operator class, I made the following adaptations in accordance with the [Operator(bpy_struct)](https://www.blender.org/api/blender_python_api_current/bpy.types.Operator.html) page:

* Renamed `main()` to `execute(self, context)` and gave it the return value `FINISHED` -- actually, a set containing only `'FINISHED'`.

* As pointed out in the [Addon Tutorial]((https://www.blender.org/api/blender_python_api_current/info_tutorial_addon.html), the context is passed to the `execute()` method, so `bpy.context.` inside the method becomes simply `context.`

* Since my functions are now methods defined within the class, calls to them need `self.` at the start.

The operator class is now defined, and will be easy to add functionality to, without making a mess.

### Registering and running the new operator

After the class definition, there are just a couple more lines to add to the file. Before it can be accessed from Blender, the operator must be registered, like so:

```
bpy.utils.register_class(RigMirror)
```

And finally, to save steps while I'm still heavily modifying and testing the script, get it to call the operator when run:

```
bpy.ops.object.rig_mirror()
```

Now the script does exactly the same thing as it did before, except that (i) the operator remains available from within Blender, by typing in 'Rig Mirror' in the spacebar search field, and (ii) it will be a lot simpler to convert it into an add-on when the time comes.

I will keep it in this form for the moment, since it is about to undergo some considerable changes in and it's simple to re-run it for testing.
