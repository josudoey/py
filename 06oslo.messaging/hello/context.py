class RequestContext(object):
    """Security context and request information.
    """

    def __init__(self, name=None, **kwargs):
        """
           :param kwargs: Extra arguments that might be present, but we ignore
                because they possibly came in from older rpc messages.
        """
        if kwargs:
            LOG.warn(_('Arguments dropped when creating context: %s') %
                    str(kwargs))

        self.name = name

    def say_hello():
        print "%s: hello!!! this ctxt method.!"


    
    def to_dict(self):
        return {'name': self.name}

    @classmethod
    def from_dict(cls, values):
        return cls(**values)


