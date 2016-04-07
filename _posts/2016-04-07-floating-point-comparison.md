---
layout: post
title: "Finding bones at the centre of the rig: a rookie mistake comparing floating-point numbers"
---

It appears that the builtin Blender armature symmetrize operation `bpy.ops.armature.symmetrize()` does most of what I wanted to do, so I started a new git branch replacing bits of my own code with that. The builtin mirrors constraints, including IK constraints, very well. It means a lot less code than I expected to have to write.

The builtin looks for side-indicating name extensions to decide which bones to copy, and gives the new bones corresponding, mirrored names matching the format the original names had, which is nice. `Armbone.L` ends up with a mirror twin `Armbone.R`, and so on.

My code checks for bones that aren't on the centre line and gives their names extensions ".L" or ".R" depending upon the location of the bone tail (where the bone "ends").

With my simple test armature, everything looked fine. The centre bones were recognized as being at the centre and so weren't mirrored, and everything else was.

When I loaded a more complicated full-human rig, the centre bones were renamed and duplicated, despite the fact that I'd set their heads and tails all to x=0.

I don't know what was the difference between my two test rigs, but I do know that comparing floating-point numbers can be dangerous, so instead of checking that the bones are lined up at exactly *x = 0*, the code now checks that they're within some small distance 'epsilon' of *x = 0*. This has solved the problem.

Specifically, I changed:

```
side_bones = [bone for bone in bone_collection if not (bone.head[0] == bone.tail[0] == 0)]
```

to

```
side_bones = [bone for bone in bone_collection if not (bone.head[0] < epsilon and bone.tail[0] < epsilon)]
```

I set `epsilon = 0.00001` and this seems to work fine.
