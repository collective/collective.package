"""Class: PackagePlugin
"""

from AccessControl.SecurityInfo import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass

from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.utils import classImplements

import interface

class PackagePlugin(BasePlugin):
    """Multi-plugin
    """

    meta_type = 'package Plugin'
    security = ClassSecurityInfo()

    def __init__( self, id, title=None ):
        self._setId( id )
        self.title = title


classImplements(PackagePlugin, interface.IPackagePlugin)

InitializeClass( PackagePlugin )
