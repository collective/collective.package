import Products.PluggableAuthService.interfaces.plugins as plugins

IAnonymousUserFactoryPlugin = plugins.IAnonymousUserFactoryPlugin
IAuthenticationPlugin = plugins.IAuthenticationPlugin
IChallengePlugin = plugins.IChallengePlugin
IChallengeProtocolChooser = plugins.IChallengeProtocolChooser
ICredentialsResetPlugin = plugins.ICredentialsResetPlugin
ICredentialsUpdatePlugin = plugins.ICredentialsUpdatePlugin
IExtractionPlugin = plugins.IExtractionPlugin
IGroupEnumerationPlugin = plugins.IGroupEnumerationPlugin
IGroupsPlugin = plugins.IGroupsPlugin
ILoginPasswordExtractionPlugin = plugins.ILoginPasswordExtractionPlugin
ILoginPasswordHostExtractionPlugin = plugins.ILoginPasswordHostExtractionPlugin
IPropertiesPlugin = plugins.IPropertiesPlugin
IRequestTypeSniffer = plugins.IRequestTypeSniffer
IRoleAssignerPlugin = plugins.IRoleAssignerPlugin
IRoleEnumerationPlugin = plugins.IRoleEnumerationPlugin
IRolesPlugin = plugins.IRolesPlugin
IUpdatePlugin = plugins.IUpdatePlugin
IUserAdderPlugin = plugins.IUserAdderPlugin
IUserEnumerationPlugin = plugins.IUserEnumerationPlugin
IUserFactoryPlugin = plugins.IUserFactoryPlugin
IValidationPlugin = plugins.IValidationPlugin


class IPackagePlugin(IAnonymousUserFactoryPlugin, IAuthenticationPlugin,
    IChallengePlugin, IChallengeProtocolChooser, ICredentialsResetPlugin,
    ICredentialsUpdatePlugin, IExtractionPlugin, IGroupEnumerationPlugin,
    IGroupsPlugin, ILoginPasswordExtractionPlugin,
    ILoginPasswordHostExtractionPlugin, IPropertiesPlugin,
    IRequestTypeSniffer, IRoleAssignerPlugin,
    IRoleEnumerationPlugin, IRolesPlugin,
    IUpdatePlugin, IUserAdderPlugin,
    IUserEnumerationPlugin, IUserFactoryPlugin, IValidationPlugin):
    """interface for PackagePlugin."""
