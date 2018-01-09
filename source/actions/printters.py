import actions.action


class PrintA(actions.action.Action):

    def __init__(self):
        actions.action.Action.__init__(self)

    def __act__(self, times):
        print("A".join(['' for i in range(times+1)]))


class PrintB(actions.action.Action):

    def __init__(self):
        actions.action.Action.__init__(self)

    def __act__(self, times):
        print("B".join(['' for i in range(times+1)]))
