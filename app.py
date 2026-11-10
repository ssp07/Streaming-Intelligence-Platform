import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Streaming Intelligence Platform",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------
# Load Data
# --------------------------------

users = pd.read_csv("users.csv")
content = pd.read_csv("content.csv")
watch = pd.read_csv("watch_history.csv")

# --------------------------------
# Merge
# --------------------------------

data = watch.merge(
    users,
    on="user_id"
)

data = data.merge(
    content,
    on="content_id"
)

# --------------------------------
# Header
# --------------------------------

st.title("🎬 Streaming Intelligence Platform")

st.markdown("""
Analytics platform for understanding user behavior,
content performance, and recommendation insights.
""")

# --------------------------------
# KPIs
# --------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Users",
    users["user_id"].nunique()
)

col2.metric(
    "Content",
    content["content_id"].nunique()
)

col3.metric(
    "Total Watch Time",
    int(data["watch_time"].sum())
)

col4.metric(
    "Avg Watch Time",
    round(data["watch_time"].mean(), 1)
)

st.divider()

# --------------------------------
# Genre Analytics
# --------------------------------

st.subheader("🎭 Genre Performance")

genre_watch = (
    data.groupby("genre")["watch_time"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    genre_watch,
    x="genre",
    y="watch_time",
    color="genre"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------
# Content Analytics
# --------------------------------

st.subheader("🏆 Top Content")

content_watch = (
    data.groupby("title")["watch_time"]
    .sum()
    .reset_index()
    .sort_values(
        by="watch_time",
        ascending=False
    )
)

fig2 = px.bar(
    content_watch,
    x="title",
    y="watch_time",
    color="watch_time"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------
# Subscription Insights
# --------------------------------

st.subheader("💳 Subscription Analysis")

sub_data = (
    data.groupby("subscription")
    ["watch_time"]
    .mean()
    .reset_index()
)

fig3 = px.pie(
    sub_data,
    values="watch_time",
    names="subscription"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------
# Recommendation Engine
# --------------------------------

st.subheader("🤖 Simple Recommendation Engine")

selected_user = st.selectbox(
    "Select User",
    users["user_id"]
)

user_history = data[
    data["user_id"] == selected_user
]["genre"].unique()

recommendations = content[
    content["genre"].isin(user_history)
]

st.write(
    "Recommended Content:"
)

st.dataframe(
    recommendations[
        ["title","genre","rating"]
    ]
)

# --------------------------------
# Insights
# --------------------------------

st.subheader("📈 Platform Insights")

top_content = content_watch.iloc[0]

st.success(
    f"Most watched title: "
    f"{top_content['title']}"
)

top_genre = genre_watch.sort_values(
    "watch_time",
    ascending=False
).iloc[0]

st.info(
    f"Most engaging genre: "
    f"{top_genre['genre']}"
)