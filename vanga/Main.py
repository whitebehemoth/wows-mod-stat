from battleStatDef import battleStat

API_VERSION = 'API_v1.0'
MOD_NAME = 'Vanga'

class Vanga:

    def __init__(self):
        self.FREQUENCY_SEC = 60
        self.MAX_BATTLE_SEC = 1200
        self.ARRAY_LEN = int(self.MAX_BATTLE_SEC / self.FREQUENCY_SEC)
        self.battles = {}
        self.setup_events()

    # callback function to be called every FREQUENCY_SEC seconds
    def callback_func(self):
        #utils.logInfo('vanga', {'event': 'callback_func','counter': self.counter,})
        self.log_state()

    #event on the battle start
    def on_battle_start(self):
        self_info = battle.getSelfPlayerInfo()        #getting self info

        self.current_battle = battleStat(self.ARRAY_LEN)    #current battle 
        self.current_battle.my_team_id = self_info.teamId
        self.current_battle.my_level = self_info.shipInfo.level

        self.battles[self_info.shipInfo.id] = self.current_battle   #storing the info using ShipId as key, as same ship can not be in more than one battle
        self.callback_handler = callbacks.callback(self.FREQUENCY_SEC, self.callback_func) # handler is required to stop calling callback

    #when a user left a battle, callback should be stopped
    def on_battle_quit(self, arg):
        if self.callback_handler is not None:
            callbacks.cancel(self.callback_handler)        

    #keeping the final number of alive ships in the last column (t0_m0 / t1_m0) 
    def on_battle_end(self, arg1, arg2):
        self.current_battle.counter = self.ARRAY_LEN - 1 # last record
        self.log_state()

    #getting all players and store the number of alive ships in array for avery team
    def log_state(self):
        players_info_collection = battle.getPlayersInfo() #not-self player info is quite empty, health, level is not available 
        for playerId in players_info_collection:
            player_info = players_info_collection[playerId]
            self.current_battle.ship_count[player_info.teamId][self.current_battle.counter] += int(player_info.isAlive)
        self.current_battle.counter += 1
        
        
    #getting after battle statistics (in a way of collection of dictionaries)
    def on_battle_get_stat(self, arg):
        #self.log_obj("after_battle_info", arg)
        stat = arg['common']
        me = arg['me']
        ship_id = me["vehicle_type_id"]
        sb = self.battles[ship_id] #just in case if this is a stat for a previous battle
        sb.battle_id +=  'W' if sb.my_team_id == stat["winner_team_id"] else 'L'
        filename = utils.getModDir() + '/vanga_result.csv'
        filemode = 'a+' if utils.isFile(filename) else 'w+' #for some reason 'a' mode does not create file
        with open(filename, filemode) as f:
            f.write('\n{0},'.format(sb.battle_id)) 
            f.write('{0},'.format(sb.my_level)) 
            f.write('{0},'.format(stat["battle_type"])) 
            f.write('{0},'.format(stat["duration_sec"])) 
            f.write('{0},'.format(stat["winner_team_id"])) 
            team0 = 0 if stat["winner_team_id"] == 0 else 1 #winner team always goes first for easier calculation
            team1 = 1 if stat["winner_team_id"] == 0 else 0
            for n in sb.ship_count[team0]: f.write('{0},'.format(n))  # could be simplified, but `map` functionality is not working in ModAPI
            for n in sb.ship_count[team1]: f.write('{0},'.format(n))  
        
    #even registration
    def setup_events(self):
        events.onBattleStart(self.on_battle_start)
        events.onBattleEnd(self.on_battle_end)
        events.onBattleStatsReceived(self.on_battle_get_stat)
        events.onBattleQuit(self.on_battle_quit)


g_Vanga = Vanga()


    # def log_obj(self, filename, obj):
    #     with open(filename + self.battle_id, 'w+') as f:
    #         f.write('%s'%(obj))