from playwright.async_api import async_playwright
from app.modules.scraper.instagram.modules.status import account_status
from app.modules.scraper.instagram.modules.constants import user_agent, locale
from app.modules.scraper.instagram.modules.env import instagram_username


async def get():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(user_agent=user_agent, locale=locale)

        info = await account_status(page=page, instagram_username=instagram_username)
        return info
