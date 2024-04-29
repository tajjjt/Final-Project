import bpy



def main(context):
    def backlightleft():
    
        bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(-1.33342 , 3.24229, 1.5945), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = -1.36788
        bpy.context.object.rotation_euler[2] = 0.57011
        bpy.context.object.data.energy = 120

    
    def backlightright():
        
        bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(0.523435 , 0.9104 , 1.44934 ), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = -1.71757
        bpy.context.object.rotation_euler[1] = -0.218545
        bpy.context.object.rotation_euler[2] = 5.72786
        bpy.context.object.data.energy = 120

    def Frontlightright():
        bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(0.673029  , -2.19193  , 1.72635), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 1.30364
        bpy.context.object.rotation_euler[1] = 0.105826
        bpy.context.object.rotation_euler[2] = 0.237859
        bpy.context.object.data.energy = 113.3
     
    def frontlightleft():
        bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(-0.610189  , -2.79623  , 1.76133), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 1.30364
        bpy.context.object.rotation_euler[1] = 0.105826
        bpy.context.object.rotation_euler[2] = -0.28563
        bpy.context.object.data.energy = 113.3

    def runall():
        backlightleft()
        backlightright()
        Frontlightright()
        frontlightleft()
        
    runall()
    
class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()


#Panel
class VIEW3D_CustomPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    #labels
    bl_label = "Lighting label"
    bl_category = "Studio lights"
    
    def draw(self,context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("object.simple_operator", text = "Add lights")
    
        
#register in blender
def register ():
    bpy.utils.register_class(VIEW3D_CustomPanel)
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_CustomPanel)

if __name__ == "__main__":
    register()