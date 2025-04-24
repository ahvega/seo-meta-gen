import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

class UBOSTaskManager:
    def __init__(self, config_path: str = ".cursor/ubos_task_manager_config.json"):
        self.config_path = Path(config_path)
        self.config = self._load_config()
        self.base_url = f"http://{self.config['server']['host']}:{self.config['server']['port']}"
        self.headers = {
            "Authorization": f"Bearer {self.config['server']['api_key']}",
            "Content-Type": "application/json"
        }

    def _load_config(self) -> Dict:
        """Load configuration from file."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            return json.load(f)

    def create_task(self, title: str, description: str, priority: Optional[str] = None,
                   category: Optional[str] = None, due_date: Optional[str] = None) -> Dict:
        """Create a new task."""
        task_data = {
            "title": title,
            "description": description,
            "priority": priority or self.config['tasks']['default_priority'],
            "category": category,
            "status": self.config['tasks']['default_status'],
            "due_date": due_date or datetime.now().isoformat(),
            "project": self.config['project']['name']
        }
        
        response = requests.post(
            f"{self.base_url}/tasks",
            headers=self.headers,
            json=task_data
        )
        response.raise_for_status()
        return response.json()

    def update_task(self, task_id: str, updates: Dict) -> Dict:
        """Update an existing task."""
        response = requests.patch(
            f"{self.base_url}/tasks/{task_id}",
            headers=self.headers,
            json=updates
        )
        response.raise_for_status()
        return response.json()

    def get_task(self, task_id: str) -> Dict:
        """Get task details."""
        response = requests.get(
            f"{self.base_url}/tasks/{task_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_tasks(self, status: Optional[str] = None,
                  category: Optional[str] = None) -> List[Dict]:
        """List all tasks with optional filters."""
        params = {}
        if status:
            params['status'] = status
        if category:
            params['category'] = category
            
        response = requests.get(
            f"{self.base_url}/tasks",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def delete_task(self, task_id: str) -> bool:
        """Delete a task."""
        response = requests.delete(
            f"{self.base_url}/tasks/{task_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return True

    def add_comment(self, task_id: str, comment: str) -> Dict:
        """Add a comment to a task."""
        response = requests.post(
            f"{self.base_url}/tasks/{task_id}/comments",
            headers=self.headers,
            json={"comment": comment}
        )
        response.raise_for_status()
        return response.json() 