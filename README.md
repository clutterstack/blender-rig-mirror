# blender-rig-mirror
**Unfinished** addon to create a full armature from a one-sided half-armature in Blender.

## Current features

This script currently assumes:

* The centre-line bones plus (only) all the bones you want to mirror have been created (it does skip any bone whose mirror-complement name is held by an existing bone).
* The rig is meant to be symmetric across the *y-z* plane (along the *x* axis).

From these starting data, it does the following for each bone not on the armature's plane of symmetry:

* Creates a new bone with the same root name as the one it's copied from, and adds a suffix to indicate the side it's on (See **Bone naming** for more detail).

* The builtin Blender operator [`bpy.ops.armature.symmetrize()`](https://www.blender.org/api/blender_python_api_current/bpy.ops.armature.html?highlight=symmetrize#bpy.ops.armature.symmetrize) is used to accomplish the following:

  * Sets the new bone's head and tail positions to mirror the original bone's position and orientation.
  * Sets the new bone's roll to mirror the roll of the complementary bone on the original side.
  * Sets the new bone's parent to be the mirror complement of the original bone's parent; if the original's parent is along the centre line of the armature, this is the new bone's parent as well.
  * Copies bone constraints from the original side of the armature to the other. This includes IK constraints, which are copied with targets on the appropriate side of the rig. At this point in the operation of the script, Limit Rotation and Limit Location constraints (and possibly other types) have identical limits on both sides, rather than being mirrored, which would be the desired behaviour in this context.


* Changes limits on Limit Rotation and Limit Location constraints so that these constraints are mirrored across the armature's plane of symmetry.


## Bone naming

The script is sophisticated enough to check for a ".L", ".l", ".R", or ".r" suffix on the off-axis bones. If it finds one of these, it will give the new bone's name the appropriate "opposite-side" suffix. For example, if the original bone names end in ".L", the new ones will end in ".R".

If there is no such suffix on the original off-centre bone names, the script checks on which side of the *y-z* plane the bone ends (where its tail is located) and gives it either a ".L" or a ".R" name ending.

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
