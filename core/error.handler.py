class StandardError(Exception):
    def __init__(self, error_tag: str, status: str) -> None:

        super().__init__()
