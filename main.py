from src import database
from src import fetching
from src import parsing
from src import telegramMessenger

status, row_id = database.insert_scraper_logs()

if status == True: 
    websites_list = database.fetch_websites()

    web_url = []
    html_structure = fetching.fetch_html(web_url)

    parsing_data = parsing.parse_html(html_structure)

    site_id = []
    novels_list = database.fetch_novels(site_id)

    updated_novel_list = []
    database.update_novels_table(updated_novel_list)

    novel_id_list = []
    subscribers_list = database.fetch_subscribers(novel_id_list)

    database.update_scraper_logs(row_id)