class DataProvider:
    """Предоставляет сырые данные для обработки"""
    
    def get_raw_data(self):
        """Возвращает словарь с данными"""
        return {
            "items": [
                {"id": 1, "name": "Alpha", "value": 10},
                {"id": 2, "name": "Beta", "value": 20},
                {"id": 3, "name": "Gamma", "value": 30}
            ],
            "metadata": {
                "source": "database",
                "version": "1.0"
            }
        }