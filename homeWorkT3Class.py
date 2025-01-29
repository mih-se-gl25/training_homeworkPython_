# Implement script that simulate ships battle. In game there are two teams.
# Each team can has one or more ships. Each ship has a power and armor.
# Power is integer number that indicate maximum hit. Hit is float number that
# can be from 25% to 100% of power. Armour is float number that need to be
# subtracted by hit after ship was hitted. If armour will decreased to 0 ship
# will began drowning. Drowning last 2 step. After drowning ship should be
# removed from team. During drowning ship can shot. Simulation consist of
# iterations, during each iteration each ship shot to random ship from enemy
# team, information about iteration should be printed. Simulation should last
# until one of that team will run out of ships. Number of ships in each team,
# armour and power of each ship should be stored in json file, designing
# format of this json is also a part of homework.