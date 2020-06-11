class Plugin:
    def __init__(self, *args, **kwargs):
        super().__init__()
        print("Plugin init (Two)", args, kwargs)

    def execute(self, a, b):
        return a-b