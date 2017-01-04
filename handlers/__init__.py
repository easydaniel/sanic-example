from utils.include import include


class Handler:
    pass


include(
    cls=Handler,
    dir='./handlers/',
    all_path=False,
)
