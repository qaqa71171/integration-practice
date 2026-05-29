class Processor:
    """Обрабатывает и нормализует данные"""
    
    def normalize_item(self, item):
        """
        Нормализует один элемент данных
        """
        return {
            "identifier": item.get("id"),
            "label": item.get("name"),
            "score": float(item.get("value", 0))
        }
    
    def process(self, raw_data):
        """
        Обрабатывает все данные и вычисляет общую сумму
        """
        items = raw_data.get("items", [])
        metadata = raw_data.get("metadata", {})
        
        processed_items = []
        total_score = 0.0
        
        for item in items:
            normalized = self.normalize_item(item)
            processed_items.append(normalized)
            total_score += normalized["score"]
        
        return {
            "processed_items": processed_items,
            "total_score": total_score,
            "metadata": metadata
        }