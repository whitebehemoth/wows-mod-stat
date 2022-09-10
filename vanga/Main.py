# coding=utf-8
# from API_v_1_0 import *

API_VERSION = 'API_v1.0'
MOD_NAME = 'Vanga'

class Vanga:

    def __init__(self):
        self.FREQUENCY_SEC = 60
        self.MAX_BATTLE_SEC = 1200
        self.ARRAY_LEN = int(self.MAX_BATTLE_SEC / self.FREQUENCY_SEC)
        self.counter = 0
        self.setup_events()

    def callback_func(self):
        utils.logInfo('vanga', {'event': 'callback_func','counter': self.counter,})
        self.log_state()

    def on_battle_start(self):
        self_info = battle.getSelfPlayerInfo()
        self.ship_count = [[0 for x in range(self.ARRAY_LEN)] for y in range(2)] # 2d array
        self.counter = 0
        self.battle_id = utils.timeNowUTC().strftime('%y%m%d_%H%M') 
        self.my_team_id = self_info.teamId
        self.my_level = self_info.shipInfo.level
        self.callback_handler = callbacks.callback(self.FREQUENCY_SEC, self.callback_func)

    def on_battle_quit(self, arg):
        callbacks.cancel(self.callback_handler)        

    def on_battle_end(self, arg1, arg2):
        self.counter = 19 # last record
        self.log_state()

    def log_state(self):
        players_info_collection = battle.getPlayersInfo()
        for playerId in players_info_collection:
            player_info = players_info_collection[playerId]
            self.ship_count[player_info.teamId][self.counter] += 1 if player_info.isAlive else 0
        self.counter += 1
        
        
        
    def on_battle_get_stat(self, arg):
        stat = arg['common']
        self.battle_id +=  'W' if self.my_team_id == stat["winner_team_id"] else 'L'
        filename = utils.getModDir() + '/vanga_result.csv'
        filemode = 'a+' if utils.isFile(filename) else 'w+' #for some reason 'a' mode does not create file
        with open(filename, filemode) as f:
            f.write('\n{0},'.format(self.battle_id)) 
            f.write('{0},'.format(self.my_level)) 
            f.write('{0},'.format(stat["battle_type"])) 
            f.write('{0},'.format(stat["duration_sec"])) 
            f.write('{0},'.format(stat["winner_team_id"])) 
            team0 = 0 if stat["winner_team_id"] == 0 else 1 #winner team always goes first for easier calculation
            team1 = 1 if stat["winner_team_id"] == 0 else 0
            for n in self.ship_count[team0]: f.write('{0},'.format(n))  # could be simplified, but `map` functionality is not working in ModAPI
            for n in self.ship_count[team1]: f.write('{0},'.format(n))  # could be simplified, but `map` functionality is not working in ModAPI
        

    def setup_events(self):
        events.onBattleStart(self.on_battle_start)
        events.onBattleEnd(self.on_battle_end)
        events.onBattleStatsReceived(self.on_battle_get_stat)
        events.onBattleQuit(self.on_battle_quit)

g_Vanga = Vanga()



    # def log_dataHub(self, filename):
    #     #players1 = dataHub.getSingleEntity('avatar')
    #     players = dataHub.getEntityCollections('avatar')
    #     # playerAvatar = dataHub.getEntityCollections('playerAvatar')
    #     health = dataHub.getEntityCollections('health')
    #     with open(filename + '.dataHub', 'w+') as f:
    #         for p in players:
    #             e=dataHub.getEntity(p.id)
    #             f.write(str(p))
    #             f.write('\n e -----------------------\n')
    #             f.write(str(e))
    #         for h in health:
    #             f.write('\n health -----------------------\n')
    #             f.write(str(h))
    #             f.write('\n h.id -----------------------\n')
    #             f.write(str(h.id))
    #             eh=dataHub.getEntity(h.id)
    #             f.write('\n eh -----------------------\n')
    #             f.write(str(eh))

            # f.write('\n playerAvatar -----------------------\n')
            # f.write(str(playerAvatar))
            # f.write('\n health -----------------------\n')
            # f.write(str(health))
            # f.write('\n players1 -----------------------\n')
            # f.write(str(players1))

            


    # def log_dataHub(self, filename):
    #     #players1 = dataHub.getSingleEntity('avatar')
    #     players = dataHub.getEntityCollections('avatar')
    #     # playerAvatar = dataHub.getEntityCollections('playerAvatar')
    #     health = dataHub.getEntityCollections('health')
    #     with open(filename + '.dataHub', 'w+') as f:
    #         for p in players:
    #             f.write(str(p))
    #             f.write('\n p.id -----------------------\n')
    #             f.write(str(p.id))
    #             f.write('\n p.name -----------------------\n')
    #             f.write(p.name + ":" + p.pureName)
    #         for h in health:
    #             f.write(str(h))
    #             f.write('\n h.id -----------------------\n')
    #             f.write(str(h.id))
    #             f.write('\n h.value delta max damage -----------------------\n')
    #             f.write(str(h.value) + ":" + str(h.delta) + ":" + str(h.max) + ":" + str(h.damage) )    
    #         # f.write('\n playerAvatar -----------------------\n')
    #         # f.write(str(playerAvatar))
    #         # f.write('\n health -----------------------\n')
    #         # f.write(str(health))
    #         # f.write('\n players1 -----------------------\n')
    #         # f.write(str(players1))

#     f.write(str(self.ship_count).replace('[','\n').replace(']','')) 

        # self.ship_count[0] = '{0},{1},{2},{3},{4},{5},{6}'.format(self.battle_id, self.my_level, self.team_size, stat["battle_type"], stat["duration_sec"], self.my_team_id, stat["winner_team_id"]) #battle header
        #     f.write(str(self.ship_count).replace('[','\n').replace(']','')) 
            #f.write('%s\n'%', '.join(map(str, self.team_ship_count))) # not working in ModAPI

        #events.onSFMEvent(self.test_event)
    # def test_event(self, en, ed):
    #     with open(str(en), 'w+') as f:
    #         f.write(str(ed)) 


    # def log_self(self, filename):
    #     self_info = battle.getSelfPlayerInfo()
    #     with open(filename, 'w+') as f:
    #         f.write('%s'%(self_info))


        #     self.team_ship_count[player_info.teamId]
        #     ship_info = battle.getSelfPlayerInfo(playerId)
        #     fpi = open(filename, 'a+')
        #     if fpi is not None:
        #         fpi.write('player_info: \n %s'%(player_info))
        #         fpi.write('\nship_info: \n %s'%(ship_info))
        #         fpi.close()
    
         


        
        #utils.logInfo('vanga', {'event': 'onBattleQuit','arg': arg,})
        #self.log_self('vanga_quit.json')



#         me."common":{
#       "win_type_id":13,
#       "winner_team_id":1,
#       "arena_id":2899542673983039L,
#       "map_type_id":25,
#       "survey_id":0,
#       "duration_sec":862,
#       "game_mode":7,
#       "clan_season_id":18,
#       "clan_season_type":"regular",
#       "battle_type":"RandomBattle",
#       "scenario_name":"Domination_3point",
#       "battle_type_id":5,
#       "start_dt":1662518890
#    },

#self.log_self(self.battle_id)

        # with open('vanga_test.pi', 'w+') as f:            
        #     for key, value in stat.iteritems() :
        #         f.write('{0}:{1}\n'.format(key, value)) 
        #utils.logInfo('vanga', {'event': 'onBattleStat', 'type(me)': type(stat)})