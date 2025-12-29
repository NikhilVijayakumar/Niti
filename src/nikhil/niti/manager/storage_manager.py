from pathlib import Path
from typing import Dict

class StorageManager:
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.categories = {
            "output": self.base_path / "output",
            "intermediate": self.base_path / "intermediate",
            "knowledge": self.base_path / "knowledge"
        }
        for path in self.categories.values():
            path.mkdir(parents=True, exist_ok=True)

    def get_path(self, category: str) -> Path:
        if category not in self.categories:
            raise ValueError(f"Category {category} not found. Available: {list(self.categories.keys())}")
        return self.categories[category]
