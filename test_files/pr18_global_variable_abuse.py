total_users = 0
active_sessions = []

def add_user(user):
    global total_users
    total_users += 1
    active_sessions.append(user)