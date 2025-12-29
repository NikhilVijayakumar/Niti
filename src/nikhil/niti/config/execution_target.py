from enum import Enum


class ExecutionTarget(Enum):
    """The top-level enum to switch between major functional areas."""
    UTILS = "utils"
    APPLICATION = "application"