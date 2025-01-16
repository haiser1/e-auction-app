

class BaseResponse:
    @staticmethod
    def response_success(data):
        return {
            "data": data
        }

    @staticmethod
    def response_error(message):
        return {
            "errors": message
        }