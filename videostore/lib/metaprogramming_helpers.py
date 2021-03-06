

class LeafSubclassRetriever:
    """
    http://code.activestate.com/recipes/577858-concrete-class-finder/
    """

    def __init__(self, base_class):
        self.base_class = base_class

    def value(self):
        direct_subclasses = self.base_class.__subclasses__()
        leaf_subclasses = list()
        for klass in direct_subclasses:
          if( len(klass.__subclasses__()) > 0 ):
                leaf_subclasses += LeafSubclassRetriever(klass).value()
          else:
                leaf_subclasses.append(klass)

        return leaf_subclasses


def leaf_subclasses(klass):
    return LeafSubclassRetriever(klass).value()
