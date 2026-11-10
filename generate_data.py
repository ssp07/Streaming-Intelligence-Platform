import pandas as pd
import random
from datetime import datetime, timedelta

# --------------------
# USERS (150 records)
# --------------------

countries = [
    "India", "USA", "UK", "Canada",
    "Germany", "Australia", "Japan"
]

plans = [
    "Basic",
    "Standard",
    "Premium"
]

users = []

for user_id in range(1, 151):
    users.append({
        "user_id": user_id,
        "age": random.randint(18, 65),
        "country": random.choice(countries),
        "subscription": random.choice(plans)
    })

users_df = pd.DataFrame(users)

# --------------------
# CONTENT (120 records)
# --------------------

genres = [
    "Action",
    "Drama",
    "Comedy",
    "Thriller",
    "Sci-Fi",
    "Crime",
    "Documentary",
    "Fantasy"
]

content = []

for content_id in range(101, 221):
    content.append({
        "content_id": content_id,
        "title": f"Movie_{content_id}",
        "genre": random.choice(genres),
        "rating": round(random.uniform(6.0, 9.8), 1)
    })

content_df = pd.DataFrame(content)

# --------------------
# WATCH HISTORY
# 1000 records
# --------------------

watch_history = []

for _ in range(1000):
    watch_history.append({
        "user_id": random.randint(1, 150),
        "content_id": random.randint(101, 220),
        "watch_time": random.randint(20, 300)
    })

watch_df = pd.DataFrame(watch_history)

# --------------------
# SAVE FILES
# --------------------

users_df.to_csv(
    "users.csv",
    index=False
)

content_df.to_csv(
    "content.csv",
    index=False
)

watch_df.to_csv(
    "watch_history.csv",
    index=False
)

print("Datasets generated successfully!")