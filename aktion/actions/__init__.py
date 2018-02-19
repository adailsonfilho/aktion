class ActionFactory:

    __actions = None
    __instance = None

    def __new__(cls):
        if ActionFactory.__instance is None:
            ActionFactory.__instance = object.__new__(cls)
            ActionFactory.__actions = {}
        return ActionFactory.__instance

    def create(self, name):
        return ActionFactory.__instance.__actions[name]()

    def register(self, classDef):
        ActionFactory.__actions[str(classDef.__name__).lower()] = classDef