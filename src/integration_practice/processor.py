"""Модуль обработки данных."""
from typing import Any, Dict, List


class Processor:
    """Класс процессора, реализующий правила обработки данных."""

    def normalize_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Нормализует одну запись данных."""
        normalized = {
            "identifier": item.get("id"),
            "label": item.get("name", ""),
            "score": float(item.get("value", 0)),
        }
        return normalized

    def process(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Обрабатывает входные данные и возвращает результат."""
        items = raw_data.get("items", [])
        normalized_items: List[Dict[str, Any]] = [
            self.normalize_item(item)
            for item in items
        ]
        total_score = sum(item["score"] for item in normalized_items)
        return {
            "processed_items": normalized_items,
            "total_score": total_score,
            "metadata": raw_data.get("metadata", {}),
        }
