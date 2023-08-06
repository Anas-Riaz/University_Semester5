from abc import abstractmethod


class Environment(object):

    @abstractmethod
    def __init__(self, n):
        self.n = n

    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n


class NRoomVaccumCleanerEnvironment(Environment):

    def __init__(self, agent, no_of_rooms):
        self.n = no_of_rooms
        self.rooms = []
        for i in range(self.n):
            self.rooms.append(Room(i + 1, 'dirty'))

        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom.location < self.n:
                    self.currentRoom = self.rooms[self.currentRoom.location]
            else:
                if self.currentRoom.location > 1:
                    self.currentRoom = self.rooms[self.currentRoom.location - 2]
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%d]" % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    def delay(self, n=100):
        self.delay = n


class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


class Agent(object):
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass


class VaccumAgent(Agent):
    def __init__(self, n):
        self.model = {}
        for i in range(n):
            self.model[i + 1] = 'dirty'

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.model[self.environment.currentRoom.location] == 'dirty':
            self.model[self.environment.currentRoom.location] = 'clean'
            return 'clean'

        if self.environment.currentRoom.location < self.environment.n:
            return 'right'
        return 'left'


if __name__ == '__main__':
    n = int(input("Enter number of rooms: "))
    vcagent = VaccumAgent(n)
    env = NRoomVaccumCleanerEnvironment(vcagent, n)
    env.executeStep(50)
