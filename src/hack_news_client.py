import requests
from bs4 import BeautifulSoup

class HackNewsClient:

    def fetch_hacker_news_hot(self):
        # Hacker News URL
        url = "https://news.ycombinator.com/"

        try:
            # Send GET request
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Parse HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Select news items
            titles = soup.select(".titleline > a")  # Titles and links
            subtexts = soup.select(".subtext")  # Scores and other info

            hot_news = []
            for i, title in enumerate(titles):
                news = {
                    "rank": i + 1,
                    "title": title.text,
                    "link": title["href"] if title["href"].startswith(
                        "http") else f"https://news.ycombinator.com/{title['href']}",
                    "score": None
                }

                # Extract score if available
                if i < len(subtexts):
                    score_tag = subtexts[i].select_one(".score")
                    if score_tag:
                        news["score"] = int(score_tag.text.split()[0])  # Convert to integer
                hot_news.append(f"Rank: {news['rank']}, Title: {news['title']}, Link: {news['link']}, Score: {news['score']}")

            result_str = "\n".join(hot_news)  # 用换行符连接列表中的字符串
            return result_str

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []


if __name__ == "__main__":
    news_list = fetch_hacker_news_hot()
    if news_list:
        for news in news_list:
            print(f"Rank: {news['rank']}, Title: {news['title']}, Link: {news['link']}, Score: {news['score']}")
    else:
        print("No news data fetched.")
