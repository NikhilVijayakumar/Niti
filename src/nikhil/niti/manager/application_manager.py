from amsha.llm_factory.domain.model.llm_type import LLMType

from src.nikhil.niti.config.application_type import ApplicationType
from src.nikhil.niti.config.settings import Settings


class ApplicationManager:

    @staticmethod
    def generate_scientific_knowledge_application():
        configs = {
            "llm": Settings.LLM_CONFIG,
            "app": Settings.APP_CONFIG,
            "job": "src/bavans/akashvani/bala/kadha/application/domain/idea/generate_kb/config/scientific_kb_config.yaml"
        }
        app = GenerateScientificKnowledgeApplication(config_paths=configs, llm_type=LLMType.CREATIVE)
        return app.run()



    @staticmethod
    def stream_run(config_type: ApplicationType):

        if config_type == ApplicationType.GENERATE_SCIENTIFIC_KNOWLEDGE_APPLICATION:
            return ApplicationManager.generate_scientific_knowledge_application()

        else:
            raise ValueError(f"Unknown configuration type: {config_type}")





