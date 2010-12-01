import install

install.register_package_plugin()

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    install.register_package_plugin_class(context)
