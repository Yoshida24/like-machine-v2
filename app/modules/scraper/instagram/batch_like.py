from playwright.async_api import async_playwright
from app.modules.scraper.instagram.modules.crawl_and_like import crawl_and_like_posts
from app.modules.scraper.instagram.modules.login import login
from app.modules.scraper.instagram.modules.constants import user_agent, locale
from app.modules.scraper.instagram.modules.env import (
    instagram_username,
    instagram_password,
)


async def post(hashtag: str, limit: int):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(user_agent=user_agent, locale=locale)

        page_authenticated = await login(
            page=page,
            instagram_username=instagram_username,
            instagram_password=instagram_password,
        )

        await crawl_and_like_posts(
            page_authenticated=page_authenticated, hashtag=hashtag, limit=limit
        )
