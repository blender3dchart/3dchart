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

import bpy
from bpy.types import Operator

class chart_input(Operator):
    bl_idname = "mesh.3dchart"
    bl_label = "3D Chart Data Input"

    text: bpy.props.StringProperty(name="Paste chart content:")

    def execute(self, context):
        bpy.types.WorkSpace.status_text_set("3D chart ok")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
