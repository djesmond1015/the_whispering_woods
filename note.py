# GameStatePersistanceWrapper => GameStateController (Business Logic) => AdventureGameEngine(Client) OR Vice versa


# All GameStateController methods:
# A1. retrieve all or a list of data with limit parameter [GET]
# A2. reset the game (empty the file) [DELETE] (this will never be used)
# A3. delete all data (delete file) [DELETE] (this will never be used)

# B1. retrieve particular data [GET] - (unique_id, player_name)
# B2. insert or create data [POST] - (player, scene_name)
# B3. update or replace data [PUT] - (unique_id, player_name, new_data)
# B4. delete data [DELETE] - list of (unique_id, player_name)

# C1. Calculate time taken to complete the game


# All GameStatePersistanceWrapper methods:
# save_game_state
# load_game_state
# delete_game_state

# Load game menu methods:
# 1. Display list of saved games that haven't completed [A1]
# 2. Load game - (only load the game that is not completed) [B1]
# 3. Reset game - delete all list of game that haven't completed [B4]

# AdventureGameEngine methods:
# initialize_game_state - [B2]
# save_game - [B3]

# Game Statistics
# Only show the completed games.

# 1. The time taken to complete the game.
# 2. The number of scenes the player has visited to complete the game.
# 3. The highest number of scenes the player has visited to complete the game.
# 4. The lowest number of scenes the player has visited to complete the game.
# 5. The average time taken to complete the game.
# 6. The shortest time taken to complete the game.
# 7. The longest time taken to complete the game.
# 8. The number of wins the player has achieved.
