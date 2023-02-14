from typing import Union, Optional, List, Tuple

def about(*args, apiVersion: bool = bool, application: bool = bool, batch: bool = bool, buildDirectory: bool = bool, buildVariant: bool = bool, codeset: bool = bool, compositingManager: bool = bool, connected: bool = bool, creativeVersion: bool = bool, ctime: bool = bool, currentDate: bool = bool, currentTime: bool = bool, customVersion: bool = bool, customVersionClient: bool = bool, customVersionMajor: bool = bool, customVersionMinor: bool = bool, customVersionString: bool = bool, cutIdentifier: bool = bool, date: bool = bool, environmentFile: bool = bool, evalVersion: bool = bool, file: bool = bool, fontInfo: bool = bool, helpDataDirectory: bool = bool, installedVersion: bool = bool, ioVersion: bool = bool, irix: bool = bool, is64: bool = bool, languageResources: bool = bool, linux: bool = bool, linux64: bool = bool, liveUpdate: bool = bool, localizedResourceLocation: bool = bool, ltVersion: bool = bool, macOS: bool = bool, macOSppc: bool = bool, macOSx86: bool = bool, majorVersion: bool = bool, minorVersion: bool = bool, ntOS: bool = bool, operatingSystem: bool = bool, operatingSystemVersion: bool = bool, patchVersion: bool = bool, preferences: bool = bool, product: bool = bool, qtVersion: bool = bool, tablet: bool = bool, tabletMode: bool = bool, uiLanguage: bool = bool, uiLanguageForStartup: bool = bool, uiLanguageIsLocalized: bool = bool, uiLocaleLanguage: bool = bool, version: bool = bool, win64: bool = bool, windowManager: bool = bool, windows: bool = bool):
    """
    This command displays version information about the application if it is executed without flags.  If one of the above flags is specified then the specified version information is returned.

    Args:
        apiVersion: (create) - Returns the api version.
        application: (create) - Returns the application name string.
        batch: (create) - Returns true if application is in batch mode.
        buildDirectory: (create) - Returns the build directory string.
        buildVariant: (create) - Returns the build variant string.
        codeset: (create) - Returns a string identifying the codeset (codepage) of the locale that Maya is running in. Example return values include "UTF-8", "ISO-8859-1", "1252". Note that the codeset values and naming conventions are highly platform dependent.  They may differ in format even if they have the same meaning (e.g. "utf8" vs. "UTF-8").
        compositingManager: (create) - On Linux, returns true if there is a compositing manager running; on all other platforms, it always returns true.
        connected: (create) - Return whether the user is connected or not to the Internet.
        creativeVersion: (create) - Returns true if this is the Maya Creative version of the application.
        ctime: (create) - Returns the current time in the format Wed Jan 02 02:03:55 1980\n\0
        currentDate: (create) - Returns the current date in the format yyyy/mm/dd, e.g. 2003/05/04.
        currentTime: (create) - Returns the current time in the format hh:mm:ss, e.g. 14:27:53.
        customVersion: (create) - Returns true if this is a custom version of Maya.
        customVersionClient: (create) - Returns the custom client version string for Maya or an empty string if this is not a custom version.
        customVersionMajor: (create) - Returns the custom major version of Maya or 0 if this is not a custom version.
        customVersionMinor: (create) - Returns the custom minor version of Maya or 0 if this is not a custom version.
        customVersionString: (create) - Returns the custom version string for Maya or an empty string if this is not a custom version.
        cutIdentifier: (create) - Returns the cut string.
        date: (create) - Returns the build date string.
        environmentFile: (create) - Returns the location of the application defaults file.
        evalVersion: (create) - This flag is now deprecated. Always returns false, as the eval version is no longer supported.
        file: (create) - Returns the file version string.
        fontInfo: (create) - Returns a string of the specifications of the fonts requested, and the specifications of the fonts that are actually being used.
        helpDataDirectory: (create) - Returns the help data directory.
        installedVersion: (create) - Returns the product version string.
        ioVersion: (create) - Returns true if this is the Maya IO version of the application.
        irix: (create) - Returns true if the operating system is Irix. Always false with support for Irix removed.
        is64: (create) - Returns true if the application is 64 bit.
        languageResources: (create) - Returns a string array of the currently installed language resources. Each string entry consists of three elements delimited with a colon (':'). The first token is the locale code (ISO 639-1 language code followed by ISO 3166-1 country code).  The second token is the language name in English. This third token is the alpha-3 code (ISO 639-2).  For example English is represented as "en_US:English:enu".
        linux: (create) - Returns true if the operating system is Linux.
        linux64: (create) - Returns true if the operating system is Linux 64 bit.
        liveUpdate: (create) - This flag is deprecated(2019) and may be removed in future releases of Maya. Returns Autodesk formatted product information.
        localizedResourceLocation: (create) - Returns the path to the top level of the localized resource directory, if we are running in an alternate language. Returns an empty string if we are running in the default language.
        ltVersion: (create) - Deprecated. Returns true if this is the Maya LT version of the application.
        macOS: (create) - Returns true if the operating system is Macintosh.
        macOSppc: (create) - Returns true if the operating system is a PowerPC Macintosh.
        macOSx86: (create) - Returns true if the operating system is an Intel Macintosh.
        majorVersion: (create) - Returns the major version of Maya.
        minorVersion: (create) - Returns the minor version of Maya.
        ntOS: (create) - Returns true if the operating system is Windows.
        operatingSystem: (create) - Returns the operating system type. Valid return types are "nt", "win64", "mac", "linux" and "linux64"
        operatingSystemVersion: (create) - Returns the operating system version. on Linux this returns the equivalent of uname -srvm
        patchVersion: (create) - Returns the patch version of Maya.
        preferences: (create) - Returns the location of the preferences directory.
        product: (create) - Returns the license product name.
        qtVersion: (create) - Returns Qt version string.
        tablet: (create) - Windows only.  Returns true if the PC is a Tablet PC.
        tabletMode: (create) - Windows 8 (and above) only.  If your device is a Tablet PC, then the convertible mode the device is currently running in.  Returns  either: tablet or laptop (keyboard attached). See the tablet flag.
        uiLanguage: (create) - Returns the language that Maya's running in.  Example return values include "en_US" for English and "ja_JP" for Japanese.
        uiLanguageForStartup: (create) - Returns the language that is used for Maya's next start up. This is read from config file and is rewritten after setting ui language in preference.
        uiLanguageIsLocalized: (create) - Returns true if we are running in an alternate language, not the default (English).
        uiLocaleLanguage: (create) - Returns the language locale of the OS. English is default.
        version: (create) - Returns the version string.
        win64: (create) - Returns true if the operating system is Windows x64 based.
        windowManager: (create) - Returns the name of the Window Manager that is assumed to be running.
        windows: (create) - Returns true if the operating system is Windows based.
    """
    pass


def addAttr(*args, attributeType: Optional[Union[str, bool]] = str, binaryTag: Optional[Union[str, bool]] = str, cachedInternally: bool = bool, category: Optional[Union[str, bool]] = str, dataType: Optional[Union[str, bool]] = str, defaultValue: Optional[Union[float, bool]] = float, disconnectBehaviour: Optional[Union[int, bool]] = int, enumName: Optional[Union[str, bool]] = str, exists: bool = bool, fromPlugin: bool = bool, hasMaxValue: bool = bool, hasMinValue: bool = bool, hasSoftMaxValue: bool = bool, hasSoftMinValue: bool = bool, hidden: bool = bool, indexMatters: bool = bool, internalSet: bool = bool, keyable: bool = bool, longName: Optional[Union[str, bool]] = str, maxValue: Optional[Union[float, bool]] = float, minValue: Optional[Union[float, bool]] = float, multi: bool = bool, niceName: Optional[Union[str, bool]] = str, numberOfChildren: Optional[Union[int, bool]] = int, parent: Optional[Union[str, bool]] = str, proxy: Optional[Union[str, bool]] = str, readable: bool = bool, shortName: Optional[Union[str, bool]] = str, softMaxValue: Optional[Union[float, bool]] = float, softMinValue: Optional[Union[float, bool]] = float, storable: bool = bool, usedAsColor: bool = bool, usedAsFilename: bool = bool, usedAsProxy: bool = bool, worldSpace: bool = bool, writable: bool = bool, edit: bool = bool, query: bool = bool):
    """
    

    Args:
        attributeType: (create, query) - Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag: (create, query) - This flag is obsolete and does not do anything any more
        cachedInternally: (create, query) - Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category: (create, edit, multiuse, query) - An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType: (create, multiuse, query) - Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue: (create, edit, query) - Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour: (create, query) - defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName: (create, edit, query) - Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists: (create, query) - Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin: (create, query) - Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue: (create, edit, query) - Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue: (create, edit, query) - Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue: (create, query) - Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue: (create, query) - Flag indicating whether a numeric attribute has a soft minimum.
        hidden: (create, query) - Will this attribute be hidden from the UI?
        indexMatters: (create, query) - Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet: (create, query) - Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable: (create, query) - Is the attribute keyable by default?
        longName: (create, query) - Sets the long name of the attribute.
        maxValue: (create, edit, query) - Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue: (create, edit, query) - Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi: (create, query) - Makes the new attribute a multi-attribute.
        niceName: (create, edit, query) - Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren: (create, query) - How many children will the new attribute have?
        parent: (create, query) - Attribute that is to be the new attribute's parent.
        proxy: (create, query) - Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable: (create, query) - Can outgoing connections be made from this attribute?
        shortName: (create, query) - Sets the short name of the attribute.
        softMaxValue: (create, edit, query) - Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue: (create, edit, query) - Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        storable: (create, query) - Can the attribute be stored out to a file?
        usedAsColor: (create, query) - Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename: (create, query) - Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy: (create, query) - Set if the specified attribute should be treated as a proxy to another attributes.
        worldSpace: (create, query) - Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection.    Otherwise, the attribute will not get computed and will not get dirty again.
        writable: (create, query) - Can incoming connections be made to this attribute?
    """
    pass


def addExtension(*args, nodeType: Optional[Union[str, bool]] = str, attributeType: Optional[Union[str, bool]] = str, binaryTag: Optional[Union[str, bool]] = str, cachedInternally: bool = bool, category: Optional[Union[str, bool]] = str, dataType: Optional[Union[str, bool]] = str, defaultValue: Optional[Union[float, bool]] = float, disconnectBehaviour: Optional[Union[int, bool]] = int, enumName: Optional[Union[str, bool]] = str, exists: bool = bool, fromPlugin: bool = bool, hasMaxValue: bool = bool, hasMinValue: bool = bool, hasSoftMaxValue: bool = bool, hasSoftMinValue: bool = bool, hidden: bool = bool, indexMatters: bool = bool, internalSet: bool = bool, keyable: bool = bool, longName: Optional[Union[str, bool]] = str, maxValue: Optional[Union[float, bool]] = float, minValue: Optional[Union[float, bool]] = float, multi: bool = bool, niceName: Optional[Union[str, bool]] = str, numberOfChildren: Optional[Union[int, bool]] = int, parent: Optional[Union[str, bool]] = str, proxy: Optional[Union[str, bool]] = str, readable: bool = bool, shortName: Optional[Union[str, bool]] = str, softMaxValue: Optional[Union[float, bool]] = float, softMinValue: Optional[Union[float, bool]] = float, storable: bool = bool, usedAsColor: bool = bool, usedAsFilename: bool = bool, usedAsProxy: bool = bool, worldSpace: bool = bool, writable: bool = bool, edit: bool = bool, query: bool = bool):
    """
    

    Args:
        nodeType: (create, edit, query) - Specifies the type of node to which the attribute will be added. See the nodeType command for the names of different node types.
        attributeType: (create, query) - Specifies the attribute type, see above table for more details. Note that the attribute types "float", "matrix" and "string" are also MEL keywords and must be enclosed in quotes.
        binaryTag: (create, query) - This flag is obsolete and does not do anything any more
        cachedInternally: (create, query) - Whether or not attribute data is cached internally in the node. This flag defaults to true for writable attributes and false for non-writable attributes. A warning will be issued if users attempt to force a writable attribute to be uncached as this will make it impossible to set keyframes.
        category: (create, edit, multiuse, query) - An attribute category is a string associated with the attribute to identify it. (e.g. the name of a plugin that created the attribute, version information, etc.) Any attribute can be associated with an arbitrary number of categories however categories can not be removed once associated.
        dataType: (create, multiuse, query) - Specifies the data type.  See "setAttr" for more information on data type names.
        defaultValue: (create, edit, query) - Specifies the default value for the attribute (can only be used for numeric attributes).
        disconnectBehaviour: (create, query) - defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
        enumName: (create, edit, query) - Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1:triplet=3:quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1:triplet=2:quintet=3".)
        exists: (create, query) - Returns true if the attribute queried is a user-added, dynamic attribute; false if not.
        fromPlugin: (create, query) - Was the attribute originally created by a plugin? Normally set automatically when the API call is made - only added here to support storing it in a file independently from the creating plugin.
        hasMaxValue: (create, edit, query) - Flag indicating whether an attribute has a maximum value. (can only be used for numeric attributes).
        hasMinValue: (create, edit, query) - Flag indicating whether an attribute has a minimum value. (can only be used for numeric attributes).
        hasSoftMaxValue: (create, query) - Flag indicating whether a numeric attribute has a soft maximum.
        hasSoftMinValue: (create, query) - Flag indicating whether a numeric attribute has a soft minimum.
        hidden: (create, query) - Will this attribute be hidden from the UI?
        indexMatters: (create, query) - Sets whether an index must be used when connecting to this multi-attribute. Setting indexMatters to false forces the attribute to non-readable.
        internalSet: (create, query) - Whether or not the internal cached value is set when this attribute value is changed.  This is an internal flag used for updating UI elements.
        keyable: (create, query) - Is the attribute keyable by default?
        longName: (create, query) - Sets the long name of the attribute.
        maxValue: (create, edit, query) - Specifies the maximum value for the attribute (can only be used for numeric attributes).
        minValue: (create, edit, query) - Specifies the minimum value for the attribute (can only be used for numeric attributes).
        multi: (create, query) - Makes the new attribute a multi-attribute.
        niceName: (create, edit, query) - Sets the nice name of the attribute for display in the UI.  Setting the attribute's nice name to a non-empty string overrides the default behaviour of looking up the nice name from Maya's string catalog.   (Use the MEL commands "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's nice name in the catalog.)
        numberOfChildren: (create, query) - How many children will the new attribute have?
        parent: (create, query) - Attribute that is to be the new attribute's parent.
        proxy: (create, query) - Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.
        readable: (create, query) - Can outgoing connections be made from this attribute?
        shortName: (create, query) - Sets the short name of the attribute.
        softMaxValue: (create, edit, query) - Soft maximum, valid for numeric attributes only.  Specifies the upper default limit used in sliders for this attribute.
        softMinValue: (create, edit, query) - Soft minimum, valid for numeric attributes only.  Specifies the lower default limit used in sliders for this attribute.
        storable: (create, query) - Can the attribute be stored out to a file?
        usedAsColor: (create, query) - Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT children to use this flag.  The attribute type "-at" should be "double3" or "float3" as appropriate.  It can also be used to less effect with data types "-dt" as "double3" or "float3" as well but some parts of the code do not support this alternative.  The special attribute types/data "spectrum" and "reflectance" also support the color flag and on them it is set by default.
        usedAsFilename: (create, query) - Is the attribute to be treated as a filename definition? This flag is only supported on attributes with data type "-dt" of "string".
        usedAsProxy: (create, query) - Set if the specified attribute should be treated as a proxy to another attributes.
        worldSpace: (create, query) - Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node and Maya requires one array element per path for worldSpace attributes. Remarks: 1. Can only be used on array attributes. 2. This property is ignored on non-dag nodes. 3. The attribute should be affected by another attribute or have a connection.    Otherwise, the attribute will not get computed and will not get dirty again.
        writable: (create, query) - Can incoming connections be made to this attribute?
    """
    pass


def affectedNet(*args, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command gets the list of attributes on a node or node type and creates nodes of type TdnAffect, one for each attribute, that are connected iff the source node's attribute affects the destination node's attribute.

    Args:
        type: (create) - Get information from the given node type instead of one node
    """
    pass


def affects(*args, by: bool = bool, type: Optional[Union[str, bool]] = str):
    """
    This command returns the list of attributes on a node or node type which affect the named attribute.

    Args:
        by: (create) - Show attributes that are affected by the given one rather than the ones that affect it.
        type: (create) - static node type from which to get 'affects' information
    """
    pass


def aliasAttr(*args, remove: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Allows aliases (alternate names) to be defined for any attribute of a specified node. When an attribute is aliased, the alias will be used by the system to display information about the attribute. The user may, however, freely use either the alias or the original name of the attribute. Only a single alias can be specified for an attribute so setting an alias on an already-aliased attribute destroys the old alias.

    Args:
        remove: (create) - Specifies that aliases listed should be removed (otherwise new aliases are added).
    """
    pass


def align(*args, alignToLead: bool = bool, coordinateSystem: Optional[Union[str, bool]] = str, xAxis: Optional[Union[str, bool]] = str, yAxis: Optional[Union[str, bool]] = str, zAxis: Optional[Union[str, bool]] = str):
    """
    Align or spread objects along X Y and Z axis.

    Args:
        alignToLead: (create) - When set, the min, center or max values are computed from the lead object. Otherwise, the values are averaged for all objects. Default is false
        coordinateSystem: (create) - Defines the X, Y, and Z coordinates. Default is the world coordinates
        xAxis: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
        yAxis: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
        zAxis: (create) - Any of none, min, mid, max, dist, stack. This defines the kind of alignment to perfom, default is none.
    """
    pass


def alignCtx(*args, align: bool = bool, anchorFirstObject: bool = bool, distribute: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, showAlignTouch: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The alignCtx command creates a tool for aligning and distributing objects.

    Args:
        align: (create, edit, query) - Align objects
        anchorFirstObject: (create, edit, query) - Anchor first or last selected object. Default false. Only applicable when aligning objects.
        distribute: (create, edit, query) - Distribute objects
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        showAlignTouch: (create, edit, query) - Show or hide align touching handles. Default true. Only applicable when aligning objects.
    """
    pass


def applyAttrPattern(*args, nodeType: Optional[Union[str, bool]] = str, patternName: Optional[Union[str, bool]] = str):
    """
    Take the attribute structure described by a pre-defined pattern and apply it either to a node (as dynamic attributes) or a node type (as extension attributes). The same pattern can be applied more than once to different nodes or node types as the operation duplicates the attribute structure described by the pattern.  See the 'createAttrPatterns' command for a description of how to create a pattern.

    Args:
        nodeType: (create) - Name of the node type to which the attribute pattern is to be applied. This flag will cause a new extension attribute tree to be created, making the new attributes available on all nodes of the given type. If it is not specified then either a node name must be specified or a node must be selected for application of dynamic attributes.
        patternName: (create) - The name of the pattern to apply. The pattern with this name must have been previously created using the createAttrPatterns command.
    """
    pass


def arcLenDimContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command used to register the arcLenDimCtx tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def art3dPaintCtx(*args, accopacity: bool = bool, afterStrokeCmd: Optional[Union[str, bool]] = str, alphablendmode: Optional[Union[str, bool]] = str, assigntxt: bool = bool, attrnames: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushdepth: Optional[Union[float, bool]] = float, brushfeedback: bool = bool, brushtype: Optional[Union[str, bool]] = str, clear: bool = bool, commonattr: Optional[Union[str, bool]] = str, dragSlider: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, extendFillColor: bool = bool, fileformat: Optional[Union[str, bool]] = str, filetxtaspectratio: Optional[Union[float, bool]] = float, filetxtsizex: Optional[Union[int, bool]] = int, filetxtsizey: Optional[Union[int, bool]] = int, floodOpacity: Optional[Union[float, bool]] = float, floodall: bool = bool, floodselect: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, keepaspectratio: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, painttxtattr: Optional[Union[str, bool]] = str, painttxtattrname: Optional[Union[str, bool]] = str, pfxScale: Optional[Union[float, bool]] = float, pfxWidth: Optional[Union[float, bool]] = float, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, pressureMapping1: Optional[Union[int, bool]] = int, pressureMapping2: Optional[Union[int, bool]] = int, pressureMapping3: Optional[Union[int, bool]] = int, pressureMax1: Optional[Union[float, bool]] = float, pressureMax2: Optional[Union[float, bool]] = float, pressureMax3: Optional[Union[float, bool]] = float, pressureMin1: Optional[Union[float, bool]] = float, pressureMin2: Optional[Union[float, bool]] = float, pressureMin3: Optional[Union[float, bool]] = float, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, reloadtexfile: bool = bool, resizeratio: Optional[Union[float, bool]] = float, resizetxt: bool = bool, rgbcolor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rgbflood: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), saveTextureOnStroke: bool = bool, saveonstroke: bool = bool, savetexture: bool = bool, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, shadernames: Optional[Union[str, bool]] = str, shapeattr: bool = bool, shapenames: Optional[Union[str, bool]] = str, showactive: bool = bool, soloAsDiffuse: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, textureFilenames: bool = bool, updateEraseTex: bool = bool, usepressure: bool = bool, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a tool context command for 3d Paint tool.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphablendmode: (create, edit, query) - Specifies the blend mode used while painting RGB channel. Currently, we support the following blend modes: "Default" "Lighten" "Darken" "Difference" "Exclusion" "Hard Light" "Soft Light" "Multiply" "Screen" "Overlay" "Constant" Default is "Default".
        assigntxt: (edit) - Sends a request to the tool to allocate and assign file textures to the specified attibute on the selected shaders.
        attrnames: (create, edit, query) - Name of attributes
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushdepth: (create, edit, query) - Depth of the brush
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        brushtype: (create, edit, query) - Name of the brush type
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        commonattr: (query) - Returns a string with the names of all common to all the shaders paintable attributes and supported by the Paint Texture Tool.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        extendFillColor: (create, edit, query) - States if the painted textures will be automatically postprocessed on each stroke to fill in the background color. Default is true.
        fileformat: (create, edit, query) - Name of the file format
        filetxtaspectratio: (create, edit, query) - Specifies the aspect ration of the texture width and height. Default is 1.
        filetxtsizex: (create, edit, query) - Specifies the width of the texture. Default is 256.
        filetxtsizey: (create, edit, query) - Specifies the height of the texture. Default is 256.
        floodOpacity: (create, edit, query) - Value of the flood opacity
        floodall: (create, edit, query) - Turn on to flood everything
        floodselect: (create, edit, query) - Should the selected area be flooded?
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keepaspectratio: (create, edit, query) - States if the aspect ratio of the file texture sizes should remain constant. Default is true. boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name: (create) - If this is a tool command, name the tool appropriately.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        painttxtattr: (create, edit, query) - Specifies the attribute on the shader which the user wants to paint. Currently, we support the following attributes: "Color", "Transparency", "Ambient", "Incandescence", "BumpMap", "Diffuse", "Translucence" "Eccentricity" "SpecularColor", "Reflectivity", "ReflectedColor", and user-defined float, float3, double, and double3 attributes. Default is "Color".
        painttxtattrname: (edit, query) - Returns a string with the names of all paintable attributes supported by the Paint Texture Tool.
        pfxScale: (edit, query) - Specifies the scale for Paint Effect brushes.
        pfxWidth: (edit, query) - Specifies the width for Paint Effect brushes.
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        pressureMapping1: (create, edit, query) - First pressure mapping value
        pressureMapping2: (create, edit, query) - Second pressure mapping value
        pressureMapping3: (create, edit, query) - Third pressure mapping value
        pressureMax1: (create, edit, query) - First pressure maximum value
        pressureMax2: (create, edit, query) - Second pressure maximum value
        pressureMax3: (create, edit, query) - Third pressure maximum value
        pressureMin1: (create, edit, query) - First pressure minimum value
        pressureMin2: (create, edit, query) - Second pressure minimum value
        pressureMin3: (create, edit, query) - Third pressure minimum value
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        reloadtexfile: (edit) - Sends a request to the tool to reload the texture from the disc.
        resizeratio: (edit, query) - Specifies the scale by which to resize the current textures.
        resizetxt: (edit) - Sends a request to the tool to resize all the currently in use textures.
        rgbcolor: (create, edit, query) - Colour value
        rgbflood: (create, edit, query) - Color of the flood
        saveTextureOnStroke: (create, edit, query) - States if the original texture will be automatically saved on each stroke. Default is false.
        saveonstroke: (create, edit, query) - States if the temporary texture will be automatically saved on each stroke. Default is false.
        savetexture: (edit) - Sends a request to the tool to save the texture to the disc.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        shadernames: (query) - Returns a string with the names of all shaders assigned to selected surfaces.
        shapeattr: (edit, query) - States if the attribute to paint is an attribute of the shape and not the shader. Default is false.
        shapenames: (query) - Returns a string with the names of all surfaces which are being painted on.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        soloAsDiffuse: (edit, query) - States if the currently paintable texture will be rendered as as diffuse texture in the viewport. Default is false.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        textureFilenames: (query) - Returns a string array with the names of all the painted file textures.
        updateEraseTex: (create, edit, query) - Should the erase texture update?
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artAttrCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, dataTypeIndex: Optional[Union[int, bool]] = int, disablelighting: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, interactiveUpdate: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintNodeArray: Optional[Union[str, bool]] = str, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, useColorRamp: bool = bool, useMaxMinColor: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artAttrPaintVertexCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, dataTypeIndex: Optional[Union[int, bool]] = int, disablelighting: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, interactiveUpdate: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintChannel: Optional[Union[str, bool]] = str, paintComponent: Optional[Union[int, bool]] = int, paintNodeArray: Optional[Union[str, bool]] = str, paintNumChannels: Optional[Union[int, bool]] = int, paintRGBA: bool = bool, paintVertexFace: bool = bool, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, useColorRamp: bool = bool, useMaxMinColor: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, vertexColorRange: bool = bool, vertexColorRangeLower: Optional[Union[float, bool]] = float, vertexColorRangeUpper: Optional[Union[float, bool]] = float, whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintChannel: (create, edit, query) - Channel to paint - RGB, RGBA, R, G, B, A
        paintComponent: (create, edit, query) - Specifies whether face or vertex or vertex face is being painted. 1 - Vertex 2 - VertexFace 3 - Face C: Default is Vertex.  Q: When queried, it returns a int.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintNumChannels: (create, edit, query) - Number of channels to paint - 1 (alpha), 3 (RGB), or 4 (RGBA)
        paintRGBA: (create, edit, query) - Specifies whether RGB or RGBA channels are being painted. TRUE: RGBA channels. FALSE: RGB channels. Alpha channel remains unaffected. C: Default is FALSE (Painting RGB channels). Q: When queried, it returns a int.
        paintVertexFace: (create, edit, query) - Specifies whether vertex face is being painted. TRUE: Vertex face being painted. (Allows each face connected to the vertex to be painted) FALSE: Vertex being painted.(affects all connected faces) C: Default is FALSE.  Q: When queried, it returns a int.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        vertexColorRange: (create, edit, query) - Specifies whether the vertex color range should be applied to the currently selected object. C: Default is false  Q: When queried, it returns a boolean.
        vertexColorRangeLower: (create, edit, query) - Specifies the min value of the vertex color range. C: Default is 0.0.  Q: When queried, it returns a float.
        vertexColorRangeUpper: (create, edit, query) - Specifies the max value of the vertex color range. C: Default is 1.0.  Q: When queried, it returns a float.
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artAttrSkinPaintCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, dataTypeIndex: Optional[Union[int, bool]] = int, disablelighting: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, influence: Optional[Union[str, bool]] = str, interactiveUpdate: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintNodeArray: Optional[Union[str, bool]] = str, paintSelectMode: Optional[Union[int, bool]] = int, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, showactive: bool = bool, skinPaintMode: Optional[Union[int, bool]] = int, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, useColorRamp: bool = bool, useMaxMinColor: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, xrayJoints: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        influence: (edit, query) - Specifies which joint has been selected by the user for painting. Q: When queried, it returns a string.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintSelectMode: (edit, query) - Specifies whether the paint select tool: adds to selection (1) removes from selection (2), toggles selection (3) Q: When queried, it returns an int as defined above.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        skinPaintMode: (edit, query) - Specifies whether the skin paint tool is in paint skin weights mode (1) Marquee select mode (0), or paint select mode (2) Q: When queried, it returns an int as defined above.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
        xrayJoints: (edit, query) - Specifies whether joints should be displayed in xray mode while painting Q: When queried, it returns a boolean.
    """
    pass


def artAttrTool(*args, add: Optional[Union[str, bool]] = str, exists: Optional[Union[str, bool]] = str, remove: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    

    Args:
        add: (create) - Adds the named tool to the internal list of tools.
        exists: (create, query) - Checks if the named tool exists, returning true if found, and false otherwise.
        remove: (create) - Removes the named tool from the internal list of tools.
    """
    pass


def artFluidAttrCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, autoSave: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, currentPaintableFluid: Optional[Union[str, bool]] = str, dataTypeIndex: Optional[Union[int, bool]] = int, delaySelectionChanged: bool = bool, disablelighting: bool = bool, displayAsRender: bool = bool, displayVelocity: bool = bool, doAutoSave: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, interactiveUpdate: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintNodeArray: Optional[Union[str, bool]] = str, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, property: Optional[Union[str, bool]] = str, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, rgbValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, useColorRamp: bool = bool, useMaxMinColor: bool = bool, useStrokeDirection: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, velocity: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        autoSave: (create, edit, query) - A MEL command to save the fluid state.  Called before an event which could overwrite unsaved values of painted fluid properties.  Such events include: changing current time, changing the current paintable property, and exiting the paint tool.  (To turn auto-save off, pass in an empty-valued string argument: e.g., "".)
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        currentPaintableFluid: (query) - Query the name of the fluid on which this context is currently painting.  Returns string.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        delaySelectionChanged: (create, edit, query) - Internal use only.  Under normal conditions, the tool responds to changes to the selection list so it can update its list of paintable geometry.  When -dsl true is used, the tool will not update its paintable list until a corresponding -dsl false is called.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        displayAsRender: (create, edit, query) - When true, sets the "Shaded Display" attribute of the fluid to "AsRender": all fluid properties displayed as hardware rendered.  When false, displays only the currently selected paintable attribute of the fluid.
        displayVelocity: (create, edit, query) - Turns on/off velocity display, independently of the above "dar/displayAsRender" setting.  Use this flag to enable velocity display while only displaying density, for example.
        doAutoSave: (edit) - Execute the -autoSave command if there are unsaved painted fluid properties.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        property: (create, edit, query) - Specifies a property to paint on the fluid. Valid values are "color", "density", "densityAndColor," "densityAndFuel," "temperature," "fuel", "velocity".
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        rgbValue: (create, edit, query) - Specifies the values of the red, green, and blue components of the color to use when painting the property "color."
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        useStrokeDirection: (create, edit, query) - Applicable only during "velocity" painting.  Specifies whether the value of the painted velocity should come from the direction of the brush stroke, overriding the value specified by the -v/-velocity flag.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        velocity: (create, edit, query) - Specifies the values of the x, y, and z components of the velocity to use when painting the property "velocity".
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artPuttyCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, autosmooth: bool = bool, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushStrength: Optional[Union[float, bool]] = float, brushalignment: bool = bool, brushfeedback: bool = bool, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, collapsecvtol: Optional[Union[float, bool]] = float, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, dataTypeIndex: Optional[Union[int, bool]] = int, disablelighting: bool = bool, dispdecr: bool = bool, dispincr: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, erasesrfupd: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, interactiveUpdate: bool = bool, invertrefvector: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxdisp: Optional[Union[float, bool]] = float, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, mouldtypehead: Optional[Union[str, bool]] = str, mouldtypemouse: Optional[Union[str, bool]] = str, mouldtypetail: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintNodeArray: Optional[Union[str, bool]] = str, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, polecv: bool = bool, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, refsurface: bool = bool, refvector: Optional[Union[str, bool]] = str, refvectoru: Optional[Union[float, bool]] = float, refvectorv: Optional[Union[float, bool]] = float, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, showactive: bool = bool, smoothiters: Optional[Union[int, bool]] = int, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, stitchcorner: bool = bool, stitchedgeflood: bool = bool, stitchtype: Optional[Union[str, bool]] = str, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, updateerasesrf: bool = bool, updaterefsrf: bool = bool, useColorRamp: bool = bool, useMaxMinColor: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        autosmooth: (create, edit, query) - Sets up the auto smoothing option. When the brush is in the smooth mode, adjusting the strength will adjust how fast the surfaces is smoothed out. C: Default is FALSE.  Q: When queried, it returns a boolean.
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushStrength: (create, edit, query) - Sets the strength of the brush. Brush strength is supported by the pinch and slide brushes. In pinch mode, adjusting the strength will adjust how quickly the surface converges on the brush center. In slide mode, the strength scales the motion of the brush. C: Default is 1.0.  Q: When queried, it returns a float.
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        collapsecvtol: (create, edit, query) - Specifies the tolerance for the collapse cv detection. C: Default is 0.005 cm.  Q: When queried, it returns a float.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dispdecr: (create, edit) - Decreases a maximum displacement by 10%.
        dispincr: (create, edit) - Increases a maximum displacement by 10%.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        erasesrfupd: (create, edit, query) - Toggles the update for the erase surface
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        invertrefvector: (create, edit, query) - Sets the invert of the reference vector option when the reflection is ON. If it is true, the reference vector for the reflected stroke is negated with respect to the original one. C: Default is FALSE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxdisp: (create, edit, query) - Defines a maximum displacement ( maxDisp in [0.0..5.0] ). C: Default is 1.0.  Q: When queried, it returns a float.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        mouldtypehead: (create, edit, query) - Type of type mould to use
        mouldtypemouse: (create, edit, query) - Specifies the putty operations/mode ("push" - pushes CVs along the given direction (see refvector flag), "pull" - pulls CVs along the specified direction, "smooth" - smooths the sculpt, "erase" - erases the paint). C: Default is "push".  Q: When queried, it returns a string.
        mouldtypetail: (create, edit, query) - Type of eraser mould to use
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        polecv: (create, edit, query) - Pull all the pole CVs to the same position.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        refsurface: (create, edit, query) - Sets on/off the update of the reference surface. If it is true the reference surface is automatically updated on the per stroke bases. If it is false, the user has to update the reference surface explicitly by pressing the update button (see updaterefsrf). C: Default is TRUE.  Q: When queried, it returns a boolean.
        refvector: (create, edit, query) - Specifies the direction of the push/pull operation ("normal" - sculpt along normals, "firstnormal" - sculpt along the first normal of the stroke, "view" - sculpt along the view direction, "xaxis", "yaxis", "zaxis" - sculpt along a given axis directions, "uisoparm", "visoparm" - sculpt along U or V isoparametric lines), "uvvector" - sculpt along an arbitrary vector in UV space. C: Default is "normal".  Q: When queried, it returns a string.
        refvectoru: (create, edit, query) - Specifies the U component of the UV vector to be used when -refVector is set to "uvvector".
        refvectorv: (create, edit, query) - Specifies the V component of the UV vector to be used when -refVector is set to "uvvector".
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        smoothiters: (create, edit, query) - Sets the quality of the smoothing operation (number of iterations). C: Default is 3.  Q: When queried, it returns an int.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        stitchcorner: (create, edit, query) - Sets on/off the stitching corner mode C: Default is "off".  Q: When queried, it returns a boolean.
        stitchedgeflood: (edit) - Triggers postprocessing stitching edge procedure.
        stitchtype: (create, edit, query) - Sets on/off the stitching mode ( "off" - stitching is turned off, "position" - position stitching is done without taking care about the tangent continuity C0, "tan" - C1 continuity is preserved). C: Default is "position".  Q: When queried, it returns a string.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        updateerasesrf: (create, edit) - Updates the erase surface.
        updaterefsrf: (create, edit) - Updates the reference surface.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artSelectCtx(*args, accopacity: bool = bool, addselection: bool = bool, afterStrokeCmd: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clear: bool = bool, dragSlider: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, importthreshold: Optional[Union[float, bool]] = float, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectall: bool = bool, selectclonesource: bool = bool, selectop: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toggleall: bool = bool, unselectall: bool = bool, usepressure: bool = bool, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command is used to select/deselect/toggle components on selected surfaces using a brush interface (Maya Artisan). Since, it selects components of the surface, it only works in the component mode.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        addselection: (create, edit, query) - If true, each new stroke adds cvs to the active list. If false, each stroke replaces the previous selection. C: Default is true. Q: When queried, it returns a boole
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        importthreshold: (create, edit, query) - Specifies the threshold for the import of the attribute maps. C: Default is 0.5.  Q: When queried, it returns a float.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name: (create) - If this is a tool command, name the tool appropriately.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectall: (create, edit) - Selects all vertices/egdes/faces/uvs.
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectop: (create, edit, query) - Specifies the selection operation ("select", "unselect", "toggle"). C: Default is "select". Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toggleall: (create, edit) - Toggle all vertices/egdes/faces/uvs.
        unselectall: (create, edit) - Unselects all vertices/egdes/faces/uvs.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artSetPaintCtx(*args, accopacity: bool = bool, afterStrokeCmd: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, clear: bool = bool, dragSlider: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, objectsetnames: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, setcolorfeedback: bool = bool, setdisplaycvs: bool = bool, setopertype: Optional[Union[str, bool]] = str, settomodify: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, usepressure: bool = bool, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This tool allows the user to modify the set membership (add, transfer, remove cvs) on nurbs surfaces using Maya Artisan's interface.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        name: (create) - If this is a tool command, name the tool appropriately.
        objectsetnames: (create, edit, query) - Default name of object sets
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        setcolorfeedback: (create, edit, query) - Specifies if the color feedback is on or off. C: Default is ON.  Q: When queried, it returns a boolean.
        setdisplaycvs: (create, edit, query) - Specifies if the active cvs are displayed. C: Default is ON. Q: When queried, it returns a boolean.
        setopertype: (create, edit, query) - Specifies the setEdit operation ("add", "transfer", "remove"). C: Default is "add". Q: When queried, it returns a string.
        settomodify: (create, edit, query) - Specifies the name of the set to modify. Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def artUserPaintCtx(*args, accopacity: bool = bool, activeListChangedProc: Optional[Union[str, bool]] = str, afterStrokeCmd: Optional[Union[str, bool]] = str, alphaclamp: Optional[Union[str, bool]] = str, alphaclamplower: Optional[Union[float, bool]] = float, alphaclampupper: Optional[Union[float, bool]] = float, attrSelected: Optional[Union[str, bool]] = str, beforeStrokeCmd: Optional[Union[str, bool]] = str, brushalignment: bool = bool, brushfeedback: bool = bool, chunkCommand: Optional[Union[str, bool]] = str, clamp: Optional[Union[str, bool]] = str, clamplower: Optional[Union[float, bool]] = float, clampupper: Optional[Union[float, bool]] = float, clear: bool = bool, colorAlphaValue: Optional[Union[float, bool]] = float, colorRGBAValue: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], colorRGBValue: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), colorRamp: Optional[Union[str, bool]] = str, colorfeedback: bool = bool, colorfeedbackOverride: bool = bool, colorrangelower: Optional[Union[float, bool]] = float, colorrangeupper: Optional[Union[float, bool]] = float, dataTypeIndex: Optional[Union[int, bool]] = int, disablelighting: bool = bool, dragSlider: Optional[Union[str, bool]] = str, duringStrokeCmd: Optional[Union[str, bool]] = str, dynclonemode: bool = bool, exists: bool = bool, expandfilename: bool = bool, exportaspectratio: Optional[Union[float, bool]] = float, exportfilemode: Optional[Union[str, bool]] = str, exportfilesave: str = str, exportfilesizex: Optional[Union[int, bool]] = int, exportfilesizey: Optional[Union[int, bool]] = int, exportfiletype: Optional[Union[str, bool]] = str, filterNodes: bool = bool, finalizeCmd: Optional[Union[str, bool]] = str, fullpaths: bool = bool, getArrayAttrCommand: Optional[Union[str, bool]] = str, getSurfaceCommand: Optional[Union[str, bool]] = str, getValueCommand: Optional[Union[str, bool]] = str, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, importfileload: str = str, importfilemode: Optional[Union[str, bool]] = str, importreassign: bool = bool, initializeCmd: Optional[Union[str, bool]] = str, interactiveUpdate: bool = bool, lastRecorderCmd: Optional[Union[str, bool]] = str, lastStampName: Optional[Union[str, bool]] = str, lowerradius: Optional[Union[float, bool]] = float, makeStroke: Optional[Union[int, bool]] = int, mappressure: Optional[Union[str, bool]] = str, maxvalue: Optional[Union[float, bool]] = float, minvalue: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, objattrArray: Optional[Union[str, bool]] = str, opacity: Optional[Union[float, bool]] = float, outline: bool = bool, outwhilepaint: bool = bool, paintNodeArray: Optional[Union[str, bool]] = str, paintattrselected: str = str, paintmode: Optional[Union[str, bool]] = str, paintoperationtype: Optional[Union[str, bool]] = str, pickColor: bool = bool, pickValue: bool = bool, playbackCursor: Optional[Union[Tuple[float, float], bool]] = [float, float], playbackPressure: Optional[Union[float, bool]] = float, preserveclonesource: bool = bool, profileShapeFile: Optional[Union[str, bool]] = str, projective: bool = bool, radius: Optional[Union[float, bool]] = float, rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), record: bool = bool, reflection: bool = bool, reflectionaboutorigin: bool = bool, reflectionaxis: Optional[Union[str, bool]] = str, screenRadius: Optional[Union[float, bool]] = float, selectclonesource: bool = bool, selectedattroper: Optional[Union[str, bool]] = str, setArrayValueCommand: Optional[Union[str, bool]] = str, setValueCommand: Optional[Union[str, bool]] = str, showactive: bool = bool, stampDepth: Optional[Union[float, bool]] = float, stampProfile: Optional[Union[str, bool]] = str, stampSpacing: Optional[Union[float, bool]] = float, strokesmooth: Optional[Union[str, bool]] = str, surfaceConformedBrushVertices: bool = bool, tablet: bool = bool, tangentOutline: bool = bool, toolCleanupCmd: Optional[Union[str, bool]] = str, toolOffProc: Optional[Union[str, bool]] = str, toolOnProc: Optional[Union[str, bool]] = str, toolSetupCmd: Optional[Union[str, bool]] = str, useColorRamp: bool = bool, useMaxMinColor: bool = bool, usepressure: bool = bool, value: Optional[Union[float, bool]] = float, whichTool: Optional[Union[str, bool]] = str, worldRadius: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations. All commands require the name of the context as the last argument as this provides the name of the context to create, edit or query.

    Args:
        accopacity: (create, edit, query) - Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool for which it is true by default). Q: When queried, it returns a boolean.
        activeListChangedProc: (create, edit, query) - Accepts a string that contains a MEL command that is invoked whenever the active list changes. There may be some situations where the UI, for example, needs to be updated, when objects are selected/deselected in the scene. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        afterStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately after the end of a stroke. C: Default is no command. Q: When queried, it returns the current command
        alphaclamp: (create, edit, query) - Specifies if the weight value should be alpha clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        alphaclamplower: (create, edit, query) - Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When queried, it returns a float.
        alphaclampupper: (create, edit, query) - Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When queried, it returns a float.
        attrSelected: (query) - Returns a name of the currently selected attribute. Q: When queried, it returns a string.
        beforeStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command immediately before the start of a stroke. C: Default is no command. Q: When queried, it returns the current command
        brushalignment: (create, edit, query) - Specifies the path brush alignemnt. If true, the brush will align to stroke path, otherwise it will align to up vector. C: Default is true. Q: When queried, it returns a boolean.
        brushfeedback: (create, edit, query) - Specifies if the brush additional feedback should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        chunkCommand: (create, edit, query) - Specifies th name of the Mel script/procedure that is called once for every selected surface when a chunk is received on that surface. Q: When queried, it returns a string.
        clamp: (create, edit, query) - Specifies if the weight value should be clamped to the lower and upper bounds. There are four options here: "none" - no clamping is performed, "lower" - clamps only to the lower bound, "upper" - clamps only to the upper bounds, "both" - clamps to the lower and upper bounds. C: Default is "none".  Q: When queried, it returns a string.
        clamplower: (create, edit, query) - Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried, it returns a float.
        clampupper: (create, edit, query) - Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried, it returns a float.
        clear: (create, edit) - Floods all cvs/vertices to the current value.
        colorAlphaValue: (create, edit, query) - The Alpha value of the color.
        colorRGBAValue: (create, edit, query) - The RGBA value of the color.
        colorRGBValue: (create, edit, query) - The RGB value of the color.
        colorRamp: (create, edit, query) - Allows a user defined color ramp to be used to map values to colors.
        colorfeedback: (create, edit, query) - Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorfeedbackOverride: (create, edit, query) - Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried, it returns a boolean.
        colorrangelower: (create, edit, query) - Specifies the value that maps to black when color feedback mode is on. C: Default is 0.0.  Q: When queried, it returns a float.
        colorrangeupper: (create, edit, query) - Specifies the value that maps to the maximum color when color feedback mode is on. C: Default is 1.0.  Q: When queried, it returns a float.
        dataTypeIndex: (edit, query) - When the selected paintable attribute is a vectorArray, it specifies which field to paint on.
        disablelighting: (create, edit, query) - If color feedback is on, this flag determines whether lighting is disabled or not for the surfaces that are affected. C: Default is FALSE.  Q: When queried, it returns a boolean.
        dragSlider: (create, edit) - Sets the current brush drag state for resizing or offsetting the brush (like the 'b' and 'm' default hotkeys). The string argument is one of: "radius", "lowradius", "opacity", "value", "depth", "displacement", "uvvector" or "none". C: Default is "none".
        duringStrokeCmd: (create, edit, query) - The passed string is executed as a MEL command during the stroke, each time the mouse is dragged. C: Default is no command. Q: When queried, it returns the current command
        dynclonemode: (create, edit, query) - Enable or disable dynamic clone mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        expandfilename: (create, edit) - If true, it will expand the name of the export file and concatenate it with the surface name. Otherwise it will take the name as it is. C: Default is true.
        exportaspectratio: (create, edit, query) - Value of aspect ratio for export
        exportfilemode: (create, edit, query) - Specifies the export channel.The valid entries here are: "alpha", "luminance", "rgb", "rgba". C: Default is "luminance/rgb". Q: When queried, it returns a string.
        exportfilesave: (edit) - Exports the attribute map and saves to a specified file.
        exportfilesizex: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfilesizey: (create, edit, query) - Specifies the width of the attribute map to export. C: Default width is 256. Q: When queried, it returns an integer.
        exportfiletype: (create, edit, query) - Specifies the image file format. It can be one of the following: "iff", "tiff", "jpeg", "alias", "rgb", "fit" "postScriptEPS", "softimage", "wavefrontRLA", "wavefrontEXP". C: default is tiff. Q: When queried, it returns a string.
        filterNodes: (edit) - Sets the node filter.
        finalizeCmd: (create, edit, query) - Specifies the name of the Mel script/procedure that is called at the end of each stroke. Q: When queried, it returns a string.
        fullpaths: (create, edit, query) - Specifies whether full path names should be used when surface names are passed to scripts. If false, just the surface name is passed. C: Default is false  Q: When queried, it returns a boolean.
        getArrayAttrCommand: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every surface that is selected for painting. This procedure returns a string, which is interpreted as a list of names referring to double array attributes on some dependency node. Q: When queried, it returns a string.
        getSurfaceCommand: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every dependency node on the selection list, whenever Artisan processes the selection list. It returns the name of the surface to paint on. Q: When queried, it returns a string.
        getValueCommand: (create, edit, query) - Specifies the name of the Mel script/procedure that is called every time a value on the surface is needed by the scriptable paint tool. Q: When queried, it returns a string.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        importfileload: (edit) - Load the attribute map a specified file.
        importfilemode: (create, edit, query) - Specifies the channel to import. The valid entries here are: "alpha", "luminance", "red", "green", "blue", and "rgb" C: Default is "alpha". Q: When queried, it returns a string.
        importreassign: (create, edit, query) - Specifies if the multiply atrribute maps are to be reassigned while importing. Only maps previously exported from within Artisan can be reassigned. C: Default is FALSE. Q: When queried, it returns a  boolean.
        initializeCmd: (create, edit, query) - Specifies the name of the Mel script/procedure that is called in the beginning of each stroke. Q: When queried, it returns a string.
        interactiveUpdate: (create, edit, query) - Specifies how often to transfer the painted values into the attribute. TRUE: transfer them "continuously" (many times per stroke) FALSE: transfer them only at the end of a stroke (on mouse button release). C: Default is TRUE. Q: When queried, it returns a boolean.
        lastRecorderCmd: (create, edit, query) - Value of last recorded command.
        lastStampName: (create, edit, query) - Value of the last stamp name.
        lowerradius: (create, edit, query) - Sets the lower size of the brush (only apply on tablet).
        makeStroke: (create, edit, multiuse, query) - Stroke point values.
        mappressure: (create, edit, query) - Sets the tablet pressure mapping when the table is used. There are three options: "Opacity" - the pressure is mapped to the opacity, "Radius" - the is mapped to modify the radius of the brush, "Both" - the pressure modifies both the opacity and the radius. C: Default is "Opacity". Q: When queried, it returns a string.
        maxvalue: (create, edit, query) - Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When queried, it returns a float.
        minvalue: (create, edit, query) - Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        name: (create) - If this is a tool command, name the tool appropriately.
        objattrArray: (query) - An array of all paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.MenuType. *MenuType: type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
        opacity: (create, edit, query) - Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
        outline: (create, edit, query) - Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it returns a boolean.
        outwhilepaint: (create, edit, query) - Specifies if the brush outline should be drawn while painting. C: Default is FALSE. Q: When queried, it returns a boolean.
        paintNodeArray: (query) - An array of paintable nodes. Q: When queried, it returns a string.
        paintattrselected: (edit) - An array of selected paintable attributes. Each element of the array is a string with the following information: NodeType.NodeName.AttributeName.
        paintmode: (create, edit, query) - Specifies the paint mode. There are two possibilities: "screen" and "tangent". C: Default is "screen". Q: When queried, it returns a string.
        paintoperationtype: (create, edit, query) - Specifies the operation type used by the Paint Tool.  Currently, we support the following paint modes: "Paint", "Smear", "Blur", "Erase" and "Clone". Default is "Paint".
        pickColor: (create, edit, query) - Set pick color mode on or off
        pickValue: (create, edit, query) - Toggle for picking
        playbackCursor: (create, edit, multiuse, query) - Values for the playback cursor.
        playbackPressure: (create, edit, multiuse, query) - Valus for the playback pressure.
        preserveclonesource: (create, edit, query) - Whether or not to preserve a clone source.
        profileShapeFile: (edit, query) - Passes a name of the image file for the stamp shape profile.
        projective: (create, edit, query) - Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        radius: (create, edit, query) - Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a float.
        rampMaxColor: (create, edit, query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (create, edit, query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        record: (create, edit, query) - Toggle on for recording.
        reflection: (create, edit, query) - Specifies the reflection mode. C: Default is 'false'. Q: When queried, it returns a boolean.
        reflectionaboutorigin: (create, edit, query) - Toggle on to reflect about the origin
        reflectionaxis: (create, edit, query) - Specifies the reflection axis. There are three possibilities: "x", "y" and "z". C: Default is "x". Q: When queried, it returns a string.
        screenRadius: (create, edit, query) - Brush radius on the screen
        selectclonesource: (create, edit, query) - Toggle on to select the clone source
        selectedattroper: (create, edit, query) - Sets the edit weight operation. Four edit weights operations are provided : "absolute" - the value of the weight is replaced by the current one, "additive" - the value of the weight is added to the current one, "scale" - the value of the weight is multiplied by the current one, "smooth" - the value of the weight is divided by the current one. C: Default is "absolute".  Q: When queried, it returns a string.
        setArrayValueCommand: (create, edit, query) - Specifies the name of the Mel script/procedure that is called for each paint stamp. A stamp may affect one or more values on the surface. This call rolls up all the calls that would be made to setValueCommand for the stamp into one call with array arguments. Q: When queried, it returns a string.
        setValueCommand: (create, edit, query) - Specifies the name of the Mel script/procedure that is called every time a value on the surface is changed. Q: When queried, it returns a string.
        showactive: (create, edit, query) - Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When queried, it returns a boolean.
        stampDepth: (create, edit, query) - Depth of the stamps
        stampProfile: (create, edit, query) - Sets the brush profile of the current stamp. Currently, the following profiles are supported: "gaussian", "poly", "solid" and "square". C: Default is gaussian. Q: When queried, it returns a string.
        stampSpacing: (create, edit, query) - Specifies the stamp spacing. Default is 1.0.
        strokesmooth: (create, edit, query) - Stroke smoothing type name
        surfaceConformedBrushVertices: (create, edit, query) - Enables/disables the the display of the effective brush area as affected vertices.
        tablet: (query) - Returns true if the tablet device is present, false if it is absent
        tangentOutline: (create, edit, query) - Enables/disables the display of the brush circle tangent to the surface.
        toolCleanupCmd: (create, edit, query) - Specifies the name of the Mel script/procedure that is called when this tool is exited. Q: When queried, it returns a string.
        toolOffProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned off. For example, cloth invokes "clothPaintToolOff" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is deactivated. It is typical that if you implement a toolOffProc you will want to implement a toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolOnProc: (create, edit, query) - Accepts a strings describing the name of a MEL procedure that is invoked whenever the tool is turned on. For example, cloth invokes "clothPaintToolOn" when the cloth paint tool is turned on. Define this callback if your tool requires special functionality when your tool is activated. It is typical that if you implement a toolOnProc you will want to implement a toolOffProc as well (see the -toolOffProc flag. In query mode, the name of the currently registered MEL command is returned and this will be an empty string if none is defined.
        toolSetupCmd: (create, edit, query) - Specifies the name of the Mel script/procedure that is called once for every selected surface when an initial click is received on that surface. Q: When queried, it returns a string.
        useColorRamp: (create, edit, query) - Specifies whether the user defined color ramp should be used to map values from to colors.  If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (create, edit, query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
        usepressure: (create, edit, query) - Sets the tablet pressure on/off. C: Default is false. Q: When queried, it returns a boolean.
        value: (create, edit, query) - Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it returns a float.
        whichTool: (create, edit, query) - The string defines the name of the tool to be used for the Artisan context. An example is "artClothPaint". In query mode, the tool name for the given context is returned. Note: due to the way MEL works, always specify the -query flag last when specifying a flag that takes arguments.
        worldRadius: (create, edit, query) - Radius in worldspace
    """
    pass


def assembly(*args, active: Optional[Union[str, bool]] = str, activeLabel: Optional[Union[str, bool]] = str, canCreate: Optional[Union[str, bool]] = str, createOptionBoxProc: Optional[Union[str, bool]] = str, createRepresentation: str = str, defaultType: Optional[Union[str, bool]] = str, deleteRepresentation: str = str, deregister: str = str, input: str = str, isAType: Optional[Union[str, bool]] = str, isTrackingMemberEdits: Optional[Union[str, bool]] = str, label: Optional[Union[str, bool]] = str, listRepTypes: bool = bool, listRepTypesProc: Optional[Union[str, bool]] = str, listRepresentations: bool = bool, listTypes: bool = bool, name: Optional[Union[str, bool]] = str, newRepLabel: str = str, postCreateUIProc: Optional[Union[str, bool]] = str, proc: str = str, renameRepresentation: str = str, repLabel: Optional[Union[str, bool]] = str, repName: str = str, repNamespace: Optional[Union[str, bool]] = str, repPostCreateUIProc: Optional[Union[str, bool]] = str, repPreCreateUIProc: Optional[Union[str, bool]] = str, repType: Optional[Union[str, bool]] = str, repTypeLabel: Optional[Union[str, bool]] = str, repTypeLabelProc: Optional[Union[str, bool]] = str, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command to register assemblies for the scene assembly framework, to create them, and to edit and query them. Assembly nodes are DAG nodes, and are therefore shown in the various DAG editors (Outliner, Hypergraph, Node Editor). At assembly creation time, the node name defaults to the node type name. The assembly command can create any node that is derived from the assembly node base class.  It also acts as a registry of these types, so that various scripting callbacks can be defined and registered with the assembly command.  These callbacks are invoked by Maya during operations on assembly nodes, and can be used to customize behavior.

    Args:
        active: (edit, query) - Set the active representation by name, or query the name of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified. Using an empty string as name means to inactivate the currently active representation.
        activeLabel: (edit, query) - Set the active representation by label, or query the label of the active representation. Edit mode can be applied to more than one assembly. Query mode will return a single string when only a single assembly is specified, and will return an array of strings when multiple assemblies are specified.
        canCreate: (query) - Query the representation types the specific assembly can create.
        createOptionBoxProc: (edit, query) - Set or query the option box menu procedure for a specific assembly type. The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        createRepresentation: (edit) - Create and add a specific type of representation for an assembly. If the representation type needs additional parameters, they must be specified using the "input" flag. For example, the Maya scene assembly reference implementation Cache and Scene representations need an input file.
        defaultType: (edit, query) - Set or query the default type of assembly.  When the assembly command is used to perform an operation on an assembly type rather than on an assembly object, it will be performed on the default type, unless the -type flag is used to specify an explicit assembly type.
        deleteRepresentation: (edit) - Delete a specific representation from an assembly.
        deregister: (edit) - Deregister a registered assembly type. If the deregistered type is the default type, the default type will be set to the empty string.
        input: (edit) - Specify the additional parameters of representation creation procedure when creating a representation. This flag must be used with createRepresentation flag.
        isAType: (query) - Query whether the given object is of an assembly type.
        isTrackingMemberEdits: (query) - Query whether the given object is tracking member edits.
        label: (edit, query) - Set or query the label for an assembly type. Assembly type is specified with flag "type". If no type specified, the default type is used.
        listRepTypes: (query) - Query the supported representation types for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        listRepTypesProc: (edit, query) - Set or query the procedure that provides the representation type list which an assembly type supports.  This procedure takes no argument, and returns a string array of representation types that represents the full set of representation types this assembly type can create.  The assembly type for which this procedure applies will be the default type, unless the type flag is used to specify an explicit assembly type.
        listRepresentations: (query) - Query the created representations list for a specific assembly.  The -repType flag can be used to filter the list and return representations for a single representation type.  If the -repType flag is not used, all created representations will be returned.
        listTypes: (query) - Query the supported assembly types.
        name: (create) - Specify the name of the assembly when creating it.
        newRepLabel: (edit) - Specify the representation label to set on representation label edit.
        postCreateUIProc: (edit, query) - Set or query the UI post-creation procedure for a given assembly type. This procedure will be invoked by Maya immediately after an assembly of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a newly-created assembly.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        proc: (edit) - Specify the procedure when setting the representation UI post- or pre-creation procedure, for a given assembly type.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type.
        renameRepresentation: (edit) - Renames the representation that is the argument to this flag.  The repName flag must be used to provide the new name.
        repLabel: (edit, query) - Query or edit the label of the representation that is the argument to this flag, for a given assembly.  In both query and edit modes, the -repLabel flag specifies the name of the representation.  In edit mode, the -newRepLabel flag must be used to specify the new representation label. 			In query mode, this flag needs a value.
        repName: (edit) - Specify the representation name to set on representation creation or rename. This flag is optional with the createRepresentation flag: if omitted, the assembly will name the representation.  It is mandatory with the renameRepresentation flag.
        repNamespace: (query) - Query the representation namespace of this assembly node. The value returned is used by Maya for creating the namespace where nodes created by the activation of a representation will be added. If a name clash occurs when the namespace is added to its parent namespace, Maya will update repNamespace with the new name. Two namespaces are involved when dealing with an assembly node: the namespace of the assembly node itself (which this flag does not affect or query), and the namespace of its representations. The representation namespace is a child of its assembly node's namespace. The assembly node's namespace is set by its containing assembly, if it is nested, or by the top-level file. Either the assembly node's namespace, or the representation namespace, or both, can be the empty string. It should be noted that if the assembly node is nested, the assembly node's namespace will be (by virtue of its nesting) the representation namespace of its containing assembly.
        repPostCreateUIProc: (edit, query) - Set or query the UI post-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes two arguments, the first the DAG path to the assembly, and the second the name of the representation.  It returns no value.  It will be invoked by Maya immediately after a representation of the specified type is created from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain and set initial parameters on a newly-created representation.  The representation type is the argument of this flag. The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type. 			In query mode, this flag needs a value.
        repPreCreateUIProc: (edit, query) - Set or query the UI pre-creation procedure for a specific representation type, and for a specific assembly type.  This procedure takes no argument, and returns a string that is passed as an argument to the -input flag when Maya invokes the assembly command with the -createRepresentation flag. The representation pre-creation procedure is invoked by Maya immediately before creating a representation of the specified type from the UI, but not through scripting.  It can be used to invoke a dialog, to obtain the creation argument for a new representation.  The representation type is the argument of this flag.  The -proc flag must be used to specify the procedure name.  The assembly type will be the default type, unless the -type flag is used to specify an explicit assembly type. 			In query mode, this flag needs a value.
        repType: (query) - Specify a representation type to use as a filter for the -listRepresentations query.  The representation type is the argument to this flag. 			In query mode, this flag needs a value.
        repTypeLabel: (query) - Query the label of the specific representation type. 			In query mode, this flag needs a value.
        repTypeLabelProc: (edit, query) - Set or query the procedure that provides the representation type label, for a given assembly type.  The procedure takes the representation type as its sole argument, and returns a localized representation type label. The assembly type for which this procedure applies will be the default type, unless the -type flag is used to specify an explicit assembly type.
        type: (create, edit, query) - Set or query properties for the specified registered assembly type. 			In query mode, this flag needs a value.
    """
    pass


def attributeInfo(*args, allAttributes: bool = bool, bool: bool = bool, enumerated: bool = bool, hidden: bool = bool, inherited: bool = bool, internal: bool = bool, leaf: bool = bool, logicalAnd: bool = bool, multi: bool = bool, short: bool = bool, userInterface: bool = bool, writable: bool = bool, type: Optional[Union[str, bool]] = str):
    """
    This command lists all of the attributes that are marked with certain flags.  Combinations of flags may be specified and all will be considered. (The method of combination depends on the state of the "logicalAnd/and" flag.) When the "allAttributes/all" flag is specified, attributes of all types will be listed.

    Args:
        allAttributes: (create) - Show all attributes associated with the node regardless of type. Use of this flag overrides any other attribute type flags and logical operation that may be specified on the command.
        bool: (create) - Show the attributes that are of type boolean. Use the 'on' state to get only boolean attributes; the 'off' state to ignore boolean attributes.
        enumerated: (create) - Show the attributes that are of type enumerated. Use the 'on' state to get only enumerated attributes; the 'off' state to ignore enumerated attributes.
        hidden: (create) - Show the attributes that are marked as hidden. Use the 'on' state to get hidden attributes; the 'off' state to get non-hidden attributes.
        inherited: (create) - Filter the attributes based on whether they belong to the node type directly or have been inherited from a root type (e.g. meshShape/direct or dagObject/inherited). Use the 'on' state to get only inherited attributes, the 'off' state to get only directly owned attributes, and leave the flag unspecified to get both.
        internal: (create) - Show the attributes that are marked as internal to the node. Use the 'on' state to get internal attributes; the 'off' state to get non-internal attributes.
        leaf: (create) - Show the attributes that are complex leaves (ie. that have parent attributes and have no children themselves). Use the 'on' state to get leaf attributes; the 'off' state to get non-leaf attributes.
        logicalAnd: (create) - The default is to take the logical 'or' of the above conditions. Specifying this flag switches to the logical 'and' instead.
        multi: (create) - Show the attributes that are multis. Use the 'on' state to get multi attributes; the 'off' state to get non-multi attributes.
        short: (create) - Show the short attribute names instead of the long names.
        userInterface: (create) - Show the UI-friendly attribute names instead of the Maya ASCII names. Takes precedence over the -s/-short flag if both are specified.
        writable: (create) - Show the attributes that are writable (ie. can have input connections). Use the 'on' state to get writable attributes; the 'off' state to get non-writable attributes.
        type: (create) - static node type from which to get 'affects' information
    """
    pass


def attributeName(*args, leaf: bool = bool, long: bool = bool, nice: bool = bool, short: bool = bool):
    """
    This command takes one "node.attribute"-style specifier on the command line and returns either the attribute's long, short, or nice name.  (The "nice" name, or UI name, is the name used to display the attribute in Maya's interface, and may be localized when running Maya in a language other than English.) If more than one "node.attribute" specifier is given on the command line, only the first valid specifier is processed.

    Args:
        leaf: (create) - When false, shows parent multi attributes (like "controlPoints[2].xValue").  When true, shows only the leaf-level attribute name (like "xValue").  Default is true. Note that for incomplete attribute strings, like a missing multi-parent index ("controlPoints.xValue") or an incorrectly named compound (cntrlPnts[2].xValue), this flag defaults to true and provides a result as long as the named leaf-level attribute is defined for the node.
        long: (create) - Returns names in "long name" format like "translateX"
        nice: (create) - Returns names in "nice name" format like "Translate X"
        short: (create) - Returns names in "short name" format like "tx"
    """
    pass


def attributeQuery(*args, affectsAppearance: bool = bool, affectsWorldspace: bool = bool, attributeType: bool = bool, cachedInternally: bool = bool, categories: bool = bool, channelBox: bool = bool, connectable: bool = bool, enum: bool = bool, exists: bool = bool, hidden: bool = bool, indeterminant: bool = bool, indexMatters: bool = bool, internal: bool = bool, internalGet: bool = bool, internalSet: bool = bool, keyable: bool = bool, listChildren: bool = bool, listDefault: bool = bool, listEnum: bool = bool, listParent: bool = bool, listSiblings: bool = bool, localizedListEnum: bool = bool, longName: bool = bool, maxExists: bool = bool, maximum: bool = bool, message: bool = bool, minExists: bool = bool, minimum: bool = bool, multi: bool = bool, niceName: bool = bool, node: Optional[Union[str, bool]] = str, numberOfChildren: bool = bool, range: bool = bool, rangeExists: bool = bool, readable: bool = bool, renderSource: bool = bool, shortName: bool = bool, softMax: bool = bool, softMaxExists: bool = bool, softMin: bool = bool, softMinExists: bool = bool, softRange: bool = bool, softRangeExists: bool = bool, storable: bool = bool, type: Optional[Union[str, bool]] = str, typeExact: Optional[Union[str, bool]] = str, usedAsColor: bool = bool, usedAsFilename: bool = bool, usesMultiBuilder: bool = bool, worldspace: bool = bool, writable: bool = bool):
    """
    attributeQuery returns information about the configuration of an attribute. It handles both boolean flags, returning true or false, as well as other return values. Specifying more than one boolean flag will return the logical "and" of all the specified boolean flags.  You may not specify any two flags when both do not provide a boolean return type.  (eg. "-internal -hidden" is okay but "-range -hidden" or "-range -softRange" is not.)

    Args:
        affectsAppearance: (create) - Return true if the attribute affects the appearance of the node
        affectsWorldspace: (create) - Return the status of the attribute flag marking attributes affecting worldspace
        attributeType: (create) - Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).
        cachedInternally: (create) - Return whether the attribute is cached within the node as well as in the datablock
        categories: (create) - Return the categories to which the attribute belongs or an empty list if it does not belong to any.
        channelBox: (create) - Return whether the attribute should show up in the channelBox or not
        connectable: (create) - Return the connectable status of the attribute
        enum: (create) - Return true if the attribute is a enum attribute
        exists: (create) - Return true if the attribute exists
        hidden: (create) - Return the hidden status of the attribute
        indeterminant: (create) - Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time
        indexMatters: (create) - Return the indexMatters status of the attribute
        internal: (create) - Return true if the attribute is either internalSet or internalGet
        internalGet: (create) - Return true if the attribute come from getCachedValue
        internalSet: (create) - Return true if the attribute must be set through setCachedValue
        keyable: (create) - Return the keyable status of the attribute
        listChildren: (create) - Return the list of children attributes of the given attribute.
        listDefault: (create) - Return the default values of numeric and compound numeric attributes.
        listEnum: (create) - Return the list of enum strings for the given attribute.
        listParent: (create) - Return the parent of the given attribute.
        listSiblings: (create) - Return the list of sibling attributes of the given attribute.
        localizedListEnum: (create) - Return the list of localized enum strings for the given attribute.
        longName: (create) - Return the long name of the attribute.
        maxExists: (create) - Return true if the attribute has a hard maximum. A min does not have to be present.
        maximum: (create) - Return the hard maximum of the attribute's value
        message: (create) - Return true if the attribute is a message attribute
        minExists: (create) - Return true if the attribute has a hard minimum. A max does not have to be present.
        minimum: (create) - Return the hard minimum of the attribute's value
        multi: (create) - Return true if the attribute is a multi-attribute
        niceName: (create) - Return the nice name (or "UI name") of the attribute.
        node: (create) - Use all attributes from node named NAME
        numberOfChildren: (create) - Return the number of children the attribute has
        range: (create) - Return the hard range of the attribute's value
        rangeExists: (create) - Return true if the attribute has a hard range. Both min and max must be present.
        readable: (create) - Return the readable status of the attribute
        renderSource: (create) - Return whether this attribute is marked as a render source or not
        shortName: (create) - Return the short name of the attribute.
        softMax: (create) - Return the soft max (slider range) of the attribute's value
        softMaxExists: (create) - Return true if the attribute has a soft maximum. A min does not have to be present.
        softMin: (create) - Return the soft min (slider range) of the attribute's value
        softMinExists: (create) - Return true if the attribute has a soft minimum. A max does not have to be present.
        softRange: (create) - Return the soft range (slider range) of the attribute's value
        softRangeExists: (create) - Return true if the attribute has a soft range. Both min and max must be present.
        storable: (create) - Return true if the attribute is storable
        type: (create) - Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.
        typeExact: (create) - Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.
        usedAsColor: (create) - Return true if the attribute should bring up a color picker
        usedAsFilename: (create) - Return true if the attribute should bring up a file browser
        usesMultiBuilder: (create) - Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data
        worldspace: (create) - Return the status of the attribute flag marking worldspace attribute
        writable: (create) - Return the writable status of the attribute
    """
    pass


def bakePartialHistory(*args, allShapes: bool = bool, postSmooth: bool = bool, preCache: bool = bool, preDeformers: bool = bool, prePostDeformers: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command is used to bake sections of the construction history of a shape node when possible. A typical usage would be on a shape that has both modelling operations and deformers in its history. Using this command with the -prePostDeformers flag will bake the modeling portions of the graph, so that only the deformers remain.

    Args:
        allShapes: (create, query) - Specifies that the bake operation should be performed on all shapes in the entire scene. By default, only selected objects are baked. If this option is specified and there are no shapes in the scene, then this command will do nothing and end successfully.
        postSmooth: (create, query) - Specifies whether or not a smoothing operation should be done on skin vertices. This smoothing is only done on vertices that are found to deviate largely from other vertex values.  The default is false.
        preCache: (create, query) - Specifies baking of any history operations that occur before the caching operation, including deformers. In query mode, returns a list of the nodes that will be baked.
        preDeformers: (create, query) - Specifies baking of any modeling operations in the history that occur before the deformers. In query mode, returns a list of the nodes that will be baked.
        prePostDeformers: (create, query) - Specifies baking of all modeling operations in the history whether they are before or after the deformers in the history. If neither the -prePostDeformers nor the -preDeformers flag is specified, prePostDeformers will be used as the default. In query mode, returns a list of the nodes that will be baked.
    """
    pass


def baseTemplate(*args, exists: bool = bool, fileName: Optional[Union[str, bool]] = str, force: bool = bool, load: bool = bool, matchFile: Optional[Union[str, bool]] = str, silent: bool = bool, unload: bool = bool, viewList: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This is the class for the commands that edit and/or query templates.

    Args:
        exists: (query) - Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        fileName: (create, query) - Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is recommended but not required that the filename and template name correspond.
        force: (create) - This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        load: () - Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.
        matchFile: (query) - Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation. 			In query mode, this flag needs a value.
        silent: (create, edit, query) - Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        unload: (create) - Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        viewList: (create, query) - Used in query mode, returns a list of all views defined on the template.
    """
    pass


def baseView(*args, itemInfo: Optional[Union[str, bool]] = str, itemList: bool = bool, viewDescription: bool = bool, viewLabel: bool = bool, viewList: bool = bool, viewName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    A view defines the layout information for the attributes of a particular node type or container.  Views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node or for a given template.  The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes), when applicable.

    Args:
        itemInfo: (query) - Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.  itemIndex  : sequential item number (0-based) itemName   : item name (string) itemLabel  : item display label (string) itemDescription : item description field (string) itemLevel  : item hierarchy level (0-n) itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute itemNumChildren: number of immediate children (groups or attributes) of this item itemAttrType : item attribute type (string) itemCallback : item callback field (string)  In query mode, this flag needs a value.
        itemList: (query) - Used in query mode, the command will return a list of information for each item in the view.  The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).
        viewDescription: (query) - Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.
        viewLabel: (query) - Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view.  Use of the view label is usually more suitable than the view name for display purposes.
        viewList: (query) - Used in query mode, command will return a list of all views defined for the given target (container or template).
        viewName: (query) - Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built-in views modes. For this reason, the view label is generally more suitable for display purposes. 			In query mode, this flag can accept a value.
    """
    pass


def boxDollyCtx(*args, alternateContext: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, toolName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a dolly context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        toolName: (create, query) - Name of the specific tool to which this command refers.
    """
    pass


def boxZoomCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, zoomScale: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a box zoom context. If this context is used on a perspective camera, the field of view and view direction are changed. If the camera is orthographic, the orthographic width and eye point are changed. The left and middle mouse interactively zoom the view. The control key can be used to enable box zoom. A box starting from left to right will zoom in, and a box starting from right to left will zoom out.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        zoomScale: (create, edit, query) - Scale the zoom.
    """
    pass


def clipEditorCurrentTimeCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to change current time within the track area of a clip editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def color(*args, rgbColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), userDefined: Optional[Union[int, bool]] = int):
    """
    This command sets the dormant wireframe color of the specified objects to be their class color or if the -ud/userDefined flag is specified, one of the user defined colors. The -rgb/rgbColor flags can be specified if the user requires floating point RGB colors.

    Args:
        rgbColor: (create) - Specifies and rgb color to set the selected object to.
        userDefined: (create) - Specifies the user defined color index to set selected object to. The valid range of numbers is [1-8].
    """
    pass


def colorIndex(*args, hueSaturationValue: bool = bool, resetToFactory: bool = bool, resetToSaved: bool = bool, query: bool = bool):
    """
    The index specifies a color index in the color palette. The r, g, and b values (between 0-1) specify the RGB values (or the HSV values if the -hsv flag is used) for the color.

    Args:
        hueSaturationValue: (create, query) - Indicates that rgb values are really hsv values. Upon query, returns the HSV valuses as an array of 3 floats.
        resetToFactory: (create) - Resets all color index palette entries to their factory defaults.
        resetToSaved: (create) - Resets all color palette entries to their saved values.
    """
    pass


def colorManagementCatalog(*args, addTransform: Optional[Union[str, bool]] = str, editUserTransformPath: Optional[Union[str, bool]] = str, listSupportedExtensions: bool = bool, listTransformConnections: bool = bool, path: Optional[Union[str, bool]] = str, queryUserTransformPath: bool = bool, removeTransform: Optional[Union[str, bool]] = str, transformConnection: Optional[Union[str, bool]] = str, type: Optional[Union[str, bool]] = str):
    """
    This non-undoable action performs additions and removals of custom color transforms from the Autodesk native color transform catalog.  Once a custom color transform has been added to the catalog, it can be used in the same way as the builtin Autodesk native color transforms.

    Args:
        addTransform: (create) - Add transform to collection.
        editUserTransformPath: (create) - Edit the user transform directory. By changing the directory, all custom transforms currently added could be changed, and new ones could appear.
        listSupportedExtensions: (create) - List the file extensions that are supported by add transform.  This list is valid for all transform types, and therefore this flag does not require use of the type flag.
        listTransformConnections: (create) - List the transforms that can be used as source (for "view" and "output" types) or destination (for "input" and "rendering space" types) to connect a custom transform to the rest of the transform collection.
        path: (create) - In addTransform mode, the path to the transform data file.
        queryUserTransformPath: (create) - Query the user transform directory.
        removeTransform: (create) - Remove transform from collection.
        transformConnection: (create) - In addTransform mode, an existing transform to which the added transform will be connected. For an input transform or rendering space transform, this will be a destination. For a view or output transform, this will be a source.
        type: (create) - The type of transform added, removed, or whose transform connections are to be listed. Must be one of "view", "rendering space", "input", or "output".
    """
    pass


def colorManagementConvert(*args, toDisplaySpace: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float)):
    """
    This command can be used to convert rendering (a.k.a. working) space color values to display space color values. This is useful if you create custom UI with colors painted to screen, where you need to handle color management yourself. The current view transform set in the Color Management user preferences will be used.

    Args:
        toDisplaySpace: (create) - Converts the given RGB value to display space.
    """
    pass


def colorManagementFileRules(*args, addRule: Optional[Union[str, bool]] = str, colorSpace: Optional[Union[str, bool]] = str, colorSpaceDescription: Optional[Union[str, bool]] = str, colorSpaceFamilies: Optional[Union[str, bool]] = str, colorSpaceNames: bool = bool, down: Optional[Union[str, bool]] = str, enabled: bool = bool, evaluate: Optional[Union[str, bool]] = str, extension: Optional[Union[str, bool]] = str, listRules: bool = bool, load: bool = bool, moveUp: Optional[Union[str, bool]] = str, pattern: Optional[Union[str, bool]] = str, remove: Optional[Union[str, bool]] = str, restoreDefaults: bool = bool, save: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This non-undoable action manages the list of rules that Maya uses to assign an initial input color space to dependency graph nodes that read in color information from a file.  Rules are structured in a chain of responsibility, from highest priority rule to lowest priority rule, each rule matching a file path pattern and extension.  If a rule matches a given file path, its color space is returned as the result of rules evaluation, and no further rule is considered.  The lowest priority rule will always return a match. Rules can be added, removed, and changed in priority in the list.  Each rule can have its file path pattern, extension, and color space changed. The rule list can be saved to user preferences, and loaded from user preferences.

    Args:
        addRule: (create) - Add a rule with the argument name to the list of rules, as the highest-priority rule.  If this flag is used, the pattern, extension, and colorSpace flags must be used as well, to specify the file rule pattern, extension, and color space, respectively.
        colorSpace: (create, edit, query) - The input color space for the rule.  If the rule matches a file path, this is the color space that is returned.  This color space must match an existing color space in the input color space list.
        colorSpaceDescription: (query) - Returns the description for a specific color space. 			In query mode, this flag needs a value.
        colorSpaceFamilies: (query) - Returns the list of families for a specific color space. Used to add submenus when populating the color spaces UI popup of a rule. 			In query mode, this flag needs a value.
        colorSpaceNames: (query) - Returns the list of available color spaces. Used to populate the color spaces UI popup of a rule.
        down: (create) - Move the rule with the argument name down one position towards lower priority.
        enabled: (query) - Are the file rules enabled?
        evaluate: (create) - Evaluates the list of rules and returns the input color space name that corresponds to the argument file path.
        extension: (create, edit, query) - The file extension for the rule is case insensitive
        listRules: (create) - Returns an array of rule name strings, in order, from lowest-priority (rule 0) to highest-priority (last rule in array).
        load: (create) - Read the rules from Maya preferences.  Any existing rules are cleared.
        moveUp: (create) - Move the rule with the argument name up one position towards higher priority.
        pattern: (create, edit, query) - The file path pattern for the rule.  This is the substring to match in the file path, expressed as a glob pattern: for example, '*' matches all files. For more information about glob pattern syntax, see http://en.wikipedia.org/wiki/Glob_%28programming%29.
        remove: (create) - Remove the rule with the argument name from the list of rules.
        restoreDefaults: (create) - Restore the list of rules to the default ones only.
        save: (create) - Save the rules to Maya preferences.
    """
    pass


def colorManagementPrefs(*args, cmConfigFileEnabled: bool = bool, cmEnabled: bool = bool, colorManageAllNodes: bool = bool, colorManagePots: bool = bool, colorManagedNodes: bool = bool, colorManagementSDKVersion: Optional[Union[str, bool]] = str, configFilePath: Optional[Union[str, bool]] = str, configFileVersion: Optional[Union[str, bool]] = str, defaultInputSpaceName: Optional[Union[str, bool]] = str, displayName: Optional[Union[str, bool]] = str, displayNames: bool = bool, equalsToPolicyFile: Optional[Union[str, bool]] = str, exportPolicy: Optional[Union[str, bool]] = str, inhibitEvents: bool = bool, inputSpaceDescription: Optional[Union[str, bool]] = str, inputSpaceFamilies: Optional[Union[str, bool]] = str, inputSpaceNames: bool = bool, loadPolicy: Optional[Union[str, bool]] = str, loadedDefaultInputSpaceName: Optional[Union[str, bool]] = str, loadedDisplayName: Optional[Union[str, bool]] = str, loadedOutputTransformName: Optional[Union[str, bool]] = str, loadedRenderingSpaceName: Optional[Union[str, bool]] = str, loadedViewName: Optional[Union[str, bool]] = str, loadedViewTransformName: Optional[Union[str, bool]] = str, missingColorSpaceNodes: bool = bool, ocioRulesEnabled: bool = bool, ociov2Enabled: bool = bool, outputTarget: Optional[Union[str, bool]] = str, outputTransformEnabled: bool = bool, outputTransformName: Optional[Union[str, bool]] = str, outputTransformNames: bool = bool, outputTransformUseColorConversion: bool = bool, outputUseViewTransform: bool = bool, policyFileName: Optional[Union[str, bool]] = str, popupOnError: bool = bool, refresh: bool = bool, renderingSpaceName: Optional[Union[str, bool]] = str, renderingSpaceNames: bool = bool, restoreDefaults: bool = bool, viewDisplayNames: Optional[Union[str, bool]] = str, viewName: Optional[Union[str, bool]] = str, viewNames: bool = bool, viewTransformName: Optional[Union[str, bool]] = str, viewTransformNames: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command allows querying and editing the color management global data in a scene.  It also allows for setting the view transform and rendering space which automatically configures the color processing in the enabled views.

    Args:
        cmConfigFileEnabled: (edit, query) - Turn on or off applying an OCIO configuration file.  If set, the color management configuration set in the preferences is used.
        cmEnabled: (edit, query) - Turn on or off color management in general.  If set, the color management configuration set in the preferences is used.
        colorManageAllNodes: (create) - Adds color management to all input nodes such as file texture nodes
        colorManagePots: (edit, query) - Turn on or off color management of color pots in the UI.  If set, colors in color pots are taken to be in rendering space, and are displayed after being transformed by the view transform set in the preferences.
        colorManagedNodes: (query) - Gets the names of all nodes that apply color management to bring pixels from an input color space to the rendering space. Examples include file texture node.
        colorManagementSDKVersion: (query) - Obtain the version of the color management SDK used by Maya.
        configFilePath: (edit, query) - The configuration file to be used, if color management is enabled.
        configFileVersion: (query) - Obtain the version of the config version.
        defaultInputSpaceName: (edit, query) - This flag is obsolete.  See the colorManagementFileRules command for more information.
        displayName: (edit, query) - The display from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        displayNames: (query) - Returns the list of available displays.  Used to populate the color management preference UI popup.
        equalsToPolicyFile: (query) - Query if the current loaded policy settings is the same with the settings described in the policy file which is the argument of the command. 			In query mode, this flag needs a value.
        exportPolicy: (create) - Export the color management parameters to policy file
        inhibitEvents: (create) - Inhibit client-server notifications and event triggers which occur when changing the color management settings.
        inputSpaceDescription: (query) - Returns the description for a specific input color space. 			In query mode, this flag needs a value.
        inputSpaceFamilies: (query) - Returns the list of families for a specific input color space. Used to add submenus when populating the input color spaces UI popup. 			In query mode, this flag needs a value.
        inputSpaceNames: (query) - Returns the list of available input color spaces. Used to populate the input color spaces UI popup.
        loadPolicy: (create) - Load the color management policy file. This file overides the color management settings.
        loadedDefaultInputSpaceName: (query) - This flag is obsolete.
        loadedDisplayName: (query) - Gets the loaded display from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedOutputTransformName: (query) - Gets the loaded output transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedRenderingSpaceName: (query) - Gets the loaded rendering space.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedViewName: (query) - Gets the loaded view from the (display, view) pair.  Used by file open, import, and reference to check for missing color spaces or transforms.
        loadedViewTransformName: (query) - Gets the loaded view transform.  Used by file open, import, and reference to check for missing color spaces or transforms.
        missingColorSpaceNodes: (query) - Gets the names of the nodes that have color spaces not defined in the selected transform collection or in the selected config file. Note that an inactive color space is not a missing color space.
        ocioRulesEnabled: (edit, query) - Turn on or off the use of colorspace assignment rules from the OCIO library.
        ociov2Enabled: (query) - Is OCIOv2 the colour management system by default.
        outputTarget: (edit, query) - Indicates to which output the outputTransformEnabled or the outputTransformName flags are to be applied. Valid values are "renderer" or "playblast". 			In query mode, this flag needs a value.
        outputTransformEnabled: (edit, query) - Turn on or off applying the output transform for out of viewport renders. If set, the output transform set in the preferences is used.
        outputTransformName: (edit, query) - The output transform to be applied for out of viewport renders.  Disables output use view transform mode.
        outputTransformNames: (query) - Returns the list of available output transforms.
        outputTransformUseColorConversion: (edit, query) - Turn on or off selecting the color space conversion for the output color space of viewport renders.  If set, a conversion color space is used; otherwise, a view transform is used.
        outputUseViewTransform: (edit, query) - Turns use view transform mode on.  In this mode, the output transform is set to match the view transform.  To turn the mode off, set an output transform using the outputTransformName flag.
        policyFileName: (edit, query) - Set the policy file name
        popupOnError: (edit) - Turn on or off displaying a modal popup on error (as well as the normal script editor reporting of the error), for this invocation of the command.  Default is off.
        refresh: (create) - Refresh the color management.
        renderingSpaceName: (edit, query) - The color space to be used during rendering.  This is the source color space to the viewing transform, for color managed viewers and color managed UI controls, and the destination color space for color managed input pixels.
        renderingSpaceNames: (query) - Returns the list of available rendering spaces.  Used to populate the color management preference UI popup.
        restoreDefaults: (create) - Restore the color management settings to their default value.
        viewDisplayNames: (query) - Returns the list of available views for a specific display. Used to populate the view name list UI for file and image plane nodes. 			In query mode, this flag needs a value.
        viewName: (edit, query) - The view from the (display, view) pair, to be applied by color managed viewers and color managed UI controls.
        viewNames: (query) - Returns the list of available views from the selected display.  Used to populate the color management preference UI popup.
        viewTransformName: (edit, query) - The view transform to be applied by color managed viewers and color managed UI controls.
        viewTransformNames: (query) - Returns the list of available view transforms.  Used to populate the color management preference UI popup.
    """
    pass


def commandLogging(*args, historySize: Optional[Union[int, bool]] = int, logCommands: bool = bool, logFile: Optional[Union[str, bool]] = str, recordCommands: bool = bool, resetLogFile: bool = bool, query: bool = bool):
    """
    This command controls logging of Maya commands, in memory and on disk.

    Args:
        historySize: (create, query) - Sets the number of entries in the in-memory command history.
        logCommands: (create, query) - Enables or disables the on-disk logging of commands.
        logFile: (create, query) - Sets the filename to use for the on-disk log. If logging is active, the current file will be closed before the new one is opened.
        recordCommands: (create, query) - Enables or disables the in-memory logging of commands.
        resetLogFile: (create, query) - Reset the log filename to the default ('mayaCommandLog.txt' in the application folder, alongside 'Maya.env' and the default projects folder).
    """
    pass


def commandPort(*args, bufferSize: Optional[Union[int, bool]] = int, close: bool = bool, echoOutput: bool = bool, listPorts: bool = bool, name: Optional[Union[str, bool]] = str, noreturn: bool = bool, pickleOutput: bool = bool, prefix: Optional[Union[str, bool]] = str, returnNumCommands: bool = bool, securityWarning: bool = bool, sourceType: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    Opens or closes the Maya command port. The command port comprises a socket to which a client program may connect. An example command port client "mcp" is included in the Motion Capture developers kit.

    Args:
        bufferSize: (create) - Commands and results are each subject to size limits. This option allows the user to specify the size of the buffer used to communicate with Maya. If unspecified the default buffer size is 4096 characters. Commands longer than bufferSize characters will cause the client connection to close. Results longer that bufferSize characters are replaced with an error message.
        close: (create) - Closes the commandPort, deletes the pipes
        echoOutput: (create) - Sends a copy of all command output to the command port. Typically only the result is transmitted. This option provides a copy of all output.
        listPorts: (create) - Returns the available ports
        name: (create) - Specifies the name of the command port which this command creates. CommandPort names of the form name create a UNIX domain socket on the localhost corresponding to name. If name does not begin with "/", then /tmp/name is used. If name begins with "/", name denotes the full path to the socket.  Names of the form :port number create an INET domain on the local host at the given port.
        noreturn: (create) - Do not write the results from executed commands back to the command port socket. Instead, the results from executed commands are written to the script editor window. As no information passes back to the command port client regarding the execution of the submitted commands, care must be taken not to overflow the command buffer, which would cause the connection to close.
        pickleOutput: (create) - Python output will be pickled.
        prefix: (create) - The string argument is the name of a Maya command taking one string argument. This command is called each time data is sent to the command port. The data written to the command port is passed as the argument to the prefix command. The data from the command port is encoded as with enocodeString and enclosed in quotes.  If newline characters are embedded in the command port data, the input is split into individual lines. These lines are treated as if they were separate writes to the command port. Only the result to the last prefix command is returned.
        returnNumCommands: (create) - Ignore the result of the command, but return the number of commands that have been read and executed in this call. This is a simple way to track buffer overflow. This flag is ignored when the noreturn flag is specified.
        securityWarning: (create) - Enables security warning on command port input.
        sourceType: (create) - The string argument is used to indicate which source type would be passed to the commandPort, like "mel", "python". The default source type is "mel".
    """
    pass


def connectAttr(*args, force: bool = bool, lock: bool = bool, nextAvailable: bool = bool, referenceDest: Optional[Union[str, bool]] = str):
    """
    Connect the attributes of two dependency nodes and return the names of the two connected attributes. The connected attributes must be be of compatible types. First argument is the source attribute, second one is the destination.

    Args:
        force: (create) - Forces the connection.  If the destination is already connected, the old connection is broken and the new one made.
        lock: (create) - If the argument is true, the destination attribute is locked after making the connection. If the argument is false, the connection is unlocked before making the connection.
        nextAvailable: (create) - If the destination multi-attribute has set the indexMatters to be false with this flag specified, a connection is made to the next available index. No index need be specified.
        referenceDest: (create) - This flag is used for file io only. The flag indicates that the connection replaces a connection made in a referenced file, and the flag argument indicates the original destination from the referenced file. This flag is used so that if the reference file is modified, maya can still attempt to make the appropriate connections in the main scene to the referenced object.
    """
    pass


def connectionInfo(*args, destinationFromSource: bool = bool, getExactDestination: bool = bool, getExactSource: bool = bool, getLockedAncestor: bool = bool, isDestination: bool = bool, isExactDestination: bool = bool, isExactSource: bool = bool, isLocked: bool = bool, isSource: bool = bool, sourceFromDestination: bool = bool):
    """
    The

    Args:
        destinationFromSource: (create) - If the specified plug (or its ancestor) is a source, this flag returns the list of destinations connected from the source. (array of strings, empty array if none)
        getExactDestination: (create) - If the plug or its ancestor is connection destination, this returns the name of the plug that is the exact destination. (empty string if there is no such connection).
        getExactSource: (create) - If the plug or its ancestor is a connection source, this returns the name of the plug that is the exact source. (empty string if there is no such connection).
        getLockedAncestor: (create) - If the specified plug is locked, its name is returned.  If an ancestor of the plug is locked, its name is returned.  If more than one ancestor is locked, only the name of the closest one is returned.  If neither this plug nor any ancestors are locked, an empty string is returned.
        isDestination: (create) - Returns true if the plug (or its ancestor) is the destination of a connection, false otherwise.
        isExactDestination: (create) - Returns true if the plug is the exact destination of a connection, false otherwise.
        isExactSource: (create) - Returns true if the plug is the exact source of a connection, false otherwise.
        isLocked: (create) - Returns true if this plug (or its ancestor) is locked
        isSource: (create) - Returns true if the plug (or its ancestor) is the source of a connection, false otherwise.
        sourceFromDestination: (create) - If the specified plug (or its ancestor) is a destination, this flag returns the source of the connection. (string, empty if none)
    """
    pass


def container(*args, addNode: Optional[Union[List[str], bool]] = [str], asset: Optional[Union[List[str], bool]] = [str], assetMember: Optional[Union[str, bool]] = str, bindAttr: Optional[Union[Tuple[str, str], bool]] = [str, str], connectionList: bool = bool, current: bool = bool, fileName: Optional[Union[List[str], bool]] = [str], findContainer: Optional[Union[List[str], bool]] = [str], force: bool = bool, includeHierarchyAbove: bool = bool, includeHierarchyBelow: bool = bool, includeNetwork: bool = bool, includeNetworkDetails: Optional[Union[str, bool]] = str, includeShaders: bool = bool, includeShapes: bool = bool, includeTransform: bool = bool, isContainer: bool = bool, name: Optional[Union[str, bool]] = str, nodeList: bool = bool, nodeNamePrefix: bool = bool, parentContainer: bool = bool, preview: bool = bool, publishAndBind: Tuple[str, str] = [str, str], publishAsChild: Optional[Union[Tuple[str, str], bool]] = [str, str], publishAsParent: Optional[Union[Tuple[str, str], bool]] = [str, str], publishAsRoot: Optional[Union[Tuple[str, bool], bool]] = [str, bool], publishAttr: Optional[Union[str, bool]] = str, publishConnections: bool = bool, publishName: Optional[Union[str, bool]] = str, removeContainer: bool = bool, removeNode: List[str] = [str], type: Optional[Union[str, bool]] = str, unbindAndUnpublish: str = str, unbindAttr: Optional[Union[Tuple[str, str], bool]] = [str, str], unbindChild: str = str, unbindParent: str = str, unpublishChild: str = str, unpublishName: str = str, unpublishParent: str = str, unsortedOrder: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create and query container nodes. It is also used to perform operations on containers such as:

    Args:
        addNode: (create, edit) - Specifies the list of nodes to add to container.
        asset: (query) - When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.
        assetMember: (query) - Can be used during query in conjunction with the bindAttr flag to query for the only published attributes related to the specified node within the container.       In query mode, this flag needs a value.
        bindAttr: (edit, query) - Bind a contained attribute to an unbound published name on the interface of the container; returns a list of bound published names. The first string specifies the node and attribute name to be bound in "node.attr" format. The second string specifies the name of the unbound published name. In query mode, returns a string array of the published names and their corresponding attributes. The flag can also be used in query mode in conjunction with the -publishName, -publishAsParent, and -publishAsChild flags.
        connectionList: (query) - Returns a list of the exterior connections to the container node.
        current: (create, edit, query) - In create mode, specify that the newly created asset should be current. In edit mode, set the selected asset as current. In query, return the current asset.
        fileName: (query) - Used to query for the assets associated with a given file name.       In query mode, this flag needs a value.
        findContainer: (query) - When queried, if all the nodes in nodeList belong to the same container, returns container's name. Otherwise returns empty string.       In query mode, this flag needs a value.
        force: (create, edit) - This flag can be used in conjunction with -addNode and -removeNode flags only. If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one. If specified with -removeNode, nodes will be removed from all containers, instead of remaining in the parent container if being removed from a nested container.
        includeHierarchyAbove: (create, edit) - Used to specify that the parent hierarchy of the supplied node list should also be included in the container (or deleted from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        includeHierarchyBelow: (create, edit) - Used to specify that the hierarchy below the supplied node list should also be included in the container (or delete from the container). Hierarchy inclusion will stop at nodes which are members of other containers.
        includeNetwork: (create, edit) - Used to specify that the node network connected to supplied node list should also be included in the container. Network traversal will stop at default nodes and nodes which are members of other containers.
        includeNetworkDetails: (create, edit, multiuse) - Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even when constraints are not specified as an input.
        includeShaders: (create, edit) - Used to specify that for any shapes included, their shaders will also be included in the container.
        includeShapes: (create, edit) - Used to specify that for any transforms selected, their direct child shapes will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyBelow is used since the child shapes and all other descendents will automatically be included.
        includeTransform: (create, edit) - Used to specify that for any shapes selected, their parent transform will be included in the container (or deleted from the container). This flag is not necessary when includeHierarchyAbove is used since the parent transform and all of its parents will automatically be included.
        isContainer: (query) - Return true if the selected or specified node is a container node. If multiple containers are queried, only the state of the first will be returned.
        name: (create) - Sets the name of the newly-created container.
        nodeList: (query) - When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container. This will also display any reordering done with the reorderContainer command.
        nodeNamePrefix: (create, edit) - Specifies that the name of published attributes should be of the form "node_attr". Must be used with the -publishConnections/-pc flag.
        parentContainer: (query) - Flag to query the parent container of a specified container.
        preview: (create) - This flag is valid in create mode only. It indicates that you do not want the container to be created, instead you want to preview its contents. When this flag is used, Maya will select the nodes that would be put in the container if you did create the container. For example you can see what would go into the container with -includeNetwork, then modify your selection as desired, and do a create container with the selected objects only.
        publishAndBind: (edit) - Publish the given name and bind the attribute to the given name. First string specifies the node and attribute name in "node.attr" format. Second string specifies the name it should be published with.
        publishAsChild: (edit, query) - Publish contained node to the interface of the container to indicate it can be a child of external nodes. The second string is the name of the published node. In query mode, returns a string of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        publishAsParent: (edit, query) - Publish contained node to the interface of the container to indicate it can be a parent to external nodes. The second string is the name of the published node. In query mode, returns a string of array of the published names and the corresponding nodes. If -publishName flag is used in query mode, only returns the published names; if -bindAttr flag is used in query mode, only returns the name of the published nodes.
        publishAsRoot: (edit, query) - Publish or unpublish a node as a root. The significance of root transform node is twofold. When container-centric selection is enabled, the root transform will be selected if a container node in the hierarchy below it is selected in the main scene view. Also, when exporting a container proxy, any published root transformation attributes such as translate, rotate or scale will be hooked up to attributes on a stand-in node. In query mode, returns the node that has been published as root.
        publishAttr: (query) - In query mode, can only be used with the -publishName(-pn) flag, and takes an attribute as an argument; returns the published name of the attribute, if any.       In query mode, this flag needs a value.
        publishConnections: (create, edit) - Publish all connections from nodes inside the container to nodes outside the container.
        publishName: (edit, query) - Publish a name to the interface of the container, and returns the actual name published to the interface.  In query mode, returns the published names for the container. If the -bindAttr flag is specified, returns only the names that are bound; if the -unbindAttr flag is specified, returns only the names that are not bound; if the -publishAsParent/-publishAsChild flags are specified, returns only names of published parents/children. if the -publishAttr is specified with an attribute argument in the "node.attr" format, returns the published name for that attribute, if any.
        removeContainer: (edit) - Disconnects all the nodes from container and deletes container node.
        removeNode: (edit) - Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.
        type: (create, query) - By default, a container node will be created. Alternatively, the type flag can be used to indicate that a different type of container should be created. At the present time, the only other valid type of container node is "dagContainer".
        unbindAndUnpublish: (edit) - Unbind the given attribute (in "node.attr" format) and unpublish its associated name. Unbinding a compound may trigger unbinds of its compound parents/children. So the advantage of using this one flag is that it will automatically unpublish the names associated with these automatic unbinds.
        unbindAttr: (edit, query) - Unbind a published attribute from its published name on the interface of the container, leaving an unbound published name on the interface of the container; returns a list of unbound published names. The first string specifies the node and attribute name to be unbound in "node.attr" format, and the second string specifies the name of the bound published name. In query mode, can only be used with the -publishName, -publishAsParent and -publishAsChild flags.
        unbindChild: (edit) - Unbind the node published as child, but do not remove its published name from the interface of the container.
        unbindParent: (edit) - Unbind the node published as parent, but do not remove its published name from the interface of the container.
        unpublishChild: (edit) - Unpublish node published as child from the interface of the container
        unpublishName: (edit) - Unpublish an unbound name from the interface of the container.
        unpublishParent: (edit) - Unpublish node published as parent from the interface of the container
        unsortedOrder: (query) - This flag has no effect on the operation of the container command (OBSOLETE).
    """
    pass


def containerBind(*args, allNames: bool = bool, bindingSet: Optional[Union[str, bool]] = str, bindingSetConditions: bool = bool, bindingSetList: bool = bool, force: bool = bool, preview: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This is an accessory command to the container command which is used for some automated binding operations on the container. A container's published interface can be bound using a bindingSet on the associated container template.

    Args:
        allNames: (create) - Specifies that all published names on the container should be considered during the binding operation.  By default only unbound published names will be operated on.  Additionally specifying the 'force' option with 'all' will cause all previously bound published names to be reset (or unbound) before the binding operation is performed; in the event that there is no appropriate binding found for the published name, it will be left in the unbound state.
        bindingSet: (query) - Specifies the name of the template binding set to use for the bind or query operation. This flag is not available in query mode. 			In query mode, this flag needs a value.
        bindingSetConditions: (query) - Used in query mode, returns a list of binding set condition entries from the specified template binding set.  The list returned is composed of of all published name / condition string pairs for each entry in the binding set. This flag returns all entries in the associated binding set and does not take into account the validity of each entry with respect to the container's list of published names, bound or unbound state, etc.
        bindingSetList: (edit, query) - Used in query mode, returns a list of available binding sets that are defined on the associated container template.
        force: (create) - This flag is used to force certain operations to proceed that would normally not be performed.
        preview: (create) - This flag will provide a preview of the results of a binding operation but will not actually perform it.  A list of publishedName/boundName pairs are returned for each published name that would be affected by the binding action. If the binding of a published name will not change as a result of the action it will not be listed. Published names that were bound but will become unbound are also listed, in this case the associated boundName will be indicated by an empty string.
    """
    pass


def containerProxy(*args, fromTemplate: Optional[Union[str, bool]] = str, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Creates a new container with the same published interface, dynamic attributes and attribute values as the specified container but with fewer container members. This proxy container can be used as a reference proxy so that values can be set on container attributes without loading in the full container. The proxy container will contain one or more locator nodes. The first locator has dynamic attributes that serve as stand-ins for the original published attributes. The remaining locators serve as stand-ins for any dag nodes that have been published as parent or as child and will be placed at the world space location of the published parent/child nodes. The expected usage of container proxies is to serve as a reference proxy for a referenced container. For automated creation, export and setup of the proxy see the doExportContainerProxy.mel script which is invoked by the "Export Container Proxy" menu item.

    Args:
        fromTemplate: (create) - Specifies the name of a template file which will be used to create the new container proxy. Stand-in attributes will be created and published for all the numeric attributes on the proxy.
        type: (create) - Specifies the type of container node to use for the proxy. This flag is only valid in conjunction with the fromTemplate flag. When creating a proxy for an existing container, the type created will always be identical to that of the source container. The default value for this flag is 'container'.
    """
    pass


def containerPublish(*args, bindNode: Optional[Union[Tuple[str, str], bool]] = [str, str], bindTemplateStandins: bool = bool, inConnections: bool = bool, mergeShared: bool = bool, outConnections: bool = bool, publishNode: Optional[Union[Tuple[str, str], bool]] = [str, str], unbindNode: Optional[Union[str, bool]] = str, unpublishNode: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This is an accessory command to the container command which is used for some advanced publishing operations on the container. For example, the "publishConnections" flag on the container will publish all the connections, but this command can be used to publish just the inputs, outputs, or to collapse the shared inputs into a single attribute before publishing.

    Args:
        bindNode: (create, edit, query) - Bind the specified node to the published node name.
        bindTemplateStandins: (create, edit, query) - This flag will create a temporary stand-in attribute for any attributes that exist in the template but are not already bound. This enables you to set values for unbound attributes.
        inConnections: (create) - Specifies that the unpublished connections to nodes in the container from external nodes should be published.
        mergeShared: (create) - For use with the inConnections flag. Indicates that when an external attribute connects to multiple internal attributes within the container, a single published attribute should be used to correspond to all of the internal attributes.
        outConnections: (create) - Specifies that the unpublished connections from nodes in the container to external nodes should be published.
        publishNode: (create, edit, query) - Publish a name and type. When first published, nothing will be bound. To bind a node to the published name, use the bindNode flag.
        unbindNode: (create, edit, query) - Unbind the node that is published with the name specified by the flag.
        unpublishNode: (create, edit, query) - Unpublish the specified published node name.
    """
    pass


def containerTemplate(*args, addBindingSet: Optional[Union[str, bool]] = str, addNames: bool = bool, addView: Optional[Union[str, bool]] = str, allKeyable: bool = bool, attribute: Optional[Union[str, bool]] = str, attributeList: Optional[Union[str, bool]] = str, baseName: Optional[Union[str, bool]] = str, bindingSetList: Optional[Union[str, bool]] = str, childAnchor: bool = bool, delete: bool = bool, expandCompounds: bool = bool, fromContainer: Optional[Union[str, bool]] = str, fromSelection: bool = bool, layoutMode: Optional[Union[int, bool]] = int, matchName: Optional[Union[str, bool]] = str, parentAnchor: bool = bool, publishedNodeList: Optional[Union[str, bool]] = str, removeBindingSet: Optional[Union[str, bool]] = str, removeView: Optional[Union[str, bool]] = str, rootTransform: bool = bool, save: bool = bool, searchPath: Optional[Union[str, bool]] = str, templateList: Optional[Union[str, bool]] = str, updateBindingSet: Optional[Union[str, bool]] = str, useHierarchy: bool = bool, exists: bool = bool, fileName: Optional[Union[str, bool]] = str, force: bool = bool, load: bool = bool, matchFile: Optional[Union[str, bool]] = str, silent: bool = bool, unload: bool = bool, viewList: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    A container template is a description of a container's published interface. This command provides the ability to create and save a template file for a container or load an existing template file.  Once a template exists, the user can query the template information.

    Args:
        addBindingSet: (create, edit) - This argument is used to add a new binding set with the given name to a template. A default binding set will be created. If the binding set already exists, the force flag must be used to replace the existing binding set. When used with the fromContainer option, default bindings will be entered based on the current bindings of the designated container. When used without a reference container, the binding set will be made with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        addNames: (edit) - In edit mode, when used with the fromContainer flag, any published name on the container not present as an attribute on the template will be added to the template.
        addView: (create, edit) - This argument is used to add a new view with the given name to a template. By default a view containing a flat list of all template attributes will be created.  The layoutMode flag provides more layout options. The template must be saved before the new view is permanently stored with the template file.
        allKeyable: (create, edit) - Used when the fromSelection flag is true and fromContainer is false. If true we will use all keyable attributes to define the template or the view, if false we use the attributes passed in with the attribute flag.
        attribute: (create, edit, multiuse) - If fromSelection is true and allKeyable is false, this attribute name will be used to create an attribute item in the template file.
        attributeList: (create, edit, query) - Used in query mode, returns a list of attributes contained in the template definition.
        baseName: (create, query) - Used in query mode, returns the base name of the template. The basename is the template name with any package qualifiers stripped off.
        bindingSetList: (create, query) - Used in query mode, returns a list of all binding sets defined on the template.
        childAnchor: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only childAnchor published nodes.
        delete: (create) - Delete the specified template and its file. All objects that are associated with this template or contained in the same template file will be deleted. To simply unload a template without permanently deleting its file, use unload instead.
        expandCompounds: (create, edit) - This argument is used to determine how compound parent attributes and their children will be added to generated views when both are published to the container. When true, the compound parent and all compound child attributes published to the container will be included in the view. When false, only the parent attribute is included in the view. Note: if only the child attributes are published and not the parent, the children will be included in the view, this flag is only used in the situation where both parent and child attributes are published to the container. The default value is false.
        fromContainer: (create) - This argument is used in create or edit mode to specify a container node to be used for generating the template contents. In template creation mode, the template definition will be created based on the list of published attributes in the specified container. In edit mode, when used with the addNames flag or with no other flag, any published name on the container not present as an attribute on the template will be added to the template. This flag is also used in conjunction with flags such as addView.
        fromSelection: (create, edit) - If true, we will use the active selection list to create the template or the view. If allKeyable is also true then we will create the template from all keyable attributes in the selection, otherwise we will create the template using the attributes specified with the attribute flag.
        layoutMode: (create) - This argument is used to specify the layout mode when creating a view. Values correspond as follows: 0: layout in flat list (default when not creating view from container) 1: layout grouped by node (default if creating view from container) The fromContainer or fromSelection argument is required to provide the reference container or selection for layout modes that require node information.  Note that views can only refer to defined template attributes. This means that when using the fromContainer or from Selection flag to add a view to an existing template, only attributes that are defined on both the template and the container or the current selection will be included in the view (i.e. published attributes on the container that are not defined in the template will be ignored).
        matchName: (query) - Used in query mode in conjunction with other flags this flag specifies an optional template name that is to be matched as part of the query operation. The base template name is used for matching, any template with the same basename will be matched even across different packages. 			In query mode, this flag needs a value.
        parentAnchor: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only parentAnchor published nodes.
        publishedNodeList: (create, edit, query) - Used in query mode, returns a list of published nodes contained in the template definition. By default all published nodes on the template will be returned. The list of published nodes can be limited to only include certain types of published nodes using one of the childAnchor, parentAnchor or rootTransform flags. If an optional flag is are specified, only nodes of the specified type will be returned.
        removeBindingSet: (create, edit) - This argument is used to remove the named binding set from the template. The template must be saved before the binding set is permanently removed from the template file.
        removeView: (create, edit) - This argument is used to remove the named view from the template. The template must be saved before the view is permanently removed from the template file.
        rootTransform: (create, query) - This flag can be optionally specified when querying the publishedNodeList. The resulting list will contain only rootTransform published nodes.
        save: (create) - Save the specified template to a file. If a filename is specified for the template, the entire file (and all templates associated with it) will be saved. If no file name is specified, a default filename will be assumed, based on the template name.
        searchPath: (edit, query) - The template searchPath is an ordered list of all locations that are being searched to locate template files (first location searched to last location searched). The template search path setting is stored in the current workspace and can also be set and queried as the file rule entry for 'templates' (see the workspace command for more information). In edit mode, this flag allows the search path setting to be customized. When setting the search path value, the list should conform to a path list format expected on the current platform.  This means that paths should be separated by a semicolon (;) on Windows and a colon (:) on Linux and MacOSX. Environment variables can also be used. Additional built-in paths may be added automatically by maya to the customized settings. In query mode, this flag returns the current contents of the search path; all paths, both customized and built-in, will be included in the query return value.
        templateList: (query) - Used in query mode, returns a list of all loaded templates. This query can be used with optional matchFile and matchName flags. When used with the matchFile flag, the list of templates will be restricted to those associated with the specified file.  When used with the matchName flag, the list of templates will be restricted to those matching the specified template name.
        updateBindingSet: (create, edit) - This argument is used to update an existing binding set with new bindings. When used with the fromContainer argument binding set entries with be replaced or merged in the binding set based on the bindings of the designated container. If the force flag is used, existing entries in the binding set are replaced with new values. When force is not used, only new entries are merged into the binding set, any existing entries will be left as-is. When used without a reference container, the binding set will be updated with placeholder entries. The template must be saved before the new binding set is permanently stored with the template file.
        useHierarchy: (create, edit) - If true, and the fromSelection flag is set, the selection list will expand to include it's hierarchy also.
        exists: (query) - Returns true or false depending upon whether the specified template exists. When used with the matchFile argument, the query will return true if the template exists and the filename it was loaded from matches the filename given.
        fileName: (create, query) - Specifies the filename associated with the template.  This argument can be used in conjunction with load, save or query modes. If no filename is associated with a template, a default file name based on the template name will be used.  It is recommended but not required that the filename and template name correspond.
        force: (create) - This flag is used with some actions to allow them to proceed with an overwrite or destructive operation. When used with load, it will allow an existing template to be reloaded from a file.  When used in create mode, it will allow an existing template to be recreated (for example when using fromContainer argument to regenerate a template).
        load: () - Load an existing template from a file. If a filename is specified for the template, the entire file (and all templates in it) will be loaded. If no file is specified, a default filename will be assumed, based on the template name.
        matchFile: (query) - Used in query mode in conjunction with other flags this flag specifies an optional file name that is to be matched as part of the query operation. 			In query mode, this flag needs a value.
        silent: (create, edit, query) - Silent mode will suppress any error or warning messages that would normally be reported from the command execution.  The return values are unaffected.
        unload: (create) - Unload the specified template.  This action will not delete the associated template file if one exists, it merely removes the template definition from the current session.
        viewList: (create, query) - Used in query mode, returns a list of all views defined on the template.
    """
    pass


def containerView(*args, itemInfo: Optional[Union[str, bool]] = str, itemList: bool = bool, viewDescription: bool = bool, viewLabel: bool = bool, viewList: bool = bool, viewName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    A container view defines the layout information for the published attributes of a particular container.  Container views can be selected from a set of built-in views or may be defined on an associated container template. This command queries the view-related information for a container node. The information returned from this command will be based on the view-related settings in force on the container node at the time of the query (i.e. the container's view mode, template name, view name attributes).

    Args:
        itemInfo: (query) - Used in query mode in conjunction with the itemList flag. The command will return a list of information for each item in the view, the information fields returned for each item are determined by this argument value. The information fields will be listed in the string array returned. The order in which the keyword is specified will determine the order in which the data will be returned by the command. One or more of the following keywords, separated by colons ':' are used to specify the argument value.  itemIndex  : sequential item number (0-based) itemName   : item name (string) itemLabel  : item display label (string) itemDescription : item description field (string) itemLevel  : item hierarchy level (0-n) itemIsGroup : (boolean 0 or 1) indicates whether or not this item is a group itemIsAttribute : (boolean 0 or 1) indicates whether or not this item is an attribute itemNumChildren: number of immediate children (groups or attributes) of this item itemAttrType : item attribute type (string) itemCallback : item callback field (string)  In query mode, this flag needs a value.
        itemList: (query) - Used in query mode, the command will return a list of information for each item in the view.  The viewName flag is used to select the view to query. The information returned about each item is determined by the itemInfo argument value. For efficiency, it is best to query all necessary item information at one time (to avoid recomputing the view information on each call).
        viewDescription: (query) - Used in query mode, returns the description field associated with the selected view. If no description was defined for this view, the value will be empty.
        viewLabel: (query) - Used in query mode, returns the display label associated with the view. An appropriate label suitable for the user interface will be returned based on the selected view.  Use of the view label is usually more suitable than the view name for display purposes.
        viewList: (query) - Used in query mode, command will return a list of all views defined for the given target (container or template).
        viewName: (query) - Used in query mode, specifies the name of the queried view when used in conjunction with a template target. When used in conjunction with a container target, it requires no string argument, and returns the name of the currently active view associated with the container; this value may be empty if the current view is not a valid template view or is generated by one of the built-in views modes. For this reason, the view label is generally more suitable for display purposes. 			In query mode, this flag can accept a value.
    """
    pass


def contextInfo(*args, c: bool = bool, escapeContext: bool = bool, exists: bool = bool, image1: bool = bool, image2: bool = bool, image3: bool = bool, title: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command allows you to get information on named contexts.

    Args:
        c: (create) - Return the class type of the named context.
        escapeContext: (create) - Return the command string that will allow you to exit the current tool.
        exists: (create) - Return true if the context exists, false if it does not exists (or is internal and therefore untouchable)
        image1: (create) - Returns the name of an xpm associated with the named context.
        image2: (create) - Returns the name of an xpm associated with the named context.
        image3: (create) - Returns the name of an xpm associated with the named context.
        title: (create) - Return the title string of the named context.
    """
    pass


def copyAttr(*args, attribute: Optional[Union[str, bool]] = str, containerParentChild: bool = bool, inConnections: bool = bool, keepSourceConnections: bool = bool, outConnections: bool = bool, renameTargetContainer: bool = bool, values: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Given two nodes, transfer the connections and/or the values from the first node to the second for all attributes whose names and data types match. When values are transferred, they are transferred directly. They are not mapped or modified in any way. The transferAttributes command can be used to transfer and remap some mesh attributes. The attributes flag can be used to specify a list of attributes to be processed. If the attributes flag is unused, all attributes will be processed. For dynamic attributes, the values and/or connections will only be transferred if the attributes names on both nodes match. This command does not support geometry shape nodes such as meshes, subds and nurbs. This command does not support transfer of multi-attribute values such as weight arrays.

    Args:
        attribute: (create, multiuse) - The name of the attribute(s) for which connections and/or values will be transferred. If no attributes are specified, then all attributes will be transferred.
        containerParentChild: (create) - For use when copying from one container to another only. This option indicates that the published parent and/or child relationships on the original container should be transferred to the target container if the published names match.
        inConnections: (create) - Indicates that incoming connections should be transferred.
        keepSourceConnections: (create) - For use with the outConnections flag only. Indicates that the connections should be maintained on the first node, in addition to making them to the second node. If outConnections is used and keepSourceConnections is not used, the out connections on the source node will be broken and made to the target node.
        outConnections: (create) - Indicates that outgoing connections should be transferred.
        renameTargetContainer: (create) - For use when copying from one container to another only. This option will rename the target container to the name of the original container, and rename the original container to its old name + "Orig". You would want to use this option if your original container was referenced and edited, and you want those edits from the main scene to now apply to the new container.
        values: (create) - Indicates that values should be transferred.
    """
    pass


def createAttrPatterns(*args, patternDefinition: Optional[Union[str, bool]] = str, patternFile: Optional[Union[str, bool]] = str, patternType: Optional[Union[str, bool]] = str):
    """
    Create a new instance of an attribute pattern given a pattern type (e.g. XML) and a string or data file containing the description of the attribute tree in the pattern's format.

    Args:
        patternDefinition: (create) - Hardcoded string containing the pattern definition, for simpler formats that don't really need a separate file for definition.
        patternFile: (create) - File where the pattern information can be found
        patternType: (create) - Name of the pattern definition type to use in creating this instance of the pattern.
    """
    pass


def createDisplayLayer(*args, empty: bool = bool, makeCurrent: bool = bool, name: Optional[Union[str, bool]] = str, noRecurse: bool = bool, number: Optional[Union[int, bool]] = int):
    """
    Create a new display layer.  The display layer number will be assigned based on the first unassigned number not less than the base index number found in the display layer global parameters.  Normally all objects and their descendants will be added to the new display layer but if the '-nr' flag is specified then only the objects themselves will be added.

    Args:
        empty: (create) - If set then create an empty display layer.  ie. Do not add the selected items to the new display layer.
        makeCurrent: (create) - If set then make the new display layer the current one.
        name: (create) - Name of the new display layer being created.
        noRecurse: (create) - If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        number: (create) - Number for the new display layer being created.
    """
    pass


def createNode(*args, name: Optional[Union[str, bool]] = str, parent: Optional[Union[str, bool]] = str, shared: bool = bool, skipSelect: bool = bool):
    """
    This command creates a new node in the dependency graph of the specified type.

    Args:
        name: (create) - Sets the name of the newly-created node. If it contains namespace path, the new node will be created under the specified namespace; if the namespace doesn't exist, we will create the namespace.
        parent: (create) - Specifies the parent in the DAG under which the new node belongs.
        shared: (create) - This node is shared across multiple files, so only create it if it does not already exist.
        skipSelect: (create) - This node is not to be selected after creation, the original selection will be preserved.
    """
    pass


def ctxAbort(*args):
    """
    This command tells the current context to reset itself, losing what has been done so far.  If a escape context has been set it then makes that context current.

    Args:
    """
    pass


def ctxCompletion(*args):
    """
    This command tells the current context to finish what it is doing and create any objects that is is working on.

    Args:
    """
    pass


def ctxEditMode(*args, buttonDown: bool = bool, buttonUp: bool = bool):
    """
    This command tells the current context to switch edit modes.

    Args:
        buttonDown: (create) - Edit mode is being invoked from a hotkey press event.
        buttonUp: (create) - Edit mode is being invoked from a hotkey release event.
    """
    pass


def ctxTraverse(*args, down: bool = bool, left: bool = bool, right: bool = bool, up: bool = bool):
    """
    This command tells the current context to do a traversal.

    Args:
        down: (create) - Move "down" as defined by the current context.
        left: (create) - Move "left" as defined by the current context.
        right: (create) - Move "right" as defined by the current context.
        up: (create) - Move "up" as defined by the current context.
    """
    pass


def currentCtx(*args):
    """
    This command returns the currently selected tool context.

    Args:
    """
    pass


def currentTimeCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to change current time within the graph editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def currentUnit(*args, angle: Optional[Union[str, bool]] = str, fullName: bool = bool, linear: Optional[Union[str, bool]] = str, time: Optional[Union[str, bool]] = str, updateAnimation: bool = bool, query: bool = bool):
    """
    This command allows you to change the units in which you will work in Maya. There are three types of units: linear, angular and time.

    Args:
        angle: (create, query) - Set the current angular unit. Valid strings are:  [deg | degree | rad | radian]  When queried, returns a string which is the current angular unit
        fullName: (query) - A query only flag. When specified in conjunction with any of the -linear/-angle/-time flags, will return the long form of the unit. For example, mm and millimeter are the same unit, but the former is the short form of the unit name, and the latter is the long form of the unit name.
        linear: (create, query) - Set the current linear unit. Valid strings are:  [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]  When queried, returns a string which is the current linear unit
        time: (create, query) - Set the current time unit. Valid strings are:  [hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]  When queried, returns a string which is the current time unit  Note that there is no long form for any of the time units. The non-seconds based time units are interpreted as the following frames per second:  game: 15 fps film: 24 fps pal: 25 fps ntsc: 30 fps show: 48 fps palf: 50 fps ntscf: 60 fps
        updateAnimation: (create) - An edit only flag.  When specified in conjunction with the -time flag indicates that times for keys are not updated.  By default when the current time unit is changed, the times for keys are modified so that playback timing is preserved.  For example a key set a frame 12film is changed to frame 15ntsc when the current time unit is changed to ntsc, since they both represent a key at a time of 0.5 seconds.  Specifying -updateAnimation false would leave the key at frame 12ntsc. Default is -updateAnimation true.
    """
    pass


def curveAddPtCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The curveAddPtCtx command creates a new curve add points context, which adds either control vertices (CVs) or edit points to an existing curve.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def curveCVCtx(*args, bezier: bool = bool, degree: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, multEndKnots: bool = bool, name: Optional[Union[str, bool]] = str, preserveShape: bool = bool, rational: bool = bool, refit: bool = bool, symmetry: bool = bool, uniform: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The curveCVCtx command creates a new context for creating curves by placing control vertices (CVs).

    Args:
        bezier: (create, edit, query) - 
        degree: (create, edit, query) - Curve degree
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        multEndKnots: (create, edit, query) - Specify if multiple end knots are to be created.
        name: (create) - If this is a tool command, name the tool appropriately.
        preserveShape: (create, edit, query) - Set this flag to make the operation preserve the shape
        rational: (create, edit, query) - Should the curve be rational?
        refit: (create, edit, query) - Set this flag to refit the curve
        symmetry: (create, edit, query) - Specify if symmetry is to be used
        uniform: (create, edit, query) - Should the curve use uniform parameterization?
    """
    pass


def curveEditorCtx(*args, direction: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, relativeTangentSize: Optional[Union[float, bool]] = float, title: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The curveEditorCtx command creates a new NURBS editor context, which is used to edit a NURBS curve or surface.

    Args:
        direction: (query) - Query the current direction of the tangent control.  Always zero for the curve case.  In the surface case, its 0 for the normal direction, 1 for U direction and 2 for V direction.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        relativeTangentSize: (create, edit, query) - Relative size of the tangent manipulator handle.  Helps to adjust as the surface parameterization controls the size of the tangent, even if the shape of the surface remains the same. The default is 4.
        title: (edit, query) - The title for the tool.
    """
    pass


def curveEPCtx(*args, bezier: bool = bool, degree: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, preserveShape: bool = bool, preserveShapeFraction: Optional[Union[float, bool]] = float, refit: bool = bool, uniform: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The curveEPCtx command creates a new context for creating curves by placing edit points.

    Args:
        bezier: (create, edit, query) - Use bezier curves
        degree: (create, edit, query) - Curve degree
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        preserveShape: (create, edit, query) - Set this flag to make the operation preserve the shape
        preserveShapeFraction: (create, edit, query) - Fraction value used when preserving the shape
        refit: (create, edit, query) - Set this flag to refit the curve
        uniform: (create, edit, query) - Should the curve use uniform parameterization?
    """
    pass


def curveMoveEPCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The curveMoveEPCtx command creates a new context for moving curve edit points using a manipulator.  Edit points can only be moved one at a time.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def curveSketchCtx(*args, degree: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The curveSketchCtx command creates a new curve sketch context, also known as the "pencil context".

    Args:
        degree: (create, edit, query) - Valid values are 1 or 3
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def cycleCheck(*args, all: bool = bool, children: bool = bool, dag: bool = bool, evaluation: bool = bool, firstCycleOnly: bool = bool, firstPlugPerNode: bool = bool, lastPlugPerNode: bool = bool, list: bool = bool, listSeparator: Optional[Union[str, bool]] = str, parents: bool = bool, secondary: bool = bool, timeLimit: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], query: bool = bool):
    """
    This command searches for plug cycles in the dependency graph. If a plug or node is selected then it searches for cycles that that plug or node is involved with. Plugs or nodes can also be passed as arguments. If the -all flag is used then the entire graph is searched.

    Args:
        all: (create) - search the entire graph for cycles instead of the selection list. (Note: if nothing is selected, -all is assumed).
        children: (create) - Do not consider cycles on the children, only the specified plugs
        dag: (create) - Also look for cycles due to relationships in the DAG. For each DAG node, the parenting connection on its children is also considered when searching for cycles.
        evaluation: (create, query) - Turn on and off cycle detection during graph evaluation
        firstCycleOnly: (create) - When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. When -firstCycleOnly is specified only the first such cycle (which will be a full cycle) is returned.
        firstPlugPerNode: (create) - When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -firstPlugPerNode is specified, only the first plug in the list for each node is returned (B.input in the example).
        lastPlugPerNode: (create) - When -list is used to return a plug list, the list will typically contain multiple plugs per node (e.g. ... A.output B.input B.output C.input ...), reflecting internal "affects" relationships rather than external DG connections. When -lastPlugPerNode is specified, only the last plug in the list for each node is returned (B.output in the example).
        list: (create) - Return all plugs involved in one or more cycles.  If not specified, returns a boolean indicating whether a cycle exists.
        listSeparator: (create) - When -list is used to return a plug list, the list may contain multiple cycles or partial cycles. Use -listSeparator to specify a string that will be inserted into the returned string array to separate the cycles.
        parents: (create) - Do not consider cycles on the parents, only the specified plugs
        secondary: (create) - Look for cycles on related plugs as well as the specified plugs Default is "on" for the "-all" case and "off" for others
        timeLimit: (create) - Limit the search to the given amount of time
    """
    pass


def delete(*args, all: bool = bool, attribute: Optional[Union[str, bool]] = str, channels: bool = bool, constraints: bool = bool, constructionHistory: bool = bool, controlPoints: bool = bool, expressions: bool = bool, hierarchy: Optional[Union[str, bool]] = str, inputConnectionsAndNodes: bool = bool, motionPaths: bool = bool, shape: bool = bool, staticChannels: bool = bool, timeAnimationCurves: bool = bool, unitlessAnimationCurves: bool = bool):
    """
    This command is used to delete selected objects, or all objects, or objects specified along with the command. Flags are available to filter the type of objects that the command acts on.

    Args:
        all: (create) - Remove all objects of specified kind, in the scene. This flag is to be used in conjunction with the following flags.
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        channels: (create) - Remove animation channels in the scene. Either all channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        constraints: (create) - Remove selected constraints and constraints attached to the selected nodes, or remove all constraints in the scene.
        constructionHistory: (create) - Remove the construction history on the objects specified or selected.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        expressions: (create) - Remove expressions in the scene. Either all expressions can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inputConnectionsAndNodes: (create) - Break input connection to specified attribute and delete all unconnected nodes that are left behind. The graph will be traversed until a node that cannot be deleted is encountered.
        motionPaths: (create) - Remove motion paths in the scene. Either all motion paths can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        staticChannels: (create) - Remove static animation channels in the scene. Either all static channels can be removed, or the scope can be narrowed down by specifying some of the above mentioned options.
        timeAnimationCurves: (create) - Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to time-input animation curves (for instance, those created by 'setKeyframe' will be deleted.  When false, no time-input animation curves will be deleted. Default: true.
        unitlessAnimationCurves: (create) - Modifies the -c/channels and -sc/staticChannels flags. When true, only channels connected to unitless-input animation curves (for instance, those created by 'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation curves will be deleted.  Default: true.
    """
    pass


def deleteAttr(*args, attribute: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command is used to delete a dynamic attribute from a node or nodes. The attribute can be specified by using either the long or short name. Only one dynamic attribute can be deleted at a time. Static attributes cannot be deleted. Children of a compound attribute cannot be deleted. You must delete the complete compound attribute. This command has no edit capabilities. The only query ability is to list all the dynamic attributes of a node.

    Args:
        attribute: (create) - Specify either the long or short name of the attribute.
    """
    pass


def deleteAttrPattern(*args, allPatterns: bool = bool, patternName: Optional[Union[str, bool]] = str, patternType: Optional[Union[str, bool]] = str):
    """
    After a while the list of attribute patterns could become cluttered. This command provides a way to remove patterns from memory so that only the ones of interest will show.

    Args:
        allPatterns: (create) - If specified it means delete all known attribute patterns.
        patternName: (create) - The name of the pattern to be deleted.
        patternType: (create) - Delete all patterns of the given type.
    """
    pass


def deleteExtension(*args, attribute: Optional[Union[str, bool]] = str, forceDelete: bool = bool, nodeType: Optional[Union[str, bool]] = str):
    """
    This command is used to delete an extension attribute from a node type. The attribute can be specified by using either the long or short name. Only one extension attribute can be deleted at a time. Children of a compound attribute cannot be deleted, you must delete the complete compound attribute. This command has no undo, edit, or query capabilities.

    Args:
        attribute: (create) - Specify either the long or short name of the attribute.
        forceDelete: (create) - If this flag is set and turned ON then data values for the extension attributes are all deleted without confirmation. If it's set and turned OFF then any extension attributes that have non-default values set on any node will remain in place. If this flag is not set at all then the user will be asked if they wish to preserve non-default values on this attribute.
        nodeType: (create) - The name of the node type.
    """
    pass


def directKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, option: Optional[Union[str, bool]] = str, selectedOnly: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to directly manipulate keyframes within the graph editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        option: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
        selectedOnly: (create, edit, query) - Controls whether only selected curves/keys can be moved, or all.
    """
    pass


def disconnectAttr(*args, nextAvailable: bool = bool):
    """
    Disconnects two connected attributes. First argument is the source attribute, second is the destination.

    Args:
        nextAvailable: (create) - If the destination multi-attribute has set the indexMatters to be false, the command will disconnect the first matching connection.  No index needs to be specified.
    """
    pass


def displayAffected(*args, query: bool = bool):
    """
    Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list.

    Args:
    """
    pass


def displayColor(*args, active: bool = bool, create: bool = bool, dormant: bool = bool, list: bool = bool, queryIndex: Optional[Union[int, bool]] = int, resetToFactory: bool = bool, resetToSaved: bool = bool, query: bool = bool):
    """
    This command changes or queries the display color for anything in the application that allows the user to set its color. The color is defined by a color index into either the dormant or active color palette. These colors are part of the UI and not part of the saved data for a model.  This command is not undoable.

    Args:
        active: (create) - Specifies the color index applies to active color palette. name Specifies the name of color to change. index The color index for the color.
        create: (create) - Creates a new display color which can be queried or set. If is used only when saving color preferences.
        dormant: (create) - Specifies the color index applies to dormant color palette. If neither of the dormant or active flags is specified, dormant is the default.
        list: (create) - Writes out a list of all color names and their value.
        queryIndex: (create) - Allows you to obtain a list of color names with the given color indices.
        resetToFactory: (create) - Resets all display colors to their factory defaults.
        resetToSaved: (create) - Resets all display colors to their saved values.
    """
    pass


def displayCull(*args, backFaceCulling: bool = bool, query: bool = bool):
    """
    This command is responsible for setting the display culling property of back faces of surfaces.

    Args:
        backFaceCulling: (create, query) - Enable/disable culling of back faces.
    """
    pass


def displayLevelOfDetail(*args, levelOfDetail: bool = bool, query: bool = bool):
    """
    This command is responsible for setting the display level-of-detail for edit refreshes.  If enabled, objects will draw with lower detail based on their distance from the camera. When disabled objects will display at full resolution at all times.  This is not an undoable command

    Args:
        levelOfDetail: () - Enable/disable level of detail.
    """
    pass


def displayPref(*args, activeObjectPivots: bool = bool, displayAffected: bool = bool, displayGradient: bool = bool, ghostFrames: Optional[Union[Tuple[int, int, int], bool]] = [int, int, int], materialLoadingMode: Optional[Union[str, bool]] = str, maxHardwareTextureResolution: bool = bool, maxTextureResolution: Optional[Union[int, bool]] = int, purgeExistingTextures: bool = bool, regionOfEffect: bool = bool, shadeTemplates: bool = bool, textureDrawPixel: bool = bool, wireframeOnShadedActive: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    This command sets/queries the state of global display parameters.

    Args:
        activeObjectPivots: (create, query) - Sets the display state for drawing pivots for active objects.
        displayAffected: (create, query) - Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list. If one of the curves in a loft were selected and this feature were turned on, then the lofted surface would be highlighted because it is affected by the loft curve.
        displayGradient: (create, query) - Set whether to display the background using a colored gradient as opposed to a constant background color.
        ghostFrames: (create, query) - Obsolete - use the "ghosting" command to set these values.
        materialLoadingMode: (create, query) - Sets the material loading mode when loading the scene.  Possible values for the string argument are "immediate", "deferred" and "parallel".
        maxHardwareTextureResolution: (query) - Query the maximum allowable hardware texture resolution available on the current video card. This maximum can vary between different video cards and different operating systems.
        maxTextureResolution: (create, query) - Sets the maximum hardware texture resolution to be used when creating hardware textures for display. The maximum will be clamped to the maximum allowable texture determined for the hardware at the time this command is invoked. Use the -maxHardwareTextureResolution to retrieve this maximum value. Existing hardware textures are not affected. Only newly created textures will be clamped to this maximum.
        purgeExistingTextures: (create) - Purge any existing hardware textures. This will force a re-evaluation of hardware textures used for display, and thus may take some time to evaluate.
        regionOfEffect: (create, query) - Turns on/off the display of the region of curves/surfaces that is affected by changes to selected CVs and edit points.
        shadeTemplates: (create, query) - Turns on/off the display of templated surfaces as shaded in shaded display mode. If its off, templated surfaces appear in wireframe.
        textureDrawPixel: (create, query) - Sets the display mode for drawing image planes. True for use of gltexture calls for perspective views. This flag should not normally be needed. Image Planes may display faster on Windows but can result in some display artifacts.
        wireframeOnShadedActive: (create, query) - Sets the display state for drawing the wireframe on active shaded objects.  Possible values for the string argument are "full", "reduced" and "none".
    """
    pass


def displayRGBColor(*args, alpha: bool = bool, create: bool = bool, hueSaturationValue: bool = bool, list: bool = bool, resetToFactory: bool = bool, resetToSaved: bool = bool, query: bool = bool):
    """
    This command changes or queries the display color for anything in the application that allows the user to set its color. These colors are part of the UI and not part of the saved data for a model.  This command is not undoable.

    Args:
        alpha: (query) - Indicates that we want to query the alpha value of the color. Upon query, returns RGBA or HSVA as an array of 4 floats.
        create: (create) - Creates a new RGB display color which can be queried or set. If is used only when saving color preferences. name Specifies the name of color to change.
        hueSaturationValue: (create, query) - Indicates that rgb values are really hsv values. Upon query, returns the HSV values as an array of 3 floats. h s v The HSV values for the color.  (Between 0-1)
        list: (create) - Writes out a list of all RGB color names and their value.
        resetToFactory: (create) - Resets all the RGB display colors to their factory defaults.
        resetToSaved: (create) - Resets all the RGB display colors to their saved values.
    """
    pass


def displaySmoothness(*args, all: bool = bool, boundary: bool = bool, defaultCreation: bool = bool, divisionsU: Optional[Union[int, bool]] = int, divisionsV: Optional[Union[int, bool]] = int, full: bool = bool, hull: bool = bool, pointsShaded: Optional[Union[int, bool]] = int, pointsWire: Optional[Union[int, bool]] = int, polygonObject: Optional[Union[int, bool]] = int, renderTessellation: bool = bool, simplifyU: Optional[Union[int, bool]] = int, simplifyV: Optional[Union[int, bool]] = int, query: bool = bool):
    """
    This command is responsible for setting the display smoothness of NURBS curves and surfaces to either predefined or custom values. It also sets display modes for smoothness such as hulls and the hull simplification factors. At present, this command is NOT un-doable.

    Args:
        all: (create, query) - Change smoothness for all curves and surfaces
        boundary: (create, query) - Display wireframe surfaces using only the boundaries of the surface Not fully implemented yet
        defaultCreation: (create, query) - The default values at creation (applies only -du, -dv, -pw, -ps)
        divisionsU: (create, query) - Number of isoparm divisions per span in the U direction. The valid range of values is [0,64].
        divisionsV: (create, query) - Number of isoparm divisions per span in the V direction. The valid range of values is [0,64].
        full: (create, query) - Display surface at full resolution - the default.
        hull: (create, query) - Display surface using the hull (control points are drawn rather than surface knot points). This mode is a useful display performance improvement when modifying a surface since it doesn't require evaluating points on the surface.
        pointsShaded: (create, query) - Number of points per surface span in shaded mode. The valid range of values is [1,64].
        pointsWire: (create, query) - Number of points per surface isoparm span or the number of points per curve span in wireframe mode. The valid range of values is [1,128]. Note: This is the only flag that also applies to nurbs curves.
        polygonObject: (create, query) - Display the polygon objects with the given resolution
        renderTessellation: (create, query) - Display using render tesselation parameters when in shaded mode.
        simplifyU: (create, query) - Number of spans to skip in the U direction when in hull display mode.
        simplifyV: (create, query) - Number of spans to skip in the V direction when in hull display mode.
    """
    pass


def displaySurface(*args, flipNormals: bool = bool, twoSidedLighting: bool = bool, xRay: bool = bool, query: bool = bool):
    """
    This command toggles display options on the specified or active surfaces. Typically this command applies to NURBS or poly mesh surfaces and ignores other type of objects.

    Args:
        flipNormals: (query) - flip normal direction on the surface
        twoSidedLighting: (query) - toggle if the surface should be considered two-sided.  If it's single-sided, drawing and rendering may use single sided lighting and back face cull to improve performance.
        xRay: (query) - toggle X ray mode (make surface transparent)
    """
    pass


def distanceDimContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command used to register the distanceDimCtx tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def distanceDimension(*args, endPoint: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], startPoint: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float]):
    """
    This command is used to create a distance dimension to display the distance between two specified points.

    Args:
        endPoint: (create) - Specifies the point to measure distance to, from the startPoint.
        startPoint: (create) - Specifies the point to start measuring distance from.
    """
    pass


def dollyCtx(*args, alternateContext: bool = bool, boxDollyType: Optional[Union[str, bool]] = str, centerOfInterestDolly: bool = bool, dollyTowardsCenter: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, localDolly: bool = bool, name: Optional[Union[str, bool]] = str, orthoZoom: bool = bool, scale: Optional[Union[float, bool]] = float, toolName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a dolly context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxDollyType: (create, edit, query) - Set the behavior of where the camera's center of interest is set to after the box dolly. In surface mode, the center of interest will be snapped to the surface point at the center of the marquee. In bbox mode, the closest bounding box to the camera will be used. Bounding box mode will use the selection mask to determine which objects to include into the calculation.
        centerOfInterestDolly: (create, edit, query) - Set the translate the camera's center of interest. Left and right drag movements with the mouse will translate the center of interest towards or away respectively from the camera. The center of interest can be snapped to objects by using the left mouse button for selection. The default select mask will be used.
        dollyTowardsCenter: (create, edit, query) - Dolly towards center (if true), else dolly towards point where user clicks in the view.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localDolly: (create, edit, query) - Dolly with respect to the camera's center of interest. The camera will not pass through the center of interest. Local dolly only applies to perspective cameras.
        name: (create) - If this is a tool command, name the tool appropriately.
        orthoZoom: (create, edit, query) - Zoom orthographic view (if true), else dolly orthographic camera. Default value is true.
        scale: (create, edit, query) - The sensitivity for dollying the camera.
        toolName: (create, query) - Name of the specific tool to which this command refers.
    """
    pass


def dragAttrContext(*args, connectTo: Optional[Union[str, bool]] = str, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, reset: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The dragAttrContext allows a user to manipulate the attributes of an object by using a virtual slider within the viewport.  The virtual slider is used by dragging in a viewport with the middle mouse button.  The speed at which the attributes are changed can be controlled by holding down the Ctrl key to slow it down and the Shift key to speed it up.

    Args:
        connectTo: (create, edit, multiuse, query) - Specifies an attribute to which to connect the context. This is a multi-use flag, but all attributes used must be from one object.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        reset: (create, edit) - Resets the list of attributes to which the context is connected.
    """
    pass


def draggerContext(*args, anchorPoint: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), button: Optional[Union[int, bool]] = int, currentStep: Optional[Union[int, bool]] = int, cursor: Optional[Union[str, bool]] = str, dragCommand: Optional[Union[str, bool]] = str, dragPoint: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), drawString: Optional[Union[str, bool]] = str, exists: bool = bool, finalize: Optional[Union[str, bool]] = str, helpString: Optional[Union[str, bool]] = str, history: bool = bool, holdCommand: Optional[Union[str, bool]] = str, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, initialize: Optional[Union[str, bool]] = str, modifier: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, plane: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), prePressCommand: Optional[Union[str, bool]] = str, pressCommand: Optional[Union[str, bool]] = str, projection: Optional[Union[str, bool]] = str, releaseCommand: Optional[Union[str, bool]] = str, snapping: bool = bool, space: Optional[Union[str, bool]] = str, stepsCount: Optional[Union[int, bool]] = int, undoMode: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The draggerContext allows the user to program the behavior of the mouse or an equivalent dragging device in MEL.

    Args:
        anchorPoint: (query) - Anchor point (double array) where dragger was initially pressed.
        button: (query) - Returns the current mouse button (1,2,3).
        currentStep: (query) - Current step (press-drag-release sequence) for dragger context. When queried before first press event happened, returns 0.
        cursor: (create, edit, query) - Cursor displayed while context is active.  Valid values are: "default", "hand", "crossHair", "dolly", "track", and "tumble".
        dragCommand: (create, edit, query) - Command called when mouse dragger is dragged.
        dragPoint: (query) - Drag point (double array) current position of dragger during drag.
        drawString: (create, edit) - A string to be drawn at the current position of the pointer.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        finalize: (create, edit, query) - Command called when the tool is exited.
        helpString: (query) - Help string for context
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        holdCommand: (create, edit, query) - Command called when mouse dragger is held.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        initialize: (create, edit, query) - Command called when the tool is entered.
        modifier: (query) - Returns the current modifier type:  ctrl, alt or none.
        name: (create) - If this is a tool command, name the tool appropriately.
        plane: (create, edit) - Provide normal of projection plane (see -projection flag for details).
        prePressCommand: (create, edit, query) - Command called when mouse dragger is pressed. It is called before pressCommand, so it can be used for initialization of context.
        pressCommand: (create, edit, query) - Command called when mouse dragger is pressed.
        projection: (create, edit, query) - Sets current projection of drag point. Valid types are:   viewPlane project to view plane   objectViewPlane project to object plane (parallel to view plane)   objectPlane project to specified plane defined by object location and normal (default) 0,1,0   plane project to specified plane defined by origin and normal (default) 0,1,0   sketchPlane project to sketch plane   xAxis project to closest point on X axis   yAxis project to closest point on Y axis   zAxis project to closest point on Z axis   boundingSphere project to closest point on object sphere bounds   boundingBox project to closest point on object bounding box
        releaseCommand: (create, edit, query) - Command called when mouse dragger is released.
        snapping: (create, edit, query) - Enable/disable snapping for dragger context.
        space: (create, edit, query) - Sets current space that coordinates are reported in. Types are:   world world space (global)   object object space (local)   screen screen space
        stepsCount: (create, edit, query) - Number of steps (press-drag-release sequences) for dragger context. When combined with undoMode flag, several steps might be recorded as single undo action.
        undoMode: (create, edit, query) - Undo queue mode for the context actions. Acceptable values are:  "all" default behaviour when every action that happens during dragger context activity is recorded as an individual undo chunk. "step" - all the actions that happen between each press and release are combined into one undo chunk. "sequence" - all the actions that happen between very first press and very last release are combined into single undo chunk. This works exactly the same as "step" for a single step dragger context.
    """
    pass


def duplicate(*args, fullPath: bool = bool, inputConnections: bool = bool, instanceLeaf: bool = bool, name: Optional[Union[str, bool]] = str, parentOnly: bool = bool, renameChildren: bool = bool, returnRootsOnly: bool = bool, smartTransform: bool = bool, transformsOnly: bool = bool, upstreamNodes: bool = bool):
    """
    This command duplicates the given objects. If no objects are given, then the selected list is duplicated.

    Args:
        fullPath: (create) - ADDED 2023 Return full pathnames instead of object names.
        inputConnections: (create) - Input connections to the node to be duplicated, are also duplicated. This would result in a fan-out scenario as the nodes at the input side are not duplicated (unlike the -un option).
        instanceLeaf: (create) - instead of duplicating leaf DAG nodes, instance them.
        name: (create) - name to give duplicated object(s)
        parentOnly: (create) - Duplicate only the specified DAG node and not any of its children.
        renameChildren: (create) - rename the child nodes of the hierarchy, to make them unique.
        returnRootsOnly: (create) - return only the root nodes of the new hierarchy. When used with upstreamNodes flag, the upstream nodes will be omitted in the result.  This flag controls only what is returned in the output string[], and it does NOT change the behaviour of the duplicate command.
        smartTransform: (create) - remembers last transformation and applies it to duplicated object(s)
        transformsOnly: (create) - Duplicate only transform nodes and not any shapes.
        upstreamNodes: (create) - the upstream nodes leading upto the selected nodes (along with their connections) are also duplicated.
    """
    pass


def dynParticleCtx(*args, conserve: Optional[Union[float, bool]] = float, cursorPlacement: bool = bool, exists: bool = bool, grid: bool = bool, gridSpacing: Optional[Union[float, bool]] = float, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, jitterRadius: Optional[Union[float, bool]] = float, lowerLeftX: Optional[Union[float, bool]] = float, lowerLeftY: Optional[Union[float, bool]] = float, lowerLeftZ: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, nucleus: bool = bool, numJitters: Optional[Union[int, bool]] = int, particleName: Optional[Union[str, bool]] = str, sketch: bool = bool, sketchInterval: Optional[Union[int, bool]] = int, textPlacement: bool = bool, upperRightX: Optional[Union[float, bool]] = float, upperRightY: Optional[Union[float, bool]] = float, upperZ: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    The particle context command creates a particle context. The particle context provides an interactive means to create particle objects. The particle context command also provides an interactive means to set the option values, through the Tool Property Sheet, for the "particle" command that the context will issue.

    Args:
        conserve: (edit, query) - Conservation of momentum control (between 0 and 1). For smaller values, the field will tend to erase any existing velocity the object has (in other words, will not conserve momentum from frame to frame). A value of 1 (the default) corresponds to the true physical law of conservation of momentum.
        cursorPlacement: (edit, query) - Use the cursor to place the lower left and upper right of the grid.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        grid: (edit, query) - Create a particle grid.
        gridSpacing: (edit, query) - Spacing between particles in the grid.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        jitterRadius: (edit, query) - Max radius from the center to place the particle instances.
        lowerLeftX: (edit, query) - Lower left X position of the particle grid.
        lowerLeftY: (edit, query) - Lower left Y position of the particle grid.
        lowerLeftZ: (edit, query) - Lower left Z position of the particle grid.
        name: (create) - If this is a tool command, name the tool appropriately.
        nucleus: (edit, query) - If set true then an nParticle is generated with a nucleus node connection. Otherwise a standard particle is created.
        numJitters: (edit, query) - Number of jitters (instances) per particle.
        particleName: (edit, query) - Particle name.
        sketch: (edit, query) - Create particles in sketch mode.
        sketchInterval: (edit, query) - Interval between particles, when in sketch mode.
        textPlacement: (edit, query) - Use the textfields to specify the lower left and upper right of/ the grid.
        upperRightX: (edit, query) - Upper right X position of the particle grid.
        upperRightY: (edit, query) - Upper right Y position of the particle grid.
        upperZ: (edit, query) - Upper right Z position of the particle grid.
    """
    pass


def editDisplayLayerGlobals(*args, baseId: Optional[Union[int, bool]] = int, currentDisplayLayer: Optional[Union[str, bool]] = str, mergeType: Optional[Union[int, bool]] = int, useCurrent: bool = bool, query: bool = bool):
    """
    Edit the parameter values common to all display layers.  Some of these paremeters, eg. baseId and mergeType, are stored as preferences and some, eg. currentDisplayLayer, are stored in the file.

    Args:
        baseId: (create, query) - Set base layer ID.  This is the number at which new layers start searching for a unique ID.
        currentDisplayLayer: (create, query) - Set current display layer; ie. the one that all new objects are added to.
        mergeType: (create, query) - Set file import merge type.  Valid values are 0, none, 1, by number, and 2, by name.
        useCurrent: (create, query) - Set whether or not to enable usage of the current display layer as the destination for all new nodes.
    """
    pass


def editDisplayLayerMembers(*args, clear: bool = bool, fullNames: bool = bool, noRecurse: bool = bool, ufeObjects: bool = bool, query: bool = bool):
    """
    This command is used to query and edit membership of display layers.  No equivalent 'remove' command is necessary since all objects must be in exactly one display layer.  Removing an object from a layer can be accomplished by adding it to a different layer.

    Args:
        clear: (create) - Remove all the objects contained in the layer by moving them to the default layer.
        fullNames: (query) - (Query only.) If set then return the full DAG paths of the objects in the layer.  Otherwise return just the name of the object.
        noRecurse: (create, query) - If set then only add selected objects to the display layer.  Otherwise all descendants of the selected objects will also be added.
        ufeObjects: (query) - (Query only.) If set will return objects that are defined through the UFE interface as well as native Maya objects.
    """
    pass


def exactWorldBoundingBox(*args, calculateExactly: bool = bool, ignoreInvisible: bool = bool):
    """
    This command figures out an exact-fit bounding box for the specified objects (or selected objects if none are specified) This bounding box is always in world space.

    Args:
        calculateExactly: (create) - Should the bounding box calculation be exact?
        ignoreInvisible: (create) - Should the bounding box calculation include or exclude invisible objects?
    """
    pass


def expandedSelection(*args, depth: Optional[Union[int, bool]] = int, expansionType: Optional[Union[str, bool]] = str):
    """
    Examines the current selection list and returns that list, expanded to meet certain criteria. See the command flags for the exact criteria that will be used.

    Args:
        depth: (create) - Number of steps away from current selection to expand to. A value of 0 will not expand the selection at all.
        expansionType: (create) - The type of graph along which to expand the selection. Legal values are: DG : Use the normal DG connections EG : Use the evaluation graph connections SG : Use the scheduling graph connections within the evaluation graph  If the actual selected node is not included in the graph being expanded on, e.g. there is no evaluation node when using the EG type, then the selected node will not appear in the output. If this flag is not specified then the type defaults to DG.
    """
    pass


def filterButterworthCtx(*args, apply: bool = bool, cutoffFrequency: Optional[Union[float, bool]] = float, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, keepKeysOnFrame: bool = bool, name: Optional[Union[str, bool]] = str, samplingRate: Optional[Union[float, bool]] = float, selectedKeys: bool = bool, startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], edit: bool = bool, query: bool = bool):
    """
    Creates/edits a Butterworth filter context. This context can be used to interactively preview/edit the Butterworth filter on a set of animation curves.

    Args:
        apply: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        cutoffFrequency: (edit, query) - Specifies the cutoff frequency setting of the Butterworth filter. Default is 7.0.
        endTime: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keepKeysOnFrame: (edit, query) - When true, the Butterworth filter will reposition output keys to whole frames for the specified sampling rate.
        name: (create) - If this is a tool command, name the tool appropriately.
        samplingRate: (edit, query) - Specifies the sampling rate setting of the Butterworth filter. Default is 30.0.
        selectedKeys: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
    pass


def filterGaussianCtx(*args, apply: bool = bool, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, sampleCount: Optional[Union[int, bool]] = int, selectedKeys: bool = bool, startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], useQuaternion: bool = bool, width: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], edit: bool = bool, query: bool = bool):
    """
    Creates a smooth (gaussian) filter context. This context can ben used to interactively preview/edit the smooth (gaussian) filter on a set of animation curves.

    Args:
        apply: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        endTime: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        sampleCount: (edit, query) - This parameter specifies the number of neighbor will be sampled.
        selectedKeys: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
        useQuaternion: (edit, query) - When this is enabled, the filter will first convert the curves (rotation channel curves, 3 sibling requires at the same time) from Euler space to quaternions. Then apply the gaussian filter on it. Convert it back from Quaternions back to Euler space eventually.
        width: (edit, query) - This parameter specifies the width of the gaussian kernel shape. Wider width will
    """
    pass


def filterInstances(*args, shapes: bool = bool, query: bool = bool):
    """
    This command filters the selection list to remove duplicate instances that refer to the same object/components. If any such instances are found they will be merged with the first selected instance.

    Args:
        shapes: (create) - If this is true then the command will check for an instanced shapes below the selected transform(s) and use them to decide whether the parent transforms should be considered instances. Default is false.
    """
    pass


def filterKeyReducerCtx(*args, apply: bool = bool, endTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, keySync: bool = bool, name: Optional[Union[str, bool]] = str, precision: Optional[Union[float, bool]] = float, precisionMode: Optional[Union[int, bool]] = int, preserveKeyTangent: Optional[Union[str, bool]] = str, selectedKeys: bool = bool, startTime: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], edit: bool = bool, query: bool = bool):
    """
    Creates/edits a KeyReducer filter context. This context can be used to interactively preview/edit the KeyReducer filter on a set of animation curves.

    Args:
        apply: (edit) - When specified, finalizes the current context state and records the command for the operation. This is equivalent to completing the tool action without exiting the current tool context.
        endTime: (edit, query) - Specifies the end time portion of the time range for this filter. This time range is used when selectedKeys is false.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        keySync: (edit, query) - When true, a secondary filter pass is applied that adds a key to sibling curves (X,Y,Z) for each key that is encountered.
        name: (create) - If this is a tool command, name the tool appropriately.
        precision: (edit, query) - Defines the precision parameter.  For the Key Reducer filter, this parameter specifies the error limit between the source and output curves. Greater values reduce precision. Lower values increase precision.
        precisionMode: (edit, query) - Specifies the precision mode for the Key Reducer filter. Avaiable modes are:  0: Absolute value. 1: Percentage  Default is 1 (percentage mode).
        preserveKeyTangent: (edit, multiuse, query) - When specified, keys whose in or out tangent type match the specified type are preserved.  Supported tangent types:  fixed linear flat smooth step clamped plateau stepnext auto
        selectedKeys: (edit, query) - If true, sets the filter to apply to the selected keys. Otherwise, the filter applies to the specified time range. Default is on.
        startTime: (edit, query) - Specifies the start time portion of the time range for this filter. This time range is used when selectedKeys is false.
    """
    pass


def geometryAttrInfo(*args, boundingBox: bool = bool, castToEdges: bool = bool, castToFaces: bool = bool, castToVerts: bool = bool, componentTagCategory: bool = bool, componentTagExpression: Optional[Union[str, bool]] = str, componentTagHash: bool = bool, componentTagHistory: bool = bool, componentTagHistoryHash: bool = bool, componentTagNames: bool = bool, components: bool = bool, deformerChain: bool = bool, elementCount: bool = bool, groupId: Optional[Union[int, bool]] = int, matrix: bool = bool, nodeChain: bool = bool, originalGeometry: bool = bool, outputPlugChain: bool = bool, plugChain: bool = bool, pointCount: bool = bool, pointIndices: bool = bool, points: bool = bool, subsetState: bool = bool):
    """
    This command provides information about the geometry in an attribute. This command therefore only works on attributes that contain geometry. A variety of types of information can be requested, like the number of verts, the boundingbox, which componentTags exist, etc.

    Args:
        boundingBox: (create) - Returns the bounding box of the geometry
        castToEdges: (create) - Ensures the componentTag expression will be resolved to edge components
        castToFaces: (create) - Ensures the componentTag expression will be resolved to face components
        castToVerts: (create) - Ensures the componentTag expression will be resolved to vert components
        componentTagCategory: (create) - This flag will return the component tag category of the resulting components. Verts are "v", edges are "e", faces are "f". In case the the category can not be determined "unknown" is returned
        componentTagExpression: (create) - Specifies the componentTagExpression we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in the combination of these componentTags
        componentTagHash: (create) - This flag will return a unique hash value for the state of all the componentTags contained in the geometry. If a hash is different from before it means that something has changed, either tags have been added/removed/renamed and/or their component contents have been altered.
        componentTagHistory: (create) - This flag will return a description of the componentTags and the nodes in the chain where they were added to the geometry.
        componentTagHistoryHash: (create) - This flag will return a unique hash value for the componentTag history of the geometry in the plug. If a hash is different from before it means that something has changed, either different nodes have created the tags or the contents of the tags have been altered.
        componentTagNames: (create) - Returns the names of the componentTags on the geometry
        components: (create) - Returns the components of the geometry
        deformerChain: (create) - This flag will return the list of deformer nodes through which the geometry passes to the specified plug
        elementCount: (create) - Returns the element count of the components
        groupId: (create) - Specifies the groupId we want to query. When specified all answers to the information requests will be limited to the subset of the geometry as is contained in this groupId
        matrix: (create) - Returns the matrix associated with the geometry
        nodeChain: (create) - This flag will return the list of nodes through which the geometry passes to the specified plug
        originalGeometry: (create) - This flag will return the name of a plug on a node upstream (likely at the front end) that is the best candidate to be used as the originalGeometry. This can return an empty plug when none exists.
        outputPlugChain: (create) - This flag will return the chain of plugs upstream of the specified plug (including only output plugs)
        plugChain: (create) - This flag will return the chain of plugs upstream of the specified plug (including both input and output plugs)
        pointCount: (create) - Returns the point count of the geometry
        pointIndices: (create) - Returns the indices of the geometry
        points: (create) - Returns a list of points of the geometry
        subsetState: (create) - Returns the state of the specified subset -1 means the subset was invalid 0 means the subset contains none of the points of the geometry 1 means the subset contains some (but not all) of the points of the geometry 2 means the subset contains all the points of the geometry
    """
    pass


def getAttr(*args, asString: bool = bool, caching: bool = bool, channelBox: bool = bool, expandEnvironmentVariables: bool = bool, keyable: bool = bool, lock: bool = bool, multiIndices: bool = bool, settable: bool = bool, silent: bool = bool, size: bool = bool, time: Optional[Union[Union[float, Tuple[float, float]], bool]] = [float, float], type: bool = bool):
    """
    This command returns the value of the named object's attribute.

    Args:
        asString: (create) - This flag is only valid for enum attributes. It allows you to get the attribute values as strings instead of integer values. Note that the returned string value is dependent on the UI language Maya is running in (about -uiLanguage). Not supported for Ufe attributes.
        caching: (create) - Returns whether the attribute is set to be cached internally Not supported for Ufe attributes.
        channelBox: (create) - Returns whether the attribute is set to show in the Channel Box. Keyable attributes also show in the Channel Box. Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is controlled using the channelBox command flag -ual/ufeFixedAttrList.
        expandEnvironmentVariables: (create) - Expand any environment variable and (tilde characters on UNIX) found in string attributes which are returned. Not supported for Ufe attributes.
        keyable: (create) - Returns the keyable state of the attribute. Not supported for Ufe attributes.
        lock: (create) - Returns the lock state of the attribute.
        multiIndices: (create) - If the attribute is a multi, this will return a list containing all of the valid indices for the attribute. Not supported for Ufe attributes.
        settable: (create) - Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An attribute is settable if it's not locked and either not connected, or has only keyframed animation. For Ufe attributes an attribute is settable if it's not locked.
        silent: (create) - When evaluating an attribute that is not a numeric or string value, suppress the error message saying that the data cannot be displayed. The attribute will be evaluated even though its data cannot be displayed. This flag does not suppress all error messages, only those that are benign. Not supported for Ufe attributes.
        size: (create) - Returns the size of a multi-attribute array.  Returns 1 if non-multi. Not supported for Ufe attributes.
        time: (create) - Evaluate the attribute at the given time instead of the current time. Not supported for Ufe attributes.
        type: (create) - Returns the type of data currently in the attribute.  Attributes of simple types such as strings and numerics always contain data, but attributes of complex types (arrays, meshes, etc) may contain no data if none has ever been assigned to them. When this happens the command will return with no result: not an empty string, but no result at all. Attempting to directly compare this non-result to another value or use it in an expression will result in an error, but you can assign it to a variable in which case the variable will be set to the default value for its type (e.g. an empty string for a string variable, zero for an integer variable, an empty array for an array variable). So to be safe when using this flag, always assign its result to a string variable, never try to use it directly.
    """
    pass


def getClassification(*args, satisfies: Optional[Union[str, bool]] = str):
    """
    Returns the classification string for a given node type.

    Args:
        satisfies: (create) - Returns true if the given node type's classification satisfies the classification string which is passed with the flag.  A non-compound classification string A is said to satisfy a non-compound classification string B if A is a subclassification of B (for example, "shaders/reflective" satisfies "shaders").  A compound classification string A satisfies a compound classification string B iff:   every component of A satisfies at least one component of B and  every component of B is satisfied by at least one component of A   Hence, "shader/reflective/phong:texture" satisfies "shader:texture", but "shader/reflective/phong" does not satisfy "shader:texture".
    """
    pass


def graphDollyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a dolly context for the graph editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def graphSelectContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a selection context for the hypergraph editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def graphTrackCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a track context for the graph editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def group(*args, absolute: bool = bool, empty: bool = bool, name: Optional[Union[str, bool]] = str, parent: Optional[Union[str, bool]] = str, relative: bool = bool, useAsGroup: Optional[Union[str, bool]] = str, world: bool = bool):
    """
    This command groups the specified objects under a new group and returns the name of the new group.

    Args:
        absolute: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        empty: (create) - create an empty group (with no objects in it)
        name: (create) - Assign given name to new group node.
        parent: (create) - put the new group under the given parent
        relative: (create) - preserve existing local object transformations (relative to the new group node)
        useAsGroup: (create) - Use the specified node as the group node. The specified node must be derived from the transform node and must not have any existing parents or children.
        world: (create) - put the new group under the world
    """
    pass


def hide(*args, allObjects: bool = bool, clearLastHidden: bool = bool, clearSelection: bool = bool, invertComponents: bool = bool, returnHidden: bool = bool, testVisibility: bool = bool):
    """
    The

    Args:
        allObjects: (create) - Make everything invisible (top level objects).
        clearLastHidden: (create) - Clear the last hidden list.
        clearSelection: (create) - Clear selection after the operation.
        invertComponents: (create) - Hide components that are not specified.
        returnHidden: (create) - Hide objects, but also return list of hidden objects.
        testVisibility: (create) - Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).
    """
    pass


def hilite(*args, replace: bool = bool, toggle: bool = bool, unHilite: bool = bool):
    """
    Hilites/Unhilites the specified object(s).  Hiliting an object makes it possible to select the components of the object.  If no objects are specified then the selection list is used.

    Args:
        replace: (create) - Hilite the specified objects.  Any objects previously hilited will no longer be hilited.
        toggle: (create) - Toggle the hilite state of the specified objects.
        unHilite: (create) - Remove the specified objects from the hilite list.
    """
    pass


def ikHandleCtx(*args, autoPriorityH: bool = bool, createCurve: bool = bool, createRootAxis: bool = bool, exists: bool = bool, forceSolverH: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, numSpans: int = int, parentCurve: bool = bool, poWeightH: Optional[Union[float, bool]] = float, priorityH: Optional[Union[int, bool]] = int, rootOnCurve: bool = bool, rootTwistMode: bool = bool, simplifyCurve: bool = bool, snapCurve: bool = bool, snapHandleH: bool = bool, solverTypeH: Optional[Union[str, bool]] = str, stickyH: Optional[Union[str, bool]] = str, twistType: str = str, weightH: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool.  The options for the tool will be set to the flags that the user specifies.

    Args:
        autoPriorityH: (create, edit, query) - Specifies that this handle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createCurve: (create, edit, query) - Specifies if a curve should be automatically created for the ikSplineHandle. The flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this flag returns an int.
        createRootAxis: (edit) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path. This flag is ignored in the ikHandleCtx. C: The default is off.  Q: When queried, this flag returns an int.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH: (create, edit, query) - Specifies if the ikSolver is enabled for the ikHandle. C: The default is on.  Q: When queried, this flag returns an int.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        numSpans: (edit) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx. C: The default is 1.  Q: When queried, this flag returns an int.
        parentCurve: (edit) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle. The flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this flag returns an int.
        poWeightH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is 1. Q: When queried, this flag returns an int.
        rootOnCurve: (edit) - Specifies if the root is locked onto the curve of the ikSplineHandle. This flag is ignored in the ikHandleCtx.  C: The default is on.  Q: When queried, this flag returns an int.
        rootTwistMode: (edit) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. This flag is ignored in the ikHandleCtx.  C: The default is off.  Q: When queried, this flag returns an int.
        simplifyCurve: (edit) - Specifies if the ikSplineHandle curve should be simplified. This flag is ignored in the ikHandleCtx. C: The default is on.  Q: When queried, this returns an int.
        snapCurve: (edit) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle. This flag is ignored in the ikHandleCtx. C: The default is off.  Q: When queried, this flag returns an int.
        snapHandleH: (create, edit, query) - Specifies if the ikHandle snapping is on. C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH: (create, edit, query) - Lists what ikSolver is being used. The ikSplineSolver may not be selected. To use an ikSplineSolver use the ikSplineHandleCtx command.  C: The default solver is the default set by the user preferences. Q: When queried, this flag returns a string.
        stickyH: (create, edit, query) - Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". C: The default is "off". Q: When queried, this flag returns a string.
        twistType: (edit) - Specifies the type of interpolation to be used by the ikSplineHandle. This flag is ignored in the ikHandleCtx. The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut".  C: The default is "linear".  Q: When queried, this flag returns a string.
        weightH: (create, edit, query) - Specifies the weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
    """
    pass


def ikSplineHandleCtx(*args, autoPriorityH: bool = bool, createCurve: bool = bool, createRootAxis: bool = bool, exists: bool = bool, forceSolverH: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, numSpans: int = int, parentCurve: bool = bool, poWeightH: Optional[Union[float, bool]] = float, priorityH: Optional[Union[int, bool]] = int, rootOnCurve: bool = bool, rootTwistMode: bool = bool, simplifyCurve: bool = bool, snapCurve: bool = bool, snapHandleH: bool = bool, solverTypeH: Optional[Union[str, bool]] = str, stickyH: Optional[Union[str, bool]] = str, twistType: str = str, weightH: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of ikSplineHandle tool.  The options for the tool will be set to the flags the user specifies.

    Args:
        autoPriorityH: (create, edit, query) - Specifies that this handle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createCurve: (create, edit, query) - Specifies if a curve should be automatically created for the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        createRootAxis: (edit) - Specifies if a root transform should automatically be created above the joints affected by the ikSplineHandle. This option is used to prevent the root flipping singularity on a motion path.  C: The default is off.  Q: When queried, this flag returns an int.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH: (create, edit, query) - Specifies if the ikSolver is enabled for the ikHandle. C: The default is on.  Q: When queried, this flag returns an int.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        numSpans: (edit) - Specifies the number of spans in the automatically generated curve of the ikSplineHandle.  C: The default is 1.  Q: When queried, this flag returns an int.
        parentCurve: (edit) - Specifies if the curve should automatically be parented to the parent of the first joint affected by the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        poWeightH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is 1. Q: When queried, this flag returns an int.
        rootOnCurve: (edit) - Specifies if the root is locked onto the curve of the ikSplineHandle.  C: The default is on.  Q: When queried, this flag returns an int.
        rootTwistMode: (edit) - Specifies whether the start joint is allowed to twist or not. If not, then the required twist is distributed over the remaining joints. This applies to all the twist types. C: The default is off.  Q: When queried, this flag returns an int.
        simplifyCurve: (edit) - Specifies if the ikSplineHandle curve should be simplified.  C: The default is on.  Q: When queried, this returns an int.
        snapCurve: (edit) - Specifies if the curve should automatically snap to the first joint affected by the ikSplineHandle.  C: The default is off.  Q: When queried, this flag returns an int.
        snapHandleH: (create, edit, query) - Specifies if the ikHandle snapping is on. This flag is ignored for the ikSplineSolver. C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH: (create, edit, query) - Lists what ikSolver is being used. For the ikSplineContext the solver can only be the ikSplineSolver and this flag is ignored.  C: The default solver is the ikSplineSolver. Q: When queried, this flag returns a string.
        stickyH: (create, edit, query) - Specifies if the ikHandle is sticky or not. Valid strings are "sticky" and "off". This flag is ignored for the ikSplineSolver. C: The default is "off". Q: When queried, this flag returns a string.
        twistType: (edit) - Specifies the type of interpolation to be used by the ikSplineHandle.  The interpolation options are "linear", "easeIn", "easeOut", and "easeInOut". C: The default is "linear".  Q: When queried, this flag returns a string.
        weightH: (create, edit, query) - Specifies the weight of the ikHandle. This flag is ignored in the ikSplineHandleCtx. C: The default is 1. Q: When queried, this flag returns a float.
    """
    pass


def inheritTransform(*args, off: bool = bool, on: bool = bool, preserve: bool = bool, toggle: bool = bool, query: bool = bool):
    """
    This command toggles the inherit state of an object. If this flag is off the object will not inherit transformations from its parent. In other words transformations applied to the parent node will not affect the object and it will act as though it is under the world.

    Args:
        off: (create, query) - turn off inherit state for the given object(s)
        on: (create, query) - turn on inherit state for the given object(s)
        preserve: (create, query) - preserve the objects world-space position by modifying the object(s) transformation matrix.
        toggle: (create, query) - toggle the inherit state for the given object(s) (default if no flags are given) -on turn on inherit state for the given object(s) -off turn off inherit state for the given object(s)
    """
    pass


def insertJointCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The command will create an insert joint context. The insert joint tool inserts joints into an existing chain of joints.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def insertKeyCtx(*args, breakdown: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, preserveTangent: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to insert keys within the graph editor

    Args:
        breakdown: (edit, query) - Specifies whether or not to create breakdown keys
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        preserveTangent: (edit, query) - Specifies whether or not to preserve tangent
    """
    pass


def instance(*args, leaf: bool = bool, name: Optional[Union[str, bool]] = str, smartTransform: bool = bool):
    """
    Instancing is a way of making the same object appear twice in the scene. This is accomplished by creation of a new transform node that points to an exisiting object. Changes to the transform are independent but changes to the "instanced" object affect all instances since the node is shared.

    Args:
        leaf: (create) - Instances leaf-level objects. Acts like duplicate except leaf-level objects are instanced.
        name: (create) - Name to give new instance
        smartTransform: (create) - Transforms instances item based on movements between transforms
    """
    pass


def instanceable(*args, allow: bool = bool, recursive: bool = bool, shape: bool = bool, query: bool = bool):
    """
    

    Args:
        allow: (create, query) - Specifies the new instanceable state for the node. Specify true to allow the node to be instanceable, and false to prevent it from being instanced. The default is true (i.e. nodes can be instanced by default).
        recursive: (create) - Can be specified with the -allow flag in create or edit mode to recursively apply the -allow setting to all non-shape children of the selected node(s). To also affect shapes, also specify the -shape flag along with -recursive.
        shape: (create) - Can be specified with the -allow flag in create or edit mode to apply the -allow setting to all shape children of the selected node(s). This flag can be specified in conjunction with the -recursive flag.
    """
    pass


def instancer(*args, addObject: bool = bool, cycle: Optional[Union[str, bool]] = str, cycleStep: Optional[Union[float, bool]] = float, cycleStepUnits: Optional[Union[str, bool]] = str, index: Optional[Union[int, bool]] = int, levelOfDetail: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, object: Optional[Union[str, bool]] = str, objectPosition: Optional[Union[str, bool]] = str, objectRotation: Optional[Union[str, bool]] = str, objectScale: Optional[Union[str, bool]] = str, pointDataSource: bool = bool, removeObject: bool = bool, rotationOrder: Optional[Union[str, bool]] = str, rotationUnits: Optional[Union[str, bool]] = str, valueName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command is used to create a instancer node and set the proper attributes in the node.

    Args:
        addObject: (create, edit) - This flag indicates that objects specified by the -object flag will be added to the instancer node as instanced objects.
        cycle: (create, edit, query) - This flag sets or queries the cycle attribute for the instancer node. The options are "none" or "sequential".  The default is "none".
        cycleStep: (create, edit, query) - This flag sets or queries the cycle step attribute for the instancer node.  This attribute indicates the size of the step in frames or seconds (see cycleStepUnit).
        cycleStepUnits: (create, edit, query) - This flag sets or queries the cycle step unit attribute for the instancer node.  The options are "frames" or "seconds".  The default is "frames".
        index: (query) - This flag is used to query the name of the ith instanced object.
        levelOfDetail: (create, edit, query) - This flag sets or queries the level of detail of the instanced objects.  The options are "geometry", "boundingBox", "boundingBoxes".  The default is "geometry".
        name: (create, query) - This flag sets or queries the name of the instancer node.
        object: (create, edit, multiuse, query) - This flag indicates which objects will be add/removed from the list of instanced objects.  The flag is used in conjuction with the -add and -remove flags.  If neither of these flags is specified on the command line then -add is assumed.
        objectPosition: (query) - This flag queries the given objects position.  This object can be any instanced object or sub-object.
        objectRotation: (query) - This flag queries the given objects rotation.  This object can be any instanced object or sub-object.
        objectScale: (query) - This flag queries the given objects scale.  This object can be any instanced object or sub-object.
        pointDataSource: (query) - This flag is used to query the source node supply the data for the input points.
        removeObject: (edit) - This flag indicates that objects specified by the -object flag will be removed from the instancer node as instanced objects.
        rotationOrder: (create, edit, query) - This flag specifies the rotation order associated with the rotation flag.  The options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
        rotationUnits: (create, edit, query) - This flag specifies the rotation units associated with the rotation flag.  The options are degrees or radians.  By default the attribute is degrees.
        valueName: (query) - This flag is used to query the value(s) of the array associated with the given name.  If the -index flag is used in conjuction with this flag then the ith value will be returned.  Otherwise, the entire array will be returned.
    """
    pass


def isConnected(*args, ignoreUnitConversion: bool = bool):
    """
    The

    Args:
        ignoreUnitConversion: (create) - In looking for connections, skip past unit conversion nodes.
    """
    pass


def isDirty(*args, connection: bool = bool, datablock: bool = bool):
    """
    The

    Args:
        connection: (create) - Check the connection of the plug (default).
        datablock: (create) - Check the datablock entry for the plug.
    """
    pass


def isolateSelect(*args, addDagObject: str = str, addSelected: bool = bool, addSelectedObjects: bool = bool, loadSelected: bool = bool, removeDagObject: str = str, removeSelected: bool = bool, state: bool = bool, update: bool = bool, viewObjects: bool = bool, query: bool = bool):
    """
    This command turns on/off isolate select mode in a specified modeling view, specified as the argument. Isolate select mode is a display mode where the currently selected objects are added to a list and only those objects are displayed in the view. It allows for selective viewing of specific objects and object components.

    Args:
        addDagObject: () - Add the specified object to the set of objects to be displayed in the view.
        addSelected: () - Add the currently active objects to the set of objects to be displayed in the view.
        addSelectedObjects: () - Add selected objects to the set of objects to be displayed in the view. This flag differs from addSelected in that it will ignore selected components and add the entire object.
        loadSelected: () - Replace the objects being displayed with the currently active objects.
        removeDagObject: () - Remove the specified object from the set of objects to be displayed in the view.
        removeSelected: () - Remove the currently active objects to the set of objects to be displayed in the view.
        state: (query) - Turns isolate select mode on/off.
        update: () - Update the view's list of objects due to a change to the set of objects to be displayed.
        viewObjects: (query) - Returns the name (if any) of the objectSet which contains the list of objects visible in the view if isolate select mode is on. If isolate select mode is off, an empty string is returned.
    """
    pass


def jointCtx(*args, autoJointOrient: Optional[Union[str, bool]] = str, autoPriorityH: bool = bool, createIKHandle: bool = bool, degreeOfFreedomJ: Optional[Union[str, bool]] = str, exists: bool = bool, forceSolverH: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, jointAutoLimits: bool = bool, jointOrientationJ: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], largeBoneLength: Optional[Union[float, bool]] = float, largeBoneRadius: Optional[Union[float, bool]] = float, poWeightH: Optional[Union[float, bool]] = float, priorityH: Optional[Union[int, bool]] = int, scaleCompensateJ: bool = bool, scaleJ: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), scaleOrientationJ: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], secondaryAxisOrient: Optional[Union[str, bool]] = str, smallBoneLength: Optional[Union[float, bool]] = float, smallBoneRadius: Optional[Union[float, bool]] = float, snapHandleH: bool = bool, solverTypeH: Optional[Union[str, bool]] = str, stickyH: Optional[Union[str, bool]] = str, symmetry: bool = bool, symmetryAxis: Optional[Union[str, bool]] = str, variableBoneSize: bool = bool, weightH: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    The joint context command (jointCtx) updates the parameters of the joint tool. The options for the tool will be set by the flags the user specifies.

    Args:
        autoJointOrient: (create, edit, query) - Specifies the joint orientation. Valid string choices are permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz", "zyx". The first letter determines which axis is aligned with the bone. C: The default is "xyz". Q: When queried, this flag returns a string.
        autoPriorityH: (create, edit, query) - Specifies if the ikHandle's priority is assigned automatically. C: The default is off. Q: When queried, this flag returns an int.
        createIKHandle: (create, edit, query) - Enables the joint tool to create an ikHandle when the tool is completed. C: The default is off. Q: When queried, this flag returns an int.
        degreeOfFreedomJ: (create, edit, query) - Specifies the degrees of freedom for all of the joints created by the tool. Valid string choices are the free axes; "x", "y", "z", "xy", "xz", "yz", "xyz", and "none". C: The default is "xyz". Q: When queried, this flag returns a string.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        forceSolverH: (create, edit, query) - Specifies if the ikSolver for the ikHandle is enabled. C: The default is on. Q: When queried, this flag returns an int.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        jointAutoLimits: (create, edit, query) - Automatically computes the joint limits based on the kind of joint created.  C: The default is off. Q: When queried, this flag returns an int.
        jointOrientationJ: (create, edit, query) - Sets the orientation of the joints created by the tool. If autoJointOrient in on, these values will be ignored. C: The default is 0 0 0. Q: When queried, this flag returns an array of three floats.
        largeBoneLength: (create, edit, query) - Specifies the length above which bones should be assigned the largeBoneRadius.
        largeBoneRadius: (create, edit, query) - Specifies the radius for bones whose length is above the largeBoneLength
        poWeightH: (create, edit, query) - Specifies the position/orientation weight of the ikHandle. C: The default is 1. Q: When queried, this flag returns a float.
        priorityH: (create, edit, query) - Specifies the priority of the ikHandle. C: The default is on. Q: When queried, this flag returns an int.
        scaleCompensateJ: (create, edit, query) - Specifies if scale compensate is enabled. C: The default is on. Q: When queried, this flag returns an int.
        scaleJ: (create, edit, query) - Sets the scale for the joints created by the tool. C: The default is 1 1 1. Q: When queried, this flag returns an array of three floats.
        scaleOrientationJ: (create, edit, query) - Sets the current value for the scale orientation. If autoJointOrient in on, these values will be ignored. C: The default is 0 0 0. Q: When queried, this flag returns an array of three floats.
        secondaryAxisOrient: (create, edit, query) - Specifies the orientation of the secondary rotate axis. Valid string choices are: "xup", "xdown", "yup", "ydown", "zup", "zdown", "none".
        smallBoneLength: (create, edit, query) - Specifies the length below which bones should be assigned the smallBoneRadius.
        smallBoneRadius: (create, edit, query) - Specifies the radius for bones whose length is below the smallBoneLength.
        snapHandleH: (create, edit, query) - Sepcifies if snapping is enabled for the ikHandle.  C: The default is on. Q: When queried, this flag returns an int.
        solverTypeH: (create, edit, query) - Sets the name of the solver to use with the ikHandle.  C: The default is the solver set to the default in the user preferences. Q: When queried, this flag returns a string.
        stickyH: (create, edit, query) - Specifies if the ikHandle is sticky or not. If "sticky" is passed then the ikHandle will be sticky. If "off" is used then ikHandle stickiness will be turned off. C: The default is "off". Q: When queried, this flag returns a string.
        symmetry: (create, edit, query) - Automaticaly create a symmetry joint based if symmetry is on.  C: The default is off. Q: When queried, this flag returns an int.
        symmetryAxis: (create, edit, query) - Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.  C: The default is x. Q: When queried, this flag returns a string.
        variableBoneSize: (create, edit, query) - Specifies whether or not variable bone length and radius settings should be used.
        weightH: (create, edit, query) - Specifies the weight of the ikHandle. The weight is relative to the other ikHandles in the scene. C: The default is 1. Q: When queried, this flag returns a float.
    """
    pass


def keyframeRegionCurrentTimeCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to change current time within the keyframe region of the dope sheet editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def keyframeRegionDirectKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, option: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to directly manipulate keyframes within the dope sheet editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        option: (create) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    pass


def keyframeRegionDollyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a dolly context for the dope sheet editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def keyframeRegionInsertKeyCtx(*args, breakdown: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to insert keys within the keyframe region of the dope sheet editor

    Args:
        breakdown: (edit, query) - Specifies whether or not to create breakdown keys
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def keyframeRegionMoveKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, option: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to move keyframes within the keyframe region of the dope sheet editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        option: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver". Specifies the keyframe -option to use.  When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    pass


def keyframeRegionScaleKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, scaleSpecifiedKeys: bool = bool, type: str = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to scale keyframes within the keyframe region of the dope sheet editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        scaleSpecifiedKeys: (edit, query) - Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        type: (edit) - rect | manip Specifies the type of scale manipulator to use
    """
    pass


def keyframeRegionSelectKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def keyframeRegionSetKeyCtx(*args, breakdown: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to set keys within the keyframe region of the dope sheet editor

    Args:
        breakdown: (edit, query) - Specifies whether or not to create breakdown keys
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def keyframeRegionTrackCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a track context for the dope sheet editor.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def lassoContext(*args, drawClosed: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Creates a context to perform selection via a "lasso".  Use for irregular selection regions, where the "marquee-style" select of the "selectContext" is inappropriate.

    Args:
        drawClosed: (create, edit, query) - Turns the closed display of the lasso on/off.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def latticeDeformKeyCtx(*args, envelope: Optional[Union[float, bool]] = float, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, latticeColumns: Optional[Union[int, bool]] = int, latticeRows: Optional[Union[int, bool]] = int, name: Optional[Union[str, bool]] = str, scaleLatticePts: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to deform key frames with lattice manipulator.  This context only works in the graph editor.

    Args:
        envelope: (edit, query) - Specifies the influence of the lattice.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        latticeColumns: (edit, query) - Specifies the number column points the lattice contains.
        latticeRows: (edit, query) - Specifies the number of rows the lattice contains.
        name: (create) - If this is a tool command, name the tool appropriately.
        scaleLatticePts: (edit, query) - Specifies if the selected lattice points should scale around the pick point. If this value is false the the default operation is 'move'
    """
    pass


def license(*args, borrow: bool = bool, info: bool = bool, isBorrowed: bool = bool, isExported: bool = bool, isTrial: bool = bool, licenseMethod: bool = bool, productChoice: bool = bool, r: bool = bool, showBorrowInfo: bool = bool, showProductInfoDialog: bool = bool, status: bool = bool, usage: bool = bool):
    """
    This command displays version information about the application if it is executed without flags.  If one of the above flags is specified then the specified version information is returned.

    Args:
        borrow: (create) - This flag is obsolete and no longer supported.
        info: (create) - This flag is obsolete and no longer supported.
        isBorrowed: (create) - This flag is obsolete and no longer supported.
        isExported: (create) - This flag is obsolete and no longer supported.
        isTrial: (create) - This flag is obsolete and no longer supported.
        licenseMethod: (create) - This flag is obsolete and no longer supported.
        productChoice: (create) - This flag is obsolete and no longer supported.
        r: (create) - This flag is obsolete and no longer supported.
        showBorrowInfo: (create) - This flag is obsolete and no longer supported.
        showProductInfoDialog: (create) - Show the Product Information Dialog
        status: (create) - This flag is obsolete and no longer supported.
        usage: (create) - This flag is obsolete and no longer supported.
    """
    pass


def listAttr(*args, array: bool = bool, attributeType: Optional[Union[str, bool]] = str, caching: bool = bool, category: Optional[Union[str, bool]] = str, changedSinceFileOpen: bool = bool, channelBox: bool = bool, connectable: bool = bool, extension: bool = bool, fromPlugin: bool = bool, fullNodeName: bool = bool, hasData: bool = bool, hasNullData: bool = bool, inUse: bool = bool, keyable: bool = bool, leaf: bool = bool, locked: bool = bool, multi: bool = bool, nodeName: bool = bool, output: bool = bool, ramp: bool = bool, read: bool = bool, readOnly: bool = bool, scalar: bool = bool, scalarAndArray: bool = bool, settable: bool = bool, shortNames: bool = bool, string: Optional[Union[str, bool]] = str, unlocked: bool = bool, usedAsFilename: bool = bool, userDefined: bool = bool, visible: bool = bool, write: bool = bool):
    """
    This command lists the attributes of a node.  If no flags are specified all attributes are listed.

    Args:
        array: (create) - only list array (not multi) attributes
        attributeType: (create, multiuse) - Return attributes of a particular type.
        caching: (create) - only show attributes that are cached internally
        category: (create, multiuse) - only show attributes belonging to the given category. Category string can be a regular expression.
        changedSinceFileOpen: (create) - Only list the attributes that have been changed since the file they came from was opened. Typically useful only for objects/attributes coming from referenced files.
        channelBox: (create) - only show non-keyable attributes that appear in the channelbox
        connectable: (create) - only show connectable attributes
        extension: (create) - list user-defined attributes for all nodes of this type (extension attributes)
        fromPlugin: (create) - only show attributes that were created by a plugin
        fullNodeName: (create) - Return full node name in result.
        hasData: (create) - list only attributes that have data (all attributes except for message attributes)
        hasNullData: (create) - list only attributes that have null data. This will list all attributes that have data (see hasData flag) but the data value is uninitialized. A common example where an attribute may have null data is when a string attribute is created but not yet assigned an initial value. Similarly array attribute data is often null until it is initialized.
        inUse: (create) - only show attributes that are currently marked as in use. This flag indicates that an attribute affects the scene data in some way. For example it has a non-default value or it is connected to another attribute.  This is the general concept though the precise implementation is subject to change.
        keyable: (create) - only show attributes that can be keyframed
        leaf: (create) - Only list the leaf-level name of the attribute. controlPoints[44].xValue would be listed as "xValue".
        locked: (create) - list only attributes which are locked
        multi: (create) - list each currently existing element of a multi-attribute
        nodeName: (create) - Return node name in result.
        output: (create) - List only the attributes which are numeric or which are compounds of numeric attributes.
        ramp: (create) - list only attributes which are ramps
        read: (create) - list only attributes which are readable
        readOnly: (create) - List only the attributes which are readable and not writable.
        scalar: (create) - only list scalar numerical attributes
        scalarAndArray: (create) - only list scalar and array attributes
        settable: (create) - list attribute which are settable
        shortNames: (create) - list short attribute names (default is to list long names)
        string: (create, multiuse) - List only the attributes that match the other criteria AND match the string(s) passed from this flag. String can be a regular expression.
        unlocked: (create) - list only attributes which are unlocked
        usedAsFilename: (create) - list only attributes which are designated to be treated as filenames
        userDefined: (create) - list user-defined (dynamic) attributes
        visible: (create) - only show visible or non-hidden attributes
        write: (create) - list only attributes which are writable
    """
    pass


def listAttrPatterns(*args, patternType: bool = bool, verbose: bool = bool):
    """
    Attribute patterns are plain text descriptions of an entire Maya attribute forest. ("forest" because there could be an arbitrary number of root level attributes, it's not restricted to having a single common parent though in general that practice is a good idea.) This command lists the various pattern types available, usually created via plugin, as well as any specific patterns that have already been instantiated. A pattern type is a thing that knows how to take some textual description of an attribute tree, e.g. XML or plaintext, and convert it into an attribute pattern that can be applied to any node or node type in Maya.

    Args:
        patternType: (create) - If turned on then show the list of pattern types rather than actual instantiated patterns.
        verbose: (create) - If turned on then show detailed information about the patterns or pattern types. The same list of instance or pattern names is returned as for the non-verbose case.
    """
    pass


def listConnections(*args, connections: bool = bool, destination: bool = bool, exactType: bool = bool, fullNodeName: bool = bool, plugs: bool = bool, shapes: bool = bool, skipConversionNodes: bool = bool, source: bool = bool, type: Optional[Union[str, bool]] = str):
    """
    This command returns a list of all attributes/objects of a specified type that are connected to the given object(s). If no objects are specified then the command lists the connections on selected nodes.

    Args:
        connections: (create) - If true, return both attributes involved in the connection. The one on the specified object is given first.  Default false.
        destination: (create) - Give the attributes/objects that are on the "destination" side of connection to the given object.  Default true.
        exactType: (create) - When set to true, -t/type only considers node of this exact type. Otherwise, derived types are also taken into account.
        fullNodeName: (create) - Return full node name in result.
        plugs: (create) - If true, return the connected attribute names; if false, return the connected object names only.  Default false;
        shapes: (create) - Actually return the shape name instead of the transform when the shape is "selected".  Default false.
        skipConversionNodes: (create) - If true, skip over unit conversion nodes and return the node connected to the conversion node on the other side.  Default false.
        source: (create) - Give the attributes/objects that are on the "source" side of connection to the given object.  Default true.
        type: (create) - If specified, only take objects of a specified type.
    """
    pass


def listHistory(*args, allConnections: bool = bool, allFuture: bool = bool, allGraphs: bool = bool, breadthFirst: bool = bool, fastIteration: bool = bool, fullNodeName: bool = bool, future: bool = bool, futureLocalAttr: bool = bool, futureWorldAttr: bool = bool, groupLevels: bool = bool, historyAttr: bool = bool, interestLevel: Optional[Union[int, bool]] = int, leaf: bool = bool, levels: Optional[Union[int, bool]] = int, pruneDagObjects: bool = bool, query: bool = bool):
    """
    This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose construction history it passes through. The construction history consists of connections to specific attributes of a node defined as the creators and results of the node's main data, eg. the curve for a Nurbs Curve node.

    Args:
        allConnections: (create) - If specified, the traversal that searches for the history or future will not restrict its traversal across nodes to only dependent plugs. Thus it will reach all upstream nodes (or all downstream nodes for f/future).
        allFuture: (create) - If listing the future, list all of it. Otherwise if a shape has an attribute that represents its output geometry data, and that plug is connected, only list the future history downstream from that connection.
        allGraphs: (create) - This flag is obsolete and has no effect.
        breadthFirst: (create) - The breadth first traversal will return the closest nodes in the traversal first. The depth first traversal will follow a complete path away from the node, then return to any other paths from the node. Default is depth first.
        fastIteration: (create) - This flag enables a faster iteration mode that offers more scalable performance, especially when traversing nodes with numerous connections.  However, the results can be slightly different, especially in cases with transitive dependencies between attributes (attribute A is affected by B which is affected by C, but A is not directly affected by C).
        fullNodeName: (create) - Return full node name in result.
        future: (create) - List the future instead of the history.
        futureLocalAttr: (query) - This flag allows querying of the local-space future-related attribute(s) on shape nodes.
        futureWorldAttr: (query) - This flag allows querying of the world-space future-related attribute(s) on shape nodes.
        groupLevels: (create) - The node names are grouped depending on the level.  > 1 is the lead, the rest are grouped with it.
        historyAttr: (query) - This flag allows querying of the attribute where history connects on shape nodes.
        interestLevel: (create) - If this flag is set, only nodes whose historicallyInteresting attribute value is not less than the value will be listed. The historicallyInteresting attribute is 0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for the users.
        leaf: (create) - If transform is selected, show history for its leaf shape. Default is true.
        levels: (create) - Levels deep to traverse. Setting the number of levels to 0 means do all levels. All levels is the default.
        pruneDagObjects: (create) - If this flag is set, prune at dag objects.
    """
    pass


def listNodesWithIncorrectNames(*args):
    """
    List all nodes with incorrect names in the Script Editor.

    Args:
    """
    pass


def listNodeTypes(*args, exclude: Optional[Union[str, bool]] = str):
    """
    Lists dependency node types satisfying a specified classification string.

    Args:
        exclude: (create) - Nodes that satisfies this exclude classification will be filtered out.
    """
    pass


def listRelatives(*args, allDescendents: bool = bool, allParents: bool = bool, children: bool = bool, fullPath: bool = bool, noIntermediate: bool = bool, parent: bool = bool, path: bool = bool, shapes: bool = bool, type: Optional[Union[str, bool]] = str):
    """
    This command lists parents and children of DAG objects. The flags -c/children, -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually exclusive. Only one can be used in a command.

    Args:
        allDescendents: (create) - Returns all the children, grand-children etc. of this dag node.  If a descendent is instanced, it will appear only once on the list returned. Note that it lists grand-children before children.
        allParents: (create) - Returns all the parents of this dag node. Normally, this command only returns the parent corresponding to the first instance of the object
        children: (create) - List all the children of this dag node (default).
        fullPath: (create) - Return full pathnames instead of object names.
        noIntermediate: (create) - No intermediate objects
        parent: (create) - Returns the parent of this dag node
        path: (create) - Return a proper object name that can be passed to other commands.
        shapes: (create) - List all the children of this dag node that are shapes (ie, not transforms)
        type: (create, multiuse) - List all relatives of the specified type.
    """
    pass


def listSets(*args, allSets: bool = bool, extendToShape: bool = bool, object: Optional[Union[str, bool]] = str, type: Optional[Union[int, bool]] = int):
    """
    The listSets command is used to get a list of all the sets an object belongs to. To get sets of a specific type for an object use the type flag as well.

    Args:
        allSets: (create) - Returns all sets in the scene.
        extendToShape: (create) - When requesting a transform's sets also walk down to the shape immediately below it for its sets.
        object: (create) - Returns all sets which this object is a member of.
        type: (create) - Returns all sets in the scene of the given type:  1 - all rendering sets 2 - all deformer sets
    """
    pass


def lockNode(*args, ignoreComponents: bool = bool, lock: bool = bool, lockName: bool = bool, lockUnpublished: bool = bool, query: bool = bool):
    """
    

    Args:
        ignoreComponents: (create, query) - Normally, the presence of a component in the list of objects to be locked will cause the command to fail with an error. But if this flag is supplied then components will be silently ignored.
        lock: (create, query) - Specifies the new lock state for the node. The default is true.
        lockName: (create, query) - Specifies the new lock state for the node's name.
        lockUnpublished: (create, query) - Used in conjunction with the lock flag. On a container, lock or unlock all unpublished attributes on the members of the container. For non-containers, lock or unlock unpublished attributes on the specified node.
    """
    pass


def ls(*args, absoluteName: bool = bool, allPaths: bool = bool, assemblies: bool = bool, cameras: bool = bool, containerType: Optional[Union[str, bool]] = str, containers: bool = bool, dagObjects: bool = bool, defaultNodes: bool = bool, dependencyNodes: bool = bool, exactType: Optional[Union[str, bool]] = str, excludeType: Optional[Union[str, bool]] = str, flatten: bool = bool, geometry: bool = bool, ghost: bool = bool, head: Optional[Union[int, bool]] = int, hilite: bool = bool, intermediateObjects: bool = bool, invisible: bool = bool, leaf: bool = bool, lights: bool = bool, live: bool = bool, lockedNodes: bool = bool, long: bool = bool, materials: bool = bool, modified: bool = bool, noIntermediate: bool = bool, nodeTypes: bool = bool, objectsOnly: bool = bool, orderedSelection: bool = bool, partitions: bool = bool, persistentNodes: bool = bool, planes: bool = bool, preSelectHilite: bool = bool, readOnly: bool = bool, recursive: bool = bool, referencedNodes: bool = bool, references: bool = bool, renderGlobals: bool = bool, renderQualities: bool = bool, renderResolutions: bool = bool, renderSetups: bool = bool, selection: bool = bool, sets: bool = bool, shapes: bool = bool, shortNames: bool = bool, showNamespace: bool = bool, showType: bool = bool, tail: Optional[Union[int, bool]] = int, templated: bool = bool, textures: bool = bool, transforms: bool = bool, type: Optional[Union[str, bool]] = str, ufeObjects: bool = bool, undeletable: bool = bool, untemplated: bool = bool, uuid: bool = bool, visible: bool = bool):
    """
    The

    Args:
        absoluteName: (create) - This flag can be used in conjunction with the showNamespace flag to specify that the namespace(s) returned by the command be in absolute namespace format. The absolute name of the namespace is a full namespace path, starting from the root namespace ":" and including all parent namespaces.  For example ":ns:ball" is an absolute namespace name while "ns:ball" is not. The absolute namespace name is invariant and is not affected by the current namespace or relative namespace modes.
        allPaths: (create) - List all paths to nodes in DAG. This flag only works if -dag is also specified or if an object name is supplied.
        assemblies: (create) - List top level transform Dag objects
        cameras: (create) - List camera shapes.
        containerType: (create, multiuse) - List containers with the specified user-defined type.  This flag cannot be used in conjunction with the type or exactType flag.
        containers: (create) - List containers. Includes both standard containers as well as other types of containers such as dagContainers.
        dagObjects: (create) - List Dag objects of any type. If object name arguments are passed to the command then this flag will list all Dag objects below the specified object(s).
        defaultNodes: (create) - Returns default nodes. A default node is one that Maya creates automatically and does not get saved out with the scene, although some of its attribute values may.
        dependencyNodes: (create) - List dependency nodes. (including Dag objects)
        exactType: (create, multiuse) - List all objects of the specified type, but not objects that are descendents of that type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.  This flag cannot be used in conjunction with the type or excludeType flag.
        excludeType: (create, multiuse) - List all objects that are not of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag.  This flag cannot be used in conjunction with the type or exactType flag.
        flatten: (create) - Flattens the returned list of objects so that each component is identified individually.
        geometry: (create) - List geometric Dag objects.
        ghost: (create) - List ghosting objects.
        head: (create) - This flag  specifies the maximum number of elements to be returned from the beginning of the list of items. Note: each type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount.
        hilite: (create) - List objects that are currently hilited for component selection.
        intermediateObjects: (create) - List only intermediate dag nodes.
        invisible: (create) - List only invisible dag nodes.
        leaf: (create) - List all leaf nodes in Dag. This flag is a modifier and must be used in conjunction with the -dag flag.
        lights: (create) - List light shapes.
        live: (create) - List objects that are currently live.
        lockedNodes: (create) - Returns locked nodes, which cannot be deleted or renamed. However, their status may change.
        long: (create) - Return full path names for Dag objects. By default the shortest unique name is returned.
        materials: (create) - List materials or shading groups.
        modified: (create) - When this flag is set, only nodes modified since the last save will be returned.
        noIntermediate: (create) - List only non intermediate dag nodes.
        nodeTypes: (create) - Lists all registered node types.
        objectsOnly: (create) - When this flag is set only object names will be returned and components/attributes will be ignored.
        orderedSelection: (create) - List objects and components that are currently selected in their order of selection.  This flag depends on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not enabled than this flag will return the same thing as the -sl/selection flag would.
        partitions: (create) - List partitions.
        persistentNodes: (create) - Returns persistent nodes, which are nodes that stay in the Maya session after a file > new. These are a special class of default nodes that do not get reset on file > new. Ex: itemFilter and selectionListOperator nodes.
        planes: (create) - List construction plane shapes.
        preSelectHilite: (create) - List components that are currently hilited for pre-selection.
        readOnly: (create) - Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please use "-referencedNodes".
        recursive: (create) - When set to true, this command will look for name matches in all namespaces. When set to false, this command will only look for matches in namespaces that are requested (e.g. by specifying a name containing the ':'... "ns1:pSphere1").
        referencedNodes: (create) - Returns referenced nodes. Referenced nodes are read only.
        references: (create) - List references associated with files. Excludes special reference nodes such as the sharedReferenceNode and unknown reference nodes.
        renderGlobals: (create) - List render globals.
        renderQualities: (create) - List named render qualities.
        renderResolutions: (create) - List render resolutions.
        renderSetups: (create) - Alias for -renderGlobals.
        selection: (create) - List objects that are currently selected.
        sets: (create) - List sets.
        shapes: (create) - List shape objects.
        shortNames: (create) - Return short attribute names. By default long attribute names are returned.
        showNamespace: (create) - Show the namespace of each object after the object name.  This flag cannot be used in conjunction with the showType flag.
        showType: (create) - List the type of each object after its name.
        tail: (create) - This flag specifies the maximum number of elements to be returned from the end of the list of items. Note: each    type flag will return at most this many items so if multiple type flags are specified then the number of items returned can be greater than this amount
        templated: (create) - List only templated dag nodes.
        textures: (create) - List textures.
        transforms: (create) - List transform objects.
        type: (create, multiuse) - List all objects of the specified type. This flag can appear multiple times on the command line. Note: the type passed to this flag is the same type name returned from the showType flag. Note: some selection items in Maya do not have a specific object/data type associated with them and will return "untyped" when listed with this flag.  This flag cannot be used in conjunction with the exactType or excludeType flag.
        ufeObjects: (create) - When used in conjunction with the -sl/selection flag, will return objects that are defined through the UFE interface as well as native Maya objects.
        undeletable: (create) - Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.
        untemplated: (create) - List only un-templated dag nodes.
        uuid: (create) - Return node UUIDs instead of names. Note that there are no "UUID paths" - combining this flag with e.g. the -long flag will not result in a path formed of node UUIDs.
        visible: (create) - List only visible dag nodes.
    """
    pass


def makeIdentity(*args, apply: bool = bool, jointOrient: bool = bool, normal: Optional[Union[int, bool]] = int, preserveNormals: bool = bool, rotate: bool = bool, scale: bool = bool, translate: bool = bool):
    """
    The makeIdentity command is a quick way to reset the selected transform and all of its children down to the shape level by the identity transformation.  You can also specify which of transform, rotate or scale is applied down from the selected transform. The identity transformation means:

    Args:
        apply: (create) - If this flag is true, the accumulated transforms are applied to the shape after the transforms are made identity, such that the world space positions of the transforms pivots are preserved, and the shapes do not move. The default is false.
        jointOrient: (create) - If this flag is set, the joint orient on joints will be reset to align with worldspace.
        normal: (create) - If this flag is set to 1, the normals on polygonal objects will be frozen.  This flag is valid only when the -apply flag is on. If this flag is set to 2, the normals on polygonal objects will be frozen only if its a non-rigid transformation matrix. ie, a transformation that does not contain shear, skew or non-proportional scaling. The default behaviour is not to freeze normals.
        preserveNormals: (create) - If this flag is true, the normals on polygonal objects will be reversed if the objects are negatively scaled (reflection). This flag is valid only when the -apply flag is on.
        rotate: (create) - If this flag is true, only the rotation is applied to the shape. The rotation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        scale: (create) - If this flag is true, only the scale is applied to the shape. The scale factor will be changed to 1, 1, 1. If neither translate nor rotate nor scale flags are specified, then all (t, r, s) are applied.
        translate: (create) - If this flag is true, only the translation is applied to the shape. The translation will be changed to 0, 0, 0. If neither translate nor rotate nor scale flags are specified, then all (t, r, s)  are applied.  (Note: the translate flag is not meaningful when applied to joints, since joints are made to preserve their world space position.  This flag will have no effect on joints.)
    """
    pass


def makeLive(*args, none: bool = bool):
    """
    This commmand makes an object live.  A live object defines the surface on which to create objects and to move object relative to.  Only construction planes, nurbs surfaces and polygon meshes can be made live.

    Args:
        none: (create) - If the -n/none flag, the live object will become dormant. Use of this flag causes any arguments to be ignored.
    """
    pass


def makePaintable(*args, activate: bool = bool, activateAll: bool = bool, altAttribute: Optional[Union[str, bool]] = str, attrType: Optional[Union[str, bool]] = str, clearAll: bool = bool, remove: bool = bool, shapeMode: Optional[Union[str, bool]] = str, uiName: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    Make attributes of nodes paintable to Attribute Paint Tool. This command is used to register new attributes to the Attribute Paint tool as paintable. Once registered the attributes will be recognized by the Attribute Paint tool and the user will be able to paint them.

    Args:
        activate: (create, query) - Activate / deactivate the given paintable attribute. Used to filter out some nodes in the attribute paint tool.
        activateAll: (create, query) - Activate / deactivate all the registered paintable attributes. Used to filter out some nodes in the attribute paint tool.
        altAttribute: (create, multiuse, query) - Define an alternate attribute which will also receive the same values. There can be multiple such flags.
        attrType: (create, query) - Paintable attribute type.    Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.
        clearAll: (create, query) - Removes all paintable attribute definitions.
        remove: (create, query) - Make the attribute not paintable any more.
        shapeMode: (create, query) - This flag controls how Artisan correlates the paintable node to a corresponding shape node.  It is used for attributes of type multi of multi, where the first multi dimension corresponds to the shape index (i.e. cluster nodes). At present, only one value of this flag is supported: "deformer". By default this flag is an empty string, which means that there is a direct indexing (no special mapping required) of the attribute with respect to vertices on the shape.
        uiName: (create, query) - UI name. Default is the attribute name.
    """
    pass


def manipMoveContext(*args, activeHandle: Optional[Union[int, bool]] = int, activeHandleNormal: Optional[Union[int, bool]] = int, alignAlong: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), bakePivotOri: bool = bool, constrainAlongNormal: bool = bool, currentActiveHandle: Optional[Union[int, bool]] = int, editPivotMode: bool = bool, editPivotPosition: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, interactiveUpdate: bool = bool, lastMode: Optional[Union[int, bool]] = int, manipVisible: bool = bool, mode: Optional[Union[int, bool]] = int, orientAxes: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), orientJoint: Optional[Union[str, bool]] = str, orientJointEnabled: bool = bool, orientObject: Optional[Union[str, bool]] = str, orientTowards: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), pinPivot: bool = bool, pivotOriHandle: bool = bool, position: bool = bool, postCommand: Optional[Union[str, bool]] = str, postDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preCommand: Optional[Union[str, bool]] = str, preDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preserveChildPosition: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAbout: int = int, reflectionAxis: int = int, reflectionTolerance: float = float, secondaryAxisOrient: Optional[Union[str, bool]] = str, snap: bool = bool, snapComponentsRelative: bool = bool, snapLiveFaceCenter: bool = bool, snapLivePoint: bool = bool, snapPivotOri: bool = bool, snapPivotPos: bool = bool, snapRelative: bool = bool, snapValue: Optional[Union[float, bool]] = float, translate: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), tweakMode: bool = bool, xformConstraint: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a move manip context. Note that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of all move manip context.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flags, will change all existing move manip context.

    Args:
        activeHandle: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all 3 axes) is active (default)
        activeHandleNormal: (edit, query) - 0 - U axis handle is active 1 - V axis handle is active 2 - N axis handle is active ( default ) 3 - Center handle (all 3 axes) is active  applicable only when the manip mode is 3.
        alignAlong: (create, edit) - Aligns active handle along vector.
        bakePivotOri: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        constrainAlongNormal: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all 3 axes) is active 4 - XY plane handle is active 5 - YZ plane handle is active 6 - XZ plane handle is active
        editPivotMode: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition: (query) - Returns the current position of the edit pivot manipulator.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        interactiveUpdate: (edit, query) - Value can be : true or false. This flag value is valid only if the mode is 3 i.e. move vertex normal.
        lastMode: (query) - Returns the previous translation mode.
        manipVisible: (query) - Returns true if the main translate manipulator is visible.
        mode: (edit, query) - Translate mode:  0 - Object Space 1 - Local Space 2 - World Space (default) 3 - Move Along Vertex Normal 4 - Move Along Rotation Axis 5 - Move Along Live Object Axis 6 - Custom Axis Orientation 10 - Component Space
        orientAxes: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientJoint: (edit, query) - Specifies the type of orientation for joint orientation. Valid options are: none, xyz, xzy, yxz, yzx, zxy, zyx.
        orientJointEnabled: (edit, query) - Specifies if joints should be reoriented when moved.
        orientObject: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards: (create, edit) - Orients active handle towards world point
        pinPivot: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position: (query) - Returns the current position of the manipulator
        postCommand: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition: (edit, query) - When false, the children objects move when their parent is moved. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        reflection: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        secondaryAxisOrient: (edit, query) - Specifies the global axis (in world coordinates) that should be used to should be used to align the second axis of the orientJointType triple. Valid options are xup, yup, zup, xdown, ydown, zdown, none.
        snap: (edit, query) - Value can be : true or false. Enable/Disable the discrete move. If set to true, the move manipulator of all the move contexts would snap at discrete points along the active handle during mouse drag.  The interval between the points can be controlled using the 'snapValue' flag.
        snapComponentsRelative: (edit, query) - Value can be : true or false. If true, while snapping a group of CVs/Vertices, the relative spacing between them will be preserved. If false, all the CVs/Vertices will be snapped to the target point (is used during grid snap(hotkey 'x'), and point snap(hotkey 'v')) Depress the 'x' key before click-dragging the manip handle and check to see the behaviour of moving a bunch of CVs, with this flag ON and OFF.
        snapLiveFaceCenter: (edit, query) - Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the face centers of the object.
        snapLivePoint: (edit, query) - Value can be : true or false. If true, while moving on the live polygon object, the move manipulator will snap to the vertices of the object.
        snapPivotOri: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative: (edit, query) - Value can be : true or false. Applicable only when the snap is enabled. If true, the snapValue is treated relative to the original position before moving. If false, the snapValue is treated relative to the world origin. NOTE:    If in local/object Space Mode, the snapRelative should be ON. Absolute discrete move is not supported in local/object mode.
        snapValue: (edit, query) - Applicable only when the snap is enabled. The manipulator of all move contexts would move in steps of 'snapValue'
        translate: (edit, query) - Returns the translation of the manipulator for its current orientation/mode.
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
        xformConstraint: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    pass


def manipMoveLimitsCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create a context for the translate limits manipulator.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def manipRotateContext(*args, activeHandle: Optional[Union[int, bool]] = int, alignAlong: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), bakePivotOri: bool = bool, centerTrackball: bool = bool, constrainAlongNormal: bool = bool, currentActiveHandle: Optional[Union[int, bool]] = int, editPivotMode: bool = bool, editPivotPosition: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, lastMode: Optional[Union[int, bool]] = int, manipVisible: bool = bool, mode: Optional[Union[int, bool]] = int, modifyTranslation: bool = bool, orientAxes: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), orientObject: Optional[Union[str, bool]] = str, orientTowards: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), pinPivot: bool = bool, pivotOriHandle: bool = bool, position: bool = bool, postCommand: Optional[Union[str, bool]] = str, postDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preCommand: Optional[Union[str, bool]] = str, preDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preserveChildPosition: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAbout: int = int, reflectionAxis: int = int, reflectionTolerance: float = float, rotate: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), snap: bool = bool, snapPivotOri: bool = bool, snapPivotPos: bool = bool, snapRelative: bool = bool, snapValue: Optional[Union[float, bool]] = float, tweakMode: bool = bool, useCenterPivot: bool = bool, useManipPivot: bool = bool, useObjectPivot: bool = bool, xformConstraint: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a rotate manip context.

    Args:
        activeHandle: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - View rotation handle (outer ring) is active (default)
        alignAlong: (create, edit) - Aligns active handle along vector.
        bakePivotOri: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        centerTrackball: (create, edit, query) - Specify if the center is to be handled like a trackball
        constrainAlongNormal: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - View rotation handle (outer ring) is active 4 - Arc Ball is active
        editPivotMode: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition: (query) - Returns the current position of the edit pivot manipulator.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        lastMode: (query) - Returns the previous rotation mode.
        manipVisible: (query) - Returns true if the rotate manipulator is visible.
        mode: (edit, query) - Rotate mode:  0 - Object Space (default) 1 - World Space 2 - Gimbal Mode 3 - Custom Axis Orientation 10 - Component Space
        modifyTranslation: (edit, query) - When false, and an object is rotated about a point other than its rotate pivot, its rotateTranslate attribute is modified to put the object at the correct position. When true, its translate attribute is used instead. Default is false.
        orientAxes: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientObject: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards: (create, edit) - Orients active handle towards world point
        pinPivot: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position: (query) - Returns the current position of the manipulator.
        postCommand: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition: (edit, query) - When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        reflection: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        rotate: (edit, query) - Returns the rotation of the manipulator for its current orientation/mode.
        snap: (create, edit, query) - Specify that the manipulation is to use absolute snap
        snapPivotOri: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative: (create, edit, query) - Specify that the manipulation is to use relative snap
        snapValue: (create, edit, query) - Specify the snapping value
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
        useCenterPivot: (edit, query) - When true, use the center of the selection's bounding box as the center of the rotation (for all objects).
        useManipPivot: (edit, query) - When true, use the manipulator's center as the center of the rotation (for all objects).
        useObjectPivot: (edit, query) - When true, use each object's pivot as the center of its rotation.
        xformConstraint: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    pass


def manipRotateLimitsCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create a context for the rotate limits manipulator.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def manipScaleContext(*args, activeHandle: Optional[Union[int, bool]] = int, alignAlong: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), bakePivotOri: bool = bool, constrainAlongNormal: bool = bool, currentActiveHandle: Optional[Union[int, bool]] = int, editPivotMode: bool = bool, editPivotPosition: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, lastMode: Optional[Union[int, bool]] = int, manipVisible: bool = bool, mode: Optional[Union[int, bool]] = int, orientAxes: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), orientObject: Optional[Union[str, bool]] = str, orientTowards: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), pinPivot: bool = bool, pivotOriHandle: bool = bool, position: bool = bool, postCommand: Optional[Union[str, bool]] = str, postDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preCommand: Optional[Union[str, bool]] = str, preDragCommand: Optional[Union[Tuple[str, str], bool]] = [str, str], preserveChildPosition: bool = bool, preserveUV: bool = bool, preventNegativeScale: bool = bool, reflection: bool = bool, reflectionAbout: int = int, reflectionAxis: int = int, reflectionTolerance: float = float, scale: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), snap: bool = bool, snapPivotOri: bool = bool, snapPivotPos: bool = bool, snapRelative: bool = bool, snapValue: Optional[Union[float, bool]] = float, tweakMode: bool = bool, useManipPivot: bool = bool, useObjectPivot: bool = bool, xformConstraint: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a scale manip context.

    Args:
        activeHandle: (edit, query) - Sets the default active handle for the manip.  That is, the handle which should be initially active when the tool is activated. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all axes) is active (default)
        alignAlong: (create, edit) - Aligns active handle along vector.
        bakePivotOri: (edit, query) - Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.
        constrainAlongNormal: (edit, query) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        currentActiveHandle: (edit, query) - Sets the active handle for the manip. Values can be:  0 - X axis handle is active 1 - Y axis handle is active 2 - Z axis handle is active 3 - Center handle (all axes) is active 4 - XY plane handle is active 5 - YZ plane handle is active 6 - XZ plane handle is active
        editPivotMode: (query) - Returns true manipulator is in edit pivot mode
        editPivotPosition: (query) - Returns the current position of the edit pivot manipulator.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        lastMode: (query) - Returns the previous scaling mode.
        manipVisible: (query) - Returns true if the scale manipulator is visible.
        mode: (edit, query) - Scale mode:  0 - Object Space 1 - Local Space 2 - World Space (default) 3 - Scale Along Vertex Normal 4 - Scale Along Rotation Axis 5 - Scale Along Live Object Axis 6 - Custom Axis Orientation 10 - Component Space
        orientAxes: (edit, query) - Orients manipulator rotating around axes by specified angles
        orientObject: (create, edit) - Orients manipulator to the passed in object/component
        orientTowards: (create, edit) - Orients active handle towards world point
        pinPivot: (edit, query) - Pin component pivot. When the component pivot is set and pinned selection changes will not reset the pivot position and orientation.
        pivotOriHandle: (edit, query) - When true, the pivot manipulator will show the orientation handle during editing. Default is true.
        position: (query) - Returns the current position of the manipulator.
        postCommand: (create, edit) - Specifies a command to be executed when the tool is exited.
        postDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the end of a drag when a node of the specified type is in the selection.
        preCommand: (create, edit) - Specifies a command to be executed when the tool is entered.
        preDragCommand: (create, edit) - Specifies a command and a node type. The command will be executed at the start of a drag when a node of the specified type is in the selection.
        preserveChildPosition: (edit, query) - When false, the children objects move when their parent is rotated. When true, the worldspace position of the children will be maintained as the parent is moved. Default is false.
        preserveUV: (edit, query) - When false, the uvs are not changes to match the vertex edit. When true, the uvs are edited to project to new values to stop texture swimming as vertices are moved.
        preventNegativeScale: (query) - When this is true, negative scale is not allowed.
        reflection: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAbout: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionAxis: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        reflectionTolerance: () - This flag is obsolete. Reflection is now managed as part of selection itself using the symmetricModeling command.
        scale: (edit, query) - Returns the scale of the manipulator for its current orientation/mode.
        snap: (create, edit, query) - Specify that the manipulation is to use absolute snap
        snapPivotOri: (edit, query) - Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.
        snapPivotPos: (edit, query) - Snap pivot position. Modify pivot position when snapping the pivot to a component.
        snapRelative: (create, edit, query) - Specify that the manipulation is to use relative snap
        snapValue: (create, edit, query) - Specify the snapping value
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
        useManipPivot: (create, edit, query) - Specify whether to pivot on the manip
        useObjectPivot: (create, edit, query) - Specify whether to pivot on the object
        xformConstraint: (edit, query) - none - no transform constraint edge - edge transform constraint surface - surface transform constraint
    """
    pass


def manipScaleLimitsCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create a context for the scale limits manipulator.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def matchTransform(*args, pivots: bool = bool, position: bool = bool, positionX: bool = bool, positionY: bool = bool, positionZ: bool = bool, rotatePivot: bool = bool, rotation: bool = bool, rotationX: bool = bool, rotationY: bool = bool, rotationZ: bool = bool, scale: bool = bool, scaleBox: bool = bool, scalePivot: bool = bool, scaleX: bool = bool, scaleY: bool = bool, scaleZ: bool = bool):
    """
    This command modifies the source object's transform to match the target object's transform.

    Args:
        pivots: (create) - Match the source object(s) scale/rotate pivot positions to the target transform's pivot.
        position: (create) - Match the source object(s) position to the target object.
        positionX: (create) - Match the source object(s) X position to the target object.
        positionY: (create) - Match the source object(s) Y position to the target object.
        positionZ: (create) - Match the source object(s) Z position to the target object.
        rotatePivot: (create) - Match the source object(s) rotate pivot position to the target transform's pivot.
        rotation: (create) - Match the source object(s) rotation to the target object.
        rotationX: (create) - Match the source object(s) X rotation to the target object.
        rotationY: (create) - Match the source object(s) Y rotation to the target object.
        rotationZ: (create) - Match the source object(s) Z rotation to the target object.
        scale: (create) - Match the source object(s) scale to the target transform.
        scaleBox: (create) - Use the source/target object's child bounding box size when matching scaling.
        scalePivot: (create) - Match the source object(s) scale pivot position to the target transform's pivot.
        scaleX: (create) - Match the source object(s) X scale to the target object.
        scaleY: (create) - Match the source object(s) Y scale to the target object.
        scaleZ: (create) - Match the source object(s) Z scale to the target object.
    """
    pass


def modelCurrentTimeCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, percent: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to change current time within the model views.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        percent: (edit, query) - Percent of the screen space that represents the full time slider range (default is 50%)
    """
    pass


def move(*args, absolute: bool = bool, componentOffset: bool = bool, componentSpace: bool = bool, constrainAlongNormal: bool = bool, deletePriorHistory: bool = bool, localSpace: bool = bool, moveX: bool = bool, moveXY: bool = bool, moveXYZ: bool = bool, moveXZ: bool = bool, moveY: bool = bool, moveYZ: bool = bool, moveZ: bool = bool, objectSpace: bool = bool, orientJoint: Optional[Union[str, bool]] = str, parameter: bool = bool, preserveChildPosition: bool = bool, preserveGeometryPosition: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAboutBBox: bool = bool, reflectionAboutOrigin: bool = bool, reflectionAboutX: bool = bool, reflectionAboutY: bool = bool, reflectionAboutZ: bool = bool, reflectionTolerance: Optional[Union[float, bool]] = float, relative: bool = bool, rotatePivotRelative: bool = bool, scalePivotRelative: bool = bool, secondaryAxisOrient: Optional[Union[str, bool]] = str, symNegative: bool = bool, worldSpace: bool = bool, worldSpaceDistance: bool = bool, xformConstraint: Optional[Union[str, bool]] = str):
    """
    The move command is used to change the positions of geometric objects.

    Args:
        absolute: (create) - Perform an absolute operation.
        componentOffset: (create) - Move components individually in local space
        componentSpace: (create) - Move in local component space
        constrainAlongNormal: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory: (create) - If true then delete the history prior to the current operation.
        localSpace: (create) - Move in local space
        moveX: (create) - Move in X direction
        moveXY: (create) - Move in XY direction
        moveXYZ: (create) - Move in all directions (default)
        moveXZ: (create) - Move in XZ direction
        moveY: (create) - Move in Y direction
        moveYZ: (create) - Move in YZ direction
        moveZ: (create) - Move in Z direction
        objectSpace: (create) - Move in object space
        orientJoint: (create) - Default is xyz.
        parameter: (create) - Move in parametric space
        preserveChildPosition: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV: (create) - When true, UV values on translated components are projected along the translation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative: (create) - Perform a operation relative to the object's current position
        rotatePivotRelative: (create) - Move relative to the object's rotate pivot point.
        scalePivotRelative: (create) - Move relative to the object's scale pivot point.
        secondaryAxisOrient: (create) - Default is xyz.
        symNegative: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        worldSpace: (create) - Move in world space
        worldSpaceDistance: (create) - Move is specified in world space units
        xformConstraint: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    pass


def moveKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, moveFunction: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, option: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to move keyframes within the graph editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        moveFunction: (edit, query) - linear | power | constant. Specifies how the keys are dragged. The default move type is constant where all keys move the same amount as controlled by user movement. Power provides a fall-off function where the center of the drag moves the most and the keys around the drag move less.
        name: (create) - If this is a tool command, name the tool appropriately.
        option: (create, edit, query) - Valid values are "move," "insert," "over," and "segmentOver." When you "move" a key, the key will not cross over (in time) any keys before or after it. When you "insert" a key, all keys before or after (depending upon the -timeChange value) will be moved an equivalent amount. When you "over" a key, the key is allowed to move to any time (as long as a key is not there already). When you "segmentOver" a set of keys (this option only has a noticeable effect when more than one key is being moved) the first key (in time) and last key define a segment (unless you specify a time range). That segment is then allowed to move over other keys, and keys will be moved to make room for the segment.
    """
    pass


def nodeCast(*args, copyDynamicAttrs: bool = bool, disableAPICallbacks: bool = bool, disableScriptJobCallbacks: bool = bool, disconnectUnmatchedAttrs: bool = bool, force: bool = bool, swapNames: bool = bool, swapValues: bool = bool):
    """
    Given two nodes, a source node of type A and a target node of type B, where type A is either type B or a sub-type of B, this command will replace the target node with the source node. That is, all node connections, DAG hierarchy and attribute values on the target node will be removed from the target node and placed on the source node. This operation will fail if either object is referenced, locked or if the nodes do not share a common sub-type. This operation is atomic. If the given parameters fail, then the source and target nodes will remain in their initial state prior to execution of the command. IMPORTANT: the command will currently ignore instance connections and instance objects.  It will also ignore reference nodes.

    Args:
        copyDynamicAttrs: (create) - If the target node contains any dynamic attributes that are not defined on the source node, then create identical dynamic attricutes on the source node and copy the values and connections from the target node into them.
        disableAPICallbacks: (create) - add comment
        disableScriptJobCallbacks: (create) - add comment
        disconnectUnmatchedAttrs: (create) - If the node that is being swapped out has any connections that do not exist on the target node, then indicate if the connection should be disconnected. By default these connections are not removed because they cannot be restored if the target node is swapped back with the source node.
        force: (create) - Forces the command to do the node cast operation even if the nodes do not share a common base object. When this flag is specified the command will try to do the best possible attribute matching when swapping the command.  It is not recommended to use the '-swapValues/sv' flag with this flag.
        swapNames: (create) - Swap the names of the nodes. By default names are not swapped.
        swapValues: (create) - Indicates if the commands should exchange attributes on the common attributes between the two nodes.  For example, if the nodes are the same base type as a transform node, then rotate, scale, translate values would be copied over.
    """
    pass


def nodeType(*args, apiType: bool = bool, derived: bool = bool, inherited: bool = bool, isTypeName: bool = bool, ufeRuntimeName: bool = bool):
    """
    This command returns a string which identifies the given node's type.

    Args:
        apiType: (create) - Return the MFn::Type value (as a string) corresponding to the given node.  This is particularly useful when the given node is defined by a plug-in, since in this case, the MFn::Type value corresponds to the underlying proxy class.  This flag cannot be used in combination with any of the other flags.
        derived: (create) - Return a string array containing the names of all the currently known node types which derive from the type of the specified node.
        inherited: (create) - Return a string array containing the names of all the base node types inherited by the specified node.
        isTypeName: (create) - If this flag is present, then the argument provided to the command is the name of a node type rather than the name of a specific node.
        ufeRuntimeName: (create) - Return the UFE Runtime name corresponding to the given node. This is particularly useful to filter between native Maya objects and non-native objects exposed to Maya through the UFE interface.
    """
    pass


def objectCenter(*args, gl: bool = bool, local: bool = bool, x: bool = bool, y: bool = bool, z: bool = bool):
    """
    This command returns the coordinates of the center of the bounding box of the specified object. If one coordinate only is specified, it will be returned as a float. If no coordinates are specified, an array of floats is returned, containing x, y, and z. If you specify multiple coordinates, only one will be returned.

    Args:
        gl: (create) - Return positional values in global coordinates (default).
        local: (create) - Return positional values in local coordinates.
        x: (create) - Return X value only
        y: (create) - Return Y value only
        z: (create) - Return Z value only
    """
    pass


def objectType(*args, isAType: Optional[Union[str, bool]] = str, isType: Optional[Union[str, bool]] = str, tagFromType: Optional[Union[str, bool]] = str, typeFromTag: Optional[Union[int, bool]] = int, typeTag: bool = bool):
    """
    This command returns the type of elements. Warning: This command is incomplete and may not be supported by all object types.

    Args:
        isAType: (create) - Returns true if the object is the specified type or derives from an object that is of the specified type. This flag will only work with dependency nodes.
        isType: (create) - Returns true if the object is exactly of the specified type. False otherwise.
        tagFromType: (create) - Returns the type tag given a type name.
        typeFromTag: (create) - Returns the type name given an integer type tag.
        typeTag: (create) - Returns an integer tag that is unique for that object type.  Not all object types will have tags.  This is the unique 4-byte value that is used to identify nodes of a given type in the binary file format.
    """
    pass


def objExists(*args):
    """
    This command simply returns true or false depending on whether an object with the given name exists.

    Args:
    """
    pass


def orbitCtx(*args, alternateContext: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, localOrbit: bool = bool, name: Optional[Union[str, bool]] = str, orbitScale: Optional[Union[float, bool]] = float, toolName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create, edit, or query an orbit context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localOrbit: (create, edit, query) - Orbit around the camera's center of interest.
        name: (create) - If this is a tool command, name the tool appropriately.
        orbitScale: (create, edit, query) - In degrees of rotation per 100 pixels of cursor drag.
        toolName: (create, query) - Name of the specific tool to which this command refers.
    """
    pass


def panZoomCtx(*args, alternateContext: bool = bool, buttonDown: bool = bool, buttonUp: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, panMode: bool = bool, toolName: Optional[Union[str, bool]] = str, zoomMode: bool = bool, zoomScale: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create camera 2D pan/zoom context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        buttonDown: (create) - Perform the button down operation
        buttonUp: (create) - Perform the button up operation
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        panMode: (create) - Specify to create a camera 2D pan context, which is the default.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        zoomMode: (create) - Specify to create a camera 2D zoom context.
        zoomScale: (create, edit, query) - Scale the zoom. The smaller the scale the slower the drag.
    """
    pass


def paramDimContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command used to register the paramDimCtx tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def paramDimension(*args):
    """
    This command is used to create a param dimension to display the parameter value of a curve/surface at a specified point on the curve/surface.

    Args:
    """
    pass


def paramLocator(*args, position: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The command creates a locator in the underworld of a NURBS curve or NURBS surface at the specified parameter value.  If no object is specified, then a locator will be created on the first valid selected item (either a curve point or a surface point).

    Args:
        position: (create) - Whether to set the locator position in normalized space.
    """
    pass


def parent(*args, absolute: bool = bool, addObject: bool = bool, noConnections: bool = bool, noInvScale: bool = bool, relative: bool = bool, removeObject: bool = bool, shape: bool = bool, world: bool = bool):
    """
    This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.

    Args:
        absolute: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) If the object to parent is a joint, it will alter the translation and joint orientation of the joint to preserve the world object transformation if this suffices. Otherwise, a transform will be inserted between the joint and the parent for this purpose. In this case, the transformation inside the joint is not altered. [default]
        addObject: (create) - preserve existing local object transformations but don't reparent, just add the object(s) under the parent. Use -world to add the world as a parent of the given objects.
        noConnections: (create) - The parent command will normally generate new instanced set connections when adding instances. (ie. make a connection to the shading engine for new instances) This flag suppresses this behaviour and is primarily used by the file format.
        noInvScale: (create) - The parent command will normally connect inverseScale to its parent scale on joints. This is used to compensate scale on joint. The connection of inverseScale will occur if both child and parent are joints and no connection is present on child's inverseScale. In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact. This flag suppresses this behaviour.
        relative: (create) - preserve existing local object transformations (relative to the parent node)
        removeObject: (create) - Remove the immediate parent of every object specified. To remove only a single instance of a shape from a parent, the path to the shape should be specified. Note: if there is a single parent then the object is effectively deleted from the scene. Use -world to remove the world as a parent of the given object.
        shape: (create) - The parent command usually only operates on transforms.  Using this flags allows a shape that is specified to be directly parented under the given transform.  This is used to instance a shape node. (ie. "parent -add -shape"    is equivalent to the "instance" command). This flag is primarily used by the file format.
        world: (create) - unparent given object(s) (parent to world)
    """
    pass


def partition(*args, addSet: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, removeSet: Optional[Union[str, bool]] = str, render: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command is used to create, query or add/remove sets to a partition. If a partition name needs to be specified, it is the first argument, other arguments represent the set names.

    Args:
        addSet: (create) - Adds the list of sets to the named partition.
        name: (create) - Assigns the given name to new partition. Valid only for create mode.
        removeSet: (create) - Removes the list of sets from the named partition.
        render: (create, query) - New partition can contain render sets. For use in creation mode only. Default is false.  Can also be used with query flag - returns boolean.
    """
    pass


def performanceOptions(*args, clusterResolution: Optional[Union[float, bool]] = float, disableStitch: Optional[Union[str, bool]] = str, disableTrimBoundaryDisplay: Optional[Union[str, bool]] = str, disableTrimDisplay: Optional[Union[str, bool]] = str, latticeResolution: Optional[Union[float, bool]] = float, passThroughBindSkinAndFlexors: Optional[Union[str, bool]] = str, passThroughBlendShape: Optional[Union[str, bool]] = str, passThroughCluster: Optional[Union[str, bool]] = str, passThroughDeltaMush: Optional[Union[str, bool]] = str, passThroughFlexors: Optional[Union[str, bool]] = str, passThroughLattice: Optional[Union[str, bool]] = str, passThroughMeshBoolean: Optional[Union[str, bool]] = str, passThroughPaintEffects: Optional[Union[str, bool]] = str, passThroughSculpt: Optional[Union[str, bool]] = str, passThroughWire: Optional[Union[str, bool]] = str, regionOfEffect: Optional[Union[str, bool]] = str, skipHierarchyTraversal: bool = bool, useClusterResolution: Optional[Union[str, bool]] = str, useLatticeResolution: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    Sets the global performance options for the application.  The options allow the disabling of features such as stitch surfaces or deformers to cut down on computation time in the scene.

    Args:
        clusterResolution: (query) - Sets the global cluster resolution.  This value may range between 0.0 (exact calculation) and 10.0 (rough approximation)
        disableStitch: (query) - Sets the state of stitch surface disablement.  Setting this to "on" suppresses the generation of stitch surfaces. Valid values are "on", "off", "interactive".
        disableTrimBoundaryDisplay: (query) - Sets the state of trim boundary drawing disablement.  Setting this to "on" suppresses the drawing of surface trim boundaries. Valid values are "on", "off", "interactive".
        disableTrimDisplay: (query) - Sets the state of trim drawing disablement.  Setting this to "on" suppresses the drawing of surface trims. Valid values are "on", "off", "interactive".
        latticeResolution: (query) - Sets the global lattice resolution.  This value may range between 0.0 (exact calculation) and 1.0 (rough approximation)
        passThroughBindSkinAndFlexors: (query) - Sets the state of bind skin and all flexors pass through. Valid values are "on", "off", "interactive".
        passThroughBlendShape: (query) - Sets the state of blend shape deformer pass through. Valid values are "on", "off", "interactive".
        passThroughCluster: (query) - Sets the state of cluster deformer pass through. Valid values are "on", "off", "interactive".
        passThroughDeltaMush: (query) - Sets the state of delta mush deformer pass through. Valid values are "on", "off", "interactive".
        passThroughFlexors: (query) - Sets the state of flexor pass through. Valid values are "on", "off", "interactive".
        passThroughLattice: (query) - Sets the state of lattice deformer pass through. Valid values are "on", "off", "interactive".
        passThroughMeshBoolean: (query) - Sets the state of mesh booleans pass through. Valid values are "on", "off", "interactive".
        passThroughPaintEffects: (query) - Sets the state of paint effects pass through. Valid values are "on", "off", "interactive".
        passThroughSculpt: (query) - Sets the state of sculpt deformer pass through. Valid values are "on", "off", "interactive".
        passThroughWire: (query) - Sets the state of wire deformer pass through. Valid values are "on", "off", "interactive".
        regionOfEffect: (query) - When enabled, an interactive update of translation commands will attempt to determine which components are being changed and only update effected components as a performance optimization while dragging a manip.
        skipHierarchyTraversal: (query) - When enabled, hierarchy traversal of invisible objects in the scene will be disabled in order to increase performance however this has a side effect of performing redundant viewport refreshes on certain actions such as manipulations, start/end of playback, idle refresh calls, etc.
        useClusterResolution: (query) - Sets the state of cluster deformer global resolution.  This allows clusters to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
        useLatticeResolution: (query) - Sets the state of lattice deformer global resolution.  This allows lattices to be calculated at a lower resolution. Valid values are "on", "off", "interactive".
    """
    pass


def pickWalk(*args, direction: Optional[Union[str, bool]] = str, recurse: bool = bool, type: Optional[Union[str, bool]] = str):
    """
    The pickWalk command allows you to quickly change the selection list relative to the nodes that are currently selected. It is called pickWalk, because it walks from one selection list to another by unselecting what's currently selected, and selecting nodes that are in the specified direction from the currently selected list. If you specify objects on the command line, the pickWalk command will walk from those objects instead of the selected list.

    Args:
        direction: (create) - The direction to walk from the node. The choices are up | down | left | right | in | out. up walks to the parent node, down to the child node, and left and right to the sibling nodes. If a CV on a surface is selected, the left and right directions walk in the U parameter direction of the surface, and the up and down directions walk in the V parameter direction. In and out are only used if the type flag is 'latticepoints'. Default is right.
        recurse: (create) - If specified then recurse down when walking
        type: (create) - The choices are nodes | instances | edgeloop | edgering | faceloop | keys | latticepoints | motiontrailpoints. If type is nodes, then the left and right direction walk to the next dag siblings. If type is instances, the left and right direction walk to the previous or next instance of the same dag node. If type is edgeloop, then the edge loop starting at the first selected edge will be selected. If type is edgering, then the edge ring starting at the first selected edge will be selected. If type is faceloop, and there are two connected quad faces selected which define a face loop, then that face loop will be selected.  edgeloop, edgering and faceloop all remember which was the first edge or faces selected for as long as consecutive selections are made by this command.  They use this information to determine what the "next" loop or ring selection should be.  Users can make selections forwards and backwards by using the direction flag with "left" or "right".  If type is motiontrailpoints, then the left and right direction walk to the previous or next motion trail points respectively.  Default is nodes.
    """
    pass


def pixelMove(*args):
    """
    The pixelMove command moves objects by what appears as pixel units based on the current view. It takes two integer arguments which specify the direction in screen space an object should appear to move. The vector between the center pixel of the view and the specified offset is mapped to some world space vector which defines the relative amount to move the selected objects. The mapping is dependent upon the view.

    Args:
    """
    pass


def polyAppendFacetCtx(*args, append: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, isRotateAvailable: bool = bool, maximumNumberOfPoints: Optional[Union[int, bool]] = int, planarConstraint: bool = bool, rotate: Optional[Union[float, bool]] = float, subdivision: Optional[Union[int, bool]] = int, texture: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Create a new context to append facets on polygonal objects

    Args:
        append: (create, edit, query) - Allows to switch to polyCreateFacetCtx tool
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        isRotateAvailable: (query) - Tells if the control associated to rotate flag is available. If several edges are already selected and they are not aligned (thus there is no "rotation axis") the rotation is no longer available.
        maximumNumberOfPoints: (create, edit, query) - Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        planarConstraint: (create, edit, query) - Allows/avoid new facet to be non-planar. If on, all new points will be projected onto current facet plane. Selected edges will be checked as well.
        rotate: (create, edit, query) - Rotate current facet around the first edge selected.
        subdivision: (create, edit, query) - Number of sub-edges created for each new edge. Default is 1.
        texture: (create, edit, query) - Number of textures. Default is 1.
    """
    pass


def polyCreaseCtx(*args, createSet: str = str, exists: bool = bool, extendSelection: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, relative: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Create a new context to crease components on polygonal objects

    Args:
        createSet: (edit) - Creates a set for the selected components.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        extendSelection: (create, edit, query) - Enable/disable extending selection to all connected creased components.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        relative: (create, edit, query) - Enable/disable applying value relative to existing crease value. If disabled, absolute value is applied.
    """
    pass


def polyCreateFacetCtx(*args, append: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, maximumNumberOfPoints: Optional[Union[int, bool]] = int, planarConstraint: bool = bool, subdivision: Optional[Union[int, bool]] = int, texture: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Create a new context to create polygonal objects

    Args:
        append: (create, edit, query) - Allows to switch to polyAppendFacetCtx tool
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        maximumNumberOfPoints: (create, edit, query) - Allows the ability to set a upper bound on the number of points in interactively place before polygon is created. A value less than 2 will mean that there is no upper bound.
        planarConstraint: (create, edit, query) - allows/avoid new facet to be non-planar. If on, all new points will be projected onto current facet plane.
        subdivision: (create, edit, query) - Number of subdivisions for each edge. Default: 1
        texture: (create, edit, query) - What texture mechanism to be applied 0=No textures, 1=Normalized, Undistorted textures 2=Unitized textures Default: 0
    """
    pass


def polyCutCtx(*args, deleteFaces: bool = bool, exists: bool = bool, extractFaces: bool = bool, extractOffset: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create a new context to cut facets on polygonal objects

    Args:
        deleteFaces: (create, edit, query) - whether to delete the one-half of the cut-faces of the poly.  If true, they are deleted. Default: false
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        extractFaces: (create, edit, query) - whether to extract the cut-faces of the poly into a separate shell.  If true, they are extracted. Default: false
        extractOffset: (create, edit, query) - The displacement offset of the cut faces. Default: 0.5, 0.5, 0.5
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def polyCutUVCtx(*args, loopSpeed: Optional[Union[int, bool]] = int, mapBordersColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), showCheckerMap: bool = bool, showTextureBorders: bool = bool, showUVShellColoring: bool = bool, steadyStroke: bool = bool, steadyStrokeDistance: Optional[Union[float, bool]] = float, symmetry: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Create a new context to cut UVs on polygonal objects

    Args:
        loopSpeed: (edit, query) - Edit the speed of loop cutting.
        mapBordersColor: (edit, query) - Color of UV map border edges in 3d view.
        showCheckerMap: (edit, query) - Display checker map.
        showTextureBorders: (edit, query) - Display texture border edges.
        showUVShellColoring: (edit, query) - Turn on UV shell coloring or not.
        steadyStroke: (edit, query) - Turn on steady stroke or not.
        steadyStrokeDistance: (edit, query) - The distance for steady stroke.
        symmetry: (edit, query) - Symmetric modeling.
    """
    pass


def polyMergeEdgeCtx(*args, activeNodes: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, immediate: bool = bool, name: Optional[Union[str, bool]] = str, previous: bool = bool, reset: bool = bool, toolNode: bool = bool, caching: bool = bool, constructionHistory: bool = bool, firstEdge: Optional[Union[int, bool]] = int, mergeMode: Optional[Union[int, bool]] = int, mergeTexture: bool = bool, nodeState: Optional[Union[int, bool]] = int, secondEdge: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Sews two border edges together.

    Args:
        activeNodes: (query) - Return the active nodes in the tool
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        immediate: (edit) - Acts on the object not the tool defaults
        name: (create) - If this is a tool command, name the tool appropriately.
        previous: (edit) - Reset to previously stored values
        reset: (edit) - Reset to default values
        toolNode: (query) - Return the node used for tool defaults
        caching: (create, edit, query) - Toggle caching for all attributes so that no recomputation is needed
        constructionHistory: (create, query) - Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.  Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        firstEdge: (create, edit, query) - First edge to merge. Invalid default value to force the value to be set. Default: -1
        mergeMode: (create, edit, query) - Merge mode : 0=first, 1=halfway between both edges, 2=second. Default: 1
        mergeTexture: (create, edit, query) - Boolean which is used to decide if uv coordinates should be merged or not - along with the geometry. Default: false
        nodeState: (create, edit, query) - Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.    The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.    The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute.  Additional details about each of these 3 states follow.     State Description   Normal The normal node state. This is the default.   HasNoEffect   The HasNoEffect option (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.   It’s typical to implement support for the HasNoEffect state in the node’s compute method and to perform appropriate operations. Plug-ins can also support HasNoEffect.   The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state leaves the input geometry undeformed on the output.     Blocking   This is implemented in the depend node base class and applies to all nodes. Blocking is applied during the evaluation phase to connections. An evaluation request to a blocked connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.   When a node is set to Blocking the behavior is supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond to getAttr requests but a getAttr on a downstream node will not reevaluate the blocked node.   Setting the root transform of a hierarchy to Blocking won’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes to the Blocking state.   For example, to set all child transforms to Blocking, you could use the following script.    import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )    Applying this script would continue to draw objects but things would not be animated.     Default: kdnNormal
        secondEdge: (create, edit, query) - Second edge to merge. Invalid default value to force the value to be set. Default: -1
    """
    pass


def polyMergeFacetCtx(*args, activeNodes: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, immediate: bool = bool, name: Optional[Union[str, bool]] = str, previous: bool = bool, reset: bool = bool, toolNode: bool = bool, caching: bool = bool, constructionHistory: bool = bool, firstFacet: Optional[Union[int, bool]] = int, mergeMode: Optional[Union[int, bool]] = int, nodeState: Optional[Union[int, bool]] = int, secondFacet: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    The second face becomes a hole in the first face.

    Args:
        activeNodes: (query) - Return the active nodes in the tool
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        immediate: (edit) - Acts on the object not the tool defaults
        name: (create) - If this is a tool command, name the tool appropriately.
        previous: (edit) - Reset to previously stored values
        reset: (edit) - Reset to default values
        toolNode: (query) - Return the node used for tool defaults
        caching: (create, edit, query) - Toggle caching for all attributes so that no recomputation is needed
        constructionHistory: (create, query) - Turn the construction history on or off (where applicable). If construction history is on then the corresponding node will be inserted into the history chain for the mesh. If construction history is off then the operation will be performed directly on the object.  Note: If the object already has construction history then this flag is ignored and the node will always be inserted into the history chain.
        firstFacet: (create, edit, query) - The number of the first (outer) face to merge.
        mergeMode: (create, edit, query) - This flag specifies how faces are merged: 0: moves second face to first one 1: moves both faces to average 2: moves first face to second one 3, 4, 5: same as above, except faces are projected but not centred 6: Nothing moves. C: Default is None (6).
        nodeState: (create, edit, query) - Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1), and Blocking (2) states can be used to alter how the graph is evaluated.    The Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5) are for internal use only. They temporarily shut off parts of the graph during interaction (e.g., manipulation). The understanding is that once the operation is done, the state will be reset appropriately, e.g. Waiting-Blocking will reset back to Blocking.    The Normal and Blocking cases apply to all nodes, while HasNoEffect is node specific; many nodes do not support this option. Plug-ins store state in the MPxNode::state attribute. Anyone can set it or check this attribute.  Additional details about each of these 3 states follow.     State Description   Normal The normal node state. This is the default.   HasNoEffect   The HasNoEffect option (a.k.a. pass-through), is used in cases where there is an operation on an input producing an output of the same data type. Nearly all deformers support this state, as do a few other nodes. As stated earlier, it is not supported by all nodes.   It’s typical to implement support for the HasNoEffect state in the node’s compute method and to perform appropriate operations. Plug-ins can also support HasNoEffect.   The usual implementation of this state is to copy the input directly to the matching output without applying the algorithm in the node. For deformers, applying this state leaves the input geometry undeformed on the output.     Blocking   This is implemented in the depend node base class and applies to all nodes. Blocking is applied during the evaluation phase to connections. An evaluation request to a blocked connection will return as failures, causing the destination plug to retain its current value. Dirty propagation is indirectly affected by this state since blocked connections are never cleaned.   When a node is set to Blocking the behavior is supposed to be the same as if all outgoing connections were broken. As long as nobody requests evaluation of the blocked node directly it won’t evaluate after that. Note that a blocked node will still respond to getAttr requests but a getAttr on a downstream node will not reevaluate the blocked node.   Setting the root transform of a hierarchy to Blocking won’t automatically influence child transforms in the hierarchy. To do this, you’d need to explicitly set all child nodes to the Blocking state.   For example, to set all child transforms to Blocking, you could use the following script.    import maya.cmds as cmds def blockTree(root): nodesToBlock = [] for node in {child:1 for child in cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock += cmds.listConnections(node, source=True, destination=True ) for node in {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' % node, 2 )    Applying this script would continue to draw objects but things would not be animated.     Default: kdnNormal
        secondFacet: (create, edit, query) - The number of the second (hole) face to merge.
    """
    pass


def polySelectCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, mode: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Create a new context to select polygon components

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mode: (create, edit, query) - Edge loop or Edge ring or Border edge mode
    """
    pass


def polySelectEditCtx(*args, adjustEdgeFlow: Optional[Union[float, bool]] = float, divisions: Optional[Union[int, bool]] = int, exists: bool = bool, fixQuads: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, insertWithEdgeFlow: bool = bool, smoothingAngle: Optional[Union[float, bool]] = float, splitType: Optional[Union[int, bool]] = int, useEqualMultiplier: bool = bool, absoluteOffset: bool = bool, autoComplete: bool = bool, deleteEdge: bool = bool, endVertexOffset: Optional[Union[float, bool]] = float, mode: Optional[Union[int, bool]] = int, startVertexOffset: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    Create a new context to select and edit polygonal objects

    Args:
        adjustEdgeFlow: (create, edit, query) - The weight value of the edge vertices to be positioned. Default: 1.0f
        divisions: (create, edit, query) - Number of divisions. Default: 2
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        fixQuads: (create, edit, query) - Fixes splits which go across a quad face leaving a 5 and 3 sided faces by splitting from the middle of the new edge to the vertex accross from the edge on the 5 sided face. Default: false
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        insertWithEdgeFlow: (create, edit, query) - True to enable edge flow. Otherwise, the edge flow is disabled. Default: false
        smoothingAngle: (create, edit, query) - Angle below which new edges will be smoothed Default: kPi
        splitType: (create, edit, query) - Format: 0 - Absolute, 1 - Relative, 2 - Multi Default: TdnpolySplitRing::Relative
        useEqualMultiplier: (create, edit, query) - Changes how the profile curve effects the offset when doing a multisplit.  If true then the verts will be offset the same distance based on the shortest edge being split.  If false then each inserted edge loop will be offset a distance relative to the length of the edge that is being split. Default: true
        absoluteOffset: (create, edit, query) - This flag is deprecated. Use splitType/stp instead. This flag is deprecated. Use splitType/stp instead.
        autoComplete: (create) - If true then use auto completion on selections
        deleteEdge: (create, edit, query) - When true, the end edges are deleted so the end triangles are converted to quads.
        endVertexOffset: (create, edit, query) - Weight value controlling the offset of the end vertex of the edgeloop.
        mode: (create, edit, query) - which mode to work on.  Available modes are 1-loop and 2-ring
        startVertexOffset: (create, edit, query) - Weight value controlling the offset of the start vertex of the edgeloop.
    """
    pass


def polyShortestPathCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the 3d viewport.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def polySplitCtx(*args, enablesnap: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, magnetsnap: Optional[Union[int, bool]] = int, precsnap: Optional[Union[float, bool]] = float, smoothingangle: Optional[Union[float, bool]] = float, snaptoedge: bool = bool, subdivision: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    Create a new context to split facets on polygonal objects

    Args:
        enablesnap: (create, edit, query) - Enable/disable custom magnet snapping to start/middle/end of edge
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        magnetsnap: (create, edit, query) - number of extra magnets to snap onto, regularly spaced along the edge
        precsnap: (create, edit, query) - precision for custom magnet snapping. Range[0,100]. Value 100 means any click on an edge will snap to either extremities or magnets.
        smoothingangle: (create, edit, query) - the threshold that controls whether newly created edges are hard or soft
        snaptoedge: (create, edit, query) - Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.
        subdivision: (create, edit, query) - number of sub-edges to add between 2 consecutive edge points. Default is 1.
    """
    pass


def polySplitCtx2(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, adjustEdgeFlow: Optional[Union[float, bool]] = float, constrainToEdges: bool = bool, edgeMagnets: Optional[Union[int, bool]] = int, insertWithEdgeFlow: bool = bool, snapTolerance: Optional[Union[float, bool]] = float, snappedToEdgeColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), snappedToFaceColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), snappedToMagnetColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), snappedToVertexColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), edit: bool = bool, query: bool = bool):
    """
    Create a new context to split facets on polygonal objects

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        adjustEdgeFlow: (create, edit, query) - The weight value of the edge vertices to be positioned.
        constrainToEdges: (create, edit, query) - Enable/disable snapping to edge. If enabled any click in the current face will snap to the closest valid edge. If there is no valid edge, the click will be ignored. NOTE: This is different from magnet snapping, which causes the click to snap to certain points along the edge.
        edgeMagnets: (create, edit, query) - number of extra magnets to snap onto, regularly spaced along the edge
        insertWithEdgeFlow: (create, edit, query) - True to enable edge flow. Otherwise, the edge flow is disabled.
        snapTolerance: (create, edit, query) - precision for custom magnet snapping. Range[0,1]. Value 1 means any click on an edge will snap to either extremities or magnets.
        snappedToEdgeColor: (create, edit, query) - Color for edge snapping.
        snappedToFaceColor: (create, edit, query) - Color for face snapping.
        snappedToMagnetColor: (create, edit, query) - Color for magnet snapping.
        snappedToVertexColor: (create, edit, query) - Color for vertex snapping.
    """
    pass


def projectionContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Set the context for projection manips

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def propModCtx(*args, animCurve: Optional[Union[str, bool]] = str, animCurveFalloff: Optional[Union[Tuple[float, float], bool]] = [float, float], animCurveParam: Optional[Union[str, bool]] = str, direction: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, linear: Optional[Union[float, bool]] = float, linearParam: Optional[Union[Tuple[float, float], bool]] = [float, float], nurbsCurve: Optional[Union[str, bool]] = str, powerCutoff: Optional[Union[float, bool]] = float, powerCutoffParam: Optional[Union[Tuple[float, float], bool]] = [float, float], powerDegree: Optional[Union[float, bool]] = float, powerDegreeParam: Optional[Union[float, bool]] = float, script: Optional[Union[str, bool]] = str, scriptParam: Optional[Union[str, bool]] = str, type: Optional[Union[int, bool]] = int, worldspace: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Controls the proportional move context.

    Args:
        animCurve: (create, edit, query) - Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds".  The profile of the curve will be used as the profile for propmod function.
        animCurveFalloff: (create, edit, query) - The profile of the curve will be used as the profile for propmod function in both U and V. This will be scaled in U, V according to the paramters provided. The ratio of the U, V scaling parameters will dictate the footprint of the fuction while the curve itself provides the magnitudes.
        animCurveParam: (create, edit, query) - Name of the anim curve to use as a drop-off curve. Only the 0 -> side of the curve will be used and the distance will be mapped to "seconds", where 1 second maps to 0.01 units in parametric space.
        direction: (create, edit, query) - Direction along which to compute the distance for the distance based drop-off functions.  The default is (1 1 1)
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        linear: (create, edit, query) - If using linear drop-off function, this is its slope.  The default of -0.1 means the point at the locator moves with it and the point 10 units away doesn't move at all.
        linearParam: (create, edit, query) - If using parametric linear drop-off function, these specify its limits along the U and V directions.
        nurbsCurve: (create, edit, query) - Name of the nurbs curve to use as a drop-off curve. The closest point distance would be used as the drop off percentage.
        powerCutoff: (create, edit, query) - If using the power drop-off function, this is its distance cutoff value.  The default is 10.0.
        powerCutoffParam: (create, edit, query) - If using the power drop-off function, these specify one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.
        powerDegree: (create, edit, query) - If using the power drop-off function, this is its degree.  The default is 3.
        powerDegreeParam: (create, edit, query) - If using the power drop-off function, this is its degree.  The default is 3.
        script: (create, edit, query) - The name of the script to use to compute the drop-off. The script takes 6 floats as input - first 3 are the position of the move locator, the next 3 the position of the point to be manipulated.  The script should return a drop-off coefficient which could be negative or zero.
        scriptParam: (create, edit, query) - The name of the script to use to compute the drop-off. The script takes 4 floats as input - first 2 are the parametric position of the move locator, the next 2 the parametric position of the point to be manipulated.  The script should return a drop-off coefficient which could be negative or zero.
        type: (create, edit, query) - Choose the type for the drop-off function.  Legal values are 1 for linear, 2 for power, 3 for script, 4 for anim curve. The default is 1.
        worldspace: (create, edit, query) - Set the space in which the tool works. True for world space, false for parametric space.
    """
    pass


def quit(*args, abort: bool = bool, exitCode: Optional[Union[int, bool]] = int, force: bool = bool):
    """
    This command is used to exit the application.

    Args:
        abort: (create) - Will quit without saving like -force, but will also prevent preferences/hotkeys/colors from being saved.  Use at your own risk.
        exitCode: (create) - Specifies the exit code to be returned once the application exits.  The default exit code is 0.
        force: (create) - If specified, this flag will force a quit without saving or prompting for saving changes. Use at your own risk.
    """
    pass


def regionSelectKeyCtx(*args, bottomManip: Optional[Union[float, bool]] = float, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, leftManip: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, rightManip: Optional[Union[float, bool]] = float, topManip: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the region select tool.

    Args:
        bottomManip: (query) - Get a point located inside the bottom manipulator of the region box, in screen space.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        leftManip: (query) - Get a point located inside the left manipulator of the region box, in screen space.
        name: (create) - If this is a tool command, name the tool appropriately.
        rightManip: (query) - Get a point located inside the right manipulator of the region box, in screen space.
        topManip: (query) - Get a point located inside the top manipulator of the region box, in screen space.
    """
    pass


def relationship(*args, b: bool = bool, relationshipData: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This is primarily for use with file IO. Rather than write out the specific attributes/connections required to maintain a relationship, a description of the related nodes/plugs is written instead. The relationship must have an owner node, and have a specific type. During file read, maya will make the connections and/or set the data necessary to represent the realtionship in the dependency graph.

    Args:
        b: (create, edit, query) - Break the specified relationship instead of creating it
        relationshipData: (create, edit, multiuse, query) - Provide relationship data to be used when creating the relationship.
    """
    pass


def rememberCtxSettings(*args):
    """
    This command restores a tool to its saved settings. This command must only be called once for each tool created and should be called at the point the tool is created.

    Args:
    """
    pass


def removeMultiInstance(*args, allChildren: bool = bool, b: bool = bool):
    """
    Removes a particular instance of a multiElement. This is only useful for input attributes since outputs will get regenerated the next time the node gets executed. This command will remove the instance and optionally break all incoming and outgoing connections to that instance. If the connections are not broken (with the -b true) flag, then the command will fail if connections exist.

    Args:
        allChildren: (create) - If the argument is true, remove all children of the multi parent.
        b: (create) - If the argument is true, all connections to the attribute will be broken before the element is removed. If false, then the command will fail if the element is connected.
    """
    pass


def rename(*args, ignoreShape: bool = bool, uuid: bool = bool):
    """
    Renames the given object to have the new name. If only one argument is supplied the command will rename the (first) selected object. If the new name conflicts with an existing name, the object will be given a unique name based on the supplied name. It is not legal to rename an object to the empty string.

    Args:
        ignoreShape: (create) - Indicates that renaming of shape nodes below transform nodes should be prevented.
        uuid: (create) - Indicates that the new name is actually a UUID, and that the command should change the node's UUID. (In which case its name remains unchanged.)
    """
    pass


def renameAttr(*args):
    """
    Renames the given user-defined attribute to the name given in the string argument. If the new name conflicts with an existing name then this command will fail. Note that it is not legal to rename an attribute to the empty string.

    Args:
    """
    pass


def renderWindowSelectContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Set the selection context for the render view panel.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def reorder(*args, back: bool = bool, front: bool = bool, relative: Optional[Union[int, bool]] = int):
    """
    This command reorders (moves) objects relative to their siblings.

    Args:
        back: (create) - Move object(s) to back of sibling list.
        front: (create) - Move object(s) to front of sibling list.
        relative: (create) - Move object(s) relative to other siblings.
    """
    pass


def reorderContainer(*args, back: bool = bool, front: bool = bool, relative: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    This command reorders (moves) objects relative to their siblings in a container.

    Args:
        back: (create, edit, query) - Move object(s) to back of container contents list
        front: (create, edit, query) - Move object(s) to front of container contents list
        relative: (create, edit, query) - Move object(s) relative to other container contents
    """
    pass


def resetTool(*args):
    """
    This command resets a tool back to its "factory settings"

    Args:
    """
    pass


def retimeKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, moveByFrame: int = int, name: Optional[Union[str, bool]] = str, snapOnFrame: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the retime tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        moveByFrame: (edit) - Move the selected retime bar by the specified number of frames
        name: (create) - If this is a tool command, name the tool appropriately.
        snapOnFrame: (edit, query) - When set, the retime markers will snap on frames as they are moved.
    """
    pass


def rollCtx(*args, alternateContext: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, rollScale: Optional[Union[float, bool]] = float, toolName: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create, edit, or query a roll context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        rollScale: (create, edit, query) - In degrees of rotation per 100 pixels of cursor drag.
        toolName: (create, query) - Name of the specific tool to which this command refers.
    """
    pass


def rotate(*args, absolute: bool = bool, centerPivot: bool = bool, componentSpace: bool = bool, constrainAlongNormal: bool = bool, deletePriorHistory: bool = bool, euler: bool = bool, forceOrderXYZ: bool = bool, objectCenterPivot: bool = bool, objectSpace: bool = bool, orientAxes: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], pivot: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], preserveChildPosition: bool = bool, preserveGeometryPosition: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAboutBBox: bool = bool, reflectionAboutOrigin: bool = bool, reflectionAboutX: bool = bool, reflectionAboutY: bool = bool, reflectionAboutZ: bool = bool, reflectionTolerance: Optional[Union[float, bool]] = float, relative: bool = bool, rotateX: bool = bool, rotateXY: bool = bool, rotateXYZ: bool = bool, rotateXZ: bool = bool, rotateY: bool = bool, rotateYZ: bool = bool, rotateZ: bool = bool, symNegative: bool = bool, translate: bool = bool, worldSpace: bool = bool, xformConstraint: Optional[Union[str, bool]] = str):
    """
    The rotate command is used to change the rotation of geometric objects. The rotation values are specified as Euler angles (rx, ry, rz). The values are interpreted based on the current working unit for Angular measurements. Most often this is degrees.

    Args:
        absolute: (create) - Perform an absolute operation.
        centerPivot: (create) - Let the pivot be the center of the bounding box of all objects
        componentSpace: (create) - Rotate in local component space
        constrainAlongNormal: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory: (create) - If true then delete the history prior to the current operation.
        euler: (create) - Modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        forceOrderXYZ: (create) - When true, euler rotation value will be understood in XYZ rotation order not per transform node basis.
        objectCenterPivot: (create) - Let the pivot be the center of the bounding box of each object
        objectSpace: (create) - Perform rotation about object-space axis.
        orientAxes: (create) - Euler axis for orientation.
        pivot: (create) - Define the pivot point for the transformation
        preserveChildPosition: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV: (create) - When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative: (create) - Perform a operation relative to the object's current position
        rotateX: (create) - Rotate in X direction
        rotateXY: (create) - Rotate in X and Y direction
        rotateXYZ: (create) - Rotate in all directions (default)
        rotateXZ: (create) - Rotate in X and Z direction
        rotateY: (create) - Rotate in Y direction
        rotateYZ: (create) - Rotate in Y and Z direction
        rotateZ: (create) - Rotate in Z direction
        symNegative: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        translate: (create) - When true, the command will modify the node's translate attribute instead of its rotateTranslate attribute, when rotating around a pivot other than the object's own rotate pivot.
        worldSpace: (create) - Perform rotation about global world-space axis.
        xformConstraint: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    pass


def saveToolSettings(*args):
    """
    This command causes all the tools not on the shelf to save their settings as optionVars.  This is called automatically by the system when Maya exits.

    Args:
    """
    pass


def scale(*args, absolute: bool = bool, centerPivot: bool = bool, componentSpace: bool = bool, constrainAlongNormal: bool = bool, deletePriorHistory: bool = bool, distanceOnly: bool = bool, localSpace: bool = bool, objectCenterPivot: bool = bool, objectSpace: bool = bool, orientAxes: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], pivot: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], preserveChildPosition: bool = bool, preserveGeometryPosition: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAboutBBox: bool = bool, reflectionAboutOrigin: bool = bool, reflectionAboutX: bool = bool, reflectionAboutY: bool = bool, reflectionAboutZ: bool = bool, reflectionTolerance: Optional[Union[float, bool]] = float, relative: bool = bool, scaleX: bool = bool, scaleXY: bool = bool, scaleXYZ: bool = bool, scaleXZ: bool = bool, scaleY: bool = bool, scaleYZ: bool = bool, scaleZ: bool = bool, symNegative: bool = bool, worldSpace: bool = bool, xformConstraint: Optional[Union[str, bool]] = str):
    """
    The scale command is used to change the sizes of geometric objects.

    Args:
        absolute: (create) - Perform an absolute operation.
        centerPivot: (create) - Let the pivot be the center of the bounding box of all objects
        componentSpace: (create) - Move in local component space
        constrainAlongNormal: (create) - When true, transform constraints are applied along the vertex normal first and only use the closest point when no intersection is found along the normal.
        deletePriorHistory: (create) - If true then delete the history prior to the current operation.
        distanceOnly: (create) - Scale only the distance between the objects.
        localSpace: (create) - Use local space for scaling
        objectCenterPivot: (create) - Let the pivot be the center of the bounding box of each object
        objectSpace: (create) - Use object space for scaling
        orientAxes: (create) - Use the angles for the orient axes.
        pivot: (create) - Define the pivot point for the transformation
        preserveChildPosition: (create) - When true, transforming an object will apply an opposite transform to its child transform to keep them at the same world-space position. Default is false.
        preserveGeometryPosition: (create) - When true, transforming an object will apply an opposite transform to its geometry points to keep them at the same world-space position. Default is false.
        preserveUV: (create) - When true, UV values on scaled components are projected along the axis of scaling in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative: (create) - Perform a operation relative to the object's current position
        scaleX: (create) - Scale in X direction
        scaleXY: (create) - Scale in X and Y direction
        scaleXYZ: (create) - Scale in all directions (default)
        scaleXZ: (create) - Scale in X and Z direction
        scaleY: (create) - Scale in Y direction
        scaleYZ: (create) - Scale in Y and Z direction
        scaleZ: (create) - Scale in Z direction
        symNegative: (create) - When set the component transformation is flipped so it is relative to the negative side of the symmetry plane. The default (no flag) is to transform components relative to the positive side of the symmetry plane.
        worldSpace: (create) - Use world space for scaling
        xformConstraint: (create) - Apply a transform constraint to moving components.  none - no constraint surface - constrain components to the surface edge - constrain components to surface edges live - constraint components to the live surface
    """
    pass


def scaleComponents(*args, pivot: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], rotation: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float]):
    """
    This is a limited version of the scale command.  First, it only works on selected components. You provide a pivot in world space, and you can provide a rotation.  This rotation affects the scaling, so that rather than scaling in X, Y, Z, this is scaling in X, Y, and Z after they have been rotated by the given rotation.

    Args:
        pivot: (create) - The pivot position in world space (default is origin)
        rotation: (create) - The rotational offset for the scaling (default is none)
    """
    pass


def scaleKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, scaleSpecifiedKeys: bool = bool, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to scale keyframes within the graph editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        scaleSpecifiedKeys: (edit, query) - Determines if only the specified keys should be scaled. If false, the non-selected keys will be adjusted during the scale. The default is true.
        type: (edit, query) - rect | manip Specifies the type of scale manipulator to use (Note: "rect" is a manipulator style context, and "manip" is a gestural style context)
    """
    pass


def sceneLint(*args, issueType: Optional[Union[str, bool]] = str, verbose: bool = bool, query: bool = bool):
    """
    { "sceneLint" : { "ISSUE_CODE" : { "description" : "DETAILED_DESCRIPTION_OF_ISSUE", "mitigation" : [        // List of mitigations that can be applied { "objects"     : [ LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ], "benefit"     : DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER, "description" : DESCRIPTION_OF_WHAT_THE_CODE_DOES, "code"        : PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES } ] } } }

    Args:
        issueType: (create, multiuse, query) - Specify a set of issue types to be checked. If omitted then all known issue types are checked. In query mode returns a description of what a particular issue type is checking. 			In query mode, this flag can accept a value.
        verbose: (create, query) - If set then include both name and description when querying the list of available issue types.
    """
    pass


def scriptCtx(*args, allComponents: bool = bool, allObjects: bool = bool, animBreakdown: bool = bool, animCurve: bool = bool, animInTangent: bool = bool, animKeyframe: bool = bool, animOutTangent: bool = bool, baseClassName: Optional[Union[str, bool]] = str, camera: bool = bool, cluster: bool = bool, collisionModel: bool = bool, controlVertex: bool = bool, cumulativeLists: bool = bool, curve: bool = bool, curveKnot: bool = bool, curveOnSurface: bool = bool, curveParameterPoint: bool = bool, dimension: bool = bool, dynamicConstraint: bool = bool, edge: bool = bool, editPoint: bool = bool, emitter: bool = bool, enableRootSelection: bool = bool, escToQuit: bool = bool, exists: bool = bool, exitUponCompletion: bool = bool, expandSelectionList: bool = bool, facet: bool = bool, field: bool = bool, finalCommandScript: Optional[Union[str, bool]] = str, fluid: bool = bool, follicle: bool = bool, forceAddSelect: bool = bool, hairSystem: bool = bool, handle: bool = bool, history: bool = bool, hull: bool = bool, ignoreInvalidItems: bool = bool, ikEndEffector: bool = bool, ikHandle: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, imagePlane: bool = bool, implicitGeometry: bool = bool, isoparm: bool = bool, joint: bool = bool, jointPivot: bool = bool, lastAutoComplete: bool = bool, lattice: bool = bool, latticePoint: bool = bool, light: bool = bool, localRotationAxis: bool = bool, locator: bool = bool, locatorUV: bool = bool, locatorXYZ: bool = bool, nCloth: bool = bool, nParticle: bool = bool, nParticleShape: bool = bool, nRigid: bool = bool, name: Optional[Union[str, bool]] = str, nonlinear: bool = bool, nurbsCurve: bool = bool, nurbsSurface: bool = bool, objectComponent: bool = bool, orientationLocator: bool = bool, particle: bool = bool, particleShape: bool = bool, plane: bool = bool, polymesh: bool = bool, polymeshEdge: bool = bool, polymeshFace: bool = bool, polymeshFreeEdge: bool = bool, polymeshUV: bool = bool, polymeshVertex: bool = bool, polymeshVtxFace: bool = bool, rigidBody: bool = bool, rigidConstraint: bool = bool, rotatePivot: bool = bool, scalePivot: bool = bool, sculpt: bool = bool, selectHandle: bool = bool, setAllowExcessCount: bool = bool, setAutoComplete: bool = bool, setAutoToggleSelection: bool = bool, setDoneSelectionPrompt: Optional[Union[str, bool]] = str, setNoSelectionHeadsUp: Optional[Union[str, bool]] = str, setNoSelectionPrompt: Optional[Union[str, bool]] = str, setSelectionCount: Optional[Union[int, bool]] = int, setSelectionHeadsUp: Optional[Union[str, bool]] = str, setSelectionPrompt: Optional[Union[str, bool]] = str, showManipulators: bool = bool, spring: bool = bool, springComponent: bool = bool, stroke: bool = bool, subdiv: bool = bool, subdivMeshEdge: bool = bool, subdivMeshFace: bool = bool, subdivMeshPoint: bool = bool, subdivMeshUV: bool = bool, surfaceEdge: bool = bool, surfaceFace: bool = bool, surfaceKnot: bool = bool, surfaceParameterPoint: bool = bool, surfaceRange: bool = bool, surfaceUV: bool = bool, texture: bool = bool, title: Optional[Union[str, bool]] = str, toolCursorType: Optional[Union[str, bool]] = str, toolFinish: Optional[Union[str, bool]] = str, toolStart: Optional[Union[str, bool]] = str, totalSelectionSets: Optional[Union[int, bool]] = int, vertex: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command allows a user to create their own tools based on the selection tool. A number of selection lists can be collected, the behaviour of the selection and the selection masks are fully customizable, etc.

    Args:
        allComponents: (create, multiuse, query) - Set all component selection masks on/off
        allObjects: (create, multiuse, query) - Set all object selection masks on/off
        animBreakdown: (create, multiuse, query) - Set animation breakdown selection mask on/off.
        animCurve: (create, multiuse, query) - Set animation curve selection mask on/off.
        animInTangent: (create, multiuse, query) - Set animation in-tangent selection mask on/off.
        animKeyframe: (create, multiuse, query) - Set animation keyframe selection mask on/off.
        animOutTangent: (create, multiuse, query) - Set animation out-tangent selection mask on/off.
        baseClassName: (create, edit, query) - This string will be used to produce MEL function names for the property sheets for the tool.  For example, if "myScriptTool" was given, the functions "myScriptToolValues" and "myScriptToolProperties" will be used for the property sheets.  The default is "scriptTool".
        camera: (create, multiuse, query) - Set camera selection mask on/off. (object flag)
        cluster: (create, multiuse, query) - Set cluster selection mask on/off. (object flag)
        collisionModel: (create, multiuse, query) - Set collision model selection mask on/off. (object flag)
        controlVertex: (create, multiuse, query) - Set control vertex selection mask on/off. (component flag)
        cumulativeLists: (create, edit, query) - If set, the selection lists will be cumulative.  For example, the second list will contain all the items from the first list, the third all the items from the second list etc.  Make sure your script specified above takes that into account.  Relevant if there is more than one selection set.
        curve: (create, multiuse, query) - Set curve selection mask on/off. (object flag)
        curveKnot: (create, multiuse, query) - Set curve knot selection mask on/off. (component flag)
        curveOnSurface: (create, multiuse, query) - Set curve-on-surface selection mask on/off. (object flag)
        curveParameterPoint: (create, multiuse, query) - Set curve parameter point selection mask on/off. (component flag)
        dimension: (create, multiuse, query) - Set dimension shape selection mask on/off. (object flag)
        dynamicConstraint: (create, multiuse, query) - Set dynamicConstraint selection mask on/off. (object flag)
        edge: (create, multiuse, query) - Set mesh edge selection mask on/off. (component flag)
        editPoint: (create, multiuse, query) - Set edit-point selection mask on/off. (component flag)
        emitter: (create, multiuse, query) - Set emitter selection mask on/off. (object flag)
        enableRootSelection: (create, edit, query) - If set, the items to be selected are at their root transform level. Default is false.
        escToQuit: (create, edit, query) - If set to true, exit the tool when press "Esc". Default is false.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        exitUponCompletion: (create, edit, query) - If set, completing the last selection set will exit the tool.  Default is true.
        expandSelectionList: (create, edit, query) - If set, the selection lists will expand to have a single component in each item.  You probably want this as a default, otherwise two isoparms on the same surface will show up as 1 item.  To ensure that components on the same object are returned in the order in which they are selected, use the selectPref -trackSelectionOrder on command in your -toolStart script to enable ordered selection, then restore it to its original value in your -toolFinish script.
        facet: (create, multiuse, query) - Set mesh face selection mask on/off. (component flag)
        field: (create, multiuse, query) - Set field selection mask on/off. (object flag)
        finalCommandScript: (create, edit, query) - Supply the script that will be run when the user presses the enter key and the context is completed.  Depending on the number of selection sets you have, the script can make use of variables string $Selection1[], $Selection2[], ...
        fluid: (create, multiuse, query) - Set fluid selection mask on/off. (object flag)
        follicle: (create, multiuse, query) - Set follicle selection mask on/off. (object flag)
        forceAddSelect: (create, edit, query) - If set to true, together with -setAutoToggleSelection (see below) on the first selection set, causes the first selection after the computation of the previous result to be "shift" selection, unless a modifier key is pressed.  Default is false. Flags for each selection set.  These flags are multi-use.
        hairSystem: (create, multiuse, query) - Set hairSystem selection mask on/off. (object flag)
        handle: (create, multiuse, query) - Set object handle selection mask on/off. (object flag)
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        hull: (create, multiuse, query) - Set hull selection mask on/off. (component flag)
        ignoreInvalidItems: (create, edit, query) - If you have multiple selection sets, the state of the selection set is recorded at the time you "complete it".  You could then delete some of the items in that list and end up with invalid items in one or more of your selection sets.  If this flag is set, those items will be detected and ignored.  You will never know it happened.  Its as if they were never selected in the first place, except that your selection set now does not have as many items as it may need.  If this flag is not set, you will get a warning and your final command callback script will likely not execute because of an error condition.
        ikEndEffector: (create, multiuse, query) - Set ik end effector selection mask on/off. (object flag)
        ikHandle: (create, multiuse, query) - Set ik handle selection mask on/off. (object flag)
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        imagePlane: (create, multiuse, query) - Set image plane selection mask on/off. (component flag)
        implicitGeometry: (create, multiuse, query) - Set implicit geometry selection mask on/off. (object flag)
        isoparm: (create, multiuse, query) - Set surface iso-parm selection mask on/off. (component flag)
        joint: (create, multiuse, query) - Set ik handle selection mask on/off. (object flag)
        jointPivot: (create, multiuse, query) - Set joint pivot selection mask on/off. (component flag)
        lastAutoComplete: (create, edit, query) - True if auto complete is set for the last selection set, false otherwise.  Mostly used for query, but if present in conjuction with -sac/setAutoComplete flag, -sac flag takes precedence.
        lattice: (create, multiuse, query) - Set lattice selection mask on/off. (object flag)
        latticePoint: (create, multiuse, query) - Set lattice point selection mask on/off. (component flag)
        light: (create, multiuse, query) - Set light selection mask on/off. (object flag)
        localRotationAxis: (create, multiuse, query) - Set local rotation axis selection mask on/off. (component flag)
        locator: (create, multiuse, query) - Set locator (all types) selection mask on/off. (object flag)
        locatorUV: (create, multiuse, query) - Set uv locator selection mask on/off. (object flag)
        locatorXYZ: (create, multiuse, query) - Set xyz locator selection mask on/off. (object flag)
        nCloth: (create, multiuse, query) - Set nCloth selection mask on/off. (object flag)
        nParticle: (create, multiuse, query) - Set nParticle point selection mask on/off. (component flag)
        nParticleShape: (create, multiuse, query) - Set nParticle shape selection mask on/off. (object flag)
        nRigid: (create, multiuse, query) - Set nRigid selection mask on/off. (object flag)
        name: (create) - If this is a tool command, name the tool appropriately.
        nonlinear: (create, multiuse, query) - Set nonlinear selection mask on/off. (object flag)
        nurbsCurve: (create, multiuse, query) - Set nurbs-curve selection mask on/off. (object flag)
        nurbsSurface: (create, multiuse, query) - Set nurbs-surface selection mask on/off. (object flag)
        objectComponent: (create, query) - Component flags apply to object mode.
        orientationLocator: (create, multiuse, query) - Set orientation locator selection mask on/off. (object flag)
        particle: (create, multiuse, query) - Set particle point selection mask on/off. (component flag)
        particleShape: (create, multiuse, query) - Set particle shape selection mask on/off. (object flag)
        plane: (create, multiuse, query) - Set sketch plane selection mask on/off. (object flag)
        polymesh: (create, multiuse, query) - Set poly-mesh selection mask on/off. (object flag)
        polymeshEdge: (create, multiuse, query) - Set poly-mesh edge selection mask on/off. (component flag)
        polymeshFace: (create, multiuse, query) - Set poly-mesh face selection mask on/off. (component flag)
        polymeshFreeEdge: (create, multiuse, query) - Set poly-mesh free-edge selection mask on/off. (component flag)
        polymeshUV: (create, multiuse, query) - Set poly-mesh UV point selection mask on/off. (component flag)
        polymeshVertex: (create, multiuse, query) - Set poly-mesh vertex selection mask on/off. (component flag)
        polymeshVtxFace: (create, multiuse, query) - Set poly-mesh vertexFace selection mask on/off. (component flag)
        rigidBody: (create, multiuse, query) - Set rigid body selection mask on/off. (object flag)
        rigidConstraint: (create, multiuse, query) - Set rigid constraint selection mask on/off. (object flag)
        rotatePivot: (create, multiuse, query) - Set rotate pivot selection mask on/off. (component flag)
        scalePivot: (create, multiuse, query) - Set scale pivot selection mask on/off. (component flag)
        sculpt: (create, multiuse, query) - Set sculpt selection mask on/off. (object flag)
        selectHandle: (create, multiuse, query) - Set select handle selection mask on/off. (component flag)
        setAllowExcessCount: (create, edit, multiuse) - If set, the number if items is to be interpreted as the minimum.
        setAutoComplete: (create, edit, multiuse) - If set to true, as soon as the specified number of items is selected the tool will start the next selection set or run the command.
        setAutoToggleSelection: (create, edit, multiuse) - If set to true, it is as if "shift" key is pressed when there are no modifiers pressed.  That means that you get the "toggle select" behaviour by default.  This only applies to the 3D view, and the selection done in the hypergraph, outliner or elsewhere is still a subject to the usual rules.
        setDoneSelectionPrompt: (create, edit, multiuse) - If setAutoComplete is not set (see below) this string will be shown as soon as the tool has enough items for a particular selection set.  If this is not set, but is needed, the same string as set with -setSelectionPrompt flag will be used.
        setNoSelectionHeadsUp: (create, edit, multiuse) - Supply a string that will be shown as a heads up prompt when there is nothing selected.  This must be set separately for each selection set.
        setNoSelectionPrompt: (create, edit, multiuse) - Supply a string that will be shown as help when there is nothing selected.  This must be set separately for each selection set.
        setSelectionCount: (create, edit, multiuse) - The number of items in this selection set.  0 means as many as you need until completion.
        setSelectionHeadsUp: (create, edit, multiuse) - Supply a string that will be shown as a heads up prompt when there is something selected.  This must be set separately for each selection set.
        setSelectionPrompt: (create, edit, multiuse) - Supply a string that will be shown as help when there is something selected.  This must be set separately for each selection set.
        showManipulators: (create, edit, query) - If set, the manipulators will be shown for any active objects. Basically, it is as if you are in the Show Manipulator tool.
        spring: (create, multiuse, query) - Set spring shape selection mask on/off. (object flag)
        springComponent: (create, multiuse, query) - Set individual spring selection mask on/off. (component flag)
        stroke: (create, multiuse, query) - Set the Paint Effects stroke selection mask on/off. (object flag)
        subdiv: (create, multiuse, query) - Set subdivision surfaces selection mask on/off. (object flag)
        subdivMeshEdge: (create, multiuse, query) - Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        subdivMeshFace: (create, multiuse, query) - Set subdivision surfaces mesh face selection mask on/off. (component flag)
        subdivMeshPoint: (create, multiuse, query) - Set subdivision surfaces mesh point selection mask on/off. (component flag)
        subdivMeshUV: (create, multiuse, query) - Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        surfaceEdge: (create, multiuse, query) - Set surface edge selection mask on/off. (component flag)
        surfaceFace: (create, multiuse, query) - Set surface face selection mask on/off. (component flag)
        surfaceKnot: (create, multiuse, query) - Set surface knot selection mask on/off. (component flag)
        surfaceParameterPoint: (create, multiuse, query) - Set surface parameter point selection mask on/off. (component flag)
        surfaceRange: (create, multiuse, query) - Set surface range selection mask on/off. (component flag)
        surfaceUV: (create, multiuse, query) - Set surface uv selection mask on/off. (component flag)
        texture: (create, multiuse, query) - Set texture selection mask on/off. (object flag)
        title: (create, edit, query) - Supply a string that will be used as a precursor to all the messages; i.e., the "name" of the tool.
        toolCursorType: (create, edit, query) - Supply the string identifier to set the tool cursor type when inside of tool. The following are the valid ids: "create", "dolly", "edit", "pencil", "track", "trackHorizontal", "trackVertical", "transformation", "tumble", "zoom", "zoomIn", "zoomOut", "flyThrough", "dot", "fleur", "leftArrow", "question", "doubleHorizArrow", "doubleVertArrow", "sizing", "dollyIn", "dollyOut", "brush", "camera", "noAccess", "input", "output", "leftCycle", "rightCycle", "rightExpand", "knife".
        toolFinish: (create, edit, query) - Supply the script that will be run when the user exits the script.
        toolStart: (create, edit, query) - Supply the script that will be run when the user first enters the script
        totalSelectionSets: (create, edit, query) - Total number of selection sets.
        vertex: (create, multiuse, query) - Set mesh vertex selection mask on/off. (component flag)
    """
    pass


def sculptMeshCacheChangeCloneSource(*args, blendShape: Optional[Union[str, bool]] = str, target: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command changes the source blend shape and target for the clone target tool. Used internally for undo/redo, and should not be called directly.

    Args:
        blendShape: (create, edit, query) - Set which blend shape should be used as the source when using the clone tool. When queried, returns the current blend shape name as a string.
        target: (create, edit, query) - Set which blend shape should be used as the target when using the clone tool. When queried, returns the current blend shape target name as a string.
    """
    pass


def sculptMeshCacheCtx(*args, adjustSize: bool = bool, adjustStrength: bool = bool, affectAllLayers: bool = bool, brushDirection: Optional[Union[int, bool]] = int, brushSize: Optional[Union[float, bool]] = float, brushStrength: Optional[Union[float, bool]] = float, buildUpRate: Optional[Union[float, bool]] = float, cloneHideSource: bool = bool, cloneMethod: Optional[Union[int, bool]] = int, cloneShapeSource: Optional[Union[str, bool]] = str, cloneTargetSource: Optional[Union[str, bool]] = str, constrainToSurface: bool = bool, direction: Optional[Union[int, bool]] = int, displayFrozen: bool = bool, displayMask: bool = bool, displayWireframe: bool = bool, falloffType: Optional[Union[int, bool]] = int, flood: Optional[Union[float, bool]] = float, floodFreeze: Optional[Union[float, bool]] = float, frame: bool = bool, freezeSelection: bool = bool, grabFollowPath: bool = bool, grabSilhouette: bool = bool, grabTwist: bool = bool, inverted: bool = bool, lastMode: Optional[Union[str, bool]] = str, lockShellBorder: bool = bool, makeStroke: Tuple[int, int, int, float, float] = [int, int, int, float, float], minSize: Optional[Union[float, bool]] = float, minStrength: Optional[Union[float, bool]] = float, mirror: Optional[Union[int, bool]] = int, mode: Optional[Union[str, bool]] = str, orientToSurface: bool = bool, recordStroke: bool = bool, sculptFalloffCurve: Optional[Union[str, bool]] = str, size: Optional[Union[float, bool]] = float, stampDistance: Optional[Union[float, bool]] = float, stampFile: Optional[Union[str, bool]] = str, stampFlipX: bool = bool, stampFlipY: bool = bool, stampOrientToStroke: bool = bool, stampPlacement: Optional[Union[int, bool]] = int, stampRandomization: bool = bool, stampRandomizationSeed: int = int, stampRandomizeFlipX: bool = bool, stampRandomizeFlipY: bool = bool, stampRandomizePosX: Optional[Union[float, bool]] = float, stampRandomizePosY: Optional[Union[float, bool]] = float, stampRandomizeRotation: Optional[Union[float, bool]] = float, stampRandomizeScale: Optional[Union[float, bool]] = float, stampRandomizeStrength: Optional[Union[float, bool]] = float, stampRotation: Optional[Union[float, bool]] = float, steadyStrokeDistance: Optional[Union[float, bool]] = float, strength: Optional[Union[float, bool]] = float, updatePlane: bool = bool, useGlobalSize: bool = bool, useScreenSpace: bool = bool, useStampDistance: bool = bool, useStampImage: bool = bool, useSteadyStroke: bool = bool, wholeStroke: bool = bool, wireframeAlpha: Optional[Union[float, bool]] = float, wireframeColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), edit: bool = bool, query: bool = bool):
    """
    This is a tool context command for mesh cache sculpting tool.

    Args:
        adjustSize: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        adjustStrength: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        affectAllLayers: (create, edit, query) - If true, the brush affects all layers at once.
        brushDirection: (edit, query) - Specifies the direction of the named brush.
        brushSize: (edit, query) - Specifies the world-space size of the named brush.
        brushStrength: (edit, query) - Specifies the world-space strength of the named brush.
        buildUpRate: (edit, query) - Specifies the brush strength increasing along the stroke.
        cloneHideSource: (create, edit, query) - True if the cloned source should be hidden.
        cloneMethod: (create, edit, query) - Controls how the source delta vectors should change the target. 0=copy 1=add
        cloneShapeSource: (create, edit, query) - Name of the shape source to clone.
        cloneTargetSource: (create, edit, query) - Name of the target source of the clone.
        constrainToSurface: (create, edit, query) - If true, the modification keeps the surface curvature.
        direction: (edit, query) - Specifies the direction in which the vertices are moved.
        displayFrozen: (create, edit, query) - If false, turns off the display of frozen area on the object.
        displayMask: (create, edit, query) - If false, turns off the display of masked area on the object.
        displayWireframe: (create, edit, query) - If false, turns off the wireframe display of the object.
        falloffType: (edit, query) - Specifies how the brush determines which vertices to affect.
        flood: (create, edit) - Sets the brush effect for each vertex to the given value.
        floodFreeze: (create, edit) - Sets the freeze value for each vertex to the given value.
        frame: (create, edit) - Frames on the sculpted area.
        freezeSelection: (create, edit) - Freezes selected components.
        grabFollowPath: (create, edit, query) - If true, the grab brush effect follows mouse movement.
        grabSilhouette: (create, edit, query) - If true, the grab brush uses paint-through mode.
        grabTwist: (create, edit, query) - If true, the grab brush twists the vertices.
        inverted: (create, edit, query) - If true, inverts the effect of the brush.
        lastMode: (edit, query) - Specifies the type of the last active sculpting brush.
        lockShellBorder: (create, edit, query) - Lock the shell borders so that they won't be moved by a UV texture brush.
        makeStroke: (edit, multiuse) - Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke. The first argument is the mesh index. The second argument is the side index. use 0 for the original side, and 1 for the mirrored side The third argument is the face index within the specified mesh. The fourth and fifth arguments are the face coordinates within the specified face.
        minSize: (edit, query) - Specifies the minimum size percentage of the current brush.
        minStrength: (edit, query) - Specifies the minimum strength percentage of the current brush.
        mirror: (edit, query) - Specifies the mirror mode of the brush.
        mode: (edit, query) - Specifies the type of sculpting effect the brush will perform.
        orientToSurface: (create, edit, query) - If true, aligns the brush display to the surface of the mesh.
        recordStroke: (edit, query) - Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.
        sculptFalloffCurve: (edit, query) - Specifies the falloff curve of sculpting effect the brush will perform.
        size: (edit, query) - Specifies the world-space size of the current brush.
        stampDistance: (edit, query) - Specifies the stamping distance of the brush.
        stampFile: (edit, query) - Specifies an image file to use as stamp.
        stampFlipX: (create, edit, query) - Specifies if the brush stamp is flipped on the X axis.
        stampFlipY: (create, edit, query) - Specifies if the brush stamp is flipped on the Y axis.
        stampOrientToStroke: (create, edit, query) - Specifies if the brush stamp is aligned to the stroke direction.
        stampPlacement: (edit, query) - Specifies the placement mode of the stamp image.
        stampRandomization: (create, edit, query) - Specifies if the brush stamp is randomized.
        stampRandomizationSeed: (edit) - Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.
        stampRandomizeFlipX: (create, edit, query) - Specifies if the brush stamp flipping is randomized on the X axis.
        stampRandomizeFlipY: (create, edit, query) - Specifies if the brush stamp flipping is randomized on the Y axis.
        stampRandomizePosX: (edit, query) - Specifies the stamp X position value is randomized.
        stampRandomizePosY: (edit, query) - Specifies the stamp Y position value is randomized.
        stampRandomizeRotation: (edit, query) - Specifies the stamp rotation value is randomized.
        stampRandomizeScale: (edit, query) - Specifies the stamp scale value is randomized.
        stampRandomizeStrength: (edit, query) - Specifies the stamp strength value is randomized.
        stampRotation: (edit, query) - Specifies the rotation value of the stamp image.
        steadyStrokeDistance: (edit, query) - Specifies the distance for the steady stroke.
        strength: (edit, query) - Specifies the world-space strength of the current brush.
        updatePlane: (create, edit, query) - Recalculates the underlying tool plane for each stamp in a stroke.
        useGlobalSize: (create, edit, query) - If true, all the brushes have a shared size property; otherwise size is local.
        useScreenSpace: (create, edit, query) - If true, the brush size is in screen space pixels.
        useStampDistance: (create, edit, query) - Force the stamps to be spread out along the stroke, rather than building up continually.
        useStampImage: (create, edit, query) - Specifies if the brush uses a stamp image.
        useSteadyStroke: (create, edit, query) - Turns using steady stroke on/off.
        wholeStroke: (create, edit, query) - Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.
        wireframeAlpha: (create, edit, query) - Sets the alpha value of the wireframe for the object that is being sculpted.
        wireframeColor: (create, edit, query) - Sets the color of the wireframe for the object that is being sculpted. Values should be 0-1 RGB.
    """
    pass


def select(*args, add: bool = bool, addFirst: bool = bool, all: bool = bool, allDagObjects: bool = bool, allDependencyNodes: bool = bool, clear: bool = bool, containerCentric: bool = bool, deselect: bool = bool, hierarchy: bool = bool, noExpand: bool = bool, replace: bool = bool, symmetry: bool = bool, symmetrySide: Optional[Union[int, bool]] = int, toggle: bool = bool, visible: bool = bool):
    """
    This command is used to put objects onto or off of the active list. If none of the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to replace the objects on the active list with the given list of objects.

    Args:
        add: (create) - Indicates that the specified items should be added to the active list without removing existing items from the active list.
        addFirst: (create) - Indicates that the specified items should be added to the front of the active list without removing existing items from the active list.
        all: (create) - Indicates that all deletable root level dag objects and all deletable non-dag dependency nodes should be selected.
        allDagObjects: (create) - Indicates that all deletable root level dag objects should be selected.
        allDependencyNodes: (create) - Indicates that all deletable dependency nodes including all deletable dag objects should be selected.
        clear: (create) - Clears the active list.  This is more efficient than "select -d;".  Also "select -d;" will not remove sets from the active list unless the "-ne" flag is also specified.
        containerCentric: (create) - Specifies that the same selection rules as apply to selection in the main viewport will also be applied to the select command. In particular, if the specified objects are members of a black-boxed container and are not published as nodes, Maya will not select them. Instead, their first parent valid for selection will be selected.
        deselect: (create) - Indicates that the specified items should be removed from the active list if they are on the active list.
        hierarchy: (create) - Indicates that all children, grandchildren, ... of the specified dag objects should also be selected.
        noExpand: (create) - Indicates that any set which is among the specified items should not be expanded to its list of members. This allows sets to be selected as opposed to the members of sets which is the default behaviour.
        replace: (create) - Indicates that the specified items should replace the existing items on the active list.
        symmetry: (create) - Specifies that components should be selected symmetrically using the current symmetricModelling command settings. If symmetric modeling is not enabled then this flag has no effect.
        symmetrySide: (create) - Indicates that components involved in the current symmetry object should be selected, according to the supplied parameter. Valid values for the parameter are: -1 : Select components in the unsymmetrical region. 0 : Select components on the symmetry seam. 1 : Select components on side 1. 2 : Select components on side 2. If symmetric modeling is not enabled then this flag has no effect. Note: currently only works for topological symmetry.
        toggle: (create) - Indicates that those items on the given list which are on the active list should be removed from the active list and those items on the given list which are not on the active list should be added to the active list.
        visible: (create) - Indicates that of the specified items only those that are visible should be affected.
    """
    pass


def selectContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Creates a context to perform selection.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def selectKey(*args, addTo: bool = bool, animation: Optional[Union[str, bool]] = str, attribute: Optional[Union[str, bool]] = str, clear: bool = bool, controlPoints: bool = bool, float: Optional[Union[Tuple[float, float], bool]] = [float, float], hierarchy: Optional[Union[str, bool]] = str, inTangent: bool = bool, includeUpperBound: bool = bool, index: Optional[Union[int, bool]] = int, keyframe: bool = bool, outTangent: bool = bool, remove: bool = bool, replace: bool = bool, shape: bool = bool, time: Optional[Union[Tuple[float, float], bool]] = [float, float], toggle: bool = bool, unsnappedKeys: Optional[Union[float, bool]] = float):
    """
    This command operates on a keyset.  A keyset is defined as a group of keys within a specified time range on one or more animation curves.

    Args:
        addTo: (create) - Add to the current selection of keyframes/tangents
        animation: (create) - Where this command should get the animation to act on.  Valid values are "objects," "keys," and "keysOrObjects" Default: "keysOrObjects."  (See Description for details.)
        attribute: (create, multiuse) - List of attributes to select       In query mode, this flag needs a value.
        clear: (create) - Remove all keyframes and tangents from the active list.
        controlPoints: (create) - This flag explicitly specifies whether or not to include the control points of a shape (see "-s" flag) in the list of attributes. Default: false.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        float: (create, multiuse) - value uniquely representing a non-time-based key (or key range) on a time-based animCurve.  Valid floatRange include single values (-f 10) or a string with a lower and upper bound, separated by a colon (-f "10:20")       In query mode, this flag needs a value.
        hierarchy: (create) - Hierarchy expansion options.  Valid values are "above," "below," "both," and "none." (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        inTangent: (create) - Select in-tangents of keyframes in the specified time range
        includeUpperBound: (create) - When the -t/time or -f/float flags represent a range of keys, this flag determines whether the keys at the upper bound of the range are included in the keyset. Default value: true.  This flag is only valid when the argument to the -t/time flag is a time range with a lower and upper bound.  (When used with the "pasteKey" command, this flag refers only to the time range of the target curve that is replaced, when using options such as "replace," "fitReplace," or "scaleReplace."  This flag has no effect on the curve pasted from the clipboard.)
        index: (create, multiuse) - index of a key on an animCurve       In query mode, this flag needs a value.
        keyframe: (create) - select only keyframes (cannot be combined with -in/-out)
        outTangent: (create) - Select out-tangents of keyframes in the specified time range
        remove: (create) - Remove from the current selection of keyframes/tangents
        replace: (create) - Replace the current selection of keyframes/tangents
        shape: (create) - Consider attributes of shapes below transforms as well, except "controlPoints".  Default: true.  (Not valid for "pasteKey" cmd.) In query mode, this flag needs a value.
        time: (create, multiuse) - time uniquely representing a key (or key range) on a time-based animCurve. See the code examples below on how to format for a single frame or frame ranges.       In query mode, this flag needs a value.
        toggle: (create) - Toggle the picked state of the specified keyset
        unsnappedKeys: (create) - Select only keys that have times that are not a multiple of the specified numeric value.
    """
    pass


def selectKeyCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to select keyframes within the graph editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def selectKeyframeRegionCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def selectMode(*args, component: bool = bool, hierarchical: bool = bool, leaf: bool = bool, object: bool = bool, preset: bool = bool, root: bool = bool, template: bool = bool, query: bool = bool):
    """
    The

    Args:
        component: (create, query) - Set component selection on. Component selection mode allows filtered selection based on the component selection mask. The component selection mask is the set of selection masks related to objects that indicate which components are selectable.
        hierarchical: (create, query) - Set hierarchical selection on. There are three types of hierarchical selection: root, leaf and template.  Hierarchical mode is set if root, leaf or template mode is set. Setting to hierarchical mode will set the mode to whichever of root, leaf, or template was last on.
        leaf: (create, query) - Set leaf selection mode on.  This mode allows the leaf level objects to be selected.  It is similar to object selection mode but ignores the object selection mask.
        object: (create, query) - Set object selection on. Object selection mode allows filtered selection based on the object selection mask. The object selection mask is the set of selection masks related to objects that indicate which objects are selectable.  The masks are controlled by the "selectType" command.  Object selection mode selects the leaf level objects.
        preset: (create, query) - Allow selection of anything with the mask set, independent of it being an object or a component.
        root: (create, query) - Set root selection mode on.  This mode allows the root of a hierarchy to be selected by selecting any of its descendents.  It ignores the object selection mask.
        template: (create, query) - Set template selection mode on.  This mode allows selection of templated objects.  It selects the templated object closest to the root of the hierarchy.
    """
    pass


def selectPref(*args, affectsActive: bool = bool, allowHiliteSelection: bool = bool, autoSelectContainer: bool = bool, autoSelectOutlinerSetMembers: bool = bool, autoUseDepth: bool = bool, clickBoxSize: Optional[Union[int, bool]] = int, clickDrag: bool = bool, containerCentricSelection: bool = bool, disableComponentPopups: bool = bool, expandPopupList: bool = bool, ignoreSelectionPriority: bool = bool, manipClickBoxSize: Optional[Union[int, bool]] = int, paintSelect: bool = bool, paintSelectWithDepth: bool = bool, popupMenuSelection: bool = bool, preSelectBackfacing: bool = bool, preSelectClosest: bool = bool, preSelectDeadSpace: Optional[Union[int, bool]] = int, preSelectHilite: bool = bool, preSelectHiliteSize: Optional[Union[float, bool]] = float, preSelectTweakDeadSpace: Optional[Union[int, bool]] = int, selectTypeChangeAffectsActive: bool = bool, selectionChildHighlightMode: Optional[Union[int, bool]] = int, singleBoxSelection: bool = bool, straightLineDistance: bool = bool, trackSelectionOrder: bool = bool, useDepth: bool = bool, xformNoSelect: bool = bool, query: bool = bool):
    """
    This command controls state variables used to selection UI behavior.

    Args:
        affectsActive: (create, query) - Set affects-active toggle which when on causes the active list to be affected when changing between object and component selection mode.
        allowHiliteSelection: (create, query) - When in component selection mode, allow selection of objects for editing.  If an object is selected for editing, it appears in the hilite color and its selectable components are automatically displayed.
        autoSelectContainer: (query) - When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.
        autoSelectOutlinerSetMembers: (query) - When enabled selecting a set in the Outliner will automatically select the set members instead.
        autoUseDepth: (query) - When enabled, useDepth and paintSelectWithDepth will be automatically enabled in shaded display mode and disabled in wireframe display mode.
        clickBoxSize: (create, query) - When click selecting, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.
        clickDrag: (create, query) - Set click/drag selection interaction on/off
        containerCentricSelection: (query) - When enabled, selecting any DAG node in a container in the viewport will select the container's root transform if there is one.  If there is no root transform then the highest DAG node in the container will be selected.  There is no effect when selecting nodes which are not in a container.
        disableComponentPopups: (create, query) - A separate preference to allow users to disable popup menus when selecting components.  This pref is only meaningful if the popupMenuSelection pref is enabled.
        expandPopupList: (create, query) - When in popup selection mode, if this is set then all selection items that contain multiple objects or components will be be expanded such that each object or component will be a single new selection item.
        ignoreSelectionPriority: (create, query) - If this is set, selection priority will be ignored when performing selection.
        manipClickBoxSize: (create, query) - When selecting a manipulator, this value defines the size of square picking region surrounding the cursor. The size of the square is twice the specified value. That is, the value defines the amount of space on all four sides of the cursor position. The size must be positive.
        paintSelect: (query) - When enabled, the select tool will use drag selection instead of marquee selection.
        paintSelectWithDepth: (query) - When enabled, paint selection will not select components that are behind the surface in the current camera view.
        popupMenuSelection: (create, query) - If this is set, a popup menu will be displayed and used to determine the object to select. The menu lists the current user box (marquee) of selected candidate objects.
        preSelectBackfacing: (query) - When enabled preselection will highlight backfacing components whose normals face away from the camera.
        preSelectClosest: (query) - When enabled and the cursor is over a surface, preselection highlighting will try to preselect the closest component to the cursor regardless of distance.
        preSelectDeadSpace: (query) - This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface.
        preSelectHilite: (query) - When enabled, the closest component under the cursor will be highlighted to indicate that clicking will select that component.
        preSelectHiliteSize: (query) - This value defines the size of the region around the cursor used for preselection highlighting. Within this region the closest component to the cursor will be highlighted.
        preSelectTweakDeadSpace: (query) - This value defines the size of the region around the cursor used for preselection highlighting when the cursor is outside the surface in tweak mode.
        selectTypeChangeAffectsActive: (query) - If true then the active list will be updated according to the new selection preferences.
        selectionChildHighlightMode: (create, query) - Controls the highlighting of the children of a selected object. Valid modes are:  0: Always highlight children 1: Never highlight children 2: Use per-object "Selection Child Highlight" setting.  Default mode is (0): Always highlight children.  For (2), each DAG object has an individual "Selection Child Highlight" boolean flag. By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred to the selected object's "Selection Child Highlight" flag.
        singleBoxSelection: (create, query) - Set single box selection on/off. This flag indicates whether just single object will be selected when the user box (marquee) selects several objects if flag set to true.  Otherwise, all those objects inside the box will be selected.
        straightLineDistance: (query) - If true then use straight line distances for selection proximity.
        trackSelectionOrder: (query) - When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able to return the active list in the order of selection which will allow scripts to be written that depend on the order.
        useDepth: (query) - When enabled, marquee selection will not select components that are behind the surface in the current camera view.
        xformNoSelect: (create, query) - Disable selection in xform tools
    """
    pass


def selectPriority(*args, allComponents: Optional[Union[int, bool]] = int, allObjects: Optional[Union[int, bool]] = int, animBreakdown: Optional[Union[int, bool]] = int, animCurve: Optional[Union[int, bool]] = int, animInTangent: Optional[Union[int, bool]] = int, animKeyframe: Optional[Union[int, bool]] = int, animOutTangent: Optional[Union[int, bool]] = int, byName: Optional[Union[Tuple[str, bool], bool]] = [str, bool], camera: Optional[Union[int, bool]] = int, cluster: Optional[Union[int, bool]] = int, collisionModel: Optional[Union[int, bool]] = int, controlVertex: Optional[Union[int, bool]] = int, curve: Optional[Union[int, bool]] = int, curveKnot: Optional[Union[int, bool]] = int, curveOnSurface: Optional[Union[int, bool]] = int, curveParameterPoint: Optional[Union[int, bool]] = int, dimension: Optional[Union[int, bool]] = int, dynamicConstraint: Optional[Union[int, bool]] = int, edge: Optional[Union[int, bool]] = int, editPoint: Optional[Union[int, bool]] = int, emitter: Optional[Union[int, bool]] = int, facet: Optional[Union[int, bool]] = int, field: Optional[Union[int, bool]] = int, fluid: Optional[Union[int, bool]] = int, follicle: Optional[Union[int, bool]] = int, hairSystem: Optional[Union[int, bool]] = int, handle: Optional[Union[int, bool]] = int, hull: Optional[Union[int, bool]] = int, ikEndEffector: Optional[Union[int, bool]] = int, ikHandle: Optional[Union[int, bool]] = int, imagePlane: Optional[Union[int, bool]] = int, implicitGeometry: Optional[Union[int, bool]] = int, isoparm: Optional[Union[int, bool]] = int, joint: Optional[Union[int, bool]] = int, jointPivot: Optional[Union[int, bool]] = int, lattice: Optional[Union[int, bool]] = int, latticePoint: Optional[Union[int, bool]] = int, light: Optional[Union[int, bool]] = int, localRotationAxis: Optional[Union[int, bool]] = int, locator: Optional[Union[int, bool]] = int, locatorUV: Optional[Union[int, bool]] = int, locatorXYZ: Optional[Union[int, bool]] = int, meshUVShell: Optional[Union[int, bool]] = int, motionTrailPoint: Optional[Union[int, bool]] = int, motionTrailTangent: Optional[Union[int, bool]] = int, nCloth: Optional[Union[int, bool]] = int, nParticle: Optional[Union[int, bool]] = int, nParticleShape: Optional[Union[int, bool]] = int, nRigid: Optional[Union[int, bool]] = int, nonlinear: Optional[Union[int, bool]] = int, nurbsCurve: Optional[Union[int, bool]] = int, nurbsSurface: Optional[Union[int, bool]] = int, orientationLocator: Optional[Union[int, bool]] = int, particle: Optional[Union[int, bool]] = int, particleShape: Optional[Union[int, bool]] = int, plane: Optional[Union[int, bool]] = int, polymesh: Optional[Union[int, bool]] = int, polymeshEdge: Optional[Union[int, bool]] = int, polymeshFace: Optional[Union[int, bool]] = int, polymeshFreeEdge: Optional[Union[int, bool]] = int, polymeshUV: Optional[Union[int, bool]] = int, polymeshVertex: Optional[Union[int, bool]] = int, polymeshVtxFace: Optional[Union[int, bool]] = int, queryByName: Optional[Union[str, bool]] = str, rigidBody: Optional[Union[int, bool]] = int, rigidConstraint: Optional[Union[int, bool]] = int, rotatePivot: Optional[Union[int, bool]] = int, scalePivot: Optional[Union[int, bool]] = int, sculpt: Optional[Union[int, bool]] = int, selectHandle: Optional[Union[int, bool]] = int, spring: Optional[Union[int, bool]] = int, springComponent: Optional[Union[int, bool]] = int, stroke: Optional[Union[int, bool]] = int, subdiv: Optional[Union[int, bool]] = int, subdivMeshEdge: Optional[Union[int, bool]] = int, subdivMeshFace: Optional[Union[int, bool]] = int, subdivMeshPoint: Optional[Union[int, bool]] = int, subdivMeshUV: Optional[Union[int, bool]] = int, surfaceEdge: Optional[Union[int, bool]] = int, surfaceFace: Optional[Union[int, bool]] = int, surfaceKnot: Optional[Union[int, bool]] = int, surfaceParameterPoint: Optional[Union[int, bool]] = int, surfaceRange: Optional[Union[int, bool]] = int, texture: Optional[Union[int, bool]] = int, vertex: Optional[Union[int, bool]] = int, query: bool = bool):
    """
    The

    Args:
        allComponents: (create, query) - Set all component selection priority
        allObjects: (create, query) - Set all object selection priority
        animBreakdown: (create, query) - Set animation breakdown selection priority
        animCurve: (create, query) - Set animation curve selection priority
        animInTangent: (create, query) - Set animation in-tangent selection priority
        animKeyframe: (create, query) - Set animation keyframe selection priority
        animOutTangent: (create, query) - Set animation out-tangent selection priority
        byName: (create, multiuse) - Set selection priority for the specified user-defined selection type
        camera: (create, query) - Set camera selection priority
        cluster: (create, query) - Set cluster selection priority
        collisionModel: (create, query) - Set collision model selection priority
        controlVertex: (create, query) - Set control vertex selection priority
        curve: (create, query) - Set curve selection priority
        curveKnot: (create, query) - Set curve knot selection priority
        curveOnSurface: (create, query) - Set curve-on-surface selection priority
        curveParameterPoint: (create, query) - Set curve parameter point selection priority
        dimension: (create, query) - Set dimension shape selection priority
        dynamicConstraint: (create, query) - Set dynamicConstraint selection priority
        edge: (create, query) - Set mesh edge selection priority
        editPoint: (create, query) - Set edit-point selection priority
        emitter: (create, query) - Set emitter selection priority
        facet: (create, query) - Set mesh face selection priority
        field: (create, query) - Set field selection priority
        fluid: (create, query) - Set fluid selection priority
        follicle: (create, query) - Set follicle selection priority
        hairSystem: (create, query) - Set hairSystem selection priority
        handle: (create, query) - Set object handle selection priority
        hull: (create, query) - Set hull selection priority
        ikEndEffector: (create, query) - Set ik end effector selection priority
        ikHandle: (create, query) - Set ik handle selection priority
        imagePlane: (create, query) - Set image plane selection mask priority
        implicitGeometry: (create, query) - Set implicit geometry selection priority
        isoparm: (create, query) - Set surface iso-parm selection priority
        joint: (create, query) - Set ik handle selection priority
        jointPivot: (create, query) - Set joint pivot selection priority
        lattice: (create, query) - Set lattice selection priority
        latticePoint: (create, query) - Set lattice point selection priority
        light: (create, query) - Set light selection priority
        localRotationAxis: (create, query) - Set local rotation axis selection priority
        locator: (create, query) - Set locator (all types) selection priority
        locatorUV: (create, query) - Set uv locator selection priority
        locatorXYZ: (create, query) - Set xyz locator selection priority
        meshUVShell: (create, query) - Set uv shell component mask on/off.
        motionTrailPoint: (create, query) - Set motion point selection priority
        motionTrailTangent: (create, query) - Set motion point tangent priority
        nCloth: (create, query) - Set nCloth selection priority
        nParticle: (create, query) - Set nParticle point selection priority
        nParticleShape: (create, query) - Set nParticle shape selection priority
        nRigid: (create, query) - Set nRigid selection priority
        nonlinear: (create, query) - Set nonlinear selection priority
        nurbsCurve: (create, query) - Set nurbs-curve selection priority
        nurbsSurface: (create, query) - Set nurbs-surface selection priority
        orientationLocator: (create, query) - Set orientation locator selection priority
        particle: (create, query) - Set particle point selection priority
        particleShape: (create, query) - Set particle shape selection priority
        plane: (create, query) - Set sketch plane selection priority
        polymesh: (create, query) - Set poly-mesh selection priority
        polymeshEdge: (create, query) - Set poly-mesh edge selection priority
        polymeshFace: (create, query) - Set poly-mesh face selection priority
        polymeshFreeEdge: (create, query) - Set poly-mesh free-edge selection priority
        polymeshUV: (create, query) - Set poly-mesh UV point selection priority
        polymeshVertex: (create, query) - Set poly-mesh vertex selection priority
        polymeshVtxFace: (create, query) - Set poly-mesh vtxFace selection priority
        queryByName: (query) - Query selection priority for the specified user-defined selection type       In query mode, this flag needs a value.
        rigidBody: (create, query) - Set rigid body selection priority
        rigidConstraint: (create, query) - Set rigid constraint selection priority
        rotatePivot: (create, query) - Set rotate pivot selection priority
        scalePivot: (create, query) - Set scale pivot selection priority
        sculpt: (create, query) - Set sculpt selection priority
        selectHandle: (create, query) - Set select handle selection priority
        spring: (create, query) - Set spring shape selection priority
        springComponent: (create, query) - Set individual spring selection priority
        stroke: (create, query) - Set stroke selection priority
        subdiv: (create, query) - Set subdivision surface selection priority
        subdivMeshEdge: (create, query) - Set subdivision surface mesh edge selection priority
        subdivMeshFace: (create, query) - Set subdivision surface mesh face selection priority
        subdivMeshPoint: (create, query) - Set subdivision surface mesh point selection priority
        subdivMeshUV: (create, query) - Set subdivision surface mesh UV map selection priority
        surfaceEdge: (create, query) - Set surface edge selection priority
        surfaceFace: (create, query) - Set surface face selection priority
        surfaceKnot: (create, query) - Set surface knot selection priority
        surfaceParameterPoint: (create, query) - Set surface parameter point selection priority
        surfaceRange: (create, query) - Set surface range selection priority
        texture: (create, query) - Set texture selection priority
        vertex: (create, query) - Set mesh vertex selection priority
    """
    pass


def selectType(*args, allComponents: bool = bool, allObjects: bool = bool, animBreakdown: bool = bool, animCurve: bool = bool, animInTangent: bool = bool, animKeyframe: bool = bool, animOutTangent: bool = bool, byName: Optional[Union[Tuple[str, bool], bool]] = [str, bool], camera: bool = bool, cluster: bool = bool, collisionModel: bool = bool, controlVertex: bool = bool, curve: bool = bool, curveKnot: bool = bool, curveOnSurface: bool = bool, curveParameterPoint: bool = bool, dimension: bool = bool, dynamicConstraint: bool = bool, edge: bool = bool, editPoint: bool = bool, emitter: bool = bool, facet: bool = bool, field: bool = bool, fluid: bool = bool, follicle: bool = bool, hairSystem: bool = bool, handle: bool = bool, hull: bool = bool, ikEndEffector: bool = bool, ikHandle: bool = bool, imagePlane: bool = bool, implicitGeometry: bool = bool, isoparm: bool = bool, joint: bool = bool, jointPivot: bool = bool, lattice: bool = bool, latticePoint: bool = bool, light: bool = bool, localRotationAxis: bool = bool, locator: bool = bool, locatorUV: bool = bool, locatorXYZ: bool = bool, meshUVShell: bool = bool, motionTrailPoint: bool = bool, motionTrailTangent: bool = bool, nCloth: bool = bool, nParticle: bool = bool, nParticleShape: bool = bool, nRigid: bool = bool, nonlinear: bool = bool, nurbsCurve: bool = bool, nurbsSurface: bool = bool, objectComponent: bool = bool, orientationLocator: bool = bool, particle: bool = bool, particleShape: bool = bool, plane: bool = bool, polymesh: bool = bool, polymeshEdge: bool = bool, polymeshFace: bool = bool, polymeshFreeEdge: bool = bool, polymeshUV: bool = bool, polymeshVertex: bool = bool, polymeshVtxFace: bool = bool, queryByName: Optional[Union[str, bool]] = str, rigidBody: bool = bool, rigidConstraint: bool = bool, rotatePivot: bool = bool, scalePivot: bool = bool, sculpt: bool = bool, selectHandle: bool = bool, spring: bool = bool, springComponent: bool = bool, stroke: bool = bool, subdiv: bool = bool, subdivMeshEdge: bool = bool, subdivMeshFace: bool = bool, subdivMeshPoint: bool = bool, subdivMeshUV: bool = bool, surfaceEdge: bool = bool, surfaceFace: bool = bool, surfaceKnot: bool = bool, surfaceParameterPoint: bool = bool, surfaceRange: bool = bool, surfaceUV: bool = bool, texture: bool = bool, vertex: bool = bool, query: bool = bool):
    """
    The

    Args:
        allComponents: (create, query) - Set all component selection masks on/off
        allObjects: (create, query) - Set all object selection masks on/off
        animBreakdown: (create, query) - Set animation breakdown selection mask on/off.
        animCurve: (create, query) - Set animation curve selection mask on/off.
        animInTangent: (create, query) - Set animation in-tangent selection mask on/off.
        animKeyframe: (create, query) - Set animation keyframe selection mask on/off.
        animOutTangent: (create, query) - Set animation out-tangent selection mask on/off.
        byName: (create, multiuse) - Set the specified user-defined selection mask on/off. (object flag)
        camera: (create, query) - Set camera selection mask on/off. (object flag)
        cluster: (create, query) - Set cluster selection mask on/off. (object flag)
        collisionModel: (create, query) - Set collision model selection mask on/off. (object flag)
        controlVertex: (create, query) - Set control vertex selection mask on/off. (component flag)
        curve: (create, query) - Set curve selection mask on/off. (object flag)
        curveKnot: (create, query) - Set curve knot selection mask on/off. (component flag)
        curveOnSurface: (create, query) - Set curve-on-surface selection mask on/off. (object flag)
        curveParameterPoint: (create, query) - Set curve parameter point selection mask on/off. (component flag)
        dimension: (create, query) - Set dimension shape selection mask on/off. (object flag)
        dynamicConstraint: (create, query) - Set dynamicConstraint selection mask on/off. (object flag)
        edge: (create, query) - Set mesh edge selection mask on/off. (component flag)
        editPoint: (create, query) - Set edit-point selection mask on/off. (component flag)
        emitter: (create, query) - Set emitter selection mask on/off. (object flag)
        facet: (create, query) - Set mesh face selection mask on/off. (component flag)
        field: (create, query) - Set field selection mask on/off. (object flag)
        fluid: (create, query) - Set fluid selection mask on/off. (object flag)
        follicle: (create, query) - Set follicle selection mask on/off. (object flag)
        hairSystem: (create, query) - Set hairSystem selection mask on/off. (object flag)
        handle: (create, query) - Set object handle selection mask on/off. (object flag)
        hull: (create, query) - Set hull selection mask on/off. (component flag)
        ikEndEffector: (create, query) - Set ik end effector selection mask on/off. (object flag)
        ikHandle: (create, query) - Set ik handle selection mask on/off. (object flag)
        imagePlane: (create, query) - Set image plane selection mask on/off. (component flag)
        implicitGeometry: (create, query) - Set implicit geometry selection mask on/off. (object flag)
        isoparm: (create, query) - Set surface iso-parm selection mask on/off. (component flag)
        joint: (create, query) - Set ik handle selection mask on/off. (object flag)
        jointPivot: (create, query) - Set joint pivot selection mask on/off. (component flag)
        lattice: (create, query) - Set lattice selection mask on/off. (object flag)
        latticePoint: (create, query) - Set lattice point selection mask on/off. (component flag)
        light: (create, query) - Set light selection mask on/off. (object flag)
        localRotationAxis: (create, query) - Set local rotation axis selection mask on/off. (component flag)
        locator: (create, query) - Set locator (all types) selection mask on/off. (object flag)
        locatorUV: (create, query) - Set uv locator selection mask on/off. (object flag)
        locatorXYZ: (create, query) - Set xyz locator selection mask on/off. (object flag)
        meshUVShell: (create, query) - Set uv shell component mask on/off.
        motionTrailPoint: (create, query) - Set motion point selection mask on/off.
        motionTrailTangent: (create, query) - Set motion point tangent mask on/off.
        nCloth: (create, query) - Set nCloth selection mask on/off. (object flag)
        nParticle: (create, query) - Set nParticle point selection mask on/off. (component flag)
        nParticleShape: (create, query) - Set nParticle shape selection mask on/off. (object flag)
        nRigid: (create, query) - Set nRigid selection mask on/off. (object flag)
        nonlinear: (create, query) - Set nonlinear selection mask on/off. (object flag)
        nurbsCurve: (create, query) - Set nurbs-curve selection mask on/off. (object flag)
        nurbsSurface: (create, query) - Set nurbs-surface selection mask on/off. (object flag)
        objectComponent: (create, query) - Component flags apply to object mode.
        orientationLocator: (create, query) - Set orientation locator selection mask on/off. (object flag)
        particle: (create, query) - Set particle point selection mask on/off. (component flag)
        particleShape: (create, query) - Set particle shape selection mask on/off. (object flag)
        plane: (create, query) - Set sketch plane selection mask on/off. (object flag)
        polymesh: (create, query) - Set poly-mesh selection mask on/off. (object flag)
        polymeshEdge: (create, query) - Set poly-mesh edge selection mask on/off. (component flag)
        polymeshFace: (create, query) - Set poly-mesh face selection mask on/off. (component flag)
        polymeshFreeEdge: (create, query) - Set poly-mesh free-edge selection mask on/off. (component flag)
        polymeshUV: (create, query) - Set poly-mesh UV point selection mask on/off. (component flag)
        polymeshVertex: (create, query) - Set poly-mesh vertex selection mask on/off. (component flag)
        polymeshVtxFace: (create, query) - Set poly-mesh vertexFace selection mask on/off. (component flag)
        queryByName: (query) - Query the specified user-defined selection mask. (object flag)       In query mode, this flag needs a value.
        rigidBody: (create, query) - Set rigid body selection mask on/off. (object flag)
        rigidConstraint: (create, query) - Set rigid constraint selection mask on/off. (object flag)
        rotatePivot: (create, query) - Set rotate pivot selection mask on/off. (component flag)
        scalePivot: (create, query) - Set scale pivot selection mask on/off. (component flag)
        sculpt: (create, query) - Set sculpt selection mask on/off. (object flag)
        selectHandle: (create, query) - Set select handle selection mask on/off. (component flag)
        spring: (create, query) - Set spring shape selection mask on/off. (object flag)
        springComponent: (create, query) - Set individual spring selection mask on/off. (component flag)
        stroke: (create, query) - Set the Paint Effects stroke selection mask on/off. (object flag)
        subdiv: (create, query) - Set subdivision surfaces selection mask on/off. (object flag)
        subdivMeshEdge: (create, query) - Set subdivision surfaces mesh edge selection mask on/off. (component flag)
        subdivMeshFace: (create, query) - Set subdivision surfaces mesh face selection mask on/off. (component flag)
        subdivMeshPoint: (create, query) - Set subdivision surfaces mesh point selection mask on/off. (component flag)
        subdivMeshUV: (create, query) - Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
        surfaceEdge: (create, query) - Set surface edge selection mask on/off. (component flag)
        surfaceFace: (create, query) - Set surface face selection mask on/off. (component flag)
        surfaceKnot: (create, query) - Set surface knot selection mask on/off. (component flag)
        surfaceParameterPoint: (create, query) - Set surface parameter point selection mask on/off. (component flag)
        surfaceRange: (create, query) - Set surface range selection mask on/off. (component flag)
        surfaceUV: (create, query) - Set surface uv selection mask on/off. (component flag)
        texture: (create, query) - Set texture selection mask on/off. (object flag)
        vertex: (create, query) - Set mesh vertex selection mask on/off. (component flag)
    """
    pass


def setAttr(*args, alteredValue: bool = bool, caching: bool = bool, capacityHint: Optional[Union[int, bool]] = int, channelBox: bool = bool, clamp: bool = bool, keyable: bool = bool, lock: bool = bool, size: Optional[Union[int, bool]] = int, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Sets the value of a dependency node attribute.  No value for the the attribute is needed when the

    Args:
        alteredValue: (create) - The value is only the current value, which may change in the next evalution (if the attribute has an incoming connection). This flag is only used during file I/O, so that attributes with incoming connections do not have their data overwritten during the first evaluation after a file is opened. Not supported for Ufe attributes.
        caching: (create) - Sets the attribute's internal caching on or off. Not all attributes can be defined as caching. Only those attributes that are not defined by default to be cached can be made caching.  As well, multi attribute elements cannot be made caching. Caching also affects child attributes for compound attributes. Not supported for Ufe attributes.
        capacityHint: (create) - Used to provide a memory allocation hint to attributes where the -size flag cannot provide enough information. This flag is optional and is primarily intended to be used during file I/O. Only certain attributes make use of this flag, and the interpretation of the flag value varies per attribute. Not supported for Ufe attributes. This flag is currently used by (node.attribute):  mesh.face - hints the total number of elements in the face edge lists
        channelBox: (create) - Sets the attribute's display in the channelBox on or off. Keyable attributes are always display in the channelBox regardless of the channelBox settting. Not supported for Ufe attributes. The display of Ufe attributes in the Channel Box is controlled using the channelBox command flag -ual/ufeFixedAttrList.
        clamp: (create) - For numeric attributes, if the value is outside the range of the attribute, clamp it to the min or max instead of failing. Not supported for Ufe attributes.
        keyable: (create) - Sets the attribute's keyable state on or off. Not supported for Ufe attributes.
        lock: (create) - Sets the attribute's lock state on or off.
        size: (create) - Defines the size of a multi-attribute array. This is only a hint, used to help allocate memory as efficiently as possible. Not supported for Ufe attributes.
        type: (create) - Identifies the type of data.  If the -type flag is not present, a numeric type is assumed. Not supported for Ufe attributes.
    """
    pass


def setEditCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a tool that can be used to modify set membership.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def setKeyCtx(*args, breakdown: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, preserveTangent: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to set keys within the graph editor

    Args:
        breakdown: (edit, query) - Specifies whether or not to create breakdown keys
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        preserveTangent: (edit, query) - Specifies whether or not to preserve tangent
    """
    pass


def sets(*args, addElement: str = str, afterFilters: bool = bool, anyMember: Optional[Union[str, bool]] = str, clear: str = str, color: Optional[Union[int, bool]] = int, copy: Optional[Union[str, bool]] = str, edges: bool = bool, editPoints: bool = bool, empty: bool = bool, facets: bool = bool, flatten: str = str, forceElement: str = str, include: str = str, intersection: Optional[Union[str, bool]] = str, isIntersecting: Optional[Union[str, bool]] = str, isMember: Optional[Union[str, bool]] = str, layer: bool = bool, name: Optional[Union[str, bool]] = str, noIntermediate: bool = bool, noSurfaceShader: bool = bool, noWarnings: bool = bool, nodesOnly: bool = bool, remove: str = str, renderable: bool = bool, size: bool = bool, split: Optional[Union[str, bool]] = str, subtract: Optional[Union[str, bool]] = str, text: Optional[Union[str, bool]] = str, union: Optional[Union[str, bool]] = str, vertices: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command is used to create a set, query some state of a set, or perform operations to update the membership of a set. A set is a logical grouping of an arbitrary collection of objects, attributes, or components of objects. Sets are dependency nodes. Connections from objects to a set define membership in the set.

    Args:
        addElement: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set because they are in another set which is in the same partition as the set to edit, the command will fail.
        afterFilters: (edit) - Default state is false. This flag is valid in edit mode only. This flag is for use on sets that are acted on by deformers such as sculpt, lattice, blendShape. The default edit mode is to edit the membership of the group acted on by the deformer. If you want to edit the group but not change the membership of the deformer, set the flag to true.
        anyMember: (create) - An operation which tests whether any of the given items are members of the given set.
        clear: (edit) - An operation which removes all items from the given set making the set empty.
        color: (create, edit, query) - Defines the hilite color of the set. Must be a value in range [-1, 7] (one of the user defined colors).  -1 marks the color has being undefined and therefore not having any affect. Only the vertices of a vertex set will be displayed in this color.
        copy: (create) - Copies the members of the given set to a new set. This flag is for use in creation mode only.
        edges: (create, query) - Indicates the new set can contain edges only. This flag is for use in creation or query mode only. The default value is false.
        editPoints: (create, query) - Indicates the new set can contain editPoints only. This flag is for use in creation or query mode only. The default value is false.
        empty: (create) - Indicates that the set to be created should be empty. That is, it ignores any arguments identifying objects to be added to the set. This flag is only valid for operations that create a new set.
        facets: (create, query) - Indicates the new set can contain facets only. This flag is for use in creation or query mode only. The default value is false.
        flatten: (edit) - An operation that flattens the structure of the given set. That is, any sets contained by the given set will be replaced by its members so that the set no longer contains other sets but contains the other sets' members.
        forceElement: (edit) - For use in edit mode only. Forces addition of the items to the set. If the items are in another set which is in the same partition as the given set, the items will be removed from the other set in order to keep the sets in the partition mutually exclusive with respect to membership.
        include: (edit) - Adds the list of items to the given set.  If some of the items cannot be added to the set, a warning will be issued. This is a less strict version of the -add/addElement operation.
        intersection: (create) - An operation that returns a list of items which are members of all the sets in the list.
        isIntersecting: (create) - An operation which tests whether the sets in the list have common members.
        isMember: (create) - An operation which tests whether all the given items are members of the given set.
        layer: (create) - OBSOLETE. DO NOT USE.
        name: (create) - Assigns string as the name for a new set. This flag is only valid for operations that create a new set.
        noIntermediate: (create, query) - Excludes intermediate objects when querying set members or using the subtract, union, itersection, or isIntersecting flags.
        noSurfaceShader: (create) - If set is renderable, do not connect it to the default surface shader.  Flag has no meaning or effect for non renderable sets. This flag is for use in creation mode only. The default value is false.
        noWarnings: (create) - Indicates that warning messages should not be reported such as when trying to add an invalid item to a set. (used by UI)
        nodesOnly: (query) - This flag is usable with the -q/query flag but is ignored if used with another queryable flags. This flag modifies the results of the set membership query such that when there are attributes (e.g. sphere1.tx) or components of nodes included in the set, only the nodes will be listed. Each node will only be listed once, even if more than one attribute or component of the node exists in the set.
        remove: (edit) - Removes the list of items from the given set.
        renderable: (create, query) - This flag indicates that a special type of set should be created. This type of set (shadingEngine as opposed to objectSet) has certain restrictions on its membership in that it can only contain renderable elements such as lights and geometry. These sets are referred to as shading groups and are automatically connected to the "renderPartition" node when created (to ensure mutual exclusivity of the set's members with the other sets in the partition). This flag is for use in creation or query mode only. The default value is false which means a normal set is created.
        size: (query) - Use the size flag to query the length of the set.
        split: (create) - Produces a new set with the list of items and removes each item in the list of items from the given set.
        subtract: (create) - An operation between two sets which returns the members of the first set that are not in the second set.
        text: (create, edit, query) - Defines an annotation string to be stored with the set.
        union: (create) - An operation that returns a list of all the members of all sets listed.
        vertices: (create, query) - Indicates the new set can contain vertices only. This flag is for use in creation or query mode only. The default value is false.
    """
    pass


def setToolTo(*args):
    """
    This command switches control to the named context.

    Args:
    """
    pass


def shadingGeometryRelCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, offCommand: Optional[Union[str, bool]] = str, onCommand: Optional[Union[str, bool]] = str, shadingCentric: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context that can be used for associating geometry to shading groups.  You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true.  This means that the shading group is selected first then geometry associated with the shading group are highlighted.  Subsequent selections result in assignments.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        offCommand: (create, edit, query) - command to be issued when context is turned on
        onCommand: (create, edit, query) - command to be issued when context is turned on
        shadingCentric: (create, edit, query) - shading-centric mode.
    """
    pass


def shadingLightRelCtx(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, offCommand: Optional[Union[str, bool]] = str, onCommand: Optional[Union[str, bool]] = str, shadingCentric: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context that can be used for associating lights to shading groups.  You can put the context into shading-centric mode by using the -shadingCentric flag and specifying true.  This means that the shading group is selected first then lights associated with the shading group are highlighted.  Subsequent selections result in assignments.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        offCommand: (create, edit, query) - command to be issued when context is turned on
        onCommand: (create, edit, query) - command to be issued when context is turned on
        shadingCentric: (create, edit, query) - shading-centric mode.
    """
    pass


def shapeCompare(*args):
    """
    Compares two shapes. If no shapes are specified in the command line, then the shapes from the active list are used.

    Args:
    """
    pass


def showHidden(*args, above: bool = bool, allObjects: bool = bool, below: bool = bool, lastHidden: bool = bool):
    """
    The

    Args:
        above: (create) - Make objects and all their invisible ancestors visible.
        allObjects: (create) - Make all invisible objects visible.
        below: (create) - Make objects and all their invisible descendants visible.
        lastHidden: (create) - Show everything that was hidden with the last hide command.
    """
    pass


def showManipCtx(*args, addAttr: str = str, currentNodeName: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, incSnap: Optional[Union[Tuple[int, bool], bool]] = [int, bool], incSnapRelative: Optional[Union[Tuple[int, bool], bool]] = [int, bool], incSnapUI: bool = bool, incSnapValue: Optional[Union[Tuple[int, float], bool]] = [int, float], iveVisible: bool = bool, lockSelection: bool = bool, moveActiveAttrDown: bool = bool, moveActiveAttrToTop: bool = bool, moveActiveAttrUp: bool = bool, name: Optional[Union[str, bool]] = str, removeAttr: str = str, resetActiveAttr: bool = bool, selectedAttributes: bool = bool, setAttrActive: str = str, setNextAttrActive: bool = bool, setPreviousAttrActive: bool = bool, toggleIncSnap: bool = bool, toolFinish: Optional[Union[str, bool]] = str, toolStart: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a show manip context.  The show manip context will display manips for all selected objects that have valid manips defined for them.

    Args:
        addAttr: (edit) - Add a specific attribute to the In View Editor attribute list.
        currentNodeName: (query) - Returns the name of the first node that the context is attached to.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        incSnap: (create, edit, multiuse, query) - If true, the manipulator owned by the context will use incremental snapping for specified mode.
        incSnapRelative: (create, edit, multiuse, query) - If true, the manipulator owned by the context will use relative incremental snapping for specified mode.
        incSnapUI: (query) - Returns an array of elements indicating what kind of incremental snap UI is required by the manipulator owned by the context. If no UI is required, the result array will contain a single element of with the value 0. The other values and their meanings are:  1 - UI for linear incremental translate 2 - UI for incremental rotate 3 - UI for inclremental scale
        incSnapValue: (create, edit, multiuse, query) - Supply the step value which the manipulator owned by the context will use for specified mode.
        iveVisible: (edit, query) - Set the In View Editor visible or not.
        lockSelection: (create, edit, query) - If true, this context will never change the current selection. By default this is set to false.
        moveActiveAttrDown: (edit) - Move the In View Editor active attribute down one in the list.
        moveActiveAttrToTop: (edit) - Move the In View Editor active attribute to the top of the list.
        moveActiveAttrUp: (edit) - Move the In View Editor active attribute up one in the list.
        name: (create) - If this is a tool command, name the tool appropriately.
        removeAttr: (edit) - Remove a specific attribute from the In View Editor attribute list.
        resetActiveAttr: (edit) - Reset the In View Editor active attribute to its default value.
        selectedAttributes: (query) - Returns a list of the names of the attributes that are currently visible in the In View Editor.
        setAttrActive: (edit) - Set a specific attribute from the In View Editor attribute list active.
        setNextAttrActive: (edit) - Set the next attribute in the In View Editor attribute list active.
        setPreviousAttrActive: (edit) - Set the previous attribute in the In View Editor attribute list active.
        toggleIncSnap: (create, edit) - Toggles (enables/disables) snapping for all modes.
        toolFinish: (create, edit, query) - Supply the script that will be run when the user exits the script.
        toolStart: (create, edit, query) - Supply the script that will be run when the user first enters the script
    """
    pass


def skinBindCtx(*args, about: Optional[Union[str, bool]] = str, axis: Optional[Union[str, bool]] = str, colorRamp: Optional[Union[str, bool]] = str, currentInfluence: Optional[Union[str, bool]] = str, displayInactiveMode: Optional[Union[int, bool]] = int, displayNormalized: bool = bool, exists: bool = bool, falloffCurve: Optional[Union[str, bool]] = str, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, symmetry: bool = bool, tolerance: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command creates a tool that can be used to edit volumes from an interactive bind.

    Args:
        about: (create, edit, query) - The space in which the axis should be mirrored. Valid values are: "world" and "object".
        axis: (create, edit, query) - The mirror axis. Valid values are: "x","y", and "z".
        colorRamp: (create, edit, query) - Set the values on the color ramp used to display the weight values.
        currentInfluence: (create, edit, query) - Set the index of the current influence or volume to be adjusted by the manipulator.
        displayInactiveMode: (create, edit, query) - Determines the display mode for drawing volumes that are not selected, in particular which volume cages if any are displayed. 0 - None 1 - Nearby volumes 2 - All volumes
        displayNormalized: (create, edit, query) - Display raw select weights (false) or finalized normalized weights (true).
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        falloffCurve: (create, edit, query) - Set the values on the falloff curve control.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        symmetry: (create, edit, query) - Controls whether or not the tool operates in symmetric (mirrored) mode.
        tolerance: (create, edit, query) - The tolerance setting for determining whether another influence is symmetric to the the current influence.
    """
    pass


def snapMode(*args, curve: bool = bool, distanceIncrement: Optional[Union[float, bool]] = float, edgeMagnet: Optional[Union[int, bool]] = int, edgeMagnetTolerance: Optional[Union[float, bool]] = float, grid: bool = bool, liveFaceCenter: bool = bool, livePoint: bool = bool, meshCenter: bool = bool, pixelCenter: bool = bool, pixelSnap: bool = bool, point: bool = bool, tolerance: Optional[Union[int, bool]] = int, useTolerance: bool = bool, uvTolerance: Optional[Union[int, bool]] = int, viewPlane: bool = bool, query: bool = bool):
    """
    The snapMode command is used to control snapping.  It toggles the snapping modes in effect and sets information used for snapping.

    Args:
        curve: (create, query) - Set curve snap mode
        distanceIncrement: (create, query) - Set the distance for the snapping to objects such as a lines or planes.
        edgeMagnet: (create, query) - Number of extra magnets to snap onto, regularly spaced along the edge.
        edgeMagnetTolerance: (create, query) - Precision for edge magnet snapping.
        grid: (create, query) - Set grid snap mode
        liveFaceCenter: (create, query) - While moving on live polygon objects, snap to its face centers.
        livePoint: (create, query) - While moving on live polygon objects, snap to its vertices.
        meshCenter: (create, query) - While moving, snap on the center of the mesh that intersect the line from the camera to the cursor.
        pixelCenter: (create, query) - Snap UV to the center of the pixel instead of the corner.
        pixelSnap: (create, query) - Snap UVs to the nearest pixel center or corner.
        point: (create, query) - Set point snap mode
        tolerance: (create, query) - Tolerance defines the size of the square region in which points must lie in order to be snapped to. The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        useTolerance: (create, query) - If useTolerance is set, then point snapping is limited to points that are within a square region surrounding the cursor position. The size of the square is determined by the tolerance value.
        uvTolerance: (create, query) - uvTolerance defines the size of the square region in which points must lie in order to be snapped to, in the UV Editor.  The tolerance value is the distance from the cursor position to the boundary of the square (in all four directions).
        viewPlane: (create, query) - Set view-plane snap mode
    """
    pass


def snapTogetherCtx(*args, clearSelection: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, setOrientation: bool = bool, snapPolygonFace: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Args:
        clearSelection: (create, edit, query) - Sets whether the tool should clear the selection on entry to the tool. Default true.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        setOrientation: (create, edit, query) - Sets whether the tool should orient as well as moving an item. Default true.
        snapPolygonFace: (create, edit, query) - Sets whether the tool should snap the cursor to polygon face centers. Default false.
    """
    pass


def softModCtx(*args, dragSlider: str = str, exists: bool = bool, falseColor: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, reset: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Controls the softMod context.

    Args:
        dragSlider: (edit) - Specify the slider mode for hotkey radius resizing.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        falseColor: (edit) - Enable or disable false color display on the soft mod manipulator.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        reset: (edit, query) - Reset the tool options to their default values.
    """
    pass


def softSelect(*args, compressUndo: Optional[Union[int, bool]] = int, enableFalseColor: Optional[Union[int, bool]] = int, softSelectColorCurve: Optional[Union[str, bool]] = str, softSelectCurve: Optional[Union[str, bool]] = str, softSelectDistance: Optional[Union[float, bool]] = float, softSelectEnabled: Optional[Union[int, bool]] = int, softSelectFalloff: Optional[Union[int, bool]] = int, softSelectReset: bool = bool, softSelectUVDistance: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command allows you to change the soft modelling options.

    Args:
        compressUndo: (create, edit, query) - Controls how soft selection settings behave in undo:  0 means all changes undo individually 1 means all consecutive changes undo as a group 2 means only interactive changes undo as a group  When queried, returns an int indicating the current undo behaviour.
        enableFalseColor: (create, edit, query) - Set soft select color feedback on or off. When queried, returns an int indicating whether color feedback is currently enabled.
        softSelectColorCurve: (create, edit, query) - Sets the color ramp used to display false color feedback for soft selected components in the viewport. The color curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 5 successive values: 3 RGB values (the color to use), an input value (the selection weight), and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current color feedback curve.
        softSelectCurve: (create, edit, query) - Sets the falloff curve used to calculate selection weights for components within the falloff distance. The curve is encoded as a string of comma separated floating point values representing the falloff curve CVs. Each CV is represented by 3 successive values: an output value (the selection weight at this point), an input value (the normalised falloff distance) and a curve interpolation type. When queried, returns a string containing the encoded CVs of the current falloff curve.
        softSelectDistance: (create, edit, query) - Sets the falloff distance (radius) used for world and object space soft selection. When queried, returns a float indicating the current falloff distance.
        softSelectEnabled: (create, edit, query) - Sets soft selection based modeling on or off. When queried, returns an int indicating the current state of the option.
        softSelectFalloff: (create, edit, query) - Sets the falloff mode:  0 for volume based falloff 1 for surface based falloff 2 for global falloff  When queried, returns an int indicating the falloff mode.
        softSelectReset: (create, edit) - Resets soft selection to its default settings.
        softSelectUVDistance: (create, edit, query) - Sets the falloff distance (radius) used for UV space soft selection. When queried, returns a float indicating the current falloff distance.
    """
    pass


def spaceLocator(*args, absolute: bool = bool, name: Optional[Union[str, bool]] = str, position: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], relative: bool = bool, edit: bool = bool, query: bool = bool):
    """
    The command creates a locator at the specified position in space. By default it is created at (0,0,0).

    Args:
        absolute: (create, edit) - If set, the locator's position is in world space.
        name: (create, edit) - Name for the locator.
        position: (create, edit, query) - Location in  3-dimensional space where locator is to be created.
        relative: (create, edit) - If set, the locator's position is relative to its local space. The locator is created in relative mode by default.
    """
    pass


def srtContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a combined transform (translate/scale/rotate) context.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def suitePrefs(*args, applyToSuite: Optional[Union[str, bool]] = str, installedAsSuite: bool = bool, isCompleteSuite: bool = bool):
    """
    This command sets the mouse and keyboard interaction mode for Maya and other Suites applications (if Maya is part of a Suites install).

    Args:
        applyToSuite: (create) - Apply the mouse and keyboard interaction settings for the given application to all applications in the Suite (if Maya is part of a Suites install). Valid values are "Maya", "3dsMax", or "undefined", which signifies that each app is to use their own settings.
        installedAsSuite: (create) - Returns true if Maya is part of a Suites install, false otherwise.
        isCompleteSuite: (create) - Returns true if the Suites install contains all Entertainment Creation Suite products, false otherwise.
    """
    pass


def symmetricModelling(*args, about: Optional[Union[str, bool]] = str, allowPartial: bool = bool, axis: Optional[Union[str, bool]] = str, preserveSeam: Optional[Union[int, bool]] = int, reset: bool = bool, seamFalloffCurve: Optional[Union[str, bool]] = str, seamTolerance: Optional[Union[float, bool]] = float, symmetry: Optional[Union[int, bool]] = int, tolerance: Optional[Union[float, bool]] = float, topoSymmetry: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command allows you to change the symmetric modelling options.

    Args:
        about: (create, edit, query) - Set the space in which symmetry should be calculated (object or world or topo). When queried, returns a string which is the current space being used.
        allowPartial: (create, edit, query) - Specifies whether partial symmetry should be allowed when enabling topological symmetry.
        axis: (create, edit, query) - Set the current axis to be reflected over. When queried, returns a string which is the current axis.
        preserveSeam: (create, edit, query) - Controls whether selection or symmetry should take priority on the plane of symmetry. When queried, returns an int for the option.
        reset: (create, edit) - Reset the redo information before starting.
        seamFalloffCurve: (create, edit, query) - Set the seam's falloff curve, used to control the seam strength within the seam tolerance. The string is a comma separated list of sets of 3 values for each curve point. When queried, returns a string which is the current space being used.
        seamTolerance: (create, edit, query) - Set the seam tolerance used for reflection. When preserveSeam is enabled, this tolerance controls the width of the enforced seam. When queried, returns a float of the seamTolerance.
        symmetry: (create, edit, query) - Set the symmetry option on or off. When queried, returns an int for the option.
        tolerance: (create, edit, query) - Set the tolerance of reflection. When queried, returns a float of the tolerance.
        topoSymmetry: (create, edit, query) - Enable/disable topological symmetry. When enabled, the supplied component/active list will be used to define the topological symmetry seam. When queried, returns the name of the active topological symmetry object.
    """
    pass


def targetWeldCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, mergeToCenter: bool = bool, preserveUV: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Create a new context to weld vertices together on a poly object.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mergeToCenter: (create, edit, query) - If mergeToCenter is set to true then the source and target vertices's will be moved to the center before doing the merge.  If set to false the source vertex will be moved to the target vertex before doing the merge.
        preserveUV: (edit, query) - When false, UVs are not changed when welding components. When true, the UVs are modified to stop texture swimming when welding components. Default is true.
    """
    pass


def texCutContext(*args, adjustSize: bool = bool, displayShellBorders: bool = bool, edgeSelectSensitive: Optional[Union[float, bool]] = float, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, mode: Optional[Union[str, bool]] = str, moveRatio: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, size: Optional[Union[float, bool]] = float, steadyStroke: bool = bool, steadyStrokeDistance: Optional[Union[float, bool]] = float, touchToSew: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context for cut uv tool.  This context only works in the UV editor.

    Args:
        adjustSize: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous mode.
        displayShellBorders: (edit, query) - Toggle the display of shell borders.
        edgeSelectSensitive: (edit, query) - Set the value of the edge selection sensitivity.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        mode: (edit, query) - Specifies the type of effect the brush will perform, Cut or Sew.
        moveRatio: (edit, query) - The cut open ratio relative to edge length.
        name: (create) - If this is a tool command, name the tool appropriately.
        size: (edit, query) - Brush size value of the brush ring.
        steadyStroke: (edit, query) - Turn on steady stroke or not.
        steadyStrokeDistance: (edit, query) - The distance for steady stroke.
        touchToSew: (edit, query) - Toggle the touch to sew mode.
    """
    pass


def texLatticeDeformContext(*args, envelope: Optional[Union[float, bool]] = float, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, latticeColumns: Optional[Union[int, bool]] = int, latticeRows: Optional[Union[int, bool]] = int, name: Optional[Union[str, bool]] = str, showMoveManipulator: bool = bool, snapPixelMode: bool = bool, useBoundingRect: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context which may be used to deform UV maps with lattice manipulator.  This context only works in the texture UV editor.

    Args:
        envelope: (create, edit, query) - Specifies the influence of the lattice.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        latticeColumns: (create, edit, query) - Specifies the number column points the lattice contains.  The maximum size lattice is restricted to 8 columns.
        latticeRows: (create, edit, query) - Specifies the number of rows the lattice contains. The maximum size lattice is restricted to 8 rows.
        name: (create) - If this is a tool command, name the tool appropriately.
        showMoveManipulator: (create, edit, query) - Specifies whether show move manipulator in UV Editor
        snapPixelMode: (create, edit, query) - Specifies the influenced uv points should be snapped to a pixel center or corner.
        useBoundingRect: (create, edit, query) - When constructing the lattice use the bounding box of the selected UVs for the extents of the lattice.  When this is disabled the extents of the marquee selections are used as the extents for the lattice.
    """
    pass


def texManipContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command used to register the texSelectCtx tool. Command used to register the texManipCtx tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def texMoveContext(*args, editPivotMode: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, position: bool = bool, snap: bool = bool, snapComponentsRelative: bool = bool, snapPixelMode: Optional[Union[int, bool]] = int, snapValue: Optional[Union[float, bool]] = float, tweakMode: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    Args:
        editPivotMode: (query) - Returns true when the manipulator is in edit pivot mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position: (query) - Returns the current position of the manipulator
        snap: (edit, query) - Sets or queries whether snapping is to be used.
        snapComponentsRelative: (edit, query) - Value can be : true or false. If true, while snapping a group of UVs, the relative spacing between them will be preserved. If false, all the UVs will be snapped to the target point
        snapPixelMode: (edit, query) - Sets the snapping mode to be the pixel center or upper left corner.
        snapValue: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and moved in one step using a click-drag interaction.
    """
    pass


def texMoveUVShellContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, iterations: Optional[Union[int, bool]] = int, mask: bool = bool, position: bool = bool, shellBorder: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        iterations: (edit, query) - Sets or queries the number of iterations to perform.
        mask: (edit, query) - Sets or queries masking on the shell.
        position: (query) - Returns the current position of the manipulator
        shellBorder: (edit, query) - Sets or queries the size of the shell border.
    """
    pass


def texRotateContext(*args, editPivotMode: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, position: bool = bool, snap: bool = bool, snapRelative: bool = bool, snapValue: Optional[Union[float, bool]] = float, tweakMode: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a rotate context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor rotate contexts.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flag, will change all existing texture editor rotate contexts.

    Args:
        editPivotMode: (query) - Returns true when the manipulator is in edit pivot mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position: (query) - Returns the current position of the manipulator.
        snap: (edit, query) - Sets or queries whether snapping is to be used.
        snapRelative: (edit, query) - Sets or queries whether snapping is relative.
        snapValue: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and rotated in one step using a click-drag interaction.
    """
    pass


def texScaleContext(*args, editPivotMode: bool = bool, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, position: bool = bool, preventNegativeScale: bool = bool, snap: bool = bool, snapRelative: bool = bool, snapValue: Optional[Union[float, bool]] = float, tweakMode: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a scale context for the UV Editor. Note that the above flag controls the global behaviour of all texture editor scale contexts.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flag, will change all existing texture editor scale contexts.

    Args:
        editPivotMode: (query) - Returns true when manipulator is in edit pivot mode.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position: (query) - Returns the current position of the manipulator.
        preventNegativeScale: (edit, query) - Prevent negative scale for components.
        snap: (edit, query) - Sets or queries whether snapping is to be used.
        snapRelative: (edit, query) - Sets or queries whether snapping is relative.
        snapValue: (edit, query) - Sets or queries the size of the snapping increment.
        tweakMode: (edit, query) - When true, the manipulator is hidden and highlighted components can be selected and scaled in one step using a click-drag interaction.
    """
    pass


def texSculptCacheContext(*args, adjustSize: bool = bool, adjustStrength: bool = bool, direction: Optional[Union[int, bool]] = int, falloffType: Optional[Union[int, bool]] = int, floodPin: Optional[Union[float, bool]] = float, grabTwist: bool = bool, inverted: bool = bool, mode: Optional[Union[str, bool]] = str, sculptFalloffCurve: Optional[Union[str, bool]] = str, showBrushRingDuringStroke: bool = bool, size: Optional[Union[float, bool]] = float, strength: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This is a tool context command for uv cache sculpting tool.

    Args:
        adjustSize: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush size. If false, puts the tool back into the previous sculpt mode.
        adjustStrength: (edit) - If true, puts the tool into the mode where dragging the mouse will edit the brush strength. If false, puts the tool back into the previous sculpt mode.
        direction: (edit, query) - Specifies how the brush determines where the uvs go.
        falloffType: (edit, query) - Specifies how the brush determines which uvs to affect.
        floodPin: (create, edit) - Sets the pin value for each UV to the given value
        grabTwist: (create, edit, query) - If true, the grab brush twists the UVs
        inverted: (create, edit, query) - If true, inverts the effect of the brush.
        mode: (edit, query) - Specifies the type of sculpting effect the brush will perform.
        sculptFalloffCurve: (edit, query) - Specifies the falloff curve that affects the brush.
        showBrushRingDuringStroke: (edit, query) - Specifies whether or not to show the brush ring during stroke.
        size: (edit, query) - Specifies the world-space size of the current brush.
        strength: (edit, query) - Specifies the world-space strength of the current brush.
    """
    pass


def texSelectContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Command used to register the texSelectCtx tool.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def texSelectShortestPathCtx(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the texture editor window.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
    """
    pass


def texSmudgeUVContext(*args, dragSlider: Optional[Union[str, bool]] = str, effectType: Optional[Union[str, bool]] = str, exists: bool = bool, functionType: Optional[Union[str, bool]] = str, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, pressure: Optional[Union[float, bool]] = float, radius: Optional[Union[float, bool]] = float, smudgeIsMiddle: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a context for smudge UV tool.  This context only works in the texture UV editor.

    Args:
        dragSlider: (edit, query) - radius | none Enables the drag slider mode. This is to support brush resizing while holding the 'b' or 'B' button.
        effectType: (edit, query) - fixed | smudge Specifies the effect of the tool. In fixed mode, the UVs move as if they are attached by a rubber band. In smudge mode the UVs are moved as the cursor is dragged over the UVs.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        functionType: (edit, query) - exponential | linear | constant. Specifies how UVs fall off from the center of influence.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        pressure: (edit, query) - Pressure value when effect type is set to smudge.
        radius: (edit, query) - Radius of the smudge tool. All UVs within this radius are affected by the tool
        smudgeIsMiddle: (edit, query) - By default, the left mouse button initiates the smudge. However, this conflicts with selection. When smudgeIsMiddle is on, smudge mode is activated by the middle mouse button instead of the left mouse button.
    """
    pass


def texturePlacementContext(*args, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, labelMapping: bool = bool, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    Create a command for creating new texture placement contexts. By default label mapping is on when the context is created.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        labelMapping: (create, edit, query) - Set the context to label mapping.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def texTweakUVContext(*args, exists: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, position: bool = bool, tolerance: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a texture editor move manip context. Note that the above flags control the global behaviour of all texture editor move manip contexts.  Changing one context independently is not allowed.  Changing a context's behaviour using the above flags, will change all existing texture editor move manip contexts.

    Args:
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        position: (query) - Returns the current position of the manipulator
        tolerance: (create, edit, query) - Controls the initial selection snapping tolerance.
    """
    pass


def texWinToolCtx(*args, alternateContext: bool = bool, boxzoom: bool = bool, dolly: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, toolName: Optional[Union[str, bool]] = str, track: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the texture window.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxzoom: (create, edit, query) - Perform Box Zoom
        dolly: (create, edit, query) - Dollies the view
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        track: (create, edit, query) - Tracks the view
    """
    pass


def threadCount(*args, numberOfThreads: Optional[Union[int, bool]] = int, query: bool = bool):
    """
    This command sets the number of threads to be used by Maya in regions of code that are multithreaded. By default the number of threads is equal to the number of logical CPUs, not the number of physical CPUs. Logical CPUs are different from physical CPUs in the following ways:

    Args:
        numberOfThreads: (create, query) - Sets the number of threads to use
    """
    pass


def threePointArcCtx(*args, degree: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, spans: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    The threePointArcCtx command creates a new context for creating 3 point arcs

    Args:
        degree: (create, edit, query) - VAlid values are 1 or 3. Default degree 3.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        spans: (create, edit, query) - Default is 8.
    """
    pass


def timeCode(*args, mayaStartFrame: Optional[Union[float, bool]] = float, productionStartFrame: Optional[Union[float, bool]] = float, productionStartHour: Optional[Union[float, bool]] = float, productionStartMinute: Optional[Union[float, bool]] = float, productionStartSecond: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    Use this command to query and set the time code information in the file

    Args:
        mayaStartFrame: (create, edit, query) - Sets the Maya start time of the time code, in frames. In query mode, returns the Maya start frame of the time code.
        productionStartFrame: (create, edit, query) - Sets the production start time of the time code, in terms of frames. In query mode, returns the sub-second frame of production start time.
        productionStartHour: (create, edit, query) - Sets the production start time of the time code, in terms of hours. In query mode, returns the hour of production start time.
        productionStartMinute: (create, edit, query) - Sets the production start time of the time code, in terms of minutes. In query mode, returns the minute of production start time.
        productionStartSecond: (create, edit, query) - Sets the production start time of the time code, in terms of seconds. In query mode, returns the second of production start time.
    """
    pass


def toggle(*args, above: bool = bool, below: bool = bool, boundary: bool = bool, boundingBox: bool = bool, controlVertex: bool = bool, doNotWrite: bool = bool, editPoint: bool = bool, extent: bool = bool, facet: bool = bool, geometry: bool = bool, gl: bool = bool, highPrecisionNurbs: bool = bool, hull: bool = bool, latticePoint: bool = bool, latticeShape: bool = bool, localAxis: bool = bool, newCurve: bool = bool, newPolymesh: bool = bool, newSurface: bool = bool, normal: bool = bool, origin: bool = bool, point: bool = bool, pointDisplay: bool = bool, pointFacet: bool = bool, rotatePivot: bool = bool, scalePivot: bool = bool, selectHandle: bool = bool, state: bool = bool, surfaceFace: bool = bool, template: bool = bool, uvCoords: bool = bool, vertex: bool = bool, query: bool = bool):
    """
    The toggle command is used to toggle the display of various object features for objects which have these components. For example, CV and edit point display may be toggled for those listed     NURB curves or surfaces.

    Args:
        above: (create) - Toggle state for all objects above listed objects.
        below: (create) - Toggle state for all objects below listed objects.
        boundary: (create, query) - Toggle boundary display of listed mesh objects.
        boundingBox: (create, query) - Toggle or query the bounding box display of listed objects.
        controlVertex: (create, query) - Toggle CV display of listed curves and surfaces.
        doNotWrite: (create, query) - Toggle the "this should be written to the file" state.
        editPoint: (create, query) - Toggle edit point display of listed curves and surfaces.
        extent: (create, query) - Toggle display of extents of listed mesh objects.
        facet: (create, query) - For use with normal flag. Set the normal display style to facet display.
        geometry: (create, query) - Toggle geometry display of listed objects.
        gl: (create) - Toggle state for all objects
        highPrecisionNurbs: (create, query) - Toggle high precision display for Nurbs
        hull: (create, query) - Toggle hull display of listed curves and surfaces.
        latticePoint: (create, query) - Toggle point display of listed lattices
        latticeShape: (create, query) - Toggle display of listed lattices
        localAxis: (create, query) - Toggle local axis display of listed objects.
        newCurve: (create, query) - Set component display state of new curve objects
        newPolymesh: (create, query) - Set component display state of new polymesh objects
        newSurface: (create, query) - Set component display state of new surface objects
        normal: (create, query) - Toggle display of normals of listed surface and mesh objects.
        origin: (create, query) - Toggle origin display of listed surfaces.
        point: (create, query) - For use with normal flag. Set the normal display style to vertex display.
        pointDisplay: (create, query) - Toggle point display of listed surfaces.
        pointFacet: (create, query) - For use with normal flag. Set the normal display style to vertex and face display.
        rotatePivot: (create, query) - Toggle rotate pivot display of listed objects.
        scalePivot: (create, query) - Toggle scale pivot display of listed objects.
        selectHandle: (create, query) - Toggle select handle display of listed objects.
        state: (create) - Explicitly set the state to true or false instead of toggling the state. Can not be queried.
        surfaceFace: (create, query) - Toggle surface face handle display of listed surfaces.
        template: (create, query) - Toggle template state of listed objects
        uvCoords: (create, query) - Toggle display uv coords of listed mesh objects.
        vertex: (create, query) - Toggle vertex display of listed mesh objects.
    """
    pass


def toggleAxis(*args, origin: bool = bool, view: bool = bool, query: bool = bool):
    """
    Toggles the state of the display axis.

    Args:
        origin: (create, query) - Turns display of the axis at the origin of the ground plane on or off.
        view: (create, query) - Turns display of the axis at the bottom left of each view on or off. (Obsolete - refer to the headsUpDisplay command)
    """
    pass


def toggleDisplacement(*args):
    """
    This command toggles the displacement preview of the polygon. This command is NOT un-doable.

    Args:
    """
    pass


def toolDropped(*args):
    """
    This command builds and executes the commands necessary to recreate the specified tool button.  It is invoked when a tool is dropped on the shelf.

    Args:
    """
    pass


def toolHasOptions(*args):
    """
    This command queries a tool to see if it has options. If it does, it returns true. Otherwise it returns false.

    Args:
    """
    pass


def toolPropertyWindow(*args, field: Optional[Union[str, bool]] = str, helpButton: Optional[Union[str, bool]] = str, icon: Optional[Union[str, bool]] = str, inMainWindow: bool = bool, location: Optional[Union[str, bool]] = str, noviceMode: bool = bool, resetButton: Optional[Union[str, bool]] = str, restore: bool = bool, selectCommand: Optional[Union[str, bool]] = str, showCommand: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    End users should only call this command as 1. a query (in the custom tool property sheet code) or 2. with no arguments to create the default tool property sheet.  The more complex uses of it are internal.

    Args:
        field: (edit, query) - Sets/returns the name of the text field used to store the tool name in the property sheet.
        helpButton: (edit, query) - Sets/returns the name of the button used to show help on the tool in the property sheet.
        icon: (edit, query) - Sets/returns the name of the static picture object (used to display the tool icon in the property sheet).
        inMainWindow: (create) - Specify true if you want the tool settings to appear in the main window rather than a separate window.
        location: (edit, query) - Sets/returns the location of the current tool property sheet, or an empty string if there is none.
        noviceMode: (edit, query) - Sets/returns the 'novice mode' flag.(unused at the moment)
        resetButton: (edit, query) - Sets/returns the name of the button used to restore the tool settings in the property sheet.
        restore: (create) - Reopens the tool settings window. This flag can be used with the flag inMainWindow for the fall back location if the tool settings can't be restored.
        selectCommand: (edit, query) - Sets/returns the property sheet's select command.
        showCommand: (edit, query) - Sets/returns the property sheet's display command.
    """
    pass


def trackCtx(*args, alternateContext: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, toolName: Optional[Union[str, bool]] = str, trackGeometry: bool = bool, trackScale: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create a track context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        trackGeometry: (create, edit, query) - Toggle whether the drag should try to track geometry. The context will compute a track plane by intersecting the initial press with geometry or the live object.
        trackScale: (create, edit, query) - Specify the distance to the track plane from the camera. The smaller the scale the slower the drag.
    """
    pass


def transformCompare(*args, root: bool = bool):
    """
    Compares two transforms passed as arguments. If they are the same, returns 0. If they are different, returns 1. If no transforms are specified in the command line, then the transforms from the active list are used.

    Args:
        root: (create) - Compare the root only, rather than the entire hierarchy below the roots.
    """
    pass


def transformLimits(*args, enableRotationX: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableRotationY: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableRotationZ: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableScaleX: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableScaleY: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableScaleZ: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableTranslationX: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableTranslationY: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], enableTranslationZ: Optional[Union[Tuple[bool, bool], bool]] = [bool, bool], remove: bool = bool, rotationX: Optional[Union[Tuple[float, float], bool]] = [float, float], rotationY: Optional[Union[Tuple[float, float], bool]] = [float, float], rotationZ: Optional[Union[Tuple[float, float], bool]] = [float, float], scaleX: Optional[Union[Tuple[float, float], bool]] = [float, float], scaleY: Optional[Union[Tuple[float, float], bool]] = [float, float], scaleZ: Optional[Union[Tuple[float, float], bool]] = [float, float], translationX: Optional[Union[Tuple[float, float], bool]] = [float, float], translationY: Optional[Union[Tuple[float, float], bool]] = [float, float], translationZ: Optional[Union[Tuple[float, float], bool]] = [float, float], edit: bool = bool, query: bool = bool):
    """
    The transformLimits command allows us to set, edit, or query the limits of the transformation that can be applied to objects.

    Args:
        enableRotationX: (query) - enable/disable the lower and upper x-rotation limits When queried, it returns boolean boolean
        enableRotationY: (query) - enable/disable the lower and upper y-rotation limits When queried, it returns boolean boolean
        enableRotationZ: (query) - enable/disable the lower and upper z-rotation limits When queried, it returns boolean boolean
        enableScaleX: (query) - enable/disable the lower and upper x-scale limits When queried, it returns boolean boolean
        enableScaleY: (query) - enable/disable the lower and upper y-scale limits When queried, it returns boolean boolean
        enableScaleZ: (query) - enable/disable the lower and upper z-scale limits When queried, it returns boolean boolean
        enableTranslationX: (query) - enable/disable the  ower and upper x-translation limits When queried, it returns boolean boolean
        enableTranslationY: (query) - enable/disable the lower and upper y-translation limits When queried, it returns boolean boolean
        enableTranslationZ: (query) - enable/disable the lower and upper z-translation limits When queried, it returns boolean boolean
        remove: (create) - turn all the limits off and reset them to their default values
        rotationX: (query) - set the lower and upper x-rotation limits When queried, it returns angle angle
        rotationY: (query) - set the lower and upper y-rotation limits When queried, it returns angle angle
        rotationZ: (query) - set the lower and upper z-rotation limits When queried, it returns angle angle
        scaleX: (query) - set the lower and upper x-scale limits When queried, it returns float float
        scaleY: (query) - set the lower and upper y-scale limits When queried, it returns float float
        scaleZ: (query) - set the lower and upper z-scale limits When queried, it returns float float
        translationX: (query) - set the lower and upper x-translation limits When queried, it returns linear linear
        translationY: (query) - set the lower and upper y-translation limits When queried, it returns linear linear
        translationZ: (query) - set the lower and upper z-translation limits When queried, it returns linear linear
    """
    pass


def tumbleCtx(*args, alternateContext: bool = bool, autoOrthoConstrain: bool = bool, autoSetPivot: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, localTumble: Optional[Union[int, bool]] = int, name: Optional[Union[str, bool]] = str, objectTumble: bool = bool, orthoLock: bool = bool, orthoStep: Optional[Union[float, bool]] = float, toolName: Optional[Union[str, bool]] = str, tumbleScale: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a tumble context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        autoOrthoConstrain: (create, edit, query) - Automatically constrain horizontal and vertical rotations when the camera is orthographic. The shift key can be used to unconstrain the rotation.
        autoSetPivot: (create, edit, query) - Automatically set the camera pivot to the selection or tool effect region
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localTumble: (create, edit, query) - Describes what point the camera will tumble around:  0 for the camera's tumble pivot 1 for the camera's center of interest 2 for the camera's local axis, offset by its tumble pivot
        name: (create) - If this is a tool command, name the tool appropriately.
        objectTumble: (create, edit, query) - Make the camera tumble around the selected object, if true.
        orthoLock: (create, edit, query) - Orthographic cameras cannot be tumbled while orthoLock is on.
        orthoStep: (create, edit, query) - Specify the angular step in degrees for orthographic rotation. If camera is orthographic and autoOrthoConstrain is toggled on the rotation will be stepped by this amount.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        tumbleScale: (create, edit, query) - Set the rotation speed. A tumble scale of 1.0 will result in in 40 degrees of rotation per 100 pixels of cursor drag.
    """
    pass


def twoPointArcCtx(*args, degree: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, spans: Optional[Union[int, bool]] = int, edit: bool = bool, query: bool = bool):
    """
    The twoPointArcCtx command creates a new context for creating two point circular arcs

    Args:
        degree: (create, edit, query) - Valid values are 1 or 3. Default degree 3.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        spans: (create, edit, query) - Default is 4.
    """
    pass


def ungroup(*args, absolute: bool = bool, parent: Optional[Union[str, bool]] = str, relative: bool = bool, world: bool = bool):
    """
    This command ungroups the specified objects.

    Args:
        absolute: (create) - preserve existing world object transformations (overall object transformation is preserved by modifying the objects local transformation) [default]
        parent: (create) - put the ungrouped objects under the given parent
        relative: (create) - preserve existing local object transformations (don't modify local transformation)
        world: (create) - put the ungrouped objects under the world
    """
    pass


def upAxis(*args, axis: Optional[Union[str, bool]] = str, rotateView: bool = bool, query: bool = bool):
    """
    The upAxis command changes the world up direction. Current implementation provides only two choices of axis (the Y-axis or the Z-axis) as the world up direction.

    Args:
        axis: (query) - This flag specifies the axis as the world up direction. The valid axis are either "y" or "z". When queried, it returns a string.
        rotateView: (create) - This flag specifies to rotate the view as well.
    """
    pass


def view2dToolCtx(*args, alternateContext: bool = bool, boxzoom: bool = bool, dolly: bool = bool, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, toolName: Optional[Union[str, bool]] = str, track: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the Hypergraph.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        boxzoom: (create, query) - Perform Box Zoom
        dolly: (create, query) - Dollies the view
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        track: (create, query) - Tracks the view
    """
    pass


def walkCtx(*args, alternateContext: bool = bool, crouchCount: Optional[Union[float, bool]] = float, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, toolName: Optional[Union[str, bool]] = str, walkHeight: Optional[Union[float, bool]] = float, walkSensitivity: Optional[Union[float, bool]] = float, walkSpeed: Optional[Union[float, bool]] = float, walkToolHud: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command can be used to create, edit, or query a walk context.

    Args:
        alternateContext: (create, query) - Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.
        crouchCount: (create, edit, query) - The camera crouch count.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        toolName: (create, query) - Name of the specific tool to which this command refers.
        walkHeight: (create, edit, query) - The camera initial height.
        walkSensitivity: (create, edit, query) - The camera rotate sensitivity.
        walkSpeed: (create, edit, query) - The camera move speed.
        walkToolHud: (create, edit, query) - Control whether show walk tool HUD.
    """
    pass


def weightsColor(*args, colorRamp: Optional[Union[str, bool]] = str, deformer: Optional[Union[str, bool]] = str, falseColor: bool = bool, outOfRangeColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMaxColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), rampMinColor: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), useColorRamp: bool = bool, useMaxMinColor: bool = bool, query: bool = bool):
    """
    Controls the coloring of deformer weights.

    Args:
        colorRamp: (query) - Allows a user defined color ramp to be used to map values to colors.
        deformer: (query) - Specify the deformer that needs to be visualized.
        falseColor: (query) - Enable or disable false color display on the geometry.
        outOfRangeColor: (query) - Defines a special color to be used for the areas outside the deformers subset.
        rampMaxColor: (query) - Defines a special color to be used when the value is greater than or equal to the maximum value.
        rampMinColor: (query) - Defines a special color to be used when the value is less than or equal to the minimum value.
        useColorRamp: (query) - Specifies whether the user defined color ramp should be used to map values from to colors. If this is turned off, the default greyscale feedback will be used.
        useMaxMinColor: (query) - Specifies whether the out of range colors should be used.  See rampMinColor and rampMaxColor flags for further details.
    """
    pass


def wireContext(*args, crossingEffect: Optional[Union[float, bool]] = float, deformationOrder: Optional[Union[str, bool]] = str, dropoffDistance: Optional[Union[float, bool]] = float, envelope: Optional[Union[float, bool]] = float, exclusive: bool = bool, exclusivePartition: Optional[Union[str, bool]] = str, exists: bool = bool, groupWithBase: bool = bool, history: bool = bool, holder: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, localInfluence: Optional[Union[float, bool]] = float, name: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a tool that can be used to create a wire deformer.

    Args:
        crossingEffect: (create, edit, query) - Set the amount of convolution filter effect. Varies from fully convolved at 0 to a simple additive effect at 1. Default is 0.
        deformationOrder: (create, edit, query) - Set the appropriate flag that determines the position in in the deformation hierarchy.
        dropoffDistance: (create, edit, query) - Set the dropoff Distance for the wires.
        envelope: (create, edit, query) - Set the envelope value for the deformer. Default is 1.0
        exclusive: (create, edit, query) - Set exclusive mode on or off.
        exclusivePartition: (create, edit, query) - Set the name of an exclusive partition.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        groupWithBase: (create, edit, query) - Groups the wire with the base wire so that they can easily be moved together to create a ripple effect. Default is false.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        holder: (create, edit) - Controls whether the user can specify holders for the wires from the wire context. A holder is a curve that you can use to limit the wire's deformation region. Default is false.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        localInfluence: (create, edit, query) - Set the amount of local influence a wire has with respect to other wires. Default is 0.
        name: (create) - If this is a tool command, name the tool appropriately.
    """
    pass


def wrinkleContext(*args, branchCount: Optional[Union[int, bool]] = int, branchDepth: Optional[Union[int, bool]] = int, exists: bool = bool, history: bool = bool, image1: Optional[Union[str, bool]] = str, image2: Optional[Union[str, bool]] = str, image3: Optional[Union[str, bool]] = str, name: Optional[Union[str, bool]] = str, randomness: Optional[Union[float, bool]] = float, style: Optional[Union[str, bool]] = str, thickness: Optional[Union[float, bool]] = float, wrinkleCount: Optional[Union[int, bool]] = int, wrinkleIntensity: Optional[Union[float, bool]] = float, edit: bool = bool, query: bool = bool):
    """
    This command creates a context that creates wrinkles.

    Args:
        branchCount: (create, edit, query) - Set the number of branches spawned from a crease for radial wrinkles. Default is 2.
        branchDepth: (create, edit, query) - Set the depth of branching for radial wrinkles. Defaults to 0.
        exists: (create) - Returns true or false depending upon whether the specified object exists. Other flags are ignored.
        history: (create) - If this is a tool command, turn the construction history on for the tool in question.
        image1: (create, edit, query) - First of three possible icons representing the tool associated with the context.
        image2: (create, edit, query) - Second of three possible icons representing the tool associated with the context.
        image3: (create, edit, query) - Third of three possible icons representing the tool associated with the context.
        name: (create) - If this is a tool command, name the tool appropriately.
        randomness: (create, edit, query) - Set the deviation of the wrinkle creases from straight lines and other elements of the wrinkle structure. Defaults to 0.2.
        style: (create, edit, query) - Set the wrinkle characteristic shape."lines"|"radial"|"custom. Default is "radial".
        thickness: (create, edit, query) - Set the thickness of wrinkle creases by setting the dropoff distance on the underlying wires.
        wrinkleCount: (create, edit, query) - Set the number of wrinkle creases. Default is 3.
        wrinkleIntensity: (create, edit, query) - Set the depth intensity of the wrinkle furrows. Defaults to 0.5.
    """
    pass


def xform(*args, absolute: bool = bool, boundingBox: bool = bool, boundingBoxInvisible: bool = bool, centerPivots: bool = bool, centerPivotsOnComponents: bool = bool, deletePriorHistory: bool = bool, euler: bool = bool, matrix: Optional[Union[Tuple[float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], bool]] = [float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float], objectSpace: bool = bool, pivots: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], preserve: bool = bool, preserveUV: bool = bool, reflection: bool = bool, reflectionAboutBBox: bool = bool, reflectionAboutOrigin: bool = bool, reflectionAboutX: bool = bool, reflectionAboutY: bool = bool, reflectionAboutZ: bool = bool, reflectionTolerance: Optional[Union[float, bool]] = float, relative: bool = bool, rotateAxis: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], rotateOrder: Optional[Union[str, bool]] = str, rotatePivot: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], rotateTranslation: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], rotation: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], scale: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), scalePivot: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], scaleTranslation: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], shear: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), translation: Optional[Union[Tuple[float, float, float], bool]] = [float, float, float], worldSpace: bool = bool, worldSpaceDistance: bool = bool, zeroTransformPivots: bool = bool, query: bool = bool):
    """
    

    Args:
        absolute: (create) - perform absolute transformation (default)
        boundingBox: (query) - Returns the bounding box of an object. The values returned are in the following order: xmin ymin zmin xmax ymax zmax.
        boundingBoxInvisible: (query) - Returns the bounding box of an object. This includes the bounding boxes of all invisible children which are not included using the boundingBox flag. The values returned are in following order: xmin ymin zmin xmax ymax zmax.
        centerPivots: (create) - Set pivot points to the center of the object's bounding box. (see -p flag)
        centerPivotsOnComponents: (create) - Set pivot points to the center of the component's bounding box. (see -p flag)
        deletePriorHistory: (create) - If true then delete the construction history before the operation is performed.
        euler: (create) - modifer for -relative flag that specifies rotation values should be added to current XYZ rotation values.
        matrix: (create, query) - Sets/returns the composite transformation matrix. *Note* the matrix is represented by 16 double arguments that are specified in row order.
        objectSpace: (create, query) - treat values as object-space transformation values (only works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags)
        pivots: (create, query) - convenience method that changes both the rotate and scale pivots simultaneously. (see -rp -sp flags for more info)
        preserve: (create) - preserve overall transformation. used to prevent object from "jumping" when changing pivots or rotation order. the default value is true. (used with -sp, -rp, -roo, -cp, -ra)
        preserveUV: (create) - When true, UV values on rotated components are projected across the rotation in 3d space. For small edits, this will freeze the world space texture mapping on the object. When false, the UV values will not change for a selected vertices. Default is false.
        reflection: (create) - To move the corresponding symmetric components also.
        reflectionAboutBBox: (create) - Sets the position of the reflection axis  at the geometry bounding box
        reflectionAboutOrigin: (create) - Sets the position of the reflection axis  at the origin
        reflectionAboutX: (create) - Specifies the X=0 as reflection plane
        reflectionAboutY: (create) - Specifies the Y=0 as reflection plane
        reflectionAboutZ: (create) - Specifies the Z=0 as reflection plane
        reflectionTolerance: (create) - Specifies the tolerance to findout the corresponding reflected components
        relative: (create) - perform relative transformation
        rotateAxis: (create, query) - rotation axis orientation (when used with the -p flag the overall rotation is preserved by modifying the rotation to compensate for the axis rotation)
        rotateOrder: (create, query) - rotation order (when used with the -p flag the overall rotation is preserved by modifying the local rotation to be quivalent to the old one) Valid values for this flag are <xyz | yzx | zxy | xzy | yxz | zyx>
        rotatePivot: (create, query) - rotate pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the rotation translation)
        rotateTranslation: (create, query) - rotation translation
        rotation: (create, query) - rotation transformation
        scale: (create, query) - scale transformation
        scalePivot: (create, query) - scale pivot point transformation (when used with the -p flag the overall transformation is preserved by modifying the scale translation)
        scaleTranslation: (create, query) - scale translation
        shear: (create, query) - shear transformation. The values represent the shear <xy,xz,yz>
        translation: (create, query) - translation
        worldSpace: (create, query) - (works for pivots, translations, rotation, rotation axis, matrix, and bounding box flags). Note that, when querying the scale, that this calculation is cumulative and is only valid if there are all uniform scales and no rotation. In a hierarchy with non-uniform scale and rotation, this value may not correspond entirely with the perceived global scale.
        worldSpaceDistance: (create, query) - Values for -sp, -rp, -st, -rt, -t, -piv flags are treated as world space distances to move along the local axis. (where the local axis depends on whether the command is operating in local-space or object-space. This flag has no effect for world space.
        zeroTransformPivots: (create) - reset pivot points and pivot translations without changing the overall matrix by applying these values into the translation channel.
    """
    pass


def xformConstraint(*args, alongNormal: Optional[Union[int, bool]] = int, live: bool = bool, type: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command allows you to change the transform constraint used by the transform tools during component transforms.

    Args:
        alongNormal: (edit, query) - When set the transform constraint will first be applied along the vertex normals of the components being transformed. When queried, returns the current state of this option.
        live: (query) - Query-only flag that can be used to check whether the current live surface will be used as a transform constraint.
        type: (create, edit, query) - Set the type of transform constraint to use. When queried, returns the current transform constraint as a string.  none - no constraint surface - constrain components to their surface edge - constrain components to surface edges
    """
    pass


