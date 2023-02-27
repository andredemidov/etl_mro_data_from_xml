class Repository:

    def __init__(self, entries: list = None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def list(self) -> list:
        """Возвращает копию списка вхождений"""
        return self._entries.copy()

    def add(self, entries: list):
        self._entries.extend(entries)
