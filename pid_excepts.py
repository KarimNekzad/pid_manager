class PIDException(Exception):
    def __init__(self, message="Something went wrong with the PID manager", error=-1):
        super().__init__(message)
        self.error = error


class AllocationError(PIDException):
    def __init__(self, message="Failed to allocate", error=-1):
        super().__init__(message)
        self.error = error


class MapAllocationError(AllocationError):
    def __init__(self, message="Failed to allocate map.", error=-1):
        super().__init__(message)
        self.error = error


class PIDAllocationError(AllocationError):
    def __init__(self, message="Failed to allocate PID", error=-1):
        super().__init__(message)
        self.error = error


class ReleaseError(PIDException):
    def __init__(self, message="Failed to release PID", error=-1):
        super().__init__(message)
        self.error = error


class OutOfBoundsError(PIDException):
    def __init__(self, message="Specified PID is out of bounds", error=-1):
        super().__init__(message)
        self.error = error
