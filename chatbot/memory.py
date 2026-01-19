class Memory:
    def __init__(self):
        self.data={
            "name":None,
            "email":None,
            "phone":None,
            "experience":None,
            "position":None,
            "location":None,
            "tech-stack":None,
            "tech_answers": {}
        }
    def is_complete(self):
        return all(self.data.values())