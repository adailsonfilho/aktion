from . import printters, registerpeople


class ActionFactory:

    actions = {
        'printa': printters.PrintA,
        'printb': printters.PrintB,
        'register_people': registerpeople.RegisterPeople,
    }

    @staticmethod
    def create(name):
        return ActionFactory.actions[name]()
