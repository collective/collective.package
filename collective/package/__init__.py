import install

install.register_package_plugin()


def initialize(context):
    """Zope 2 product initialization
    """
    install.register_package_plugin_class(context)
