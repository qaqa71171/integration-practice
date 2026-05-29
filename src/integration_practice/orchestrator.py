"""Модуль оркестрации и интеграции компонентов."""
from typing import Dict, Any

from .data_provider import DataProvider
from .processor import Processor


class Orchestrator:
    """Класс для управления взаимодействием между компонентами."""

    def __init__(
        self,
        provider: DataProvider = None,
        processor: Processor = None,
    ):
        self.provider = provider or DataProvider()
        self.processor = processor or Processor()

    def run(self) -> Dict[str, Any]:
        """Выполняет полную интеграцию: поставку данных и их обработку."""
        raw_data = self.provider.get_raw_data()
        if not isinstance(raw_data, dict):
            raise TypeError("Raw data must be a dictionary")

        result = self.processor.process(raw_data)
        result["integrated"] = True
        return result
