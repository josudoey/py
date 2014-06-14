class HelloException(Exception):
    msg_fmt = "An unknown exception occurred"

    def __init__(self,message=None, **kwargs):
        self.kwargs = kwargs
        if not message:
            try:
                message = self.msg_fmt % kwargs
            except Exception:
                message = self.msg_fmt
        super(HelloException, self).__init__(message)

