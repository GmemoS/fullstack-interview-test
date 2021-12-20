class MissingEnv(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.env = kwargs.pop('env')
        super().__init__(*args, **kwargs)


class NoBranch(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.branch = kwargs.pop('branch')
        super().__init__(*args, **kwargs)


class NoCommit(Exception):
    def __init__(self, *args, **kwargs) -> None:
        self.commit = kwargs.pop('commit')
        super().__init__(*args, **kwargs)
