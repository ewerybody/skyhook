class Constants:
    """
    Some very general constants that are used throughout SkyHook
    """
    function_name   = "FunctionName"
    parameters      = "Parameters"
    module          = "_Module"
    undefined       = "undefined"


class Ports:
    """
    Ports that the host programs use and for the clients to connect to
    """
    undefined = 65500
    maya = 65501
    houdini = 65502
    blender = 65504
    unreal = 8080


class HostPrograms:
    """
    List of host programs
    """
    blender = "blender"
    unreal  = "unreal"
    maya    = "maya"
    houdini = "houdini"


class ServerCommands:
    """
    These are commands that are not run from any modules, but in the server class. In case of Unreal, since we don't
    control the server, these commands will have to be overridden in the client.
    """
    SKY_SHUTDOWN       = "SKY_SHUTDOWN"
    SKY_LS             = "SKY_LS"
    SKY_RELOAD_MODULES = "SKY_RELOAD_MODULES"
    SKY_HOTLOAD        = "SKY_HOTLOAD"
    SKY_UNLOAD         = "SKY_UNLOAD"
    SKY_FUNCTION_HELP  = "SKY_FUNCTION_HELP"


class Errors:
    """
    Errors when things go wrong
    """
    CALLING_FUNCTION = "An error occurred when calling the function"
    IN_FUNCTION      = "An error occurred when executing the function"
    SERVER_COMMAND   = "An error occurred processing this server command"