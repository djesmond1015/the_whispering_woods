# from datetime import datetime
# import time


# initial_time = datetime.now()
# time.sleep(5)
# final_time = datetime.now()

# time_lapsed = final_time - initial_time

# print(time_lapsed)

# total_seconds = time_lapsed.total_seconds()

# hours = int(total_seconds // 3600)  # 3600 seconds in 1 hour
# minutes = int((total_seconds % 3600) // 60)  # 60 seconds in 1 minute
# seconds = int(total_seconds % 60)  # 60 seconds in 1 minute

# formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
# print(formatted_time)

# import pickle
# from datetime import datetime

# # Storing data
# data = {"name": "John", "age": 25}

# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)


# # Retrieving data
# def retrieve_data():
#     with open("data.pkl", "rb") as f:
#         data = pickle.load(f)
#         # print(data)
#         return data


# # Updating data (single field and multiple fields)
# def insert_data(new_data):
#     data = retrieve_data()

#     with open("data.pkl", "wb") as f:
#         data.append(new_data)

#         pickle.dump(data, f)


# Empty data
# with open("data.pkl", "wb") as f:
#     pickle.dump({}, f)

# time = datetime.now()

# insert_data({"name": "Mary", "age": 30, "time": time})
# print("Insert data done")
# print(retrieve_data())
# print("Retrieve data done")


# 6. delete the file


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


# arr = [{"name": "John", "age": 25}]
