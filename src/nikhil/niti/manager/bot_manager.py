from typing import Optional, Dict, Any, List

from niti.config.application_type import ApplicationType
from niti.config.utils_type import UtilsType
from niti.manager.application_manager import ApplicationManager
from niti.manager.utils_manager import UtilsManager
from pravaha.domain.bot.protocol.bot_manager_protocol import BotManagerProtocol


class BotManager(BotManagerProtocol[UtilsType, ApplicationType]):

    @staticmethod
    def run(utility_task: UtilsType,inputs: Optional[List[Dict[str, Any]]] = None):
        # Now the type hint is UtilsType, matching the protocol and the Pydantic model
        if not isinstance(utility_task, UtilsType):
            raise TypeError(f"Task must be a member of UtilsType. Got {type(utility_task).__name__}.")

        return UtilsManager.run(utility_task,inputs)

    @staticmethod
    def stream_run(application_task: ApplicationType,inputs: Optional[List[Dict[str, Any]]] = None):
        # Now the type hint is ApplicationType
        if not isinstance(application_task, ApplicationType):
            raise TypeError(f"Task must be a member of ApplicationType. Got {type(application_task).__name__}.")

        return ApplicationManager.stream_run(application_task,inputs)