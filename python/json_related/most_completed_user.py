# ------------------------------------------------------------
# --  Title: most_completed_user.py
# --  Description: Find the users who completed the most tasks.
# --  Author: Dong Haixia
# --  Date: 2020-08-10
# ------------------------------------------------------------

import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(response.text)
todos = response.json()

# Map userId with the number of complete TODOs with that user.
todos_by_user = {}

# Increment complete TODOS count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOS.
max_complete = top_users[0][1]

# Create a list of all users who have completed the maximum numbers of TODOS.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
#print("{0} have completed {1} TODOS!".format(max_users, max_complete))



# Define a function to filter out completed TODOs of users with max completed TODOS.
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
dir = r"C:\HPE-file\frequent-use\Scripts-personal\python\json_related"
with open(dir + r"\filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)