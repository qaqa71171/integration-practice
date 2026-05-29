import sys
import os
import pytest

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from integration_practice.data_provider import DataProvider
from integration_practice.orchestrator import Orchestrator
from integration_practice.processor import Processor


class StubProvider(DataProvider):
    """Заглушка для DataProvider"""
    def get_raw_data(self):
        return {
            "items": [{"id": 10, "name": "Stub", "value": 99}],
            "metadata": {"source": "stub"},
        }


class StubProcessor(Processor):
    """Заглушка для Processor"""
    def process(self, raw_data):
        return {
            "processed_items": [],
            "total_score": 0.0,
            "metadata": raw_data.get("metadata", {}),
        }


def test_orchestrator_integration():
    """Тест интеграции: проверяем, что orchestrator.run() возвращает корректный результат"""
    orchestrator = Orchestrator(
        provider=StubProvider(),
        processor=StubProcessor(),
    )
    result = orchestrator.run()

    assert result["integrated"] is True
    assert result["metadata"]["source"] == "stub"


def test_orchestrator_rejects_invalid_raw_data():
    """Тест: проверяем, что orchestrator выбрасывает TypeError при неверных данных"""
    class BrokenProvider(DataProvider):
        def get_raw_data(self):
            return "not-a-dict"  # Возвращаем строку вместо словаря

    orchestrator = Orchestrator(
        provider=BrokenProvider(),
        processor=StubProcessor(),
    )

    with pytest.raises(TypeError, match="Raw data must be a dictionary"):
        orchestrator.run()