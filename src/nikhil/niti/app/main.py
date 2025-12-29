# src.bavans.akashvani.application.app.api.py
from pravaha.domain.api.factory.api_factory import create_fastapi_app

# Import your local configuration and manager
from src.bavans.akashvani.bala.kadha.application.config.task_config import AppTaskConfig
from src.bavans.akashvani.bala.kadha.application.manager.bot_manager import BotManager

# Create instances required by the factory
bot_manager_instance = BotManager() # Create an instance of your concrete manager
task_config_instance = AppTaskConfig() # Create an instance of your concrete config

# The factory builds the full FastAPI application!
app = create_fastapi_app(
    bot_manager=bot_manager_instance,
    task_config=task_config_instance
)

# You would then run this file using uvicorn:
# uvicorn src.bavans.akashvani.application.app.api:app --reload