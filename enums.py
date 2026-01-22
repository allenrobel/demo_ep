from enum import Enum


class VerbEnum(str, Enum):
    """
    # Summary

    Enum for HTTP verb values used in endpoints.

    ## Members

    - GET: Represents the HTTP GET method.
    - POST: Represents the HTTP POST method.
    - PUT: Represents the HTTP PUT method.
    - DELETE: Represents the HTTP DELETE method.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class BooleanStringEnum(str, Enum):
    """
    # Summary

    Enum for boolean string values used in query parameters.

    ## Members

    - TRUE: Represents the string "true".
    - FALSE: Represents the string "false".
    """

    TRUE = "true"
    FALSE = "false"
