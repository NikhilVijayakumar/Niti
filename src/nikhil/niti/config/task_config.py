
from pravaha.domain.bot.protocol.task_config_protocol import TaskConfigProtocol

# Import your application's Enums
from src.nikhil.niti.config.application_type import ApplicationType
from src.nikhil.niti.config.execution_target import ExecutionTarget
from src.nikhil.niti.config.utils_type import UtilsType



class AppTaskConfig(TaskConfigProtocol):
    """
    A concrete implementation of TaskConfigProtocol to expose the application's Enums
    to the shared API Factory.
    """
    GENERATE_SCIENTIFIC_KNOWLEDGE_APPLICATION = "generate_scientific_knowledge_application"


    UtilsType = UtilsType
    ApplicationType = ApplicationType
    ExecutionTarget = ExecutionTarget

