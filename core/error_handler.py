from crud import crud_error
import logging

logging.basicConfig(
    filename="error_log.log",
    level=logging.WARNING,
    format="%(asctime)s : 	%(message)s : %(levelname)s",
)


class StandardError(Exception):
    def __init__(self, error_tag: str, status: str, message: str = None) -> None:
        self.error_tag = error_tag
        self.status = status
        self.get_db_values()

    def __str__(self) -> str:
        return "An error ocurred with the message {} -- Status Code : {}".format(
            self.message, self.status
        )

    def get_db_values(self):
        error = crud_error.get_erro_by_error_tag(self.error_tag)
        self.message = error.message
        logging.warning(self.__str__())
