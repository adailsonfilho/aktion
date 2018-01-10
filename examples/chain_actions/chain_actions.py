from actions.aktion import Aktion
from executor import ExecutionPlan
from actions import ActionFactory


# A class that prints A 'x' times
class GenerateA(Aktion):

    def __init__(self):
        super().__init__()

    def __act__(self, times):
        return "A".join(['' for i in range(times+1)])


# A class that prints B 'x' times
class GenerateB(Aktion):

    def __init__(self):
        super().__init__()
        self.retryin = []

    def __act__(self, times):
        return "B".join(['' for i in range(times+1)])


class ConcatSrt(Aktion):

    def __init__(self):
        super().__init__()

    def __act__(self, items, times=1):
        result = "".join([i for i in items])
        result = result.join(['' for i in range(times+1)])
        print(result)


if __name__ == "__main__":

    factory = ActionFactory()
    factory.register(GenerateA)
    factory.register(GenerateB)
    factory.register(ConcatSrt)

    plan = ExecutionPlan(r"chain_actions.json")
    plan.run()
