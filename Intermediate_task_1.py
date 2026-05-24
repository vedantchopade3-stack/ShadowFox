import scrapy
import json
import pdfkit
import os
from scrapy.crawler import CrawlerProcess

class YouTubeSpider(scrapy.Spider):

    name = "youtube"

    start_urls = [
        "https://www.youtube.com/results?search_query=python"
    ]

    video_data = []

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
    }

    def parse(self, response):

        try:

            scripts = response.css(
                "script::text"
            ).getall()

            for script in scripts:

                if "var ytInitialData" in script:

                    try:

                        data_text = script.split(
                            "var ytInitialData = "
                        )[1].split(";")[0]

                        data = json.loads(data_text)

                        sections = data["contents"][
                            "twoColumnSearchResultsRenderer"
                        ]["primaryContents"][
                            "sectionListRenderer"
                        ]["contents"]

                        for section in sections:

                            items = section.get(
                                "itemSectionRenderer", {}
                            ).get(
                                "contents", []
                            )

                            for item in items:

                                video = item.get(
                                    "videoRenderer"
                                )

                                if video:

                                    title = video[
                                        "title"
                                    ]["runs"][0]["text"]

                                    video_id = video[
                                        "videoId"
                                    ]

                                    url = (
                                        "https://www.youtube.com/watch?v="
                                        + video_id
                                    )

                                    self.video_data.append({
                                        "title": title,
                                        "url": url
                                    })

                    except:
                        pass

        except Exception as e:
            print("Error:", e)

    def closed(self, reason):

        html = """
        <html>
        <body>
        <h1>YouTube Scraping Results</h1>
        """

        for i, video in enumerate(
                self.video_data,
                start=1):

            html += f"""
            <h3>{i}. {video['title']}</h3>
            <p>{video['url']}</p>
            <hr>
            """

        html += """
        </body>
        </html>
        """

        with open(
            "youtube_output.html",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        pdfkit.from_file(
            "youtube_output.html",
            "youtube_output.pdf"
        )

        print(
            "PDF Created Successfully"
        )

        os.startfile(
            "youtube_output.pdf"
        )


process = CrawlerProcess()

process.crawl(
    YouTubeSpider
)

process.start()