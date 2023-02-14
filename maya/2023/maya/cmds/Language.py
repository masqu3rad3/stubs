from typing import Union, Optional, List, Tuple

def assignCommand(*args, addDivider: str = str, altModifier: bool = bool, annotation: Optional[Union[str, bool]] = str, command: Optional[Union[str, bool]] = str, commandModifier: bool = bool, ctrlModifier: bool = bool, data1: Optional[Union[str, bool]] = str, data2: Optional[Union[str, bool]] = str, data3: Optional[Union[str, bool]] = str, delete: int = int, dividerString: Optional[Union[str, bool]] = str, enableCommandRepeat: bool = bool, factorySettings: bool = bool, index: int = int, keyArray: bool = bool, keyString: Optional[Union[str, bool]] = str, keyUp: bool = bool, name: bool = bool, numDividersPreceding: Optional[Union[int, bool]] = int, numElements: bool = bool, optionModifier: bool = bool, sortByKey: bool = bool, sourceUserCommands: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command allows the user to assign hotkeys and manipulate the internal array of named command objects. Each object in the array has an 1-based index which is used for referencing. Under expected usage you should not need to use this command directly as the Hotkey Editor may be used to assign hotkeys.

    Args:
        addDivider: (edit) - Appends an "annotated divider" item to the end of the list of commands.
        altModifier: (edit) - This flag specifies if an alt modifier is used for the key.
        annotation: (edit, query) - The string is the english name describing the command.
        command: (edit, query) - This is the command that is executed when this object is mapped to a key or menuItem.
        commandModifier: (edit) - This flag specifies if a command modifier is used for the key. This is only available on systems which support a separate command key.
        ctrlModifier: (edit) - This flag specifies if a ctrl modifier is used for the key.
        data1: (edit, query) - Optional, user-defined data strings may be attached to the nameCommand objects.
        data2: (edit, query) - Optional, user-defined data strings may be attached to the nameCommand objects.
        data3: (edit, query) - Optional, user-defined data strings may be attached to the nameCommand objects.
        delete: (edit) - This tells the Manager to delete the object at position index.
        dividerString: (query) - If the passed index corresponds to a "divider" item, then the divider's annotation is returned.  Otherwise, a null string is returned.
        enableCommandRepeat: (edit) - This flag specifies whether command repeat is enabled.
        factorySettings: (edit) - This flag sets the manager back to factory settings.
        index: (edit) - The index of the object to operate on. The index value ranges from 1 to the number of name command objects.
        keyArray: (query) - This flag returns all of the hotkeys on the command.
        keyString: (edit, query) - This specifies a key to assign a command to in edit mode. In query mode this flag returns the key string, modifiers and indicates if the command is mapped to keyUp or keyDown.
        keyUp: (edit) - This flag specifies if the command is executed on keyUp or keyDown.
        name: (query) - The name of the command object.
        numDividersPreceding: (query) - If the index of a namedCommand object C is passed in, then this flag returns the number of "divider" items preceding C when the namedCommands are sorted by category.
        numElements: (query) - This command returns the number of namedCommands in the system. This flag doesn't require the index to be specified.
        optionModifier: (edit) - This flag specifies if an option modifier is used for the key.
        sortByKey: (edit, query) - This key tells the manager to sort by key or by order of creation.
        sourceUserCommands: (edit) - This command sources the user named command file.
    """
    pass


def commandEcho(*args, addFilter: Optional[Union[List[str], bool]] = [str], filter: Optional[Union[List[str], bool]] = [str], lineNumbers: bool = bool, state: bool = bool, query: bool = bool):
    """
    This command controls what is echoed to the command window.

    Args:
        addFilter: (create) - This flag allows you to append filters to the current list of filtered commands when echo all commands is enabled. Just like the filter flag, you can provide a partial command name, so all commands that start with a substring specified in the addFilter entry will be filtered out.
        filter: (create, query) - This flag allows you to filter out unwanted commands when echo all commands is enabled. You can provide a partial command name, so all commands that start with a substring specified in filter entry will be filtered out. If filter is empty, all commands are echoed to the command window.
        lineNumbers: (create, query) - If true then file name and line number information is provided in error and warning messages. If false then no file name and line number information is provided in error and warning messages.
        state: (create, query) - If true then all commands are echoed to the command window. If false then only relevant commands are echoed.
    """
    pass


def condition(*args, delete: bool = bool, dependency: Optional[Union[str, bool]] = str, initialize: bool = bool, script: Optional[Union[str, bool]] = str, state: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a new named condition object whose true/false value is calculated by running a mel script. This new condition can then be used for dimming, or controlling other scripts, or whatever.

    Args:
        delete: (create) - Deletes the condition.
        dependency: (create, multiuse) - Each -dependency flag specifies another condition that the new condition will be dependent on.  When any of these conditions change, the new-state-script will run, and the state of this condition will be set accordingly.  It is possible to define infinite loops, but they will be caught and handled correctly at run-time.
        initialize: (create) - Initializes the condition, by forcing it to run its script as soon as it is created.  If this flag is not specified, the script will not run until one of the dependencies is triggered.
        script: (create) - The script that determines the new state of the condition.
        state: (create, edit, query) - Sets the state of the condition. This can be used to create a manually triggered condition: you could create a condition without any dependencies and without a new-state-script. This condition would only change state in response to the -st/state flag.
    """
    pass


def connectControl(*args, fileName: bool = bool, index: Optional[Union[int, bool]] = int, preventContextualMenu: bool = bool, preventOverride: bool = bool):
    """
    This command attaches a UI widget, specified as the first argument, to one or more dependency node attributes. The attributes/nodes don't have to exist yet, they will get looked up as needed. With no flag specified, this command works on these kinds of controls: floatField, floatScrollBar, floatSlider, intField, intScrollBar, intSlider, floatFieldGrp, intFieldGrp, checkBox, radioCollection, and optionMenu. With the

    Args:
        fileName: (create) - This flag causes the connection to be treated as a filename, and the conversion from internal to external filename representation is made as the data is copied. This only applies to connections to Tfield controls.
        index: (create) - This flag enables you to pick out a sub-control from a group that contains a number of different controls. For example, you can connect one field of a floatFieldGrp.  You must count each member of the group, including any text labels that may exist.  For example, if you have a check box group with a label, the label will count as index 1, and the first check box as index 2.  (Indices are 1-based)
        preventContextualMenu: (create) - If true, this flag will block the right mouse button menu of the associated control attribute.
        preventOverride: (create) - If true, this flag disallows overriding the control's attribute via the control's right mouse button menu.
    """
    pass


def deleteUI(*args, collection: bool = bool, control: bool = bool, editor: bool = bool, layout: bool = bool, menu: bool = bool, menuItem: bool = bool, panel: bool = bool, panelConfig: bool = bool, radioMenuItemCollection: bool = bool, toolContext: bool = bool, uiTemplate: bool = bool, window: bool = bool):
    """
    This command deletes UI objects such as windows and controls.  Deleting a layout or window will also delete all of its children.  If a flag is used then all objects being deleted must be of the specified type. This command may not be edited or queried.

    Args:
        collection: (create) - Object names for deletion are all radio or tool collections.
        control: (create) - Object names for deletion are all controls.
        editor: (create) - Object names for deletion are all editors.
        layout: (create) - Object names for deletion are all layouts.
        menu: (create) - Object names for deletion are all menus.
        menuItem: (create) - Object names for deletion are all menu items.
        panel: (create) - Object names for deletion are all panels.
        panelConfig: (create) - Object names for deletion are panel configurations.
        radioMenuItemCollection: (create) - Object names for deletion are all radio menu item collections.
        toolContext: (create) - Object names for deletion are all tool contexts.
        uiTemplate: (create) - Object names for deletion are all UI templates.
        window: (create) - Object names for deletion are all windows.
    """
    pass


def dimWhen(*args, clear: bool = bool, false: bool = bool, true: bool = bool):
    """
    This method attaches the named UI object (first argument) to the named condition (second argument) so that the object will be dimmed when the condition is in a particular state.

    Args:
        clear: (create) - Remove the condition on the specified dimmable.
        false: (create) - Dim the object when the condition is false.
        true: (create) - Dim the object when the condition is true. (default)
    """
    pass


def disable(*args, value: bool = bool):
    """
    This command enables or disables the control passed as argument.

    Args:
        value: (create) - If true, this command disables the control. If false, this command enables the control. Default value is true (disable)
    """
    pass


def encodeString(*args):
    """
    This action will take a string and encode any character that would need to be escaped before being sent to some other command. Such characters include:

    Args:
    """
    pass


def eval(*args):
    """
    This function takes a string which contains MEL code and evaluates it using the MEL interpreter. The result is converted into a Python data type and is returned. If an error occurs during the execution of the MEL script, a Python exception is raised with the appropriate error message.

    Args:
    """
    pass


def evalDeferred(*args, evaluateNext: bool = bool, list: bool = bool, lowPriority: bool = bool, lowestPriority: bool = bool):
    """
    This command takes the string it is given and evaluates it during the next available idle time.  It is useful for attaching commands to controls that can change or delete the control.

    Args:
        evaluateNext: (create) - Specified that the command to be executed should be ran with the highest priority, ideally queued up next.
        list: (create) - Return a list of the command strings that are currently pending on the idle queue. By default, it will return the list of commands for all priorities. The -lowestPriority and -lowPriority can be used to restrict the list of commands to a given priority level.
        lowPriority: (create) - Specified that the command to be executed should be deferred with the low priority. That is, it will be executed whenever Maya is idle.
        lowestPriority: (create) - Specified that the command to be executed should be deferred with the lowest priority. That is, it will be executed when no other idle events are scheduled.
    """
    pass


def isTrue(*args):
    """
    This commmand returns the state of the named condition. If the condition is true, it returns 1.  Otherwise it returns 0.

    Args:
    """
    pass


def itemFilter(*args, byBin: Optional[Union[str, bool]] = str, byName: Optional[Union[str, bool]] = str, byScript: Optional[Union[str, bool]] = str, byType: Optional[Union[str, bool]] = str, category: Optional[Union[str, bool]] = str, classification: Optional[Union[str, bool]] = str, clearByBin: bool = bool, clearByType: bool = bool, difference: Optional[Union[Tuple[str, str], bool]] = [str, str], exists: bool = bool, intersect: Optional[Union[Tuple[str, str], bool]] = [str, str], listBuiltInFilters: bool = bool, listOtherFilters: bool = bool, listUserFilters: bool = bool, negate: bool = bool, parent: Optional[Union[str, bool]] = str, pythonModule: Optional[Union[str, bool]] = str, secondScript: Optional[Union[str, bool]] = str, text: Optional[Union[str, bool]] = str, union: Optional[Union[Tuple[str, str], bool]] = [str, str], uniqueNodeNames: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a named itemFilter object.  This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them.  Using union, intersection and difference filters, complex composite filters can be created.

    Args:
        byBin: (create, edit, multiuse, query) - The filter will only pass items whose bin list contains the given string as a bin name. This is a multi-use flag. If more than one occurance of this flag is used in a single command, the filter will accept a node if it matches at least one of the given bins (in other words, a union or logical or of all given bins.
        byName: (create, edit, query) - The filter will only pass items whose names match the given regular expression string.  This string can contain the special characters * and ?.  '?' matches any one character, and '*' matches any substring.
        byScript: (create, edit, query) - The filter will run a MEL script named by the given string on each item name.  Items will pass the filter if the script returns a non-zero value. The script name string must be the name of a proc whose signature is: global proc int procName( string $name ) or def procName(*args, **keywordArgs) if -pym/pythonModule is specified. Note that if -secondScript is also used, it will always take precedence.
        byType: (create, edit, multiuse, query) - The filter will only pass items whose typeName matches the given string.  The typeName of an object can be found using the nodeType command.  This is a multi-use flag. If more than one occurance of this flag is used in a single command, the filter will accept a node if it matches at least one of the given types (in other words, a union or logical or of all given types.
        category: (create, edit, multiuse, query) - A string for categorizing the filter.
        classification: (create, edit, query) - Indicates whether the filter is a built-in or user filter. The string argument must be either "builtIn" or "user". The "other" classification is deprecated. Use "user" instead.  Filters will not be deleted by a file new, and filter nodes will be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and will not be accessible from the command-line.
        clearByBin: (create, edit) - This flag will clear any existing bins associated with this filter.
        clearByType: (create, edit) - This flag will clear any existing typeNames associated with this filter.
        difference: (create, edit, query) - The filter will consist of the set difference of two other filters, whose names are the given strings. Items will pass this filter if and only if they pass the first filter but not the second filter.
        exists: (create) - Returns true|false depending upon whether the specified object exists. Other flags are ignored.
        intersect: (create, edit, query) - The filter will consist of the intersection of two other filters, whose names are the given strings. Items will pass this filter if and only if they pass both of the contained filters.
        listBuiltInFilters: (query) - Returns an array of all item filters with classification "builtIn".
        listOtherFilters: (query) - The "other" classification is deprecated. Use "user" instead. Returns an array of all item filters with classification "other".
        listUserFilters: (query) - Returns an array of all item filters with classification "user".
        negate: (create, edit, query) - This flag can be used to cause the filter to invert itself, and reverse what passes and what fails.
        parent: (create, edit, query) - Optional.  If specified, the filter's life-span is linked to that of the parent.  When the parent goes out of scope, so does the filter.  If not specified, the filter will exist until explicitly deleted.
        pythonModule: (create, edit, query) - Treat -bs/byScript and -ss/secondScript as Python functions located in the specified module.
        secondScript: (create, edit, query) - Cannot be used in conjunction with the -bs flag.  The second script is for filtering whole lists at once, rather than individually.  Its signature must be: global proc string[] procName( string[] $name ) or def procName(*args, **keywordArgs) if -pym/pythonModule is specified. It should take in a list of items, and return a filtered list of items.
        text: (create, edit, query) - Defines an annotation string to be stored with the filter
        union: (create, edit, query) - The filter will consist of the union of two other filters, whose names are the given strings. Items will pass this filter if they pass at least one of the contained filters.
        uniqueNodeNames: (create, edit, query) - Returns unique node names to script filters so there are no naming conflicts.
    """
    pass


def itemFilterAttr(*args, byName: Optional[Union[str, bool]] = str, byNameString: Optional[Union[str, bool]] = str, byScript: Optional[Union[str, bool]] = str, classification: Optional[Union[str, bool]] = str, dynamic: bool = bool, exists: bool = bool, hasCurve: bool = bool, hasDrivenKey: bool = bool, hasExpression: bool = bool, hidden: bool = bool, intersect: Optional[Union[Tuple[str, str], bool]] = [str, str], keyable: bool = bool, listBuiltInFilters: bool = bool, listOtherFilters: bool = bool, listUserFilters: bool = bool, negate: bool = bool, parent: str = str, published: bool = bool, readable: bool = bool, scaleRotateTranslate: bool = bool, secondScript: Optional[Union[str, bool]] = str, text: Optional[Union[str, bool]] = str, union: Optional[Union[Tuple[str, str], bool]] = [str, str], writable: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a named itemFilterAttr object.  This object can be attached to editors, in order to filter the attributes going through them. Using union and intersection filters, complex composite filters can be created.

    Args:
        byName: (create, edit, query) - The filter will only pass items whose names match the given regular expression string.  This string can contain the special characters * and ?.  '?' matches any one character, and '*' matches any substring. This flag cannot be used in conjunction with the -byScript or -secondScript flags.
        byNameString: (create, edit, multiuse, query) - The filter will only pass items whose names match the given string. This is a multi-use flag which allows the user to specify several strings. The filter will pass items that match any of the strings. This flag cannot be used in conjunction with the -byScript or -secondScript flags.
        byScript: (create, edit, query) - The filter will run a MEL script named by the given string on each attribute name.  Attributes will pass the filter if the script returns a non-zero value. The script name string must be the name of a proc whose signature is: global proc int procName( string $nodeName string $attrName ) This flag cannot be used in conjunction with the -byName or -byNameString flags.
        classification: (create, edit, query) - Indicates whether the filter is a built-in or user filter. The string argument must be either "builtIn" or "user". The "other" filter classification is deprecated. Use "user" instead.  Filters created by Maya should be classified as "builtIn". Filters created by plugins or user scripts should be classified as "user".  Filters will not be deleted by a file new. Filter nodes will be hidden from the UI (ex: Attribute Editor, Hypergraph etc) and will not be accessible from the command-line.
        dynamic: (create, edit, query) - The filter will only pass dynamic attributes
        exists: (create, edit, query) - The filter will only pass attributs that exist
        hasCurve: (create, edit, query) - The filter will only pass attributes that are driven by animation curves.
        hasDrivenKey: (create, edit, query) - The filter will only pass attributes that are driven by driven keys
        hasExpression: (create, edit, query) - The filter will only pass attributes that are driven by expressions
        hidden: (create, edit, query) - The filter will only pass attributes that are hidden to the user
        intersect: (create, edit, query) - The filter will consist of the intersection of two other filters, whose names are the given strings. Attributes will pass this filter if and only if they pass both of the contained filters.
        keyable: (create, edit, query) - The filter will only pass attributes that are keyable
        listBuiltInFilters: (query) - Returns an array of all attribute filters with classification "builtIn".
        listOtherFilters: (query) - The "other" classification has been deprecated. Use "user" instead. Returns an array of all attribute filters with classification "other".
        listUserFilters: (query) - Returns an array of all attribute filters with classification "user".
        negate: (create, edit, query) - This flag can be used to cause the filter to invert itself, and reverse what passes and what fails.
        parent: () - This flag is no longer supported.
        published: (create, edit, query) - The filter will only pass attributes that are published on the container.
        readable: (create, edit, query) - The filter will only pass attributes that are readable (outputs)
        scaleRotateTranslate: (create, edit, query) - The filter will show only SRT attributes: scale, rotate, translate and their children
        secondScript: (create, edit, query) - Can be used in conjunction with the -bs flag.  The second script is for filtering whole lists at once, rather than individually.  Its signature must be: global proc string[] procName( string[] $nodeName string[] $attrName ) It should take in a list of attributes, and return a filtered list of attributes. This flag cannot be used in conjunction with the -byName or -byNameString flags.
        text: (create, edit, query) - Defines an annotation string to be stored with the filter
        union: (create, edit, query) - The filter will consist of the union of two other filters, whose names are the given strings. Attributes will pass this filter if they pass at least one of the contained filters.
        writable: (create, edit, query) - The filter will only pass attributes that are writable (inputs)
    """
    pass


def itemFilterType(*args, text: Optional[Union[str, bool]] = str, type: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command queries a named itemFilter object.  This object can be attached to selectionConnection objects, or to editors, in order to filter the item lists going through them.  Using union and intersection filters, complex composite filters can be created.

    Args:
        text: (edit, query) - Defines an annotation string to be stored with the filter
        type: (query) - Query the type of the filter object. Possible return values are: itemFilter, attributeFilter, renderFilter, or unknownFilter.
    """
    pass


def lsUI(*args, cmdTemplates: bool = bool, collection: bool = bool, contexts: bool = bool, controlLayouts: bool = bool, controls: bool = bool, dumpWidgets: bool = bool, editors: bool = bool, head: Optional[Union[int, bool]] = int, long: bool = bool, menuItems: bool = bool, menus: bool = bool, numWidgets: bool = bool, panels: bool = bool, radioMenuItemCollections: bool = bool, tail: Optional[Union[int, bool]] = int, type: Optional[Union[str, bool]] = str, windows: bool = bool, workspaceControls: bool = bool):
    """
    This command returns the names of UI objects.

    Args:
        cmdTemplates: (create) - UI command templates created using ELF UI commands.
        collection: (create) - Control collections created using ELF UI commands.
        contexts: (create) - Tool contexts created using ELF UI commands.
        controlLayouts: (create) - Control layouts created using ELF UI commands [e.g. formLayouts, paneLayouts, etc.]
        controls: (create) - Controls created using ELF UI commands. [e.g. buttons, checkboxes, etc]
        dumpWidgets: (create) - Dump all QT widgets used by Maya.
        editors: (create) - All currently existing editors.
        head: (create) - The parameter specifies the maximum number of elements to be returned from the beginning of the list of items. (Note: each flag will return at most this many items so if multiple flags are specified then the number of items returned will be greater than the value specified).
        long: (create) - Use long pathnames instead of short non-path names.
        menuItems: (create) - Menu items created using ELF UI commands.
        menus: (create) - Menus created using ELF UI commands.
        numWidgets: (create) - Reports the number of QT widgets used by Maya.
        panels: (create) - All currently existing panels.
        radioMenuItemCollections: (create) - Menu item collections created using ELF UI commands.
        tail: (create) - The parameter specifies the maximum number of elements to be returned from the end of the list of items. (Note: each flag will return at most this many items so if multiple flags are specified then the number of items returned will be greater than the value specified).
        type: (create, multiuse) - List all objects of a certain type specified by the string argument. For example, "window", "menu", "control", or "controlLayout".
        windows: (create) - Windows created using ELF UI commands.
        workspaceControls: (create) - Workspace controls created using ELF UI commands.
    """
    pass


def matrixUtil(*args, inverse: bool = bool, quaternion: Optional[Union[Tuple[float, float, float, float], bool]] = [float, float, float, float], relative: bool = bool, rotation: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), scale: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), shear: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), translation: Optional[Union[Tuple[float, float, float], bool]] = (float, float, float), transpose: bool = bool, edit: bool = bool, query: bool = bool):
    """
    Command to deal with matrix, composition and decomposition

    Args:
        inverse: (create, edit, query) - Compose or query will return the inversed matrix.
        quaternion: (create, edit, query) - Compose, edit or query a matrix using specified quaternion values as rotation components.
        relative: (create, edit, query) - Add translation, rotation, scale or shear, instead of seting it as absolute.
        rotation: (create, edit, query) - Compose, edit or query a matrix using specified values as rotation components.
        scale: (create, edit, query) - Compose, edit or query a matrix using specified values as scale components.
        shear: (create, edit, query) - Compose, edit or query a matrix using specified values as shear components.
        translation: (create, edit, query) - Compose a matrix using specified values as translation components.
        transpose: (create, edit, query) - Compose or query will return the transposed matrix.
    """
    pass


def melOptions(*args, duplicateVariableWarnings: bool = bool, query: bool = bool):
    """
    Set and query options that affect the behavior of Maya's Embedded Language (MEL).

    Args:
        duplicateVariableWarnings: (create, query) - When turned on, this option will cause a warning to be generated whenever a MEL variable is declared within the same scope as another variable with the same name. The warnings will be generated when the script is sourced, not when it is executed. Usually these warnings indicate an error in the script.  On query the current setting of the option will be returned.  The corresponding preference optionVar is melDuplicateVariableWarnings.
    """
    pass


def objectTypeUI(*args, isType: Optional[Union[str, bool]] = str, listAll: bool = bool, superClasses: bool = bool):
    """
    This command returns the type of UI element such as button, sliders, etc.

    Args:
        isType: (create) - Returns true|false if the object is of the specified type.
        listAll: (create) - Returns a list of all known UI commands and their respective types. Each entry contains three strings which are the command name, ui type and class name. Note that the class name is internal and is subject to change.
        superClasses: (create) - Returns a list of the names of all super classes for the given object. Note that all class names are internal and are subject to change.
    """
    pass


def optionVar(*args, arraySize: Optional[Union[str, bool]] = str, category: Optional[Union[str, bool]] = str, clearArray: Optional[Union[str, bool]] = str, clearStash: Optional[Union[str, bool]] = str, default: bool = bool, exists: Optional[Union[str, bool]] = str, floatArray: Optional[Union[str, bool]] = str, floatValue: Optional[Union[Tuple[str, float], bool]] = [str, float], floatValue2: Optional[Union[Tuple[str, float, float], bool]] = [str, float, float], floatValue3: Optional[Union[Tuple[str, float, float, float], bool]] = [str, float, float, float], floatValue4: Optional[Union[Tuple[str, float, float, float, float], bool]] = [str, float, float, float], floatValueAppend: Optional[Union[Tuple[str, float], bool]] = [str, float], init: bool = bool, intArray: Optional[Union[str, bool]] = str, intValue: Optional[Union[Tuple[str, int], bool]] = [str, int], intValue2: Optional[Union[Tuple[str, int, int], bool]] = [str, int, int], intValue3: Optional[Union[Tuple[str, int, int, int], bool]] = [str, int, int, int], intValue4: Optional[Union[Tuple[str, int, int, int, int], bool]] = [str, int, int, int, int], intValueAppend: Optional[Union[Tuple[str, int], bool]] = [str, int], list: bool = bool, listCategories: bool = bool, listModified: bool = bool, prefFile: Optional[Union[str, bool]] = str, remove: Optional[Union[str, bool]] = str, removeFromArray: Optional[Union[Tuple[str, int], bool]] = [str, int], stash: Optional[Union[str, bool]] = str, stringArray: Optional[Union[str, bool]] = str, stringValue: Optional[Union[Tuple[str, str], bool]] = [str, str], stringValueAppend: Optional[Union[Tuple[str, str], bool]] = [str, str], transient: bool = bool, unstash: Optional[Union[str, bool]] = str, version: Optional[Union[int, bool]] = int, query: bool = bool):
    """
    This command allows you to set and query variables which are persistent between different invocations of Maya.  These variables are stored as part of the preferences.

    Args:
        arraySize: (create) - returns the size of the array named "string".  If no such variable exists, it returns 0.  If the variable is not an array, it returns 1.
        category: (create) - Set category for the specified variables.  This flag can also be combined with list/listModified flags to get all the variables in the specified category.
        clearArray: (create, multiuse) - If there is an array named "string", it is set to be empty. Empty arrays are not saved.
        clearStash: (create, multiuse) - Clear backup copy of a variable.
        default: (create) - The variable's current and default values will be set to the specified values.  This flag can also be combined with the query flag to get the default value or with the exists flag to determine if a default value has been specified.  It can also be used with list/listModifed flags to list variables with a default value.
        exists: (create) - Returns 1 if a variable named "string" exists, 0 otherwise. The default/transient flags can be used to list variables that have a default value or are transient. All other flags will be ignored if this is used. (Query has higher precedence)
        floatArray: (create, multiuse) - Creates a new empty float array variable named "string". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        floatValue: (create, multiuse) - creates a new variable named "string" with float value "float". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different)
        floatValue2: (create, multiuse) - Creates a new variable named "string" with a 2 element float array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        floatValue3: (create, multiuse) - Creates a new variable named "string" with a 3 element float array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        floatValue4: (create, multiuse) - Creates a new variable named "string" with a 4 element float array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        floatValueAppend: (create, multiuse) - adds this value to the end of the array of floats named "string". If no such array exists, one is created.  If there was a float value with this name before, it becomes the first element of the array.  If any other kind of value existed, it is overridden.
        init: (create) - Used to initialize or reset variables. If the flag is set to true or the variable does not exist then the variable's current and default values will be set to the specified values. If the flag if set to false then only the default value will be set and the current value will not be modified.
        intArray: (create, multiuse) - Creates a new empty int array variable named "string". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        intValue: (create, multiuse) - creates a new variable named "string" with integer value "int". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        intValue2: (create, multiuse) - Creates a new variable named "string" with a 2 element int array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        intValue3: (create, multiuse) - Creates a new variable named "string" with a 3 element int array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        intValue4: (create, multiuse) - Creates a new variable named "string" with a 4 element int array. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        intValueAppend: (create, multiuse) - adds this value to the end of the array of ints named "string". If no such array exists, one is created.  If there was an int value with this name before, it becomes the first element of the array.  If any other kind of value existed, it is overridden.
        list: (create) - This returns a list of all the defined variable names.  The category flag can be used to list variables in the specified category and the default/transient flags can be used to list variables that have a default value or are transient.  All other flags will be ignored if this one is used. (Query and exists flags have a higher precedence).
        listCategories: (create) - This returns a list of all the defined variable categories. All other flags will be ignored if this one is used. (Query and exists flags have a higher precedence).
        listModified: (create) - This returns a list of all the variables that have been changed from their default value.  Variables that don't have a default value will also be returned unless the default flag is used to filter the list to variables that have a default value. The category flag can also be used to filter the list by category.  All other flags will be ignored if this one is used. (Query and exists flags have a higher precedence).
        prefFile: (create, query) - Flag need to be used in conjunction with category Specify where the optionVars from specified category need to be saved when saving preferences.
        remove: (create, multiuse) - removes the variable named "string", if one exists. Note: all removals are done before any value setting, if both the -r and other (-sv, -iv, -fv) flags are used in the same command.
        removeFromArray: (create, multiuse) - removes the element numbered "int" in the array named "string". Everything beyond it then gets shuffled down.
        stash: (create, multiuse) - Make a backup copy of a variable.
        stringArray: (create, multiuse) - Creates a new empty string array variable named "string". If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different).
        stringValue: (create, multiuse) - creates a new variable named using the first string with value given by the second string. If a variable already exists with this name, it is overridden in favour of the new value (even if the type is different)
        stringValueAppend: (create, multiuse) - adds the value given by the second string to the end of the array of strings named by the first string. If no such array exists, one is created. If there was a string value with this name before, it becomes the first element of the array. If any other kind of value existed, it is overridden.
        transient: (create) - Indicates that specified variables will not be persisted across sessions. This flag can also be combined with -exists to determine if a variable is transient.
        unstash: (create, multiuse) - Restore a variable from a backup copy.
        version: (create) - Preferences version number to warn about incompatbile preference files
    """
    pass


def pause(*args, seconds: Optional[Union[int, bool]] = int):
    """
    Pause for a specified number of seconds for canned demos or for test scripts to allow user to view results.

    Args:
        seconds: (create) - Pause for the specified number of seconds.
    """
    pass


def refresh(*args, currentView: bool = bool, fileExtension: Optional[Union[str, bool]] = str, filename: Optional[Union[str, bool]] = str, force: bool = bool, suspend: bool = bool):
    """
    This command is used to force a redraw during script execution. Normally, redraw is suspended while scripts are executing but sometimes it is useful to show intermediate results for purposes such as capturing images from the screen.

    Args:
        currentView: (create) - Redraw only the current view (default redraws all views).
        fileExtension: (create) - Specify the type of file to save using the filename flag.
        filename: (create) - Specify the name of a file in which to save a snapshot of the viewports, or just the current one if the currentView flag is set.
        force: (create) - Force the refresh regardless of the state of the model.
        suspend: (create) - Suspends or resumes Maya's handling of refresh events. Specify "on" to suspend refreshing, and "off" to resume refreshing. Note that resuming refresh does not itself cause a refresh -- the next natural refresh event in Maya after "refresh -suspend off" is issued will cause the refresh to occur. Use this flag with caution: although it provides opportunities to enhance performance, much of Maya's dependency graph evaluation in interactive mode is refresh driven, thus use of this flag may lead to slight solve differences when you have a complex dependency graph with interrelations.
    """
    pass


def renameUI(*args):
    """
    This command renames the UI object passed as first arument to the new name specified as second argument. If the new name is a duplicate, or not valid, then re-naming fails and the old name is returned.

    Args:
    """
    pass


def resourceManager(*args, nameFilter: Optional[Union[str, bool]] = str, saveAs: Optional[Union[Tuple[str, str], bool]] = [str, str]):
    """
    List resources matching certain properties.

    Args:
        nameFilter: (create) - List only resources matching the name. Argument may contain ? and * characters.
        saveAs: (create) - Saves a copy of the resource (first parameter) as a separate file (second parameter).
    """
    pass


def scriptJob(*args, allChildren: bool = bool, attributeAdded: Optional[Union[Tuple[str, str], bool]] = [str, str], attributeChange: Optional[Union[Tuple[str, str], bool]] = [str, str], attributeDeleted: Optional[Union[Tuple[str, str], bool]] = [str, str], compressUndo: bool = bool, conditionChange: Optional[Union[Tuple[str, str], bool]] = [str, str], conditionFalse: Optional[Union[Tuple[str, str], bool]] = [str, str], conditionTrue: Optional[Union[Tuple[str, str], bool]] = [str, str], connectionChange: Optional[Union[Tuple[str, str], bool]] = [str, str], disregardIndex: bool = bool, event: Optional[Union[Tuple[str, str], bool]] = [str, str], exists: Optional[Union[int, bool]] = int, force: bool = bool, idleEvent: Optional[Union[str, bool]] = str, kill: Optional[Union[int, bool]] = int, killAll: bool = bool, killWithScene: bool = bool, listConditions: bool = bool, listEvents: bool = bool, listJobs: bool = bool, nodeDeleted: Optional[Union[Tuple[str, str], bool]] = [str, str], nodeNameChanged: Optional[Union[Tuple[str, str], bool]] = [str, str], optionVarChanged: Optional[Union[Tuple[str, str], bool]] = [str, str], parent: Optional[Union[str, bool]] = str, permanent: bool = bool, protected: bool = bool, replacePrevious: bool = bool, runOnce: bool = bool, timeChange: Optional[Union[str, bool]] = str, uiDeleted: Optional[Union[Tuple[str, str], bool]] = [str, str]):
    """
    This command creates a "script job", which is a MEL command or script.  This job is attached to the named condition, event, or attribute. Each time the condition switches to the desired state (or the trigger is triggered, etc), the script is run.

    Args:
        allChildren: (create) - This flag can only be used in conjunction with the -ac/attributeChange flag.  If it is specified, and the job is attached to a compound attribute, then the job will run due to changes to the specified attribute as well as changes to its children.
        attributeAdded: (create) - Run the script when the named attribute is added. The string must identify both the dependency node and the particular attribute.  If the dependency node is deleted, this job is killed (even if the deletion is undoable).
        attributeChange: (create) - Run the script when the named attribute changes value. The string must identify both the dependency node and the particular attribute.  If the dependency node is deleted, this job is killed (even if the deletion is undoable).
        attributeDeleted: (create) - Run the script when the named attribute is deleted. The string must identify both the dependency node and the particular attribute.  If the dependency node is deleted, this job is killed (even if the deletion is undoable).
        compressUndo: (create) - If this is set to true, and the scriptJob is undoable, then its action will be bundled with the last user action for undo purposes.  For example; if the scriptJob was triggered by a selection change, then pressing undo will undo both the scriptJob and the selection change at the same time.
        conditionChange: (create) - Run the script when the named condition changes state. The string must be the name of a pre-defined, or a user-defined boolean condition.  To get a list of what conditions exist, use the -listConditions flag.
        conditionFalse: (create) - Run the script when the named condition becomes false. The string must be the name of a pre-defined, or a user-defined boolean condition.  To get a list of what conditions exist, use the -listConditions flag.
        conditionTrue: (create) - Run the script when the named condition becomes true. The string must be the name of a pre-defined, or a user-defined boolean condition.  To get a list of what conditions exist, use the -listConditions flag.
        connectionChange: (create) - Run the script when the named attribute changes its connectivity.  The string must identify both the dependency node and the particular attribute.  If the dependency node is deleted, this job is killed (even if the deletion is undoable).
        disregardIndex: (create) - This flag can only be used in conjunction with the -ac/attributeChange flag.  If it is specified, and the job is attached to a multi (indexed) attribute, then the job will run no matter which attribute in the multi changes.
        event: (create) - Run the script when the named event occurs.  This string must be the name of a pre-defined maya event.  To get a list of what events exist, use the -listEvents flag.
        exists: (create) - Returns true if a scriptJob with the specified "job number" exists, and false otherwise. The "job number" should be a value that was returned on creation of a new scriptJob.
        force: (create) - This flag can only be used with -kill, -killAll, or -replacePrevious. It enables the deletion of protected jobs.
        idleEvent: (create) - Run the script every time maya is idle.  WARNING, as long as an idle event is is registered, the application will keep calling it and will use up all available CPU time. Use idleEvents with caution.
        kill: (create, multiuse) - Kills the job with the specified job number. Permanent jobs cannot be killed, however, and protected jobs can only be killed if the -force flag is used in the command.
        killAll: (create) - Kills all jobs. Permanent jobs will not be deleted, and protected jobs will only be deleted if the -force flag is used.
        killWithScene: (create) - Attaches the job to the current scene, and when the scene is emptied. The current scene is emptied by opening a new or existing scene.
        listConditions: (create) - This causes the command to return a string array containing the names of all existing conditions.  Below is the descriptions for all the existing conditions: Events Based on Available Maya Features These events are true when the given feature is available.  Event Name  Maya Feature AnimationExists  Animation  AnimationUIExists User Interface for Animation BaseMayaExists  Any Basic Maya  BaseUIExists  Any Interactive Maya DatabaseUIExists  DeformersExists  Deformer Functions  DeformersUIExists User Interface for Deformers DevicesExists Device Support DimensionsExists Dimensioning DynamicsExists  Dynamics  DynamicsUIExists User Interface for Dynamics ExplorerExists  Explorer  ImageUIExists User Interface for Imaging KinematicsExists  Kinematics  KinematicsUIExists User Interface for Kinematics ManipsExists Manipulators ModelExists  Basic Modeling Tools ModelUIExists User Interface for Basic Modeling NurbsExists  Nurbs Modeling Tools NurbsUIExists User Interface for Nurbs Modeling PolyCoreExists Basic Polygonal Support PolygonsExists  Polygonal Modeling  PolygonsUIExists User Interface for Polygonal Modeling PolyTextureExists  Polygonal Texturing  RenderingExists  Built-in Rendering  RenderingUIExists User Interface for Rendering   Other Events  autoKeyframeState: true when Maya has autoKeyframing enabled busy: true when Maya is busy. deleteAllCondition: true when in the middle of a delete-all operation flushingScene: true while the scene is being flushed out GoButtonEnabled: true when the Go button in the panel context is enabled.  hotkeyListChange: true when the list of hotkey definitions has changed playingBack: true when Maya is playing back animation keyframes. playbackIconsCondition: instance of the playingBack condition used on the time slider readingFile: true when Maya is reading a file. RedoAvailable: true when there are commands available for redo.  SomethingSelected: true when some object(s) is selected. UndoAvailable: true when there are commands available for undo.
        listEvents: (create) - This causes the command to return a string array containing the names of all existing events.  Below is the descriptions for all the existing events:  angularToleranceChanged: when the tolerance on angular units is changed. This tolerance can be changed by:  using the MEL command, "tolerance" with the "-angular" flag  changing the pref under Options->GeneralPreferences-> Modeling tab->Tangential Tolerance  angularUnitChanged: when the user changes the angular unit. axisAtOriginChanged: when the axis changes at the origin.   axisInViewChanged: when the axis changes at a particular view. ColorIndexChanged: when the color index values change. constructionHistoryChanged:  when construction history is turned on or off. currentContainerChanged:  when the user set or unset the current container. currentSoundNodeChanged: whenever the sound displayed in the time slider changes due to:  the sound being removed (or no longer displayed) [RMB in the time slider] a new sound being displayed [RMB in the time slider] sound display being toggled [animation options] sound display mode being changed [animation options]  DagObjectCreated: when a new DAG object is created. deleteAll: when a file new occurs DisplayColorChanged: when the display color changes. displayLayerChange: when a layer has been created or destroyed. displayLayerManagerChange: when the display layer manager has changed. DisplayRGBColorChanged: when the RGB display color changes. glFrameTrigger: for internal use only. ChannelBoxLabelSelected: when Channel Box label(first column) selection changes. gridDisplayChanged: for internal use only. idle:  when Maya is idle and there are no high priority idle tasks idleHigh:  when Maya is idle.  This is called before low priority idle tasks.  You should almost always use "idle" instead. lightLinkingChanged: when any change occurs which modifies light linking relationships. lightLinkingChangedNonSG: when any change occurs which modifies light linking relationships, except when the change is a change of shading assignment. linearToleranceChanged:  when the linear tolerance has been changed.  This tolerance can be changed by:  using the MEL command, "tolerance" with the  "-linear" flag  changing the pref under Options->GeneralPreferences-> Modeling tab->Positional Tolerance  linearUnitChanged:  when the user changes the linear unit through the Options menu. MenuModeChanged:  when the user changes the menu set for the menu bar in the main Maya window (for example, from "Modeling" to "Animation"). RecentCommandChanged:  for internal use only. NewSceneOpened: when a new scene has been opened. PostSceneRead: after a scene has been read. Specifically after a file open, import or all child references have been read. nurbsToPolygonsPrefsChanged:  when any of the nurbs-to-polygons prefs have changed.  These prefs can be changed by:  using the Mel command, "nurbsToPolygonsPref"  changing the prefs under Polygons->Nurbs To Polygons->Option Box  playbackRangeChanged: when the playback keyframe range changes. playbackRangeSliderChanged: when the animation start/end range (i.e. the leftmost or rightmost entry cells in the time slider range, the inner ones adjust the playback range) change preferredRendererChanged: when the preferred renderer changes. quitApplication: when the user has chosen to quit, either through the quit MEL command, or through the Exit menu item. Redo: when user has selected redo from the menu and there was something to redo.  This callback can be used for updating UI or local storage.  Do not change the state of the scene or DG during this callback. renderLayerChange: when creation or deletion of a render layer node has occured. renderLayerManagerChange: when the current render layer has changed. RebuildUIValues: for internal use only. SceneOpened: when a scene has been opened. SceneSaved: when a scene has been saved. SelectionChanged:  when a new selection is made. UFESelectionChanged:  when a new UFE selection is made. SelectModeChanged:  when the selection mode changes. SelectPreferenceChanged:  for internal use only. SelectPriorityChanged: when the selection priority changes. SelectTypeChanged:  when the selection type changes. setEditorChanged: obsolete.  No longer used. SetModified: when the set command is used to modify a set SequencerActiveShotChanged:  when the active sequencer shot is changed. snapModeChanged: when the snap mode changes. E.g. changes to grid snapping.  timeChanged: when the time changes. timeUnitChanged:  when the user changes the time unit. ToolChanged:  when the user changes the tool/context. PostToolChanged:  after the user changes the tool/context. NameChanged:  when the user changes the name of an object with the rename command. Undo: when user has selected undo from the menu and there was something to undo.  This callback can be used for updating UI or local storage.  Do not change the state of the scene or DG during this callback. modelEditorChanged:  when the user changes the options of a model editor. colorMgtEnabledChanged:  when the global per-scene color management enabled flag changes. colorMgtConfigFileEnableChanged:  when the global per-scene color management OCIO configuration enabled flag changes. colorMgtPrefsViewTransformChanged:  when the global per-scene color management view transform preferences transform changes. colorMgtWorkingSpaceChanged:  when the global per-scene color management working space changes. colorMgtConfigFilePathChanged:  when the global per-scene color management OCIO configuration file path changes. colorMgtConfigChanged:  when the color management mode changes from native to OCIO, or when a different OCIO configuration is loaded. colorMgtPrefsReloaded:  when all the global per-scene color management settings are reloaded. colorMgtUserPrefsChanged:  when any user-level color management preference has changed. colorMgtOutputChanged:  when the color management transform, or its enabled state, has changed. colorMgtOCIORulesChanged:  when the type of rules in OCIO mode has changed. colorMgtRefreshed:  when the color management is refreshed to trap environment variable changes. metadataVisualStatusChanged:  for internal use only. shapeEditorTreeviewSelectionChanged:  when a new selection in shape editor's treeview is made . RenderViewCameraChanged:  when the Render View's current camera is changed. tabletModeChanged:  Windows only: if your device is a Tablet PC, then the convertible mode has changed.  You can use command about -tabletMode to query if your device is currently running in tablet or laptop (keyboard attached) mode.
        listJobs: (create) - This causes the command to return a string array containing a description of all existing jobs, along with their job numbers.  These numbers can be used to kill the jobs later.
        nodeDeleted: (create) - Run the script when the named node is deleted
        nodeNameChanged: (create) - Run the script when the name of the named node changes
        optionVarChanged: (create) - Run the script when the named optionVar changes value. If the optioNVar is deleted, this job is killed (even if the deletion is undoable).
        parent: (create) - Attaches this job to a piece of maya UI.  When the UI is destroyed, the job will be killed along with it.
        permanent: (create) - Makes the job un-killable. Permanent jobs exist for the life of the application, or for the life of their parent object. The -killWithScene flag does apply to permanent jobs.
        protected: (create) - Makes the job harder to kill. Protected jobs must be killed or replaced intentionally by using the -force flag. The -killWithScene flag does apply to protected jobs.
        replacePrevious: (create) - This flag can only be used with the -parent flag.  Before the new scriptJob is created, any existing scriptJobs that have the same parent are first deleted.
        runOnce: (create) - If this is set to true, the script will only be run a single time.  If false (the default) the script will run every time the triggering condition/event occurs.  If the -uid or -nd flags are used, runOnce is turned on automatically.
        timeChange: (create) - Run the script whenever the current time changes. The script will not be executed if the time is changed by clicking on the time slider, whereas scripts triggered by the "timeChanged" condition will be executed.
        uiDeleted: (create) - Run the script when the named piece of UI is deleted.
    """
    pass


def selectionConnection(*args, activeCacheList: bool = bool, activeCharacterList: bool = bool, activeList: bool = bool, addScript: Optional[Union[str, bool]] = str, addTo: Optional[Union[str, bool]] = str, characterList: bool = bool, clear: bool = bool, connectionList: bool = bool, defineTemplate: Optional[Union[str, bool]] = str, deselect: Optional[Union[str, bool]] = str, editor: Optional[Union[str, bool]] = str, exists: bool = bool, filter: Optional[Union[str, bool]] = str, findObject: Optional[Union[str, bool]] = str, g: bool = bool, highlightList: bool = bool, identify: bool = bool, keyframeList: bool = bool, lock: bool = bool, modelList: bool = bool, object: Optional[Union[str, bool]] = str, parent: Optional[Union[str, bool]] = str, remove: Optional[Union[str, bool]] = str, removeScript: Optional[Union[str, bool]] = str, select: Optional[Union[str, bool]] = str, setList: bool = bool, switch: bool = bool, useTemplate: Optional[Union[str, bool]] = str, worldList: bool = bool, edit: bool = bool, query: bool = bool):
    """
    This command creates a named selectionConnection object. This object is simply a shared selection list. It may be used by editors to share their highlight data. For example, an outliner may attach its selected list to one of these objects, and a graph editor may use the same object as a list source. Then, the graph editor would only display objects that are selected in the outliner.

    Args:
        activeCacheList: (create) - Specifies that this connection should reflect the cache that objects on the active list belong to.
        activeCharacterList: (create) - Specifies that this connection should reflect the characters that objects on the active list belong to.
        activeList: (create) - Specifies that this connection should reflect the active list (geometry objects and keys).
        addScript: (create, edit, query) - Specify a script to be called when something is added to the selection.
        addTo: (create, edit) - The name of a selection connection that should be added to this list of connections.
        characterList: (create) - Specifies that this connection should reflect all the characters in the world.
        clear: (create, edit) - Remove everything from the selection connection.
        connectionList: (create, query) - Specifies that this connection should contain a list of selection connections.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        deselect: (create, edit) - Remove something from the selection.
        editor: (create, edit, query) - Specifies that this connection should reflect the -mainListConnection of the specified editor.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        filter: (create, edit, query) - Optionally specifies an itemFilter for this connection. An empty string ("") clears the current filter. If a filter is specified, all the information going into the selectionConnection must first pass through the filter before being accepted.  NOTE: filters can only be attached to regular selectionConnections. They cannot be attached to any connection created using the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags. We strongly recommend that you do not attach filters to a selectionConnection --- it is better to attach your filter to the editor that is using the selectionConnection instead.
        findObject: (query) - Find a selection connection in this list that wraps the specified object.
        g: (create, edit, query) - A global selection connection cannot be deleted by any script commands.
        highlightList: (create) - Specifies that this connection is being used as a highlight list.
        identify: (query) - Find out what type of selection connection this is.  May be: activeList | modelList | keyframeList | worldList | objectList listList | editorList | connection | unknown
        keyframeList: (create) - Specifies that this connection should reflect the animation portion of the active list.
        lock: (create, edit, query) - For activeList connections, locking the connection means that it will not listen to activeList changes.
        modelList: (create) - Specifies that this connection should reflect the modeling (i.e. excluding keys) portion of the active list.
        object: (create, edit, query) - Specifies that this connection should wrap around the specified object (which may be a set).  Query will return all the members of the selection connection (if the connection wraps a set, the set members will be returned)
        parent: (create, edit, query) - The name of a UI object this should be attached to.  When the parent is destroyed, the selectionConnection will auto-delete. If no parent is specified, the connection is created in the current controlLayout.
        remove: (create, edit) - The name of a selection connection that should be removed from this list of connections.
        removeScript: (create, edit, query) - Specify a script to be called when something is removed from the selection.
        select: (create, edit) - Add something to the selection. This does not replace the existing selection.
        setList: (create) - Specifies that this connection should reflect all the sets in the world.
        switch: (create, query) - Acts as a modifier to -connectionList which sets the list of objects to be the first non-empty selection connection.  selection connections are tested in the order in which they are added.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
        worldList: (create) - Specifies that this connection should reflect all objects in the world.
    """
    pass


def setParent(*args, defineTemplate: Optional[Union[str, bool]] = str, menu: bool = bool, topLevel: bool = bool, upLevel: bool = bool, useTemplate: Optional[Union[str, bool]] = str, query: bool = bool):
    """
    This command changes the default parent to be the specified parent. Two special parents are "|" which indicates the top level layout of the window hierarchy, or ".." which indicates one level up in the hierarchy. Trying to move above the top level has no effect.

    Args:
        defineTemplate: (create) - Put a command in a mode where any other flags and args are parsed and added to the command template with the given name. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        menu: (create, query) - Parent menu for menu items.
        topLevel: (create) - Move to the top level layout in the hierarchy. Equivalent to use "|"
        upLevel: (create) - Move up one level in the hierarchy. Equivalent to use ".."
        useTemplate: (create) - Will force the command to use a command template given by the name other than the current one.
    """
    pass


def setUITemplate(*args, popTemplate: bool = bool, pushTemplate: bool = bool, query: bool = bool):
    """
    This command sets the current(default) command template for the ELF commands.  The special name NONE can be used to set no templates current. See "uiTemplate" command also.

    Args:
        popTemplate: (create) - Pop the current template off of the stack and sets the next template on the stack to be current.
        pushTemplate: (create) - Push the current template onto a stack that can later be popped.
    """
    pass


def sortCaseInsensitive(*args):
    """
    This command sorts all the strings of an array in a case insensitive way.

    Args:
    """
    pass


def stringArrayIntersector(*args, allowDuplicates: bool = bool, defineTemplate: Optional[Union[str, bool]] = str, exists: bool = bool, intersect: Optional[Union[List[str], bool]] = [str], reset: bool = bool, useTemplate: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    The stringArrayIntersector command creates and edits an object which is able to efficiently intersect large string arrays. The intersector object maintains a sense of "the intersection so far", and updates the intersection when new string arrays are provided using the -i/intersect flag.

    Args:
        allowDuplicates: (create) - Should the intersector allow duplicates in the input arrays (true), or combine all duplicate entries into a single, unique entry (false). This flag must be used when initially creating the intersector. Default is 'false'.
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        intersect: (create, edit) - Intersect the specified string array with the current intersection being maintained by the intersector.
        reset: (edit) - Reset the intersector to begin a new intersection.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    pass


def uiTemplate(*args, defineTemplate: Optional[Union[str, bool]] = str, exists: bool = bool, useTemplate: Optional[Union[str, bool]] = str, edit: bool = bool, query: bool = bool):
    """
    This command creates a new command template object. Template objects can hold default flag arguments for multiple UI commands. The command arguments are specified with the individual commands using the -defineTemplate flag and the desired flags and arguments.  See also

    Args:
        defineTemplate: (create) - Puts the command in a mode where any other flags and arguments are parsed and added to the command template specified in the argument. They will be used as default arguments in any subsequent invocations of the command when templateName is set as the current template.
        exists: (create) - Returns whether the specified object exists or not. Other flags are ignored.
        useTemplate: (create) - Forces the command to use a command template other than the current one.
    """
    pass


def waitCursor(*args, state: bool = bool, query: bool = bool):
    """
    This command sets/resets a wait cursor for the entire Maya application. This works as a stack, such that for each

    Args:
        state: (create, query) - Set or reset the wait cursor for the entire Maya application.
    """
    pass


