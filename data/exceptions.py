class InvalidDateException(Exception):
    def __init_subclass__(self, *args, **kwargs):
        return super().__init_subclass__(*args, **kwargs)