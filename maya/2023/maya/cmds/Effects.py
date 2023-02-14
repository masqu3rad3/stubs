from typing import Union, Optional, List, Tuple

def addDynamic(*args):
    """
    Makes the "object" specified as second argument the source of an existing field or emitter specified as the first argument. In practical terms, what this means is that a field will emanate its force from its owner object, and an emitter will emit from its owner object.

    Args:
    """
    pass


def addPP(*args, attribute: Optional[Union[str, bool]] = str):
    """
    Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an attribute of an emitter or field.  The -atr flag identifies the attribute.  If no attribute is named, addPP returns a warning and does nothing.

    Args:
        attribute: (create) - Name of attribute to which you wish to add PP capability. Currently the only attribute supported is rate (for emitters).
    """
    pass


def air(*args, attenuation: Optional[Union[float, bool]] = float, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, enableSpread: bool = bool, fanSetup: bool = bool, inheritRotation: bool = bool, inheritVelocity: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], speed: Optional[Union[float, bool]] = float, spread: Optional[Union[float, bool]] = float, torusSectionRadius: Optional[Union[float, bool]] = float, velocityComponentOnly: bool = bool, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, wakeSetup: bool = bool, windSetup: bool = bool, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        directionX: (edit, query) - 
        directionY: (edit, query) - 
        directionZ: (edit, query) - Direction that the air will try to match the affected particles' velocity to. NOTE: This is not the velocity; this is only the direction. Use the -s flag to set the speed.
        enableSpread: (edit, query) - This tells the system whether or not to use the spread angle given by '-sp'. If this is 'false' then all connected objectswithin the maximum distance will be affected. Also, if this is set to 'false', all affected objects are forced to match their velocities along the direction vector. If this is set to 'true' and spread is used, then the direction of the force is along the direction from the field to the object.
        fanSetup: (edit) - Similar to 'windSetup' except that the effects of a fan or a person blowing air are approximated. The user can pass the same flags on the command line to adjust them from the defaults. These are the values that get set to approximate a 'fan': inheritVelocity 1.0 inheritRotation true componentOnly false enableSpread true spread .5 (45 degrees from center )
        inheritRotation: (edit, query) - If this is set to 'true', then the direction vector described with -dx, -dy, and -dz will be considered local to the owning object. Therefore, if the owning object's transform undergoes any rotation (by itself or one of its parents), the direction vector of the air field will undergo that same rotation.
        inheritVelocity: (edit, query) - Amount (from 0 to 1) of the field-owner's velocity added to the vector determined by the direction and speed flags. The combination of these two vectors makes up the TOTAL velocity vector for the air field. This allows the air to be determined directly by the motion of the owning object.
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        speed: (edit, query) - How fast the affected objects' speed reaches the speed (based on the -mag, -dx, -dy, -dz flags) of the air field. This value gets clamped internally to be between 0.0 and 1.0.  A value of 0.0 will make the air field have no effect. A value of 1.0 will try to match the air field's speed much quicker, but not necessarily immediately.
        spread: (edit, query) - This represents the angle from the direction vector within which objects will be affected. The values are in the range of 0 to 1. A value of 0 will result in an effect only exactly in front of the air field along the direction vector. A value of 1 will result in any object in front of the owning object, 90 degrees in all direction from the direction vector.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        velocityComponentOnly: (edit, query) - If this is 'false', the air will accelerate or decelerate the affected objects so that their velocities will eventually match the TOTAL velocity vector of the air field. If this is 'true', only ACCELERTION is applied to the affected objects so that their velocity component along the TOTAL velocity vector matches or is greater in magnitude than the TOTAL velocity vector. This will not slow objects down to match velocities, only speed them up to match components. This is most useful when using the -iv flag with a value >0.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
        wakeSetup: (edit) - Like the 'windSetup' and 'fanSetup', 'wakeSetup' sets certain values in the field to approximate the movement of air near a moving object, such as  a character's foot or hand. The values that are set are: inheritVelocity 1.0 inheritRotation false componentOnly true enableSpread false speed 0.0
        windSetup: (edit) - This will set some of the values above in a way that approximates the effects of a basic wind. This allows the user to then change certain values as he/she wishes on the same command line. First the preset values get set, and then any other flags that were passed get taken into account. These are the values that get set to approximate 'wind': inheritVelocity 0.0 inheritRotation true componentOnly false enableSpread false
    """
    pass


def arrayMapper(*args, destAttr: Optional[Union[str, bool]] = str, inputU: Optional[Union[str, bool]] = str, inputV: Optional[Union[str, bool]] = str, mapTo: Optional[Union[str, bool]] = str, target: Optional[Union[str, bool]] = str, type: Optional[Union[str, bool]] = str):
    """
    Create an arrayMapper node and connect it to a target object. If the -type flag is used, then this command also creates an external node used for computing the output values. If the input attribute does not already exist, it will be created. The output attribute must exists. If    a flag is omitted, the selection list will be used to supply the needed objects. If none are found, that action is omitted.

    Args:
        destAttr: (create) - Specifies the attribute which will be the downstream connection for the output data from the mapper node. The attribute type will be used to determine which output attribute to use: float array gets outValuePP, vector array gets outColorPP. If the flag is omitted, no output connection is made.
        inputU: (create) - Specifies the upstream attribute to connect to the mapper's uCoordPP attribute. If the flag is omitted, no input connection is made.
        inputV: (create) - Specifies the upstream attribute to connect to the mapper's vCoordPP attribute. If the flag is omitted, no input connection is made.
        mapTo: (create) - Specifies an existing node to be used to compute the output values. This node must be of the appropriate type. Currently, only ramp nodes may be used.
        target: (create, multiuse) - Specifies the target object to be connected to.
        type: (create) - Specifies the node type to create which will be used to compute the output values. Currently, only ramp is valid. If the flag is omitted, no connection is made and the external node is not created.
    """
    pass


def collision(*args, friction: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, offset: Optional[Union[float, bool]] = float, resilience: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        friction: (edit, query) - Friction of the surface.  This is the amount of the colliding particle's velocity parallel to the surface which is removed when the particle collides. A value of 0 will mean that no tangential velocity is lost, while a value of 1 will cause the particle to reflect straight along the normal of the surface.
        name: (edit, query) - name of field
        offset: (edit, query) - Offset value for the connector.
        resilience: (edit, query) - Resilience of the surface.  This is the amount of the colliding particle's velocity reflected along the normal of the surface.  A value of 1 will give perfect reflection, while a value of 0 will have no reflection along the normal of the surface.
    """
    pass


def colorAtPoint(*args, coordU: Optional[Union[float, bool]] = float, coordV: Optional[Union[float, bool]] = float, maxU: Optional[Union[float, bool]] = float, maxV: Optional[Union[float, bool]] = float, minU: Optional[Union[float, bool]] = float, minV: Optional[Union[float, bool]] = float, output: Optional[Union[str, bool]] = str, samplesU: Optional[Union[int, bool]] = int, samplesV: Optional[Union[int, bool]] = int):
    """
    The

    Args:
        coordU: (create, multiuse) - Input u coordinate to sample texture at.
        coordV: (create, multiuse) - Input v coordinate to sample texture at.
        maxU: (create) - DEFAULT 1.0 Maximum u bounds to sample.
        maxV: (create) - DEFAULT 1.0 Maximum v bounds to sample.
        minU: (create) - DEFAULT 0.0 Minimum u bounds to sample.
        minV: (create) - DEFAULT 0.0 Minimum v bounds to sample.
        output: (create) - Type of data to output:         A        = alpha only         RGB  = color only         RGBA = color and alpha
        samplesU: (create) - DEFAULT 1 The number of points to sample in the U dimension.
        samplesV: (create) - DEFAULT 1 The number of points to sample in the V dimension.
    """
    pass


def connectDynamic(*args, addScriptHandler: Optional[Union[str, bool]] = str, collisions: Optional[Union[str, bool]] = str, delete: bool = bool, emitters: Optional[Union[str, bool]] = str, fields: Optional[Union[str, bool]] = str, removeScriptHandler: Optional[Union[int, bool]] = int):
    """
    Dynamic connection specifies that the force fields, emitters, or collisions of an object affect another dynamic object. The dynamic object that is connected to a field, emitter, or collision object is influenced by those fields, emitters and collision objects.

    Args:
        addScriptHandler: (create) - Registers a script that will be given a chance to handle calls to the dynamicConnect command. This flag allows other dynamics systems to override the behaviour of the connectDynamic command. You must pass a Python function as the argument for this flag, and that function must take the following keyword arguments: fields, emitters, collisionObjects and objects. The python function must return True if it has handled the call to connectDynamic. In the case that the script returns true, the connectDynamic command will not do anything as it assumes that the work was handled by the script. If all of the callbacks return false, the connectDynamic command will proceed as normal.  The addScriptHandler flag may not be used with any other flags. When the flag is used, the command will return a numerical id that can be used to deregister the callback later (see the removeScriptHandler flag)
        collisions: (create, multiuse) - Connects each object to the collision models of the given object.
        delete: (create) - Deletes existing connections.
        emitters: (create, multiuse) - Connects each object to the emitters of the given object.
        fields: (create, multiuse) - Connects each object to the fields of the given object.
        removeScriptHandler: (create) - This flag is used to remove a callback that was previously registered with the addScriptHandler flag. The argument to this flag is the numerical id returned by dynamicConnect when the addScriptHandler flag was used. If this flag is called with an invalid id, then the command will do nothing.  This flag may not be used with any other flag.
    """
    pass


def constrain(*args, barrier: bool = bool, damping: Optional[Union[float, bool]] = float, directionalHinge: bool = bool, hinge: bool = bool, interpenetrate: bool = bool, nail: bool = bool, name: Optional[Union[str, bool]] = str, orientation: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), pinConstraint: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), restLength: Optional[Union[float, bool]] = float, spring: bool = bool, stiffness: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command constrains rigid bodies to the world or other rigid bodies.

    Args:
        barrier: (create, query) - Creates a barrier constraint.  This command requires one rigid bodies.
        damping: (create, edit, query) - Sets the damping constant. Default value: 0.1 Range: -1000.0 to 1000.0
        directionalHinge: (create, query) - Creates a directional hinge constraint.  This command requires two rigid bodies. The directional hinge always maintains the initial direction of its axis.
        hinge: (create, query) - Creates a hinge constraint.  This command requires one or two rigid bodies.
        interpenetrate: (create, edit, query) - Allows (or disallows) the rigid bodies defined in the constrain to ipenetrate.
        nail: (create, query) - Creates a nail constraint.  This command requires one rigid body.
        name: (create, edit, query) - Names the rigid constraint.
        orientation: (create, edit, query) - Set initial orientation of the constraint in world space.  This command is only valid with hinge and barrier constraints Default value: 0.0 0.0 0.0
        pinConstraint: (create, query) - Creates a pin constraint.  This command requires two rigid bodies.
        position: (create, edit, query) - Set initial position of the constraint in world space. Default value: 0.0 0.0 0.0 for uni-constraints, midpoint of bodies for deul constraint.
        restLength: (create, edit, query) - Sets the rest length. Default value: 1.0
        spring: (create, query) - Creates a spring constraint.  This command requires one or two rigidies.
        stiffness: (create, edit, query) - Sets the springs stiffness constant. Default value: 5.0
    """
    pass


def drag(*args, attenuation: Optional[Union[float, bool]] = float, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, useDirection: bool = bool, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        directionX: (edit, query) - X-component of direction.
        directionY: (edit, query) - Y-component of direction.
        directionZ: (edit, query) - Z-component of direction
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        useDirection: (edit, query) - Enable/disable direction. Drag will use -dx/-dy/-dz arguments if and only if this flag is set true.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def dynCache(*args):
    """
    Cache the current state of all particle shapes at the current time.

    Args:
    """
    pass


def dynExport(*args, allObjects: bool = bool, attribute: Optional[Union[str, bool]] = str, format: Optional[Union[str, bool]] = str, maxFrame: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], minFrame: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], onlyUpdateParticles: bool = bool, overSampling: Optional[Union[int, bool]] = int, path: Optional[Union[str, bool]] = str):
    """
    Export particle data to disk files.

    Args:
        allObjects: (create) - Ignore the selection list and export all particle objects. If you also specify an object name, the -all flag will be ignored.
        attribute: (create, multiuse) - Name of attribute to be exported. If any specified object does not have one of the specified attributes, dynExport will issue an error and not do the export.
        format: (create) - Desired format: "binary" ("pdb"), "ascii" ("pda"), or "cache" ("pdc"). The pdc format is for use by the Maya particle system to cache particle data.  The pda and pdb format options are intended for pipelines involving other software (for example, sending the data to some program written in-house); Maya cannot read pda or pdb files. There is no formal description of the PDB format, but the ExploreMe/particles/readpdb directory contains the source and Makefile for a small, simple C program called "readpdb" which reads it. Note that you must compile and run readpdb on the platform which you exported the files on.
        maxFrame: (create) - Ending frame to be exported.
        minFrame: (create) - Starting frame to be exported. The export operation will play the scene through from min frame to max frame as it exports.
        onlyUpdateParticles: (create) - Specify to only update the particles before exporting.
        overSampling: (create) - OverSampling to be used during export.
        path: (create) - This option allows you to specify a subdirectory of the workspace "particles" directory where you want the exported files to be stored. By default, files are stored in the workspace particles directory, i.e., -path is relative to that directory. ( Please Read This:  This is a change from previous versions of Maya in which the path was relative to the workspace root directory.) You can set the "particles" directory anywhere you want using the project window or workspace -fr command. (In this way, you can use an absolute path for export). The -path flag cannot handle strings which include "/" or "\", in other words, it lets you go down only one level in the directory hierarchy. If you specify a path which doesn't exist, the action will create it if possible; if it can't create the path it will warn you and fail. If you are using a project for which a particle data directory is not defined, dynExport will create a default one called "particles" and add it to your workspace.
    """
    pass


def dynExpression(*args, creation: bool = bool, runtime: bool = bool, runtimeAfterDynamics: bool = bool, runtimeBeforeDynamics: bool = bool, string: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command describes an expression that belongs to the specified particle shape.  The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) or per-particle attribute(s) in the scene.  One expression can read and alter any number of these attributes.  Every particle shape in your scene has three expressions, one for the runtimeBeforeDynamics, one for the runtimeAfterDynamics and one for creation time.  The create expression gets executed for every particle in the object whose age is 0.0.  The runtime expression gets executed for each particle with an age greater then 0.0.  Unlike expressions created with the

    Args:
        creation: (create, edit, query) - Tells the command that the string passed will be a creation expression for the particle shape.  This means that this expression will be executed when a particle is emitted or at the beginning of the scene for existing particles.
        runtime: (create, edit, query) - Tells the command that the string passed will be a runtime expression for the particle shape.  This expression will be executed at the beginning of runtime.
        runtimeAfterDynamics: (create, edit, query) - Tells the command that the string passed will be a runtime expression for the particle shape.  This expression will be executed after dynamics whenever a particle's age is greater then zero (0).
        runtimeBeforeDynamics: (create, edit, query) - Tells the command that the string passed will be a runtime expression for the particle shape.  This expression will be executed before dynamics whenever a particle's age is greater then zero (0).
        string: (create, edit) - Set the expression string. This is queriable with the -q/query flag and the -rbd/runtimeBeforeDynamics, the -rab/runtimeAfterDynamics or the -c/creation flag.
    """
    pass


def dynGlobals(*args, active: bool = bool, listAll: bool = bool, overSampling: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    This node edits and queries the attributes of the active dynGlobals node in the scene. There can be only one active node of this type. The active dynGlobals node is the first one that was created, either with a "createNode" command or by accessing/editing any of the attributes on the node through this command.

    Args:
        active: (query) - This flag returns the name of the active dynGlobals node in the the scene.  Only one dynGlobals node is active. It is the first on created.  Any additional dynGlobals nodes will be ignored.
        listAll: (query) - This flag will list all of the dynGlobals nodes in the scene.
        overSampling: (edit, query) - This flag will set the current overSampling value for all of the particle in the scene.
    """
    pass


def dynPaintEditor(*args, activeOnly: bool = bool, autoSave: bool = bool, camera: Optional[Union[str, bool]] = str, canvasMode: bool = bool, canvasUndo: bool = bool, changeCommand: Optional[Union[Tuple[str, str, str, str], bool]] = [str, str, str], clear: Tuple[float, float, float] = (float, float, float), control: bool = bool, currentCanvasSize: bool = bool, defineTemplate: Optional[Union[str, bool]] = str, displayAppearance: Optional[Union[str, bool]] = str, displayFog: bool = bool, displayImage: Optional[Union[int, bool]] = int, displayLights: Optional[Union[str, bool]] = str, displayStyle: Optional[Union[str, bool]] = str, displayTextures: bool = bool, docTag: Optional[Union[str, bool]] = str, doubleBuffer: bool = bool, drawAxis: bool = bool, drawContext: bool = bool, exists: bool = bool, fastUpdate: int = int, fileName: Optional[Union[str, bool]] = str, filter: Optional[Union[str, bool]] = str, forceMainConnection: Optional[Union[str, bool]] = str, highlightConnection: Optional[Union[str, bool]] = str, iconGrab: bool = bool, loadImage: str = str, lockMainConnection: bool = bool, mainListConnection: Optional[Union[str, bool]] = str, menu: Optional[Union[str, bool]] = str, nbImages: bool = bool, newImage: Optional[Union[Tuple[int, int, float, float, float], bool]] = [int, int, float, float, float], paintAll: float = float, panel: Optional[Union[str, bool]] = str, parent: Optional[Union[str, bool]] = str, redrawLast: bool = bool, refresh: bool = bool, refreshMode: Optional[Union[int, bool]] = int, removeAllImages: bool = bool, removeImage: bool = bool, rollImage: Tuple[float, float] = [float, float], saveAlpha: bool = bool, saveBumpmap: Optional[Union[str, bool]] = str, saveImage: bool = bool, scaleBlue: Optional[Union[float, bool]] = float, scaleGreen: Optional[Union[float, bool]] = float, scaleRed: Optional[Union[float, bool]] = float, selectionConnection: Optional[Union[str, bool]] = str, singleBuffer: bool = bool, snapShot: bool = bool, stateString: bool = bool, swap: int = int, tileSize: int = int, unParent: bool = bool, undoCache: bool = bool, unlockMainConnection: bool = bool, updateMainConnection: bool = bool, useTemplate: Optional[Union[str, bool]] = str, wrap: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], writeImage: str = str, zoom: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    Create a editor window that can be painted into

    Args:
        activeOnly: (edit, query) - For Scene mode, this determines if only the active strokes will be refreshed.
        autoSave: (edit, query) - For Canvas mode, this determines if the buffer will be saved to a disk file after every stroke. Good for painting textures and viewing the results in shaded display in the model view.
        camera: (edit, query) - Sets the name of the camera which the Paint Effects panel looks through.
        canvasMode: (edit, query) - Sets the Paint Effects panel into Canvas mode if true.
        canvasUndo: (edit) - Does a fast undo in Canvas mode. This is a special undo because we are not using any history when we paint in Canvas mode so we provide a single level undo for the Canvas.
        changeCommand: (create, edit, query) - Parameters:  First string: command Second string: editorName Third string: editorCmd Fourth string: updateFunc   Call the command when something changes in the editor The command should have this prototype :  command(string $editor, string $editorCmd, string $updateFunc, int $reason)  The possible reasons could be :  0: no particular reason 1: scale color 2: buffer (single/double) 3: axis  4: image displayed 5: image saved in memory
        clear: (edit) - Clears the buffer (if in Canvas mode) to the floating point values (R,G,B).
        control: (query) - Query only. Returns the top level control for this editor. Usually used for getting a parent to attach popup menus. Caution: It is possible for an editor to exist without a control. The query will return "NONE" if no control is present.
        currentCanvasSize: (query) - In Query mode, this returns the (X,Y) resolution of the current canvas.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        displayAppearance: (edit, query) - Sets the display appearance of the model panel.  Possible values are "wireframe", "points", "boundingBox", "smoothShaded", "flatShaded".  This flag may be used with the -interactive and -default flags.  Note that only "wireframe", "points", and "boundingBox" are valid for the interactive mode.
        displayFog: (edit, query) - For Scene mode, this determines if fog will be displayed in the Paint Effects panel when refreshing the scene. If fog is on, but this is off, fog will only be drawn on the strokes, not the rest of the scene.
        displayImage: (edit, query) - Set a particular image in the Editor Image Stack as the current Editor Image. Images are added to the Editor Image Stack using the "si/saveImage" flag.
        displayLights: (edit, query) - Sets the lighting for shaded mode.  Possible values are "selected", "active", "all", "default".
        displayStyle: (create, edit, query) - Set the mode to display the image. Valid values are:  "color" to display the basic RGB image "mask" to display the mask channel "lum" to display the luminance of the image
        displayTextures: (edit, query) - Turns on or off display of textures in shaded mode
        docTag: (create, edit, query) - Attaches a tag to the editor.
        doubleBuffer: (create, edit, query) - Set the display in double buffer mode
        drawAxis: (create, edit, query) - Set or query whether the axis will be drawn.
        drawContext: (query) - Returns the name of the context.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        fastUpdate: () - Obsolete - do not use
        fileName: (edit, query) - This sets the file to which the canvas will be saved.
        filter: (create, edit, query) - Specifies the name of an itemFilter object to be used with this editor. This filters the information coming onto the main list of the editor.
        forceMainConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object. This is a variant of the -mainListConnection flag in that it will force a change even when the connection is locked. This flag is used to reduce the overhead when using the -unlockMainConnection , -mainListConnection, -lockMainConnection flags in immediate succession.
        highlightConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its highlight list. Not all editors have a highlight list. For those that do, it is a secondary selection list.
        iconGrab: (edit) - This puts the Paint Effects panel into Grab Icon mode where the user is expected to drag out a section of the screen to be made into an icon.
        loadImage: (edit) - load an image from disk and set it as the current Editor Image
        lockMainConnection: (create, edit) - Locks the current list of objects within the mainConnection, so that only those objects are displayed within the editor. Further changes to the original mainConnection are ignored.
        mainListConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will use as its source of content. The editor will only display items contained in the selectionConnection object.
        menu: (create) - Sets the name of the script used to build a menu in the editor. The script takes the editor name as an argument.
        nbImages: (query) - returns the number of images
        newImage: (edit, query) - Starts a new image in edit mode, setting the resolution to the integer values (X,Y) and clearing the buffer to the floating point values (R,G,B). In Query mode, this returns the (X,Y) resolution of the current Image.
        paintAll: (edit) - Redraws the buffer in current refresh mode.
        panel: (create, query) - Specifies the panel for this editor. By default if an editor is created in the create callback of a scripted panel it will belong to that panel. If an editor does not belong to a panel it will be deleted when the window that it is in is deleted.
        parent: (create, edit, query) - Specifies the parent layout for this editor. This flag will only have an effect if the editor is currently un-parented.
        redrawLast: (edit) - Redraws the last stroke again. Useful when it's brush has just changed. This feature does a fast undo and redraws the stroke again.
        refresh: (edit) - requests a refresh of the current Editor Image.
        refreshMode: (edit, query) - Sets the refresh mode to the specified value. 0 - Do not draw strokes on refresh, 1 - Redraw strokes in wireframe mode, 2 - Redraw strokes in final rendered mode.
        removeAllImages: (edit) - remove all the Editor Images from the Editor Image Stack
        removeImage: (edit) - remove the current Editor Image from the Editor Image Stack
        rollImage: (edit) - In Canvas mode, this rolls the image by the floating point values (X,Y). X and Y are between 0 (no roll) and 1 (full roll). A value of .5 rolls the image 50% (ie. the border moves to the center of the screen.
        saveAlpha: (edit, query) - For Canvas mode, this determines if the alpha will be saved when storing the canvas to a disk file.
        saveBumpmap: (edit, query) - Saves the current buffer as a bump map to the specified file.
        saveImage: (edit) - save the current Editor Image to memory. Saved Editor Images are stored in an Editor Image Stack. The most recently saved image is stored in position 0, the second most recently saved image in position 1, and so on... To set the current Editor Image to a previously saved image use the "di/displayImage" flag.
        scaleBlue: (create, edit, query) - Define the scaling factor for the blue component in the View. The default value is 1 and can be between -1000 to +1000
        scaleGreen: (create, edit, query) - Define the scaling factor for the green component in the View. The default value is 1 and can be between -1000 to +1000
        scaleRed: (create, edit, query) - Define the scaling factor for the red component in the View. The default value is 1 and can be between -1000 to +1000
        selectionConnection: (create, edit, query) - Specifies the name of a selectionConnection object that the editor will synchronize with its own selection list. As the user selects things in this editor, they will be selected in the selectionConnection object. If the object undergoes changes, the editor updates to show the changes.
        singleBuffer: (create, edit, query) - Set the display in single buffer mode
        snapShot: (edit) - Takes a snapshot of the current camera view.
        stateString: (query) - Query only flag. Returns the MEL command that will create an editor to match the current editor state. The returned command string uses the string variable $editorName in place of a specific name.
        swap: () - Obsolete - do not use
        tileSize: (edit) - Sets the size of the tile for the hardware texture redraw of the display buffer.
        unParent: (create, edit) - Specifies that the editor should be removed from its layout. This cannot be used in query mode.
        undoCache: (edit) - By default the last image is cached for undo. If this is set false, then undoing will be disabled in canvas mode and undo in scene mode will force a full refresh. Less memory will be used if this is set false before the first clear or refresh of the current scene.
        unlockMainConnection: (create, edit) - Unlocks the mainConnection, effectively restoring the original mainConnection (if it is still available), and dynamic updates.
        updateMainConnection: (create, edit) - Causes a locked mainConnection to be updated from the orginal mainConnection, but preserves the lock state.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        wrap: (edit, query) - For Canvas mode, should the buffer wrap in U, and V (respectively) when painting.
        writeImage: (edit) - write the current Editor Image to disk
        zoom: (edit, query) - Zooms the Canvas image by the specified value.
    """
    pass


def dynPref(*args, autoCreate: bool = bool, echoCollision: bool = bool, runupFrom: Optional[Union[int, bool]] = int, runupToCurrentTime: bool = bool, saveOnQuit: bool = bool, saveRuntimeState: bool = bool, query: bool = bool):
    """
    This action modifies and queries the current state of "autoCreate rigid bodies", "run up to current time", and  "run up from" (previous time or start time).

    Args:
        autoCreate: (create, query) - If on, autoCreate rigid bodies.
        echoCollision: (create, query) - If on, will cause particle systems to echo to the Script Editor the command that they are running for each particle collision event. If off, only the output of the command will be echoed.
        runupFrom: (create, query) - If on, run up from previous time; if 2, run up from start time
        runupToCurrentTime: (create, query) - If on, run up the scene to current time
        saveOnQuit: (create, query) - If on, save the current values of preferences to userPrefs file.
        saveRuntimeState: (create, query) - If on, runtime state as well as initial state of all particle objects will be saved to file. If off, only initial state will be saved.
    """
    pass


def emit(*args, attribute: Optional[Union[str, bool]] = str, floatValue: Optional[Union[float, bool]] = float, object: Optional[Union[str, bool]] = str, position: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), vectorValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float)):
    """
    The

    Args:
        attribute: (create, multiuse) - Specifies the attribute on the particle object that any value flags following it and before the next -attribute flag will be associated with.  The same attribute can be specified later in the command to pick up where the first one left off. The attributes used must be per-particle attributes.  This will accept both long and short names for the attributes. Note the per-particle attribute must already exist on the particle object prior to being specified via this command flag.
        floatValue: (create, multiuse) - Sets the float value to be used for the "current" attribute of the "current" particle.  By current attribute, it is meant the attribute specified by the most recent -attribute flag.  By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that  have been set for the "current" attribute.  If the current attribute is a vector-per-particle attribute, then the float value specified will be used for all three components of the vector.
        object: (create) - This flag takes the name of a particleShape or the transform directly above it in the DAG as its parent.  It specifies which object to add the particles to.  This flag must be passed, as the selection list is ignored for this action.
        position: (create, multiuse) - Specifies the positions in the particle object's space (usually world space) where the particles are to be created. One particle is created for each occurence of this flag.
        vectorValue: (create, multiuse) - Sets the vector value to be used for the "current" attribute of the "current" particle.  By current attribute, it is meant the attribute specified by the most recent -attribute flag.  By current particle, it is meant the particle in the list of -position flags that corresponds to the number of values that have been set for the "current" attribute.  If the current attribute is a float-per-particle attribute, then the length of the vector described by this flag will be used.  The length is described as SQR( xVal2 + yVal2 + zVal2 ).
    """
    pass


def emitter(*args, alongAxis: Optional[Union[float, bool]] = float, aroundAxis: Optional[Union[float, bool]] = float, awayFromAxis: Optional[Union[float, bool]] = float, awayFromCenter: Optional[Union[float, bool]] = float, cycleEmission: Optional[Union[str, bool]] = str, cycleInterval: Optional[Union[int, bool]] = int, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, directionalSpeed: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, minDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, needParentUV: bool = bool, normalSpeed: Optional[Union[float, bool]] = float, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], randomDirection: Optional[Union[float, bool]] = float, rate: Optional[Union[float, bool]] = float, scaleRateByObjectSize: bool = bool, scaleSpeedBySize: bool = bool, speed: Optional[Union[float, bool]] = float, speedRandom: Optional[Union[float, bool]] = float, spread: Optional[Union[float, bool]] = float, tangentSpeed: Optional[Union[float, bool]] = float, torusSectionRadius: Optional[Union[float, bool]] = float, type: Optional[Union[str, bool]] = str, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter). Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene.  Particles will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.

    Args:
        alongAxis: (edit, query) - Initial velocity multiplier in the direction along the central axis of the volume.  See the diagrams in the documentation.  Applies only to volume emitters.
        aroundAxis: (edit, query) - Initial velocity multiplier in the direction around the central axis of the volume.  See the diagrams in the documentation.  Applies only to volume emitters.
        awayFromAxis: (edit, query) - Initial velocity multiplier in the direction away from the central axis of the volume.  See the diagrams in the documentation.  Used only with the cylinder, cone, and torus volume emitters.
        awayFromCenter: (edit, query) - Initial velocity multiplier in the direction away from the center point of a cube or sphere volume emitter. Used only with the cube and sphere volume emitters.
        cycleEmission: (edit, query) - Possible values are "none" and "frame." Cycling emission restarts the random number stream after a specified interval.  This can either be a number of frames or a number of emitted particles.  In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to "frame" and cycleInterval to 1 will then re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.
        cycleInterval: (edit, query) - Specifies the number of frames or particles between restarts of the random number stream.  See cycleEmission.  Has no effect if cycleEmission is set to None.
        directionX: (edit, query) - x-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.
        directionY: (edit, query) - y-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.
        directionZ: (edit, query) - z-component of emission direction. Used for directional emitters, and for volume emitters with directionalSpeed.
        directionalSpeed: (edit, query) - For volume emitters only, adds a component of speed in the direction specified by the directionX, Y, and Z attributes. Applies only to volume emitters. Does not apply to other types of emitters.
        maxDistance: (edit, query) - Maximum distance at which emission ends.
        minDistance: (edit, query) - Minimum distance at which emission starts.
        name: (create, edit, query) - Object name
        needParentUV: (edit, query) - If aNeedParentUV is true, compute parentUV value from each triangle or each line segment, then send out to the target particle object. You also need to add parentU and parentV attributes to the particle object to store these values.
        normalSpeed: (edit, query) - Normal speed multiple for point emission. For each emitted particle, multiplies the component of the velocity normal to the surface or curve by this amount. Surface and curve emitters only.
        position: (create, edit, multiuse, query) - world-space position
        randomDirection: (edit, query) - Magnitude of a random component of the speed from volume emission.
        rate: (edit, query) - Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of area per unit time.
        scaleRateByObjectSize: (edit, query) - Applies to curve and surface emitters, only. If true, number of particles is determined by object size (area or length) times rate value.  If false, object size is ignored and the rate value is used without modification. The former is the way Maya behaved prior to version 3.0.
        scaleSpeedBySize: (edit, query) - Indicates whether the scale of a volume emitter affects its velocity.
        speed: (edit, query) - Speed multiple.  Multiplies the velocity of the emitted particles by this amount. Does not apply to volume emitters.  For that emitter type, use directionalSpeed.
        speedRandom: (edit, query) - Identifies a range of random variation for the speed of each generated particle.  If set to a non-zero value, speed becomes the mean value of the generated particles, whose speeds vary by a random amount up to plus or minus speedRandom/2. For example, speed 5 and speedRandom 2 will make the speeds vary between 4 and 6.
        spread: (edit, query) - Random spread (0-1), as a fraction of 90 degrees, along specified direction.   Directional emitters only.
        tangentSpeed: (edit, query) - Tangent speed multiple for point emission. For each emitted particle, multiplies the component of the velocity tangent to the surface  or curve by this amount. Surface and curve emitters only.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        type: (edit, query) - Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are: omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.
        volumeOffset: (edit, query) - Volume offset of the emitter.  Volume offset translates the emission volume by the specified amount from the actual emitter location.  This is in the emitter's local space.
        volumeShape: (edit, query) - Volume shape of the emitter.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which particles are generated. Values are: "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def event(*args, count: Optional[Union[int, bool]] = int, delete: bool = bool, dieAtCollision: bool = bool, emit: Optional[Union[int, bool]] = int, list: bool = bool, name: Optional[Union[str, bool]] = str, proc: Optional[Union[str, bool]] = str, random: bool = bool, rename: Optional[Union[str, bool]] = str, select: bool = bool, split: Optional[Union[int, bool]] = int, spread: Optional[Union[float, bool]] = float, target: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The event command assigns collision events to a particle object. Collision events are stored in multi-attributes in the particle shape. The event command returns the event name.

    Args:
        count: (edit, query) - Collision number (for each particle) to which this event applies. Zero (the default) indicates that it applies to all collisions.
        delete: (create) - Delete the specified event.
        dieAtCollision: (edit, query) - Particle dies at the collision specified by "count." If no count value is given, die at first collision.
        emit: (edit, query) - Emit n additional particles into the assigned target object. The original (colliding) particle survives as well, and remains in its original object.  The new particles have age zero and mass equal to the emitting particle. They use the velocity inheritance parameter of the target object.
        list: (create) - List all events for the chosen shape, like this: event1Name event2Name ... If no shape identified, list all events for all shapes, like this: shape1Name event1Name shape2Name event2Name... Returns a string array.
        name: (create, edit, query) - Assign a name to an event you are creating, or identify an event you wish to edit, query, or delete. See examples.
        proc: (create, edit, query) - Specify a MEL proc to be called each time the event occurs. This must be a global proc with arguments as follows: global proc procName( string obj, int id, string objHit ); Arguments passed in are the name of the particle object, the id of the particle which collided, and the name of the object collided with.  You can use particle -id -q to get values of the particle's attributes.
        random: (edit, query) - Used with -split and -emit flags.  If -random is set true and -split or -emit is set to n, then a random number of particles uniformly distributed between 1 and n will be created at the event.
        rename: (query) - Assign a new name to an event you are editing. See examples.
        select: () - This flag is obsolete.  See the -name flag.
        split: (edit, query) - Colliding particle splits into specified number of new particles. These new particles become part of the assigned target object. If no target has been assigned, they become part of the same object.  The new particles inherit the current age of the particle that split.  They use the velocity inheritance parameter of the target object.  If you set both emit and split, the event will do both: first emit new particles, then split the original one. This is a change from earlier versions where emit and split were mutually exclusive.
        spread: (edit, query) - Particles created at collision will spread out a random amount from the rebound direction of the colliding particle.  The spread is specified as a fraction (0-1) of 90 degrees.  If spread is set at 0 (the default) all the new particles created may coincide.
        target: (edit, query) - Target object for emitting or split particles. New particles created through the -emit or -split flags join this object.
    """
    pass


def expression(*args, alwaysEvaluate: Optional[Union[int, bool]] = int, animated: Optional[Union[int, bool]] = int, attribute: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, object: Optional[Union[str, bool]] = str, safe: bool = bool, shortNames: bool = bool, string: Optional[Union[str, bool]] = str, timeDependent: bool = bool, unitConversion: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command describes an expression that belongs to the current scene. The expression is a block of code of unlimited length with a C-like syntax that can perform conversions, mathematical operations, and logical decision making on any numeric attribute(s) in the scene.  One expression can read and alter any number of numeric attributes.  Theoretically, every expression in a scene can be combined into one long expression, but it is recommended that they are separated for ease of use and editing, as well as efficiency.

    Args:
        alwaysEvaluate: (create, edit, query) - If this is TRUE (the default), then the expression will be evaluated whenever time changes regardless of whether the other inputs have changed, and an output is requested.  If it is FALSE, then the expression will only be evaluated if one or more of the inputs changes and an output is requested.  Note, if 'time' or 'frame' are inputs, then the expression will act as if this was set to TRUE.
        animated: (create, edit, query) - Sets the animation mode on the expression node: 0 = Not Animated, 1 = Animated, 2 = Animated with No Callback.
        attribute: (create, edit, query) - Sets the name of the attribute to use for the expression
        name: (create, edit, query) - Sets the name of the dependency graph node to use for the expression
        object: (create, edit, query) - Sets the "default" object for the expression.  This allows the expression writer to not type the object name for frequently-used objects.  See the examples below.
        safe: (query) - Returns true if no potential side effect can occurs running that expression. Safe expression will be optimized to evaluate only when needed even if flagged alwaysEvaluate.
        shortNames: (create, edit, query) - When used with the -q/query flag, tells the command to return the expression with attribute names as short as possible. The default is to return the FULL attribute name, regardless of how the user entered it into the expression, including the object names.  With this flag set, attribute names are returned as their short versions, and any attribute that belongs to the default object, if there is one specified, will not display the object's name.
        string: (create, edit, query) - Set the expression string
        timeDependent: (query) - Returns true if expression is evaluated when time change. An expression can be time-dependent for the following reasons: - The expression refers to 'time' or 'frame' keywords. - The expression have side effects (unsafe). - The expression node's "time" attribute is connected manually. If the expression is safe and not time dependend, then they will always evaluate on depend, even if alwaysEvaluate is on.
        unitConversion: (edit, query) - Insert specified unit conversion nodes at creation: "all", "none," or "angularOnly." Default is "all."  For angularOnly, will insert unit conversion nodes only for angular attributes (allowing degrees-to-radians conversion).  This is for performance tuning. If queried, returns the option used when the expression was created or last edited.
    """
    pass


def expressionEditorListen(*args, listenFile: Optional[Union[str, bool]] = str, listenForAttr: Optional[Union[str, bool]] = str, listenForExpression: Optional[Union[str, bool]] = str, listenForName: Optional[Union[str, bool]] = str, stopListenForAttr: Optional[Union[str, bool]] = str, stopListenForExpression: Optional[Union[str, bool]] = str, stopListenForName: Optional[Union[str, bool]] = str):
    """
    Listens for messages for the Expression Editor, at its request, and communicates them to it.  This action is for internal use only and should not be called by users.  This action should be called only by the Expression Editor.

    Args:
        listenFile: (create) - Listen for changes to the file argument.
        listenForAttr: (create) - Listen for changes to the attributes of the node argument.
        listenForExpression: (create) - Listen for changes to the named expression
        listenForName: (create) - Listen for name changes for the node argument.
        stopListenForAttr: (create) - Stop listening for changes to the attributes of the node argument.
        stopListenForExpression: (create) - Stop listening for changes to the named expression
        stopListenForName: (create) - Stop listening for name changes for the node argument.
    """
    pass


def fluidCacheInfo(*args, attribute: Optional[Union[str, bool]] = str, cacheTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], endFrame: bool = bool, hasCache: bool = bool, hasData: bool = bool, initialConditions: bool = bool, playback: bool = bool, resolution: bool = bool, startFrame: bool = bool, edit: bool = bool, query: bool = bool):
    """
    A command to get information about the fluids cache. Get the startFrame and resolution for InitialConditions. Get the endFrame as well for a playback cache. Note that for the playback cache, it will look at the current time (or last frame if the current time is past end of cache)

    Args:
        attribute: (create, edit, query) - Modifier to the "hasData" flag, used to query whether a cache has data (at the current time) for a specific fluid attribute.  Valid attribute values are "density", "velocity", "temperature", "fuel", "color", "coordinates" (for texture coordinates), "falloff".
        cacheTime: (create, edit, query) - Only valid with the -hasData flag.  The time the -hasData flag uses when it queries the cache to see if there is data.
        endFrame: (create, edit, query) - Returns end time of cache as float.
        hasCache: (create, edit, query) - Returns true if fluid has specified cache, false if not.
        hasData: (create, edit, query) - Queries whether a given cache has data in it at the time specified by the -time flag.  (If not -time flag is present, -hasData assumes the current time.) When used with the "attribute" flag, indicates if data for the specified attribute exists in the cache.  When used without the "attribute" flag, "hasData" indicates whether there is data in the cache for any of the valid fluid attributes.
        initialConditions: (create, edit, query) - Specifies the cache to be queried is the "Initial Conditions" cache.
        playback: (create, edit, query) - Specifies the cache to be queried is the "Playback" cache.
        resolution: (create, edit, query) - Returns cache resolution as float[].
        startFrame: (create, edit, query) - Returns start time for cache as float.
    """
    pass


def fluidEmitter(*args, cycleEmission: Optional[Union[str, bool]] = str, cycleInterval: Optional[Union[int, bool]] = int, densityEmissionRate: Optional[Union[float, bool]] = float, fluidDropoff: Optional[Union[float, bool]] = float, fuelEmissionRate: Optional[Union[float, bool]] = float, heatEmissionRate: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, minDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], rate: Optional[Union[float, bool]] = float, torusSectionRadius: Optional[Union[float, bool]] = float, type: Optional[Union[str, bool]] = str, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter). Creates an emitter object. If object names are provided or if objects are selected, applies the emitter to the named/selected object(s)in the scene.  Fluid will then be emitted from each. If no objects are named or selected, or if the -pos option is specified, creates a positional emitter.

    Args:
        cycleEmission: (edit, query) - Possible values are "none" and "frame." Cycling emission restarts the random number stream after a specified interval.  This can either be a number of frames or a number of emitted particles.  In each case the number is specified by the cycleInterval attribute. Setting cycleEmission to "frame" and cycleInterval to 1 will then re-start the random stream every frame. Setting cycleInterval to values greater than 1 can be used to generate cycles for games work.
        cycleInterval: (edit, query) - Specifies the number of frames or particles between restarts of the random number stream.  See cycleEmission.  Has no effect if cycleEmission is set to None.
        densityEmissionRate: (edit, query) - Rate at which density is emitted.
        fluidDropoff: (edit, query) - Fluid Emission Dropoff in volume
        fuelEmissionRate: (edit, query) - Rate at which  is emitted.
        heatEmissionRate: (edit, query) - Rate at which density is emitted.
        maxDistance: (edit, query) - Maximum distance at which emission ends.
        minDistance: (edit, query) - Minimum distance at which emission starts.
        name: (create, edit, query) - Object name
        position: (create, edit, multiuse, query) - world-space position
        rate: (edit, query) - Rate at which particles emitted (can be non-integer). For point emission this is rate per point per unit time. For surface emission it is rate per square unit of area per unit time.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        type: (edit, query) - Type of emitter. The choices are omni | dir | direction | surf | surface | curve | curv. The default is omni. The full definition of these types are: omnidirectional point emitter, directional point emitter, surface emitter, or curve emitter.
        volumeOffset: (edit, query) - Volume offset of the emitter.  Volume offset translates the emission volume by the specified amount from the actual emitter location.  This is in the emitter's local space.
        volumeShape: (edit, query) - Volume shape of the emitter.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which particles are generated. Values are: "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def fluidVoxelInfo(*args, checkBounds: bool = bool, inBounds: Optional[Union[Tuple[int, int, int], bool]] = [int, int, int], objectSpace: bool = bool, radius: Optional[Union[float, bool]] = float, voxel: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), voxelCenter: bool = bool, xIndex: Optional[Union[int, bool]] = int, yIndex: Optional[Union[int, bool]] = int, zIndex: Optional[Union[int, bool]] = int):
    """
    Provides basic information about the mapping of a fluid voxel grid into world- or object space of the fluid.  Use this command to determine the center point of a voxel, or to find the voxel containing a given point, among other things.

    Args:
        checkBounds: (create) - If this flag is on, and the voxel index of a point that is out of bounds is requested, then we return nothing.
        inBounds: (create) - Are the three ints representing the x, y, z indices of a voxel within the bounds of the fluid's voxel grid?  True if yes, false if not.  (For 2D fluids, pass in z=0 for the third argument.  See examples.)
        objectSpace: (create) - Whether the queried value should be returned in object space (TRUE), or world space (FALSE, the default).
        radius: (create) - Modifier for the -voxel flag.  Returns a list of index triples identifying voxels that fall within the given radius of the point specified by the -voxel flag.
        voxel: (create) - Returns array of three ints representing the x, y, z indices of the voxel within which the given point position is contained. If the checkBounds flag is on, and the point is out of bounds, we return nothing. Otherwise, even if the point is out of bounds, index values are returned. When combined with the -radius flag, returns an array of index triples representing a list of voxels within a given radius of the given point position.
        voxelCenter: (create) - The center position of the specified voxels.  Returns an array of floats (three for each of the indices in the query).  (Valid only with the -xIndex, -yIndex, and -zIndex flags.)
        xIndex: (create) - Only return values for cells with this X index
        yIndex: (create) - Only return values for cells with this Y index
        zIndex: (create) - Only return values for cells with this Z index
    """
    pass


def getDefaultBrush(*args):
    """
    The command returns the name of the default Paint Effects brush.

    Args:
    """
    pass


def getFluidAttr(*args, attribute: Optional[Union[str, bool]] = str, lowerFace: bool = bool, xIndex: Optional[Union[int, bool]] = int, xvalue: bool = bool, yIndex: Optional[Union[int, bool]] = int, yvalue: bool = bool, zIndex: Optional[Union[int, bool]] = int, zvalue: bool = bool):
    """
    Returns values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    Args:
        attribute: (create) - Specifies the fluid attribute for which to display values.  Valid attributes are "force", "velocity", "density", "falloff", "fuel", "color", and "temperature".  (Note that getting force values is an alternate way of getting velocity values at one time step.)
        lowerFace: (create) - Only valid with "-at velocity".  Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity necessarily affects neighboring voxels.  Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.
        xIndex: (create) - Only return values for cells with this X index
        xvalue: () - Only get the first component of the vector-valued attribute specified by the "-at/attribute" flag.
        yIndex: (create) - Only return values for cells with this Y index
        yvalue: () - Only get the second component of the vector-valued attribute specified by the "-at/attribute" flag.
        zIndex: (create) - Only return values for cells with this Z index
        zvalue: () - Only get the third component of the vector-valued attribute specified by the "-at/attribute" flag.
    """
    pass


def getParticleAttr(*args, array: bool = bool, attribute: Optional[Union[str, bool]] = str, object: Optional[Union[str, bool]] = str):
    """
    This action will return either an array of values, or the average value and maximum offset, for a specied per-particle attribute of a particle object or component.  If a particle component is specified on the command line, values are returned for that component only.  If an object name is given instead, values are returned for all particles in that object.  If no object name is passed, but a particle object or component is selected, values are returned for the selection.

    Args:
        array: (create) - Tells the action whether you want a full array of data. If set true, the action returns an array of floats containing the values for all the specified particles.  If set false (the default), the action returns the average value and the maximum offset from the average over the component.  If the attribute is a vector attribute, the action returns six values: Average X, Average Y, Average Z, Maximum offset in X, Y, and Z of component.
        attribute: (create) - Tells the action which attribute you want the value of. Must be a per-particle attribute.
        object: (create) - This flag is obsolete.  Instead of using it, please pass the name of the object and/or components you want on the command line. See the examples.
    """
    pass


def goal(*args, goal: Optional[Union[str, bool]] = str, index: bool = bool, useTransformAsGoal: bool = bool, weight: Optional[Union[float, bool]] = float, query: bool = bool):
    """
    Specifies the given objects as being goals for the given particle object.  If the goal objects are geometry, each particle in the particle object will each try to follow or match its position to that of a certain vertex/CV/lattice point of the goal.  If the goal object is another particle object, each particle will try to follow a paricle of the goal. In any other case, all the particles will try to follow the current location of the goal object's transform.  You can get this latter behavior for a geometry or particle object too by using -utr true.

    Args:
        goal: (create, multiuse, query) - This flag specifies string to be a goal of the particle object on the command line or the currently selected particle object.  This flag can be used multiple times to specify multiple goals for a particle object.  Query is for use by the attribute editor.
        index: (query) - Returns array of multi-attribute indices for the goals. Intended for use by the Attribute Editor.
        useTransformAsGoal: (create) - Use transform of specified object instead of the shape. Meaningful only for particle and geometry objects.  Can only be passed once, applies to all objects passed with -g.
        weight: (create) - This specifies the goal weight as a value from 0 to 1.  A value of 0 means that the goal's position will have no effect on the particle object, while a weight of 1 will make the particle object try to follow the goal object exactly.  This flag can only be passed once and sets the weight for every goal passed with the -g/-goal flag.
    """
    pass


def gravity(*args, attenuation: Optional[Union[float, bool]] = float, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        directionX: (edit, query) - X-component of direction.
        directionY: (edit, query) - Y-component of direction.
        directionZ: (edit, query) - Z-component of direction
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def loadFluid(*args, currentTime: bool = bool, frame: Optional[Union[float, bool]] = float, initialConditions: bool = bool, edit: bool = bool, query: bool = bool):
    """
    A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in the grid from the initial state cache

    Args:
        currentTime: (create, edit, query) - This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.
        frame: (create, edit, query) - This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.
        initialConditions: (create, edit, query) - load initial conditions cache
    """
    pass


def nBase(*args, clearCachedTextureMap: Optional[Union[str, bool]] = str, clearStart: bool = bool, stuffStart: bool = bool, textureToVertex: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid and nParticle objects, but the options on this command do not currently apply to nParticle objects.

    Args:
        clearCachedTextureMap: (create, edit) - Clear the cached texture map for the specified attribute from the nBase.
        clearStart: (create, edit) - Indicates that start state should be cleared
        stuffStart: (create, edit) - Indicates that current state should be stuffed into the start state
        textureToVertex: (create, edit) - Transfer the texture map data for the specified attribute into the related per-vertex attribute.
    """
    pass


def newton(*args, attenuation: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, minDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        minDistance: (edit, query) - Minimum distance at which field is exerted. Distance is in the denominator of the field force equation. Setting md to a small positive number avoids bizarre behavior when the distance gets extremely small.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def nParticle(*args, attribute: Optional[Union[str, bool]] = str, cache: bool = bool, conserve: Optional[Union[float, bool]] = float, count: bool = bool, deleteCache: bool = bool, dynamicAttrList: bool = bool, floatValue: float = float, gridSpacing: Optional[Union[float, bool]] = float, inherit: Optional[Union[float, bool]] = float, jitterBasePoint: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], jitterRadius: Optional[Union[float, bool]] = float, lowerLeft: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], name: Optional[Union[str, bool]] = str, numJitters: Optional[Union[int, bool]] = int, order: Optional[Union[int, bool]] = int, particleId: Optional[Union[int, bool]] = int, perParticleDouble: bool = bool, perParticleVector: bool = bool, position: Tuple[float, float, float] = [float, float, float], shapeName: Optional[Union[str, bool]] = str, upperRight: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], vectorValue: Tuple[float, float, float] = (float, float, float), edit: bool = bool, query: bool = bool):
    """
    The nParticle command creates a new nParticle object from a list of world space points. If an nParticle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    Args:
        attribute: (edit, query) - Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.       In query mode, this flag needs a value.
        cache: (create, edit, query) - Turns caching on/off for the particle shape.
        conserve: (edit, query) - Conservation of momentum control (between 0 and 1).  Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.
        count: (query) - Returns the number of particles in the object.
        deleteCache: (create) - Deletes the particle shapes cache. This command is not undoable.
        dynamicAttrList: (query) - Returns a list of the dynamic attributes in the object.
        floatValue: (edit) - Used only in per particle attribute edit.  Specifies that the edit is of a float attribute and must be followed by the new float value.
        gridSpacing: (create, multiuse, query) - Spacing between particles in the grid.
        inherit: (edit, query) - Inherit this fraction (0-1) of emitting object's velocity.
        jitterBasePoint: (create, multiuse, query) - Base point (center point) for jitters.  The command will create one swatch of jitters for each base point.  It will pair up other flags with base points in the order they are given in the command line.  If not enough instances of the other flags are availble, the last one on the line with be used for all other instances of -jpb.
        jitterRadius: (create, multiuse, query) - Max radius from the center to place the particle instances.
        lowerLeft: (create, multiuse, query) - Lower left point of grid.
        name: (edit, query) - name of particle object
        numJitters: (create, multiuse, query) - Number of jitters (instances) per particle.
        order: (edit, query) - Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried  or edited in the particle array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.       In query mode, this flag needs a value.
        particleId: (edit, query) - Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.       In query mode, this flag needs a value.
        perParticleDouble: (query) - Returns a list of the per-particle double attributes, excluding initial-state, cache, and information-only attributes.
        perParticleVector: (query) - Returns a list of the per-particle vector attributes, excluding initial-state, cache, and information-only attributes.
        position: (multiuse) - World-space position of each particle.
        shapeName: (edit, query) - Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.
        upperRight: (create, multiuse, query) - Upper right point of grid.
        vectorValue: (edit) - Used only in per particle attribute edit.  Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.
    """
    pass


def nSoft(*args, convert: bool = bool, duplicate: bool = bool, duplicateHistory: bool = bool, goal: Optional[Union[float, bool]] = float, hideOriginal: bool = bool, query: bool = bool):
    """
    Makes a nSoft body from the object(s) passed on the command line or in the selection list.  The geometry can be a NURBS, polygonal, lattice object.  The resulting nSoft body is made up of a hierarchy with a particle shape and a geometry shape, thus:

    Args:
        convert: (create) - This tells the command that you want the original object to be the actual deformed object.  The particle shape portion of the nSoft body will be inserted in the same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity).  If no flags are passed, then this is assumed.  The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.
        duplicate: (create) - This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object are duplicated.  You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a nSoft body. This flag and -dh are mutually exclusive.
        duplicateHistory: (create) - This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.
        goal: (create) - This is the same as -d, but in addition it tells the command that you want the resulting nSoft body to try to follow the original geometry, using the set goal weight as the value that controls how strongly it is to follow it.  A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The default value is 0.5.  This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant.  If you want history to be duplicated, you can use -dh and -g together.
        hideOriginal: (create) - This flag is used only when duplicating (-d, -g, or -dh).  If set to true, whichever of the two objects is NOT the nSoft object will be hidden. In other words, with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non-dynamic object as a goal for the nSoft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.
    """
    pass


def paintEffectsDisplay(*args, meshDrawEnable: bool = bool, query: bool = bool):
    """
    Command to set the global display methods for paint effects items

    Args:
        meshDrawEnable: (create, query) - Set whether mesh draw is enabled on objects
    """
    pass


def particle(*args, attribute: Optional[Union[str, bool]] = str, cache: bool = bool, conserve: Optional[Union[float, bool]] = float, count: bool = bool, deleteCache: bool = bool, dynamicAttrList: bool = bool, floatValue: float = float, gridSpacing: Optional[Union[float, bool]] = float, inherit: Optional[Union[float, bool]] = float, jitterBasePoint: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], jitterRadius: Optional[Union[float, bool]] = float, lowerLeft: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], name: Optional[Union[str, bool]] = str, numJitters: Optional[Union[int, bool]] = int, order: Optional[Union[int, bool]] = int, particleId: Optional[Union[int, bool]] = int, perParticleDouble: bool = bool, perParticleVector: bool = bool, position: Tuple[float, float, float] = [float, float, float], shapeName: Optional[Union[str, bool]] = str, upperRight: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], vectorValue: Tuple[float, float, float] = (float, float, float), edit: bool = bool, query: bool = bool):
    """
    The particle command creates a new particle object from a list of world space points. If a particle object is created, the command returns the names of the new particle shape and its associated particle object dependency node. If an object was queried, the results of the query are returned. Per particle attributes can be queried using the particleId or the order of the particle in the particle array. If an object was edited, nothing is returned.

    Args:
        attribute: (edit, query) - Used in per particle attribute query and edit. Specifies the name of the attribute being queried or edited.       In query mode, this flag needs a value.
        cache: (create, edit, query) - Turns caching on/off for the particle shape.
        conserve: (edit, query) - Conservation of momentum control (between 0 and 1).  Specifies the fraction of the particle shape's existing momentum which is conserved from frame to frame. A value of 1 (the default) corresponds to true Newtonian physics, in which momentum is conserved.
        count: (query) - Returns the number of particles in the object.
        deleteCache: (create) - Deletes the particle shapes cache. This command is not undoable.
        dynamicAttrList: (query) - Returns a list of the dynamic attributes in the object.
        floatValue: (edit) - Used only in per particle attribute edit.  Specifies that the edit is of a float attribute and must be followed by the new float value.
        gridSpacing: (create, multiuse, query) - Spacing between particles in the grid.
        inherit: (edit, query) - Inherit this fraction (0-1) of emitting object's velocity.
        jitterBasePoint: (create, multiuse, query) - Base point (center point) for jitters.  The command will create one swatch of jitters for each base point.  It will pair up other flags with base points in the order they are given in the command line.  If not enough instances of the other flags are availble, the last one on the line with be used for all other instances of -jpb.
        jitterRadius: (create, multiuse, query) - Max radius from the center to place the particle instances.
        lowerLeft: (create, multiuse, query) - Lower left point of grid.
        name: (edit, query) - name of particle object
        numJitters: (create, multiuse, query) - Number of jitters (instances) per particle.
        order: (edit, query) - Used in per particle attribute query and edit. Specifies the zero-based order (index) of the particle whose attribute is being queried  or edited in the particle array. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.       In query mode, this flag needs a value.
        particleId: (edit, query) - Used in per particle attribute query and edit. Specifies the id of the particle whose attribute is being queried or edited. Querying the value of a per particle attribute requires the -attribute and -id or -order flags and their arguments to precede the -q flag.       In query mode, this flag needs a value.
        perParticleDouble: (query) - Returns a list of the per-particle double attributes, excluding initial-state, cache, and information-only attributes.
        perParticleVector: (query) - Returns a list of the per-particle vector attributes, excluding initial-state, cache, and information-only attributes.
        position: (multiuse) - World-space position of each particle.
        shapeName: (edit, query) - Specify the shape name used for geometry instancing. DO not confuse this with the -n flag which names the particle object.
        upperRight: (create, multiuse, query) - Upper right point of grid.
        vectorValue: (edit) - Used only in per particle attribute edit.  Specifies that the edit is of a vector attribute and must be followed by all three float values for the vector.
    """
    pass


def particleExists(*args):
    """
    This command is used to query if a particle or soft object with the given name exists. Either the transform or shape name can be used as well as the name of the soft object.

    Args:
    """
    pass


def particleFill(*args, closePacking: bool = bool, doubleWalled: bool = bool, maxX: Optional[Union[float, bool]] = float, maxY: Optional[Union[float, bool]] = float, maxZ: Optional[Union[float, bool]] = float, minX: Optional[Union[float, bool]] = float, minY: Optional[Union[float, bool]] = float, minZ: Optional[Union[float, bool]] = float, particleDensity: Optional[Union[float, bool]] = float, resolution: Optional[Union[int, bool]] = int):
    """
    This command generates an nParticle system that fills the selected object with a grid of particles.

    Args:
        closePacking: (create) - If this is on then the particles are positioned as closely as possible in a hexagonal close packing arrangement. Otherwise particles are packed in a uniform grid lattice.
        doubleWalled: (create) - This flag should be used if the thickness of the object to fill has been modeled( for example a mug ). Otherwise the particles will be created inside the wall. Note that doubleWalled will not handle some cases very well. For example a double walled donut shape may get the center region of the donut filled. In cases like this it may be better to make the internal wall a separate mesh then fill that without using doubleWalled.
        maxX: (create) - The fill max bounds of the particles in X relative to the X bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.
        maxY: (create) - The fill max bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.
        maxZ: (create) - The fill max bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.
        minX: (create) - The fill lower bounds of the particles in X relative to the X bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.
        minY: (create) - The fill lower bounds of the particles in Y relative to the Y bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.
        minZ: (create) - The fill lower bounds of the particles in Z relative to the Z bounds of the object. A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.
        particleDensity: (create) - This controls the size of the particles. At a value of 1.0 the particle size will exactly match the grid spacing determined by the resolution parameter and the object bounds. Particles which overlap the surface will be rejected even if the center of the particle is inside.
        resolution: (create) - This determines the total number of particles generated. It represent the resolution along the largest axis of the object's bounding box. For a cube shape the total potential particles will be the cube of the resolution. For other shapes it will be less. The default value for this flag is 10, so 1000 particles could be generated for a cube shape.
    """
    pass


def particleInstancer(*args, addObject: bool = bool, aimAxis: Optional[Union[str, bool]] = str, aimDirection: Optional[Union[str, bool]] = str, aimPosition: Optional[Union[str, bool]] = str, aimUpAxis: Optional[Union[str, bool]] = str, aimWorldUp: Optional[Union[str, bool]] = str, attributeMapping: bool = bool, cycle: Optional[Union[str, bool]] = str, cycleStartObject: Optional[Union[str, bool]] = str, cycleStep: Optional[Union[float, bool]] = float, cycleStepUnits: Optional[Union[str, bool]] = str, index: Optional[Union[int, bool]] = int, instanceId: Optional[Union[str, bool]] = str, levelOfDetail: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, object: Optional[Union[str, bool]] = str, objectIndex: Optional[Union[str, bool]] = str, particleAge: Optional[Union[str, bool]] = str, position: Optional[Union[str, bool]] = str, removeObject: bool = bool, rotation: Optional[Union[str, bool]] = str, rotationOrder: Optional[Union[str, bool]] = str, rotationType: Optional[Union[str, bool]] = str, rotationUnits: Optional[Union[str, bool]] = str, scale: Optional[Union[str, bool]] = str, shear: Optional[Union[str, bool]] = str, visibility: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command is used to create a particle instancer node and set the proper attributes in the particle shape and in the instancer node.  It will also create the connections needed between the particle shape and the instancer node.

    Args:
        addObject: (create, edit) - This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        aimAxis: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the aim axis of the instanced objects.
        aimDirection: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the aim direction of the instanced objects.
        aimPosition: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the aim position of the instanced objects.
        aimUpAxis: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the aim up axis of the instanced objects.
        aimWorldUp: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the aim world up of the instanced objects.
        attributeMapping: (query) - This flag queries the particle attribute mapping list.
        cycle: (create, edit, query) - This flag sets or queries the cycle attribute for the instancer node.  The options are "none", "sequential". The default is "none".
        cycleStartObject: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the cycle start object of the instanced objects.
        cycleStep: (create, edit, query) - This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnits).
        cycleStepUnits: (create, edit, query) - This flag sets or queries the cycle step unit attribute for the instancer node. The options are "frames" or "seconds".  The default is "frames".
        index: (query) - This flag is used to query the name of the ith instanced object.
        instanceId: (query) - This flag queries the particle attribute name to be used for the id of the instanced objects.
        levelOfDetail: (create, edit, query) - This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox" or "boundingBoxes".  The default is "geometry".
        name: (create, query) - This flag sets or queries the name of the instancer node.
        object: (create, edit, multiuse, query) - This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -addObject and -remove flags.  If neither of these flags is specified on the command line then -addObject is assumed.
        objectIndex: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the object index of the instanced objects.
        particleAge: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the age of the instanced objects.
        position: (create, edit, query) - DEFAULT "worldPosition" This flag sets or queries the particle attribute name to be used for the positions of the instanced objects.  By default the attribute is worldPosition.
        removeObject: (edit) - This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        rotation: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the rotation of the instanced objects.
        rotationOrder: (create, edit, query) - This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        rotationType: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the rotation type of the instanced objects.
        rotationUnits: (create, edit, query) - This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        scale: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the scale of the instanced objects.
        shear: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the shear of the instanced objects.
        visibility: (create, edit, query) - This flag sets or queries the particle attribute name to be used for the visibility of the instanced objects.
    """
    pass


def particleRenderInfo(*args, attrList: Optional[Union[int, bool]] = int, attrListAll: bool = bool, name: Optional[Union[int, bool]] = int, renderTypeCount: bool = bool, query: bool = bool):
    """
    This action provides information access to the particle render subclasses. These are derived from TdynRenderBase. This action is used primarily by the Attribute Editor to gather information about attributes used for rendering.

    Args:
        attrList: (query) - Return the list of attributes used by this render type.
        attrListAll: (query) - Return a complete list of all render attributes used by the particle object. This also includes the per particle attributes.
        name: (query) - Return the name of the render subclass using the render type.
        renderTypeCount: (query) - Return the count of registered render classes for particle.
    """
    pass


def pfxstrokes(*args, filename: Optional[Union[str, bool]] = str, postCallback: bool = bool, selected: bool = bool):
    """
    This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write the current state of all the tubes to a file. For normal stroke nodes tubes must be ON in the brush or there will be no output. For pfxHair nodes there will always be output, but the format is different than for stroke nodes(however one can assign a brush with tubes = ON to a pfxHair node, in which case it will output the same format as strokes). The general file format is ASCII, using commas to separate numerical values and newlines between blocks of data. The format used for pfxHair nodes presents the hair curves points in order from root to tip of the hair. The hairs follow sequentially in the following fashion: NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc... NumCvs pointX,pointY,pointZ, normalX,normalY,normalZ, width, colorR,colorG,colorB, paramU etc.. The format used to output files for brushes with tubes=ON is more complex. The tubes can branch and the order the segments are written is the same order they are drawn in. Slowly drawing a tall grass brush in the paint effects panel can help to illustrate the order the segments will appear in the file. New tubes can start "growing" before others are finished. There is no line for "NumCvs". Instead all data for each segment appears on each line. The data on each line is the same as passed into the paint effects runtime function. See the argument list of paintRuntimeFunc.mel for the order and a description of these parameters. The parameters match up exactly in the order they appear on a line of the output file with the order of arguments to this function. If one wishes to parse the output file and connect the segments together into curves the branchId, parentId and siblingCnt parameters can help when sorting which segment connects to which line. Using the -postCallback option will write out the tubes data after it has been proessed by the runTime callback.

    Args:
        filename: (create) - The output file.
        postCallback: (create) - Output information to the file after the Runtime Callback MEL function has been invoked. The default is to output the information prior to the callback.
        selected: (create) - Only loop through the selected strokes.
    """
    pass


def radial(*args, attenuation: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, type: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        type: (edit, query) - Type of radial field (0 - 1).  This controls the algorithm by which the field is attenuated. Type 1, provided for backward compatibility, specifies the same algorithm as Alias | Wavefront Dynamation. A value between 0 and 1 yields a linear blend.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def resampleFluid(*args, resampleDepth: Optional[Union[int, bool]] = int, resampleHeight: Optional[Union[int, bool]] = int, resampleWidth: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    A command to extend the fluid grid, keeping the voxels the same size, and keeping the existing contents of the fluid in the same place. Note that the fluid transform is also modified to make this possible.

    Args:
        resampleDepth: (create, edit, query) - Change depth resolution to this value
        resampleHeight: (create, edit, query) - Change height resolution to this value
        resampleWidth: (create, edit, query) - Change width resolution to this value
    """
    pass


def rigidBody(*args, active: bool = bool, angularVelocity: bool = bool, applyForceAt: Optional[Union[str, bool]] = str, bounciness: Optional[Union[float, bool]] = float, cache: bool = bool, centerOfMass: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), collisions: bool = bool, contactCount: bool = bool, contactName: bool = bool, contactPosition: bool = bool, damping: Optional[Union[float, bool]] = float, deleteCache: bool = bool, dynamicFriction: Optional[Union[float, bool]] = float, force: bool = bool, ignore: bool = bool, impulse: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), impulsePosition: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), initialAngularVelocity: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), initialVelocity: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), layer: Optional[Union[int, bool]] = int, lockCenterOfMass: bool = bool, mass: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, orientation: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), particleCollision: bool = bool, passive: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), removeShape: Optional[Union[str, bool]] = str, solver: Optional[Union[str, bool]] = str, spinImpulse: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), standInObject: Optional[Union[str, bool]] = str, staticFriction: Optional[Union[float, bool]] = float, tesselationFactor: Optional[Union[int, bool]] = int, velocity: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a rigid body from a polygonal or nurbs surface.

    Args:
        active: (create, edit, query) - Creates a rigid body that is active.  An active rigid body accepts and causes collisions and is effected by dynamic fields.  This is the default.
        angularVelocity: (query) - Current angular velocity of rigid body.
        applyForceAt: (create, edit, query) - Determines how forces are applied to the rigid body. The choices are centerOfMass | boundingBox | verticesOrCVs. Default: boundingBox
        bounciness: (create, edit, query) - Sets the restitution (or bounciness) of the rigid body. Range:   0.0 - 2.0 Default: 0.6
        cache: (create, edit, query) - Turns caching on (1) or off (0) for the rigid body. Default: off
        centerOfMass: (create, edit, query) - Sets the center of mass (x,y,z) of the rigid body. Default: actual center of mass.
        collisions: (create, edit, query) - Truns collisions on/off for the rigid body.  If the collisions are turned of the rigid body will not collide with any other rigid body. Default: on.
        contactCount: (query) - returns the current contact count for the rigid body.
        contactName: (query) - returns all the rigid body names which are in contact with this shape.  One name for each contact will be returned.
        contactPosition: (query) - returns all the contact position.  One position for each contact will be returned.
        damping: (create, edit, query) - Sets the damping value of the rigid body. Range:   -2.0 - 2.0 Default: 0.0
        deleteCache: (edit) - Deletes the cache (if one exists) of the rigid body.
        dynamicFriction: (create, edit, query) - Sets the dynamic friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2
        force: (query) - Current force on the rigid body.
        ignore: (create, edit, query) - Causes the rigid body to be ignored in the rigid solver. Default: off
        impulse: (create, edit) - Applies an impulse (instantaneous) force on a rigid body. Default: 0.0 0.0 0.0
        impulsePosition: (create, edit) - The position at which the impulse is applied. Default: the bodies center of mass.
        initialAngularVelocity: (create, edit, query) - Sets the initial angular velocity of the rigid body. Default: 0.0 0.0 0.0
        initialVelocity: (create, edit, query) - Sets the initial velocity of the rigid body. Default: 0.0 0.0 0.0
        layer: (create, edit, query) - Sets the collision layer of the rigid body.  Only rigid bodies in the same collision layer can collide with each other. Range:   >= 0 Default: 0.
        lockCenterOfMass: (create, edit, query) - Locks the center of mass for the rigid body. Default: off
        mass: (create, edit, query) - Sets the mass of the rigid body. Range:   > 0 Default: 1.0
        name: (create, edit, query) - Assigns the rigid body the given name.
        orientation: (create, edit, query) - Sets the initial orientation (x,y,z) of the rigid body. Default: current orientation.
        particleCollision: (create, edit, query) - Turns the ability for a rigid body to collide with particles on and off.  The particles will exert a force on the rigid body. Default: off
        passive: (create, edit, query) - Creates a rigid body that is passive.  A passive rigid body does not react to collisions but active rigid bodies can collide with it. Dynamic Fields will not effect a passive rigid body.  Only passive rigid bodies can be keyframed.
        position: (create, edit, query) - Sets the initial position (x,y,z) of the rigid body. Default: current position.
        removeShape: (create, edit, query) - Remove the named shape.
        solver: (create, edit, query) - The name of the solver which this rigid node is to resided.  If the solver does not exists then the rigid body will not be created.  If the edit flag is thrown add the solver exists, the rigid body will be moved to that solver.
        spinImpulse: (create, edit) - Applies an spin impulse (instantaneous rotational) force on a rigid body. Default: 0.0 0.0 0.0
        standInObject: (create, edit, query) - Causes the simulator to use a stand in object for the simulation. The choices are none | cube | sphere. The default is none. Default: none
        staticFriction: (create, edit, query) - Sets the static friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2
        tesselationFactor: (create, query) - Sets the tesselation factor for a rigid body surface. Range:   >= 10 Default: 200.
        velocity: (query) - Current velocity of rigid body.
    """
    pass


def rigidSolver(*args, autoTolerances: bool = bool, bounciness: bool = bool, cacheData: bool = bool, collide: bool = bool, collisionTolerance: Optional[Union[float, bool]] = float, contactData: bool = bool, create: bool = bool, current: bool = bool, deleteCache: bool = bool, displayCenterOfMass: bool = bool, displayConstraint: bool = bool, displayVelocity: bool = bool, dynamics: bool = bool, friction: bool = bool, interpenetrate: bool = bool, interpenetrationCheck: bool = bool, name: Optional[Union[str, bool]] = str, rigidBodies: bool = bool, rigidBodyCount: bool = bool, showCollision: bool = bool, showInterpenetration: bool = bool, solverMethod: Optional[Union[int, bool]] = int, startTime: Optional[Union[float, bool]] = float, state: bool = bool, statistics: bool = bool, stepSize: Optional[Union[float, bool]] = float, velocityVectorScale: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command sets the attributes for the rigid solver

    Args:
        autoTolerances: (edit, query) - Turns the auto tolerance calculation on and off.  The auto tolerances calculation will override the default or user defined values of the step size and collision tolerance value that is calculated based on the objects in the scene. Default: 0 (off)
        bounciness: (edit, query) - Turns bounciness on and off for the an the objects in the simulation. Default value: on
        cacheData: (edit, query) - Turns the cache on fall all rigid bodies in the system. Default value: off
        collide: (edit, query) - Disallows the interpenetration of the two rigid bodies listed. Default: Collide is on for all bodies.
        collisionTolerance: (edit, query) - Sets the collision tolerance.  This is the error at which two objects are considered to have collided. Range:   0.0005 - 1.000 Default: 0.02
        contactData: (edit, query) - Turns the contact data information on/off for all rigid bodies. Default value: off
        create: (create) - Creates a new rigid solver.
        current: (create) - Sets rigid solver as the current solver.
        deleteCache: (edit, query) - Deletes the cache for all rigid bodies in the system.
        displayCenterOfMass: (edit, query) - Displays the center of mass icon. Default value: on
        displayConstraint: (edit, query) - Displays the constraint vectors. Default value: on
        displayVelocity: (edit, query) - Displays the velocity vectors. Default value: off
        dynamics: (edit, query) - Turns dynamics on and off for the an the objects in the simulation. Default value: on
        friction: (edit, query) - Turns friction on and off for the an the objects in the simulation. Default value: on
        interpenetrate: (edit, query) - Allows the two rigid bodies listed to interpenetrate. Default: interpenetration is off for all bodies.
        interpenetrationCheck: (edit) - Checks for interpenetrating rigid bodies in the scene.
        name: (create, edit, query) - Name of the new object
        rigidBodies: (query) - Returns a list of rigid bodies in the solver.
        rigidBodyCount: (query) - Returns the number of rigid bodies in the solver.
        showCollision: (edit, query) - Displays the colliding objects in a different color.
        showInterpenetration: (edit, query) - Displays the interpenetrating objects in a different color.
        solverMethod: (edit, query) - Sets the solver method.  The choices are 0 | 1 | 2. 0 = Euler (fastest/least acurate), 1 = Runge-Kutta ( slower/more acurate), 2 = adaptive Runge-Kutta (slowest/most acurate). The default is 2 (adaptive Runge-Kutta)
        startTime: (create, edit, query) - Sets the start time for the solver.
        state: (edit, query) - Turns the rigid solver on or off.
        statistics: (edit, query) - Turns the statistic information on/off for all rigid bodies. Default value: off
        stepSize: (edit, query) - Sets the solvers step size.  This is the maximum size of a single step the solver will take at one time. Range:   0.0004 - 0.100 Default: 0.0333
        velocityVectorScale: (edit, query) - scales the velocity vector display. Default value: 1.0
    """
    pass


def runup(*args, cache: bool = bool, fromPreviousFrame: bool = bool, fromStartFrame: bool = bool, maxFrame: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], state: bool = bool):
    """
    runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it does so.   If no max frame is specified, runup runs up to the current time.

    Args:
        cache: (create) - Cache the state after the runup.
        fromPreviousFrame: (create) - Run up the animation from the previously evaluated frame. If no flag is supplied this is the default.
        fromStartFrame: (create) - Run up the animation from the start frame. If no flag is supplied -fromPreviousFrame is the default.
        maxFrame: (create) - Ending time for runup, in current user time units. The runup will always start at the minimum start frame for all dynamic objects.
        state: (create) - Turns runup and cache on/off.
    """
    pass


def saveFluid(*args, currentTime: Optional[Union[int, bool]] = int, endTime: Optional[Union[int, bool]] = int, startTime: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    A command to save the current state of the fluid to the initial state cache. The grids to be saved are determined by the cache attributes: cacheDensity, cacheVelocity, etc. These attributes are normally set from the options on Set Initial State. The cache must be set up before invoking this command.

    Args:
        currentTime: (create, edit, query) - cache state of fluid at current time
        endTime: (create, edit, query) - end Time for cacheing
        startTime: (create, edit, query) - start Time for cacheing
    """
    pass


def saveInitialState(*args, attribute: Optional[Union[str, bool]] = str, saveall: bool = bool):
    """
    saveInitialState saves the current state of dynamics objects as the initial state.  A dynamic object is a particle shape, rigid body, rigid constraint or rigid solver.  If no objects are specified, it saves the initial state for any selected objects. It returns the names of the objects for which initial state was saved.

    Args:
        attribute: (create, multiuse) - Save the initial state of the specified attribute only. This is a multi-use flag.
        saveall: (create) - Save the initial state for all dynamics objects in the scene.
    """
    pass


def setDynamic(*args, allOnWhenRun: bool = bool, disableAllOnWhenRun: bool = bool, setAll: bool = bool, setOff: bool = bool, setOn: bool = bool):
    """
    setDynamic sets the isDynamic attribute of particle objects on or off.  If no objects are specified, it sets the attribute for any selected objects.  If -all is thrown, it sets the attribute for all particle objects in the scene. By default it sets the attribute true (on); if the -off flag is thrown, it sets the attribute false (off).

    Args:
        allOnWhenRun: (create) - Obsolete, no longer suppported or necessary.
        disableAllOnWhenRun: (create) - Obsolete, no longer suppported or necessary.
        setAll: (create) - Set for all objects.
        setOff: (create) - Sets isDynamic false.
        setOn: (create) - Sets isDynamic true.  This flag is set by default.
    """
    pass


def setFluidAttr(*args, addValue: bool = bool, attribute: Optional[Union[str, bool]] = str, clear: bool = bool, floatRandom: float = float, floatValue: float = float, lowerFace: bool = bool, reset: bool = bool, vectorRandom: Tuple[float, float, float] = (float, float, float), vectorValue: Tuple[float, float, float] = (float, float, float), xIndex: Optional[Union[int, bool]] = int, xvalue: bool = bool, yIndex: Optional[Union[int, bool]] = int, yvalue: bool = bool, zIndex: Optional[Union[int, bool]] = int, zvalue: bool = bool):
    """
    Sets values of built-in fluid attributes such as density, velocity, etc., for individual grid cells or for all cells in the grid.

    Args:
        addValue: () - Add specified value to attribute
        attribute: (create) - Specifies the fluid attribute for which to set values.  Valid attributes are "velocity", "density", "fuel", "color", "falloff", and "temperature".
        clear: () - Set this attribute to 0
        floatRandom: () - If this was a scalar (e.g. density) attribute, use a random value in +-VALUE If fv is specified, it is used as the base value and combined with the random value. If the fv flag is not specified, the  base is assumed to be 0.
        floatValue: () - If this was a scalar (e.g. density) attribute, use this value
        lowerFace: (create) - Only valid with "-at velocity".  Since velocity values are stored on the edges of each voxel and not at the center, using voxel based indices to set velocity necessarily affects neighboring voxels.  Use this flag to only set velocity components on the lower left three faces of a voxel, rather than all six.
        reset: () - Set this attribute to default value
        vectorRandom: () - If this was a vector (e.g. velocity) attribute, use a random value in +-VALUE If vv is specified, it is used as the base value and combined with the random value. If the vv flag is not specified, the  base is assumed to be 0,0,0.
        vectorValue: () - If this was a vector (e.g. velocity) attribute, use this value
        xIndex: (create) - Only return values for cells with this X index
        xvalue: () - Only set the first component of the vector-valued attribute specified by the "-at/attribute" flag.
        yIndex: (create) - Only return values for cells with this Y index
        yvalue: () - Only set the second component of the vector-valued attribute specified by the "-at/attribute" flag.
        zIndex: (create) - Only return values for cells with this Z index
        zvalue: () - Only set the third component of the vector-valued attribute specified by the "-at/attribute" flag.
    """
    pass


def setParticleAttr(*args, attribute: Optional[Union[str, bool]] = str, floatValue: Optional[Union[float, bool]] = float, object: Optional[Union[str, bool]] = str, randomFloat: Optional[Union[float, bool]] = float, randomVector: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), relative: bool = bool, vectorValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float)):
    """
    This action will set the value of the chosen attribute for every particle or selected component in the selected or passed particle object. Components should not be passed to the command line. For setting the values of components, the components must be selected and only the particle object's names should be passed to this action. If the attribute is a vector attribute and the -vv flag is passed, then the three floats passed will be used to set the values.  If the attribute is a vector and the -fv flag is pass and the -vv flag is not passed, then the float will be repeated for each of the X, Y, and Z values of the attribute.  Similarly, if the attribute is a float attribute and a vector value is passed, then the length of the vector passed will be used for the value. Note:  The attribute passed must be a Per-Particle attribute.

    Args:
        attribute: (create) - Tells the action which attribute you want to set
        floatValue: (create) - Tells what you want the value to be set to of a float attribute
        object: (create) - If this flag is passed and the STRING is the name of a particle object's transform or shape, then ONLY that object will be edited, ignoring the selection list or command line, and ALL of its particles' values will be changed for the specified attribute.
        randomFloat: (create) - Tells the command to add a random value from -FLOAT to +FLOAT to the results of each particle.  The default is 0.0.
        randomVector: (create) - Tells the command to add a random value from <<-x,-y,-z>> to <<x,y,z>> to the results of each particle. The default 0 0 0.
        relative: (create) - If this is set to TRUE (the default is FALSE), then the float or vector value will be added to the current value for each particle.
        vectorValue: (create) - Tells what you want the value to be set to of a vector attribute
    """
    pass


def soft(*args, convert: bool = bool, duplicate: bool = bool, duplicateHistory: bool = bool, goal: Optional[Union[float, bool]] = float, hideOriginal: bool = bool, name: str = str, query: bool = bool):
    """
    Makes a soft body from the object(s) passed on the command line or in the selection list.  The geometry can be a NURBS, polygonal, lattice object.  The resulting soft body is made up of a hierarchy with a particle shape and a geometry shape, thus:

    Args:
        convert: (create) - This tells the command that you want the original object to be the actual deformed object.  The particle shape portion of the soft body will be inserted in the same hierarchy as the original, under the same parent (with one additional intervening transform which is initially the identity).  If no flags are passed, then this is assumed.  The combination -c -h 1 is not valid; if you have this in your scripts, remove the -h 1.
        duplicate: (create) - This tells the command that you want to make a copy of the original object and use the copy as the deforming geometry. Input connections to the original object are duplicated.  You would do this if you wanted to keep the original object in your scene and also have a copy of it that was a soft body. This flag and -dh are mutually exclusive.
        duplicateHistory: (create) - This is the same as -d, except that upstream history, is duplicated as well, instead of just input connections. This flag and -d are mutually exclusive.
        goal: (create) - This is the same as -d, but in addition it tells the command that you want the resulting soft body to try to follow the original geometry, using the set goal weight as the value that controls how strongly it is to follow it.  A value of 1.0 will try to follow exactly, and a value of 0.0 will not follow at all. The default value is 0.5.  This value must be from 0.0 to 1.0. You could use -d with -g, but it is redundant.  If you want history to be duplicated, you can use -dh and -g together.
        hideOriginal: (create) - This flag is used only when duplicating (-d, -g, or -dh).  If set to true, whichever of the two objects is NOT the soft object will be hidden. In other words, with -d -h true, the original object will be hidden; with -d -c -h 1 the duplicate object will be hidden. You would typically do this if you want to use the non-dynamic object as a goal for the soft one (see -g) but you do not want it visible in the scene. The flags -h 1 and -c are mutually exclusive.
        name: () - This flag is obsolete.  If you wish to give your new soft object a name, use the rename command (or from the UI, use the outliner).
    """
    pass


def spring(*args, addSprings: bool = bool, allPoints: bool = bool, count: bool = bool, damping: Optional[Union[float, bool]] = float, dampingPS: Optional[Union[float, bool]] = float, endForceWeight: Optional[Union[float, bool]] = float, exclusive: bool = bool, length: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, minDistance: Optional[Union[float, bool]] = float, minMax: bool = bool, name: Optional[Union[str, bool]] = str, noDuplicate: bool = bool, restLength: Optional[Union[float, bool]] = float, restLengthPS: Optional[Union[float, bool]] = float, startForceWeight: Optional[Union[float, bool]] = float, stiffness: Optional[Union[float, bool]] = float, stiffnessPS: Optional[Union[float, bool]] = float, useDampingPS: bool = bool, useRestLengthPS: bool = bool, useStiffnessPS: bool = bool, walkLength: Optional[Union[int, bool]] = int, wireframe: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The spring command can do any of the following:

    Args:
        addSprings: (create) - If specified, springs will be added to the existing selected set of springs. (Default is to create a new spring object.)
        allPoints: (create, edit) - If True, sets the mode of spring application to All.  This will add springs between all points selected. (Default is False.)
        count: (query) - Return the number of springs in the shape.  Query-only. We maintain this flag only for compatibility with earlier versions of Maya.  To get the count of springs, it is much faster and simpler to use the spring shape's count attribute: getAttr <shapeName>.count.
        damping: (create, edit, query) - Damping factor for the springs created in the spring object. (Default = 0.2 )
        dampingPS: (create, edit, query) - Damping factor for the springs created in the spring object. This will initialize all the entries in dampingPS to the specified value. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = 0.2 )
        endForceWeight: (create, edit, query) - Amount of the force of the spring that gets applied to the point to which the spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )
        exclusive: (create) - If true, tells the command to create springs only between pairs of points which are not in the same object. (Default is False.)
        length: (create, edit, query) - Vestigial form of "restLength." Please use "restLength" instead.
        maxDistance: (create, edit) - Maximum distance between two points that a spring would be considered.
        minDistance: (create) - Minimum distance between two points that a spring would be considered. (Default = 0.0. See Defaults for more information on this flag's default.)
        minMax: (create) - If True, sets the mode of the spring application to Min/Max. This will add springs between all points from the specified point groups that are between the minimum and maximum distance values set with min and max. (Default is False.) Note: This gets automatically set if either the min or max flags are used.
        name: (create, query) - Name of spring object.
        noDuplicate: (create) - Check for existing springs and don't add a new spring between two points already connected by a spring in the same object. Only the object the command is working on is checked.  This flag is relevant only when using -add. (Default = false)
        restLength: (create, edit, query) - Per-object rest length for the new springs. Springs can use either their per-object or per-spring rest length.  See the -lPS and -ulp flags.
        restLengthPS: (create, edit, query) - Per-spring rest length for the new springs. This will initialize all the entries in restLengthPS to the specified value. If this flag is not thrown, each rest length will be initialized to the distance between the two  points at the time the spring is created (i.e., the initial length of the spring).   When playing back, springs can use either their per-spring or per-object rest length.  See the -rl and -urp flags. In both the flag and the attribute name, "PS" stands for "per-spring."
        startForceWeight: (create, edit, query) - Amount of the force of the spring that gets applied to the point from which the spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )
        stiffness: (create, edit, query) - Stiffness of the springs created in the spring object. (Default = 1.0 ) -damp float Vestigial form of "damping."  Please use "damping" instead.
        stiffnessPS: (create, edit, query) - Stiffness of the springs created in the spring object. This will initialize all the entries in stiffnessPS to the specified value. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = 1.0 )
        useDampingPS: (create, edit, query) - Specifies whether to use dampingPS (per spring damping). If set to false, the per object damping attribute value will be used. This flag simply sets the useDampingPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )
        useRestLengthPS: (create, edit, query) - Specifies whether to use restLengthPS (per spring restLength). If set to false, the per object restLength attribute value will be used. This flag simply sets the useRestLengthPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )
        useStiffnessPS: (create, edit, query) - Specifies whether to use stiffnessPS (per spring stiffness). If set to false, the per object stiffness attribute value will be used. This flag simply sets the useStiffnessPS attribute of the spring shape. In both the flag and the attribute name, "PS" stands for "per-spring." (Default = false )
        walkLength: (create) - This flag is valid only when doing wireframe creation. It will create springs between pairs of points connected by the specified number of edges.  For example, if walk length is 2, each pair of points separated by no more than 2 edges will get a spring.  Walk length measures the distance between pairs of vertices just like the number of blocks measures the distance between two intersections in a city.
        wireframe: (create) - If True, sets the mode of the spring application to Wireframe. This is valid only for springs created on a soft body. It will add springs along all edges connecting the adjacent points (vertices or CV's) of curves and surfaces. (Default is False.)
    """
    pass


def stroke(*args, name: Optional[Union[str, bool]] = str, pressure: bool = bool, seed: Optional[Union[int, bool]] = int):
    """
    The stroke command creates a new Paint Effects stroke node.

    Args:
        name: (create) - Sets the name of the stroke to the input string
        pressure: (create) - On creation, allows the copying of the pressure mapping settings from the Paint Effects Tool. Default is false.
        seed: (create) - Sets the random seed for this stroke.
    """
    pass


def truncateFluidCache(*args, edit: bool = bool, query: bool = bool):
    """
    This command sets the end time of a fluid cache to the current time. If the current time is less than the end time of the cache, the cache is truncated so that only the portion of the cache up to and including the current time is preserved.

    Args:
    """
    pass


def truncateHairCache(*args, edit: bool = bool, query: bool = bool):
    """
    This command sets the end time of a hair cache to the current time. If the current time is less than the end time of the cache, the cache is truncated so that only the portion of the cache up to and including the current time is preserved.

    Args:
    """
    pass


def turbulence(*args, attenuation: Optional[Union[float, bool]] = float, frequency: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, noiseLevel: Optional[Union[int, bool]] = int, noiseRatio: Optional[Union[float, bool]] = float, perVertex: bool = bool, phase: Optional[Union[float, bool]] = float, phaseX: Optional[Union[float, bool]] = float, phaseY: Optional[Union[float, bool]] = float, phaseZ: Optional[Union[float, bool]] = float, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        frequency: (edit, query) - Frequency of turbulence field. This determines how often motion is disrupted.
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        noiseLevel: (edit, query) - If the noiseLevel parameter is greater than zero, the field will do multiple lookups in the table.  Each additional lookup is weighted using noiseRatio (which see).  The noiseLevel is the number of additional lookups, so if noiseLevel is 0, there is just one lookup.  A value of 0 (the default) corresponds to the way the field behaved prior to Maya 3.0.
        noiseRatio: (edit, query) - If noiseLevel is greater than zero, then noiseRatio is the relative magnitude for each consecutive noise evaluation. These are cumulative: for example, if noiseRatio is 0.5, then the first evaluation is weighted 0.5, the second 0.25, and so on. Has no effect if noiseLevel is zero.
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        phase: (edit, query) - Phase shift of turbulence field. This influences the direction of the disruption.  This flag is obsolete and is retained only for backward compatibility.  It is replaced by -phaseX, -phaseY, and -phaseZ.  Setting -phase is identical to setting -phaseZ (the phase shift was always in the Z dimension).
        phaseX: (edit, query) - X component of phase shift of turbulence field. This influences the direction of the disruption.
        phaseY: (edit, query) - Y component of phase shift of turbulence field. This influences the direction of the disruption.
        phaseZ: (edit, query) - Z component of phase shift of turbulence field. This influences the direction of the disruption.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def uniform(*args, attenuation: Optional[Union[float, bool]] = float, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        directionX: (edit, query) - X-component of direction.
        directionY: (edit, query) - Y-component of direction.
        directionZ: (edit, query) - Z-component of direction
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def volumeAxis(*args, alongAxis: Optional[Union[float, bool]] = float, aroundAxis: Optional[Union[float, bool]] = float, attenuation: Optional[Union[float, bool]] = float, awayFromAxis: Optional[Union[float, bool]] = float, awayFromCenter: Optional[Union[float, bool]] = float, detailTurbulence: Optional[Union[float, bool]] = float, directionX: Optional[Union[float, bool]] = float, directionY: Optional[Union[float, bool]] = float, directionZ: Optional[Union[float, bool]] = float, directionalSpeed: Optional[Union[float, bool]] = float, invertAttenuation: bool = bool, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, turbulence: Optional[Union[float, bool]] = float, turbulenceFrequencyX: Optional[Union[float, bool]] = float, turbulenceFrequencyY: Optional[Union[float, bool]] = float, turbulenceFrequencyZ: Optional[Union[float, bool]] = float, turbulenceOffsetX: Optional[Union[float, bool]] = float, turbulenceOffsetY: Optional[Union[float, bool]] = float, turbulenceOffsetZ: Optional[Union[float, bool]] = float, turbulenceSpeed: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        alongAxis: (edit, query) - Initial velocity multiplier in the direction along the central axis of the volume.  See the diagrams in the documentation.
        aroundAxis: (edit, query) - Initial velocity multiplier in the direction around the central axis of the volume.  See the diagrams in the documentation.
        attenuation: (edit, query) - Attentuation rate of field
        awayFromAxis: (edit, query) - Initial velocity multiplier in the direction away from the central axis of the volume.  See the diagrams in the documentation.  Used only with the cylinder, cone, and torus volumes.
        awayFromCenter: (edit, query) - Initial velocity multiplier in the direction away from the center point of a cube or sphere volume. Used only with the cube and sphere volumes.
        detailTurbulence: (edit, query) - The relative intensity of a second higher frequency turbulence. This can be used to create fine features in large scale flows. Both the speed and the frequency on this second turbulence are higher than the primary turbulence. When the detailTurbulence is non-zero the simulation may run a bit slower, due to the computation of a second turbulence.
        directionX: (edit, query) - x-component of force direction.  Used with directional speed.
        directionY: (edit, query) - y-component of force direction.  Used with directional speed.
        directionZ: (edit, query) - z-component of force direction.  Used with directional speed.
        directionalSpeed: (edit, query) - Adds a component of speed in the direction specified by the directionX, Y, and Z attributes.
        invertAttenuation: (edit, query) - If this attribute is FALSE, the default, then the attenuation makes the field's effect decrease as the affected point is further from the volume's axis and closer to its edge.  If the is set to TRUE, then the effect of the field increases in this case, making the full effect of the field felt at the volume's edge.
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        turbulence: (edit, query) - Adds a force simulating a turbulent wind that evolves over time.
        turbulenceFrequencyX: (edit, query) - The repeats of the turbulence function in X.
        turbulenceFrequencyY: (edit, query) - The repeats of the turbulence function in Y.
        turbulenceFrequencyZ: (edit, query) - The repeats of the turbulence function in Z.
        turbulenceOffsetX: (edit, query) - The translation of the turbulence function in X.
        turbulenceOffsetY: (edit, query) - The translation of the turbulence function in Y.
        turbulenceOffsetZ: (edit, query) - The translation of the turbulence function in Z.
        turbulenceSpeed: (edit, query) - The rate of change of the turbulence over time. The turbulence loops seamlessly every 1.0/turbulenceSpeed seconds. To animate this rate attach a new time node to the time input on the volumeAxisNode then animate the time value on the time node.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


def vortex(*args, attenuation: Optional[Union[float, bool]] = float, axisX: Optional[Union[float, bool]] = float, axisY: Optional[Union[float, bool]] = float, axisZ: Optional[Union[float, bool]] = float, magnitude: Optional[Union[float, bool]] = float, maxDistance: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, perVertex: bool = bool, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], torusSectionRadius: Optional[Union[float, bool]] = float, volumeExclusion: bool = bool, volumeOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], volumeShape: Optional[Union[str, bool]] = str, volumeSweep: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    For each listed object, the command creates a new field. The field has a shape which lives in the DAG and it has an associated dependency node. The field is added to the list of fields owned by the object. Use connectDynamic to cause the field to affect a dynamic object. Note that if more than one object is listed, a separate field is created for each object.

    Args:
        attenuation: (edit, query) - Attentuation rate of field
        axisX: (edit, query) - X-component of vortex axis
        axisY: (edit, query) - Y-component of vortex axis
        axisZ: (edit, query) - Z-component of vortex axis
        magnitude: (edit, query) - Strength of field.
        maxDistance: (edit, query) - Maximum distance at which field is exerted. -1 indicates that the field has no maximum distance.
        name: (edit, query) - name of field
        perVertex: (edit, query) - Per-vertex application. If this flag is set true, then each individual point (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the force field. If this flag is set to false, then the froce is exerted only from the geometric center of the set of points.
        position: (edit, multiuse, query) - Position in space (x,y,z) where you want to place a gravity field. The gravity then emanates from this position in space rather than from an object. Note that you can both use -pos (creating a field at a position) and also provide object names.
        torusSectionRadius: (edit, query) - Section radius for a torus volume.  Applies only to torus. Similar to the section radius in the torus modelling primitive.
        volumeExclusion: (edit, query) - Volume exclusion of the field.  If true, points outside the volume (defined by the volume shape attribute) are affected,  If false, points inside the volume are affected.  Has no effect if volumeShape is set to "none."
        volumeOffset: (edit, query) - Volume offset of the field.  Volume offset translates the field's volume by the specified amount from the actual field location. This is in the field's local space.
        volumeShape: (edit, query) - Volume shape of the field.  Sets/edits/queries the field's volume shape attribute.  If set to any value other than "none", determines a 3-D volume within which the field has effect. Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."
        volumeSweep: (edit, query) - Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.  Similar effect to the sweep attribute in modelling.
    """
    pass


