"""Модуль поставки данных."""
from typing import Any, Dict


class DataProvider:
    """Класс поставщика данных, эмулирующий компонент источника данных."""

    def get_raw_data(self) -> Dict[str, Any]:
        """Возвращает исходные данные для обработки."""
        # Здесь может быть реализация для чтения из API, БД или файла.
        return {
            "items": [
                {"id": 1, "name": "Alpha", "value": 10},
                {"id": 2, "name": "Beta", "value": 20},
                {"id": 3, "name": "Gamma", "value": 30},
            ],
            "metadata": {"source": "simulated", "version": "1.0"},
        }
