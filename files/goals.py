import pandas as pd
from datetime import datetime, timedelta

def set_goal(user_id, goal_type, amount, users_path='data/users.csv'):
    """
    Set a daily or weekly XP goal for a user.
    Args:
        user_id (str): User's ID or username
        goal_type (str): 'daily' or 'weekly'
        amount (int): XP goal amount
        users_path (str): Path to users.csv
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return False
        col_goal = f'{goal_type}_goal'
        col_progress = f'{goal_type}_progress'
        if col_goal not in users.columns:
            users[col_goal] = 0
        if col_progress not in users.columns:
            users[col_progress] = 0
        users.loc[idx[0], col_goal] = int(amount)
        users.loc[idx[0], col_progress] = 0
        users.to_csv(users_path, index=False)
        return True
    except Exception as e:
        print(f"Error setting goal: {e}")
        return False

def get_goal(user_id, goal_type, users_path='data/users.csv'):
    """
    Get the current daily or weekly XP goal for a user.
    Args:
        user_id (str): User's ID or username
        goal_type (str): 'daily' or 'weekly'
        users_path (str): Path to users.csv
    Returns:
        int: Goal amount, or None if not set
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return None
        col_goal = f'{goal_type}_goal'
        if col_goal in users.columns:
            return int(users.loc[idx[0], col_goal])
        return None
    except Exception as e:
        print(f"Error getting goal: {e}")
        return None

def update_goal_progress(user_id, xp_earned, users_path='data/users.csv'):
    """
    Update both daily and weekly goal progress for a user.
    Args:
        user_id (str): User's ID or username
        xp_earned (int): XP earned to add
        users_path (str): Path to users.csv
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return False
        for goal_type in ['daily', 'weekly']:
            col_progress = f'{goal_type}_progress'
            if col_progress not in users.columns:
                users[col_progress] = 0
            users.loc[idx[0], col_progress] = int(users.loc[idx[0], col_progress]) + int(xp_earned)
        users.to_csv(users_path, index=False)
        return True
    except Exception as e:
        print(f"Error updating goal progress: {e}")
        return False

def check_goal_completion(user_id, goal_type, users_path='data/users.csv'):
    """
    Check if a user's daily or weekly goal is met, reset or adjust as needed.
    Args:
        user_id (str): User's ID or username
        goal_type (str): 'daily' or 'weekly'
        users_path (str): Path to users.csv
    Returns:
        bool: True if goal met, False otherwise
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return False
        col_goal = f'{goal_type}_goal'
        col_progress = f'{goal_type}_progress'
        if col_goal not in users.columns or col_progress not in users.columns:
            return False
        goal = int(users.loc[idx[0], col_goal])
        progress = int(users.loc[idx[0], col_progress])
        if progress >= goal and goal > 0:
            # Reset progress for next period
            users.loc[idx[0], col_progress] = 0
            users.to_csv(users_path, index=False)
            return True
        return False
    except Exception as e:
        print(f"Error checking goal completion: {e}")
        return False 