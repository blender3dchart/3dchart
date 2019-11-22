# Copyright (C) 2019 Donald Wong
# 
# This file is part of Blender 3D Chart.
# 
# Blender 3D Chart is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Blender 3D Chart is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Blender 3D Chart.  If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    "name": "3D Chart",
    "author": "Donald Wong",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "description": ("Generate 3D chart in one go"),
    "category": "Mesh"
}

if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(operators)
else:
    import bpy
    from . import (ui, operators)

def register():
    bpy.utils.register_class(operators.chart_input)
    bpy.types.VIEW3D_MT_mesh_add.append(ui.menu_func_chart)

def unregister():
    bpy.utils.unregister_class(operators.chart_input)
    bpy.types.VIEW3D_MT_mesh_add.remove(ui.menu_func_chart)

if __name__ == "__main__":
    register()
    