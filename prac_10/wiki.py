import wikipedia
import warnings
from bs4 import GuessedAtParserWarning

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)


def main():
    page_title = input("Enter a page title or search phrase (blank to quit): ")

    while page_title != "":

        try:
            page = wikipedia.page(page_title)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError:
            print("Disambiguation page. Please specify a more specific title.")
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        page_title = input("Enter a page title or search phrase (blank to quit): ")


if __name__ == "__main__":
    main()
