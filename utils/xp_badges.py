import pandas as pd
from datetime import datetime, timedelta
import os

# XP and Badges Module

def add_xp(user_id, amount, users_path='data/users.csv'):
    """
    Add XP to a user and persist to users.csv
    Args:
        user_id (str): User's ID or username
        amount (int): XP to add
        users_path (str): Path to users.csv
    Returns:
        int: New XP total, or None on error
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return None
        users.loc[idx[0], 'xp'] = int(users.loc[idx[0], 'xp']) + int(amount)
        users.to_csv(users_path, index=False)
        return int(users.loc[idx[0], 'xp'])
    except Exception as e:
        print(f"Error adding XP: {e}")
        return None

def check_for_badges(user_id, users_path='data/users.csv'):
    """
    Check and award badges for milestones (5-day streak, 100 XP, etc.)
    Args:
        user_id (str): User's ID or username
        users_path (str): Path to users.csv
    Returns:
        list: List of newly awarded badges
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return []
        user = users.loc[idx[0]]
        badges = set(str(user.get('badges', '')).split(',')) if 'badges' in users.columns else set()
        new_badges = []
        # Badge: 5-day streak
        if int(user.get('streak', 0)) >= 5 and '5-day streak' not in badges:
            badges.add('5-day streak')
            new_badges.append('5-day streak')
        # Badge: 100 XP
        if int(user.get('xp', 0)) >= 100 and '100 XP' not in badges:
            badges.add('100 XP')
            new_badges.append('100 XP')
        # Badge: 7-day streak
        if int(user.get('streak', 0)) >= 7 and '7-day streak' not in badges:
            badges.add('7-day streak')
            new_badges.append('7-day streak')
        # Badge: 500 XP
        if int(user.get('xp', 0)) >= 500 and '500 XP' not in badges:
            badges.add('500 XP')
            new_badges.append('500 XP')
        # Save badges back
        if 'badges' not in users.columns:
            users['badges'] = ''
        users.loc[idx[0], 'badges'] = ','.join(sorted(b for b in badges if b and b != 'nan'))
        users.to_csv(users_path, index=False)
        return new_badges
    except Exception as e:
        print(f"Error checking badges: {e}")
        return []

def update_streak(user_id, users_path='data/users.csv'):
    """
    Update user's streak based on last activity date
    Args:
        user_id (str): User's ID or username
        users_path (str): Path to users.csv
    Returns:
        int: New streak value, or None on error
    """
    try:
        users = pd.read_csv(users_path)
        idx = users[users['username'] == user_id].index
        if len(idx) == 0:
            return None
        today = datetime.now().date()
        last_active = users.loc[idx[0], 'last_active'] if 'last_active' in users.columns else ''
        if last_active:
            last_active_date = datetime.strptime(str(last_active), '%Y-%m-%d').date()
            if (today - last_active_date).days == 1:
                users.loc[idx[0], 'streak'] = int(users.loc[idx[0], 'streak']) + 1
            elif (today - last_active_date).days > 1:
                users.loc[idx[0], 'streak'] = 1
            # else: same day, streak unchanged
        else:
            users.loc[idx[0], 'streak'] = 1
        users.loc[idx[0], 'last_active'] = today.strftime('%Y-%m-%d')
        users.to_csv(users_path, index=False)
        return int(users.loc[idx[0], 'streak'])
    except Exception as e:
        print(f"Error updating streak: {e}")
        return None


