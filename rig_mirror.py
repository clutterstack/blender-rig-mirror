# rig_mirror.py: intended to automatically complete an armature
# beginning with one half of an armature. NOT COMPLETE!
# SEE README for updates as to functionality.

#  ***** BEGIN GPL LICENSE BLOCK *****
#
# Copyright (C) 2016 Chris Nicoll zeta@chrisnicoll.net
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#  ***** END GPL LICENSE BLOCK *****

import bpy

# Constant stuff

# Dict of complementary name suffixes.
suffixes = {".L":".R", ".R":".L", ".l":".r", ".r":".l"}

#Helper functions

def fixnames(old_bone):
    # Check for a pre-existing symmetry suffix on the original bones.
    prefix = old_bone.name[:-2]
    suffix = old_bone.name[-2:]

    new_suffix = suffixes.get(suffix)
    #if new_suffix != None: print(new_suffix)
    if new_suffix == None:
        print("No side indication found in name")
        # Assume it's the lhs that's been constructed even if not labelled
        prefix = old_bone.name
        old_bone.name = prefix + ".L"
        new_suffix = ".R"

    new_name = prefix + new_suffix
    print(old_bone.name)
    print(new_name)
    return new_name


def main():

    # Get the active object's name (the armature we're working on, one hopes)
    # Check that the active object is indeed an armature:
    if bpy.context.active_object.type == 'ARMATURE':
        # make sure we're in edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        # deselect all bones in the armature
        bpy.ops.armature.select_all(action='DESELECT')
        bone_collection = bpy.context.object.data.edit_bones
        mylength = len(bone_collection)
        # Only want to copy bones that aren't at x=0 (rel to armature origin)
        for old_bone in bone_collection[0:mylength]:
            print("bone head (x,y) is (" + str(old_bone.head[0]) + "," + str(old_bone.head[1]) + ")")
            if not (old_bone.head[0] == old_bone.tail[0] == 0):
                print(old_bone.name + " is not on the armature's line of symmetry so copy and rename it.")

                # Add the new bone with the name mirrored
                new_bone_name = fixnames(old_bone)
                bone_collection.new(new_bone_name)
                new_bone = bpy.context.object.data.edit_bones[new_bone_name]

                # Set this bone's position.
                new_bone.head = Vector((-old_bone.head[0], old_bone.head[1], old_bone.head[2]))
                new_bone.tail = Vector((-old_bone.tail[0], old_bone.tail[1], old_bone.tail[2]))
                #new_bone.select = True

                # Set its roll to negative (x-mirror) of the original's.
                new_bone.roll = -old_bone.roll

        bpy.context.scene.update() # To show what we've done in the viewport

    else: print("The active object isn't an armature.")

main()
