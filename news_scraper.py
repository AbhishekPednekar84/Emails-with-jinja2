import requests
import bs4
from jinja2 import FileSystemLoader, Environment


def scrape_render(template):
    statesman = requests.get("https://www.thestatesman.com/")
    statesman.raise_for_status()
    soup = bs4.BeautifulSoup(statesman.text, "lxml")
    final_content = {}

    for top_picks in soup.find_all("div", class_="aroundtheword"):
        for sl, news in enumerate(top_picks.ul.find_all("li"), start=1):
            headline = news.a.text
            url = news.a["href"]
            image = news.a.img["src"]

            final_content[headline] = [url, image]

    template_loader = FileSystemLoader(searchpath="templates/")
    template_env = Environment(loader=template_loader)
    final_template = template_env.get_template(template)

    return final_template.render(final_content=final_content)
