class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0.0

    def __repr__(self) -> str:
        return self.name

class RestAPI:

    def __init__(self, database=None):
        if database is None:
            self.database = {"users" : []}
        else:
            self.database = database

    def get(self, url, payload=None):
        url = url[1:]
        data = self.database[url]


    def post(self, url, payload=None):
        pass


