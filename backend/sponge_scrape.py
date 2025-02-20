import requests
from bs4 import BeautifulSoup
import re

def checkNone(soup_html, index):
    """
    Make sure the html is not none.

    If none use html in row above:
        If none in row above:
            repeat
    """
    if soup_html is None:
        print(soup)
    else:
        return



url = "https://en.wikipedia.org/wiki/List_of_SpongeBob_SquarePants_episodes"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
current_row_span = 1

for row in soup.find_all(class_="vevent module-episode-list-row"):
    line_sep = "––––––––––––––––––"
    print(f"\n{line_sep*10}\n")
    if row.find("th") is not None:
        row_span = re.search('rowspan="[0-50]"', str(row)).group(0)
        row_span = ''.join(re.findall(r'\d', row_span))
        print(f"NEEWWWWWWW\nNumber of Columns: {len(row)}\nRow Span: {row_span}\n{row.prettify()}\n")

        temp_row = []
    else:
        if current_row_span > 1:
            print(row.prettify())

