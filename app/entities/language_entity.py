class LanguageEntity:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def to_dict(self):
        return {'id': str(self.id), 'name': str(self.name), 'status': str(self.status)}