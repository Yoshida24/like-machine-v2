from playwright.async_api import Page


async def account_status(page: Page, instagram_username: str) -> str | None:
    await page.goto("https://www.instagram.com/" + instagram_username + "/")
    info = await page.locator(".x78zum5.x1q0g3np.xieb3on").text_content()
    return info
