default_profile = 'profile-docent.group.vocabularies:default'


def upgrade(upgrade_product,version):
    """ Decorator for updating the QuickInstaller of a upgrade """
    def wrap_func(fn):
        def wrap_func_args(context,*args):
            p = getToolByName(context,'portal_quickinstaller').get(upgrade_product)
            setattr(p,'installedversion',version)
            return fn(context,*args)
        return wrap_func_args
    return wrap_func

@upgrade('docent.group.vocabularies', '1.1')
def upgradeTo1_1(context):
    print "docent.group.vocabularies upgraded to version 1.1"