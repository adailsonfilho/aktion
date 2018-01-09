import collections
import json
import os

from actions.action import Action
from actions import ActionFactory

class Executor:

    def __init__(self):
        pass

    def execute(self, plan):
        assert isinstance(plan, ExecutionPlan)

    def __execute(self, action):
        assert isinstance(action, Action)
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

    def __init__(self, file):
        if not os.path.isabs(file):
            file = os.path.join(os.getcwd(), file)

        if not os.path.isfile(file):
            raise FileNotFoundError(file)

        with open(file, 'r') as plan_text:
            plan = json.loads(plan_text.read())
            self.execution_id = plan[ExecutionPlan.EXECUTION_ID]
            self.actions = plan[ExecutionPlan.ACTIONS]

    def run(self):
        for action_config in self.actions:
            action = ActionFactory().create(action_config[ExecutionPlan.NAME])
            action.act(**action_config[ExecutionPlan.ARGUMENTS])
