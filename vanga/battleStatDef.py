class battleStat:
    def __init__(self, size):
        self.arraySize = size
        self.ship_count = [[0 for x in range(self.arraySize)] for y in range(2)] # 2d array
        self.counter = 0
        self.battle_id = utils.timeNowUTC().strftime('%y%m%d_%H%M') 
        self.my_team_id = 0
        self.my_level = 0
