class AppException(Exception):
    def __init__(
            self,
            message : str,
            status_code = 400,
            error_code = "APP_ERROR"
    ):

        self.message = message
        self.status_code = status_code
        self.error_code = error_code