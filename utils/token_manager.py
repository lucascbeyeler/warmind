import os
import json

class TokenManager:

    _creds_file_path: str

    def __init__(self) -> None:
        home_dir = os.path.expanduser("~")
        warmind_dir = os.path.join(home_dir, ".warmind")
        os.makedirs(warmind_dir, exist_ok=True)
        self._creds_file_path = os.path.join(warmind_dir, "creds")
        # Set permissions to 600 (owner read/write)
        if not os.path.exists(self._creds_file_path):
            with open(self._creds_file_path, 'w') as f:
                f.write("") # Create empty file if it doesn't exist
        os.chmod(self._creds_file_path, 0o600)

    @property
    def token(self):
        try:
            with open(self._creds_file_path, 'r') as f:
                content = f.read()
                if content:
                    return json.loads(content)
                return {}
        except FileNotFoundError:
            return {}
    
    @token.setter
    def token(self, value: dict[str, any]):
        with open(self._creds_file_path, 'w') as f:
            json.dump(value, f)
    
    def save(self, value: dict[str, any]):
        self.token = value
        