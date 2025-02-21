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
header_row = []

for row in soup.find_all(class_="vevent module-episode-list-row"):
    line_sep = "––––––––––––––––––"
    print(f"\n{line_sep*10}\n")

    # Find rows with table headers (spans multiple rows sometimes.)
    if row.find("th") is not None:
        # Find the row_span number (how many rows a column spans)
        row_span = re.search('rowspan="[0-50]"', str(row)).group(0)
        row_span = ''.join(re.findall(r'\d', row_span))
        current_row_span = int(row_span)

        temp_row = []
        for item in row.find_all("td"):
            sub_string = (f'rowspan="{row_span}"')
            if re.search(f'rowspan="{row_span}"', str(row)):
                temp_row.append(item.getText())
                header_row = temp_row
                for t in header_row:
                    print(t)
            else:
                temp_row.append(item)
                print(f"\n\n{item}\n\n")
    else:
        if current_row_span > 1:
            print(row.prettify())
            current_row_span -= 1
        else:
            header_row = []
