# blender-rig-mirror
**Unfinished** addon to create a full armature from a one-sided half-armature in Blender.

## Current features

**The blender-rig-mirror script currently doesn't set up any constraints on the new bones.**

This script currently assumes:

1. The centre-line bones plus (only) all the bones you want to mirror have been created.
2. The rig is meant to be symmetric across the *y-z* plane (along the x axis).

From these starting data, it does the following for each bone not on the armature's plane of symmetry:

1. Creates a new bone with the same root name as the one it's copied from, and adds a suffix to indicate the side it's on (See **Bone naming** for more detail).
2. Sets the new bone's head and tail positions to mirror the original bone's position and orientation.
3. Sets the new bone's roll to mirror the roll of the complementary bone on the original side.
4. Sets the new bone's parent to be the mirror complement of the original bone's parent; if the original's parent is along the centre line of the armature, this is the new bone's parent as well.

## Bone naming

So far, the script is sophisticated enough to check for a ".L", ".l", ".R", or ".r" suffix on the off-axis bones. If it finds one of these, it will give the new bone's name the appropriate "opposite-side" suffix. For example, if the original bone names end in ".L", the new ones will end in ".R".

If there is no such suffix on the original off-centre bone names, the script checks which side of the *y-z* plane the bone originates (where its head is located) and gives it either a ".L" or a ".R" name ending.

If any bones exist with names that conflict with the names it plans to give to mirrored bones, the script will not continue.

## Running this script

While this is still just a script and not an addon, it can be run using

```
filename = "/full/path/to/blender-rig-mirror.py"
```

```
exec(compile(open(filename).read(), filename, 'exec'))
```

in Blender's Python console (from https://www.blender.org/api/blender_python_api_current/info_tips_and_tricks.html).
