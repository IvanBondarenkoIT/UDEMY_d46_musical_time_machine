from scrape_manager import scrape_top_song_titles

TEST_DATE = '2010-12-31'


def main(date_to_travel):
    top_songs_titles = scrape_top_song_titles(date_to_travel)
    return top_songs_titles


if __name__ == '__main__':
    # user_date = input("Enter date which you want to travel to (YYYY-MM-DD):")
    user_date = TEST_DATE
    print(main(user_date))

