# coding=utf-8
# from API_v_1_0 import *

API_VERSION = 'API_v1.0'
MOD_NAME = 'Vanga'

print ("Vanga found")

class Vanga:

    def __init__(self):
        self.setup_events()

    def log_state(self):
        players_info_collection = battle.getPlayersInfo()
        for playerId in players_info_collection:
            player_info = players_info_collection[playerId]
            ship_info = battle.getPlayerShipInfo(playerId)
            fpi = open('fpi_vanga.txt', 'a')
            fpi1 = open('fpi_vanga1.txt', 'w')
            if fpi1 is not None:
                fpi1.write('player_info: \n %s'%(player_info))
                fpi1.write('player_info: \n %s'%(player_info))
                fpi1.close()
            if fpi is not None:
                fpi.write('player_info: \n %s'%(player_info))
                fpi.write('\nship_info: \n %s'%(ship_info))
                fpi.close()
                
    def on_battle_start(self):
        self.log_state()

    def on_battle_quit(self, arg):
        self.log_state()

    def setup_events(self):
        events.onBattleStart(self.on_battle_start)
        events.onBattleQuit(self.on_battle_quit)


g_Vanga = Vanga()
