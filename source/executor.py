import collections
import json
import os

from actions.aktion import Aktion
from actions import ActionFactory

class Executor:

    def __init__(self):
        pass

    def execute(self, plan):
        assert isinstance(plan, ExecutionPlan)

    def __execute(self, action):
        assert isinstance(action, Aktion)
        action.act()

    def __execute_batch(self, actions):
        assert isinstance(actions, collections.Iterable)

        for action in actions:
            action.act()


class ExecutionPlan:

    EXECUTION_ID = 'execution_id'
    ACTIONS = 'actions'
    NAME = 'name'
    ARGUMENTS = 'arguments'
    OUTPUT_ID = 'output_id'
    DYNAMIC_ARGUMENTS= 'DYNAMIC_ARGUMENTS'.lower()

    def __init__(self, file):
        if not os.path.isabs(file):
            file = os.path.join(os.getcwd(), file)

        if not os.path.isfile(file):
            raise FileNotFoundError(file)

        with open(file, 'r') as plan_text:
            plan = json.loads(plan_text.read())
            self.execution_id = plan[ExecutionPlan.EXECUTION_ID]
            self.actions = plan[ExecutionPlan.ACTIONS]
        self.outputs = {}

    def __fill_dynamic_arguments(self, kwargs):

        def recursive_replacement(d):
            if isinstance(d, collections.Iterable) and not isinstance(d, str):
                for i, item in enumerate(d):
                    if isinstance(d, dict):
                        d[item] = recursive_replacement(d[item])
                    elif isinstance(d, list):
                        d[i] = recursive_replacement(item)
            elif isinstance(d, str):
                return self.outputs[d]
            return d

        recursive_replacement(kwargs)

    def run(self):

        for action_config in self.actions:
            action = ActionFactory().create(action_config[ExecutionPlan.NAME])
            out = None

            if ExecutionPlan.DYNAMIC_ARGUMENTS in action_config:
                arguments = action_config[ExecutionPlan.DYNAMIC_ARGUMENTS]
                self.__fill_dynamic_arguments(arguments)
                out = action.act(**arguments)
            else:
                out = action.act(** action_config[ExecutionPlan.ARGUMENTS])

            if ExecutionPlan.OUTPUT_ID in action_config:
                self.outputs[action_config[ExecutionPlan.OUTPUT_ID]] = out
