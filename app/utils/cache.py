from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Optional
from app.config import settings

class Cache:


    def __init__(self):
        self._cache: Dict[str, Dict[str, Any]] = {}


    def set(self, key: str, value: Any) -> None:
        expiry = datetime.now(timezone.utc) + timedelta(seconds=settings.CACHE_EXPIRY_SECONDS)
        self._cache[key] = {
            "value": value,
            "expiry": expiry
        }


    def get(self, key: str) -> Optional[Any]:
        if key not in self._cache:
            return None
        
        cached_data = self._cache[key]
        if cached_data["expiry"] < datetime.now(timezone.utc):
            del self._cache[key]
            return None
        
        return cached_data["value"]


    def delete(self, key: str) -> None:
        if key in self._cache:
            del self._cache[key]


    def clear(self) -> None:
        self._cache.clear()


cache = Cache()
