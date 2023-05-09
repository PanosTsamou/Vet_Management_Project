class Species:

    def __init__(self, input_name, input_id = None):
        self.name  = input_name
        self.id = input_id

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.id == __o.id
