import actions.action


class RegisterPeople(actions.action.Action):

    def __init__(self):
        actions.action.Action.__init__(self)

    def __act__(self):
        print("[BEGIN] Register People")
        print("[END] Register People")