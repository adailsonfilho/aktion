import actions.action
from executor import ExecutionPlan
from actions import ActionFactory


# A class that prints A 'x' times
class PrintA(actions.action.Action):

    def __init__(self):
        super().__init__()

    def __act__(self, times):
        print("A".join(['' for i in range(times+1)]))


# A class that prints B 'x' times
class PrintB(actions.action.Action):

    def __init__(self):
        super().__init__()

    def __act__(self, times):
        print("B".join(['' for i in range(times+1)]))


if __name__ == "__main__":

    factory = ActionFactory()
    factory.register(PrintA)
    factory.register(PrintB)

    plan = ExecutionPlan(r"examples\simple_actions\exec_naive_test.json")
    plan.run()
