from rest_framework import status
from rest_framework.response import Response


class ApiMessageResponse(Response):
    """
    A generic API Response
    """

    def __init__(
        self,
        data,
        status=status.HTTP_200_OK,
        template_name=None,
        headers=None,
        content_type=None,
    ):
        super().__init__(
            {"data": data}, status, template_name, headers, content_type
        )
