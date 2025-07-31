from dataclasses import dataclass

from Entities.Types import ErrorCode

@dataclass
class GenericResponse:

    ErrorCode: ErrorCode
    ThrottleSeconds: int
    ErrorStatus: str
    Message: str
    MessageData: object
    Response: int = None
    DetailedErrorTrace: str = None