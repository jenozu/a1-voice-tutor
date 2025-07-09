import pandas as pd
from datetime import datetime, timedelta
import os

def get_week_start(date=None):
    """
    Get the start date (Monday) of the week for a given date.
    """
    if date is None:
        date = datetime.now().date()
    return (date - timedelta(days=date.weekday())).strftime('%Y-%m-%d')

def get_leaderboard(leaderboard_path='data/leaderboard.csv', top_n=10):
    """
    Get the top N users by XP for the current week.
    Args:
        leaderboard_path (str): Path to leaderboard.csv
        top_n (int): Number of top users to return
    Returns:
        DataFrame: Top N leaderboard entries
    """
    try:
        week_start = get_week_start()
        if os.path.exists(leaderboard_path):
            df = pd.read_csv(leaderboard_path)
            df_week = df[df['week_start'] == week_start]
            df_week = df_week.sort_values('xp', ascending=False).head(top_n)
            return df_week
        else:
            return pd.DataFrame(columns=['username', 'week_start', 'xp'])
    except Exception as e:
        print(f"Error getting leaderboard: {e}")
        return pd.DataFrame(columns=['username', 'week_start', 'xp'])

def update_leaderboard(user_id, xp, leaderboard_path='data/leaderboard.csv'):
    """
    Update or add a user's weekly XP in the leaderboard.
    Args:
        user_id (str): User's ID or username
        xp (int): XP to add for this week
        leaderboard_path (str): Path to leaderboard.csv
    """
    try:
        week_start = get_week_start()
        if os.path.exists(leaderboard_path):
            df = pd.read_csv(leaderboard_path)
        else:
            df = pd.DataFrame(columns=['username', 'week_start', 'xp'])
        idx = df[(df['username'] == user_id) & (df['week_start'] == week_start)].index
        if len(idx) > 0:
            df.loc[idx[0], 'xp'] = int(df.loc[idx[0], 'xp']) + int(xp)
        else:
            df = pd.concat([df, pd.DataFrame([{'username': user_id, 'week_start': week_start, 'xp': int(xp)}])], ignore_index=True)
        df.to_csv(leaderboard_path, index=False)
        return True
    except Exception as e:
        print(f"Error updating leaderboard: {e}")
        return False

def reset_leaderboard(leaderboard_path='data/leaderboard.csv'):
    """
    Reset the leaderboard for a new week.
    Args:
        leaderboard_path (str): Path to leaderboard.csv
    """
    try:
        week_start = get_week_start()
        # Optionally, archive old leaderboard here
        df = pd.DataFrame(columns=['username', 'week_start', 'xp'])
        df.to_csv(leaderboard_path, index=False)
        return True
    except Exception as e:
        print(f"Error resetting leaderboard: {e}")
        return False 