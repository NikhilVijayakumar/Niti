from typing import Optional, List, Dict, Any
from amsha.llm_factory.domain.model.llm_type import LLMType

from niti.config.application_type import ApplicationType
from niti.config.settings import Settings
from niti.domain.generate_story.generate_story_application import GenerateStoryApplication


class ApplicationManager:

    @staticmethod
    def generate_story_application():
        configs = {
            "llm": Settings.LLM_CONFIG,
            "app": Settings.APP_CONFIG,
            "job": "src/nikhil/niti/domain/generate_story/config/generate_story_config.yaml"
        }
        app = GenerateStoryApplication(config_paths=configs, llm_type=LLMType.CREATIVE)
        return app.run()

    @staticmethod
    def stream_run(application_task: ApplicationType, inputs: Optional[List[Dict[str, Any]]] = None):
        if application_task == ApplicationType.GENERATE_STORY_APPLICATION:
            return ApplicationManager.generate_story_application()
        else:
            raise NotImplementedError(f"Application {application_task} not implemented")




