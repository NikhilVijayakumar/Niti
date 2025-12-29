
from pravaha.domain.bot.protocol.task_config_protocol import TaskConfigProtocol

# Import your application's Enums
from niti.config.application_type import ApplicationType
from niti.config.execution_target import ExecutionTarget
from niti.config.utils_type import UtilsType



class AppTaskConfig(TaskConfigProtocol):
    """
    A concrete implementation of TaskConfigProtocol to expose the application's Enums
    to the shared API Factory.
    """
    GENERATE_STORY_APPLICATION = "generate_story_application"


    UtilsType = UtilsType
    ApplicationType = ApplicationType
    ExecutionTarget = ExecutionTarget

