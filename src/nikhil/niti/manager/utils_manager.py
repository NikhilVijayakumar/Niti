from typing import Optional, List, Dict, Any
from niti.config.utils_type import UtilsType

class UtilsManager:
    @staticmethod
    def run(utility_task: UtilsType, inputs: Optional[List[Dict[str, Any]]] = None):
        if utility_task == UtilsType.VALIDATE_CREW:
            print("Validating crew...")
            return {"status": "success", "message": "Crew validated"}
        else:
            raise NotImplementedError(f"Utility {utility_task} not implemented")