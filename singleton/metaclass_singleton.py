

class MetaSingleton(type):

    __instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwds)
        return cls.__instance[cls]

class Logger(metaclass=MetaSingleton):
    pass

log1 = Logger()
print(f'Log 1: {id(log1)}')

log2 = Logger()
print(f'Log 1: {id(log2)}')