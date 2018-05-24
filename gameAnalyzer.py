import enum

class gameAnalyzer():
    class staticPlays(enum.Enum):
        FreeHomeKick = 1
        FreeAwayKick = 2

    def __init__(self, tasklist, state, play=None):
        # tasklist -> list of available tactics
        # state -> belief state
        # play -> static play, if it is None means we have decide it dynamically
        self.tasklist = tasklist
        self.state = state
        self.play = play

    def availableBots():
        # return list of available bots using state

    def targetPoints(tasks):
        # input -> list of tasks(Tactics)
        # ouput -> a dict, keyword -> tasks name, value -> their target point

        # here make instance of tactics and call their target ponint function
        # we are assuming that tactics have this function
        # Example : TReceiver = TReceiver(agrs)
        #           ReceiverPos = TReceiver.getTargetPos()

    def staticPlays():
        curPlay = 0
        for play in staticPlays:
            if play.value == self.play:
                curPlay = play.value
                break
        if curPlay != 0:
            if curPlay == 1:
                # FreeHomeKick
                requiredTasks = ['BallHandler']  # add more task here
                tasks = self.intersection(requiredTasks, self.tasklist)
                # task is dict, keyword -> tasks name, value -> their target point
                tasks = self.targetPoints(tasks)
                bots = self.availableBots()
                return tasks, bots
        else:
            print("this static play is not available!!")
