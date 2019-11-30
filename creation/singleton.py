
class Logger():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger


if __name__ == "__main__":
    logger1 = Logger()
    print(id(logger1))

    logger2 = Logger()
    print(id(logger2))
        