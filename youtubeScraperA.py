from youtubesearchpython import VideosSearch
import csv

def get_videos(keyword):
    videosSearch = VideosSearch(f'{keyword} new', limit=30)

    for i in videosSearch.result()["result"]:
        publ = str(i["publishedTime"]).lower()

        if "year" in publ:
            continue

        if "month" in publ:
            continue

        if "week" in publ:
            continue

        no_of_days = int(publ.split(" ")[0])

        with open("data.csv", "a", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([i["title"], no_of_days,  i["link"], keyword])



