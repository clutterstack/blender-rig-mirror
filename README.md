# blender-rig-mirror
**Unfinished** addon to create a full rig from half a rig

## Current features

**The blender-rig-mirror script currently doesn't set up any parenting or any constraints on the new bones, so can't be considered particularly useful relative to mirroring the armature during creation.**

This script currently assumes:

1. The centre-line bones plus (only) all the bones to one side of the armature have been created.
2. The rig is meant to be symmetric across the y-z plane (along the x axis).

From these starting data, it does the following for each bone not on the armature's plane of symmetry:

1. Creates a new bone with the same root name as the one it's copied from, and adds a suffix to indicate the side it's on (See **Bone naming** for more detail).
2. Sets the new bone's head and tail positions to mirror the original bone's position and orientation.
3. Sets the new bone's roll to mirror the roll of the complementary bone on the original side.
4. Sets the new bone's parent to be the mirror complement of the original bone's parent; if the original's parent is along the centre line of the armature, this is the new bone's parent as well.

## Bone naming

So far, the script is sophisticated enough to check for a ".L", ".l", ".R", or ".r" suffix on the off-axis bones. If it finds one of these, it will give the new bone's name the appropriate "opposite-side" suffix. For example, if the original bone names end in ".L", the new ones will end in ".R".

If there is no such suffix on the original bone names, the script currently assumes the bones are on the armature's left-hand side (positive x) and will add ".L" suffixes to their names, then give the new bones ".R" suffixes.

## Running this script

From https://www.blender.org/api/blender_python_api_2_59_2/info_tips_and_tricks.html (didn't find it in the newest API pages but it still works for me in Blender 2.76 on Mac OSX):
While this is still just a script and not an addon, it can be run using

```
filename = "/full/path/to/blender-rig-mirror.py"
exec(compile(open(filename).read(), filename, 'exec'))
```
in the Blender Python console.
