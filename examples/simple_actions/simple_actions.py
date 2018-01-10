from actions.aktion import Aktion
from executor import ExecutionPlan
from actions import ActionFactory


# A class that prints A 'x' times
class PrintA(Aktion):

    def __init__(self):
        super().__init__()

    def __act__(self, times):
        print("A".join(['' for i in range(times+1)]))


# A class that prints B 'x' times
class PrintB(Aktion):

    def __init__(self):
        super().__init__()
        self.retryin = []

    def __act__(self, times):
        print("B".join(['' for i in range(times+1)]))


if __name__ == "__main__":

    factory = ActionFactory()
    factory.register(PrintA)
    factory.register(PrintB)

    plan = ExecutionPlan("simple_actions.json")

    plan.run()
