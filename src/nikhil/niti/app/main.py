# src.bavans.akashvani.application.app.api.py
from pravaha.domain.api.factory.api_factory import create_fastapi_app

# Import your local configuration and manager
from niti.config.task_config import AppTaskConfig
from niti.manager.bot_manager import BotManager
from niti.manager.storage_manager import StorageManager

# Create instances required by the factory
bot_manager_instance = BotManager() # Create an instance of your concrete manager
task_config_instance = AppTaskConfig() # Create an instance of your concrete config
storage_manager_instance = StorageManager() # Create an instance of your concrete storage manager

# The factory builds the full FastAPI application!
app = create_fastapi_app(
    bot_manager=bot_manager_instance,
    task_config=task_config_instance,
    storage_manager=storage_manager_instance
)

# You would then run this file using uvicorn:
# uvicorn src.bavans.akashvani.application.app.api:app --reload