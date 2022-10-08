class CharPaths:

    def __init__(self, available_paths: list, active_id_path=None):
        self._available_paths = available_paths
        self._active_path = None
        if active_id_path is None:
            self._active_path = available_paths[0]
        else:
            self.set_active(active_id_path)

    @property
    def available_paths(self):
        return self._available_paths

    @property
    def active_path(self):
        return self._active_path

    def __str__(self):
        result = f"Paths:\n"
        for path in self._available_paths:
            result += f"{path}\n"
        return result

    def set_active(self, id_path):
        for path in self._available_paths:
            if path.id_path == id_path:
                self._active_path = path

    def add_path(self, path):
        self._available_paths.append(path)
