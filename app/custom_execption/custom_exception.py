from app.custom_execption.app_exception import AppException




class UserNotFoundException(AppException):
    def __init__(
        self,
        message: str,
    ):
        super().__init__(
            message=message,
            status_code=404,
            error_code="USER_NOT_FOUND"
        )


class UserAlreadyExist(AppException):
    def __init__(
        self,
        message: str,
    ):
        super().__init__(
            message=message,
            status_code=409,
            error_code="USER_CONFLICT"
        )