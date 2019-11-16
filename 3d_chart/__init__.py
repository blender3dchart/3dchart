# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "3D Chart",
    "author": "Donald Wong",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "description": ("Generate 3D chart in one go"),
    "category": "Mesh"
}

def register():
    print("register 3d chart")


def unregister():
    print("unregister 3d chart")


if __name__ == "__main__":
    register()
    