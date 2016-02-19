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

class RigMirror(bpy.types.Operator):

    bl_idname = "object.rig_mirror"
    bl_label = "Rig Mirror" # Human friendly name
    bl_options = {'REGISTER', 'UNDO'} # Enable undo


    # Dict of complementary name suffixes.
    suffixes = {".L":".R", ".R":".L", ".l":".r", ".r":".l"}

    def execute(self, context):

        # Get the active object's name (the armature we're working on, one hopes)
        # Check that the active object is indeed an armature:
        if context.active_object.type == 'ARMATURE':

            # Initialize an empty list to hold the names of created bones.
            new_bone_names = []

            # Make sure we're in edit mode
            bpy.ops.object.mode_set(mode='EDIT')
            # Deselect all bones in the armature
            bpy.ops.armature.select_all(action='DESELECT')
            bone_collection = context.object.data.edit_bones
            #numbones = len(bone_collection)

            side_bones = [bone for bone in bone_collection if not (bone.head[0] == bone.tail[0] == 0)]

            self.rename_old_bones(side_bones)

            # Stop if there are already any bones matching names we will give to new bones;
            # this may mean that the armature is already symmetric, or some other complication.
            if self.check_name_conflict(side_bones) == False:

                '''At this point can use bpy.ops.armature.symmetrize() in edit mode with all bones selected.'''
                # Select all bones. This assumes there's only a half armature. So did the code I wrote before.
                bpy.ops.armature.select_all(action='SELECT')
                bpy.ops.armature.symmetrize()
                context.scene.update() # To show what we've done in the viewport

                # At this point, I think we need to go to pose mode and loop again.

        else: print("The active object isn't an armature.")
        return {'FINISHED'}

    # Helper function(s)
    def rename_old_bones(self, existing_bones):
        '''If a bone's head is at x <>0, and its name has no side indicator,
        this function will give it a .L or .R ending'''
        for bone in existing_bones:
            suffix = bone.name[-2:]
            new_suffix = self.suffixes.get(suffix)
            if not new_suffix: # i.e. wasn't one of the dict keys
                #print("No side indication found in name")
                # Assume it's the lhs that's been constructed even if not labelled
                print("Bone " + bone.name + " didn't have a .L/.l or .R/.r suffix")
                prefix = bone.name
                if bone.head[0] > 0: # bone head is on the LHS
                    bone.name = prefix + ".L"
                elif bone.head[0] < 0: # bone head is on the RHS
                    bone.name = prefix + ".R"


    def check_name_conflict(self, existing_bones):
        '''Checks all the names we want to use for mirrored bones against
        existing bone names.'''
        bone_names = [bone.name for bone in existing_bones]
        for bone in existing_bones:
            if self.get_mirrored_name(bone) in bone_names:
                print("There is a naming conflict with an existing bone")
                return True
            else:
                print("No naming conflict")
                return False

    def get_mirrored_name(self, bone):
        prefix = bone.name[:-2]
        suffix = bone.name[-2:]
        new_suffix = self.suffixes.get(suffix)
        if new_suffix:
            mirrored_name = prefix + new_suffix
            return mirrored_name
        else:
            print("The original bone doesn't have a side suffix")

# Register the operator class so it can be used in Blender
bpy.utils.register_class(RigMirror)

# Run it
bpy.ops.object.rig_mirror()
