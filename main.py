import streamlit as st
import pandas as pd
from youtubeScraperA import get_videos
import csv

def get_file_data(file):
    with open(file, "r") as f:
        data = f.read().strip().split("\n")
    return data

def update_file_data(file, data):
    with open(file, "w") as f:
        f.write(data)


# take channel link as input
channel_link = st.text_input("Enter the channel name here: ", placeholder="Codebasics")
list_of_channels = get_file_data("list_of_channels.txt")
# drop down to select the channel
channel = st.selectbox("Select the channel: ", list_of_channels)
col1, col2, col3, col4 = st.columns(4)

with col1:
    # a button to start the process
    if st.button("Add Channel"):
        st.write("Running")
        list_of_channels = get_file_data("list_of_channels.txt")

        if channel_link not in list_of_channels:
            list_of_channels.append(channel_link)
            update_file_data("list_of_channels.txt", "\n".join(list_of_channels))
            st.write("Channel Added")
        else:
            st.write("Channel Already Added")


with col2:
    # delete a channel
    if st.button("Delete Channel"):
        st.write("Running")
        list_of_channels = get_file_data("list_of_channels.txt")
        print(list_of_channels)
        print(channel)
        if str(channel) in list_of_channels:
            list_of_channels.remove(channel)
            update_file_data("list_of_channels.txt", "\n".join(list_of_channels))
            st.write("Channel Deleted")
        else:
            st.write("Channel Not Found")


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link

    return f'<a target="_blank" href="{link}">Watch Video</a>'


with col3:
    # a button to start the process
    if st.button("Start Process"):
        st.write("Running")
        with open("data.csv", "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["Title", "Published Time", "Link", "Channel"])
        list_of_channels = get_file_data("list_of_channels.txt")
        for i in list_of_channels:
            if i == "":
                continue
            get_videos(i)

        st.write("Process Completed")

with col4:
    # a button to show the data
    show_data = st.button("Show Data")
if show_data:
    df = pd.read_csv("data.csv")

    columns = ["Title", "Published Time", "Link", "Channel"]
    df.columns = columns
    # sort the data by published time
    df = df.sort_values(by="Published Time")

    # add days ago in published time
    df["Published Time"] = df["Published Time"].apply(lambda x: f"{x} days ago")

    df['Link'] = df['Link'].apply(make_clickable)
    df = df.to_html(escape=False)


    # show a table
    st.write(df, unsafe_allow_html=True)






