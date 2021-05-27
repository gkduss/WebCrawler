from utils.db_library import (
    select_all_urls,
    select_available_urls,
    select_unstored_urls,
    update_row,
)
import sqlite3
import bs4

# res = requests.get("https://linkmoum.live", stream=True)
# soup = bs4.BeautifulSoup(res.content)

urls = select_all_urls()
unnormalized = [url for url in urls if url[-1] == "/"]
print(unnormalized)
# with sqlite3.connect("illegals.db") as db_connection:
#     for url in unnormalized:
#         query = f"""
#             UPDATE illegal_sites
#             SET main_url = ?
#             WHERE main_url = ?
#         """
#         cursor = db_connection.cursor()
#         cursor.execute(query, (url[:-1], url))


# print(res.raw.connection.sock)