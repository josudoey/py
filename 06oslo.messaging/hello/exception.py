class HelloException(Exception):
    msg_fmt = "An unknown exception occurred"

    def __init__(self,message=None, **kwargs):
        self.kwargs = kwargs
        if not message:
            message = self.format_message()
        super(HelloException, self).__init__(message)

    def format_message(self):
        try:
            message = self.msg_fmt % self.kwargs
        except Exception:
            message = self.msg_fmt
        return message

class OopsException(HelloException):
    msg_fmt = "[OopsException] %(name)s : oops."
