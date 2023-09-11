from playwright.async_api import Page


async def login(page: Page, instagram_username: str, instagram_password: str) -> Page:
    # Login
    url = "https://www.instagram.com/"
    await page.goto(url)
    await page.click('[name="username"]')
    await page.fill('[name="username"]', instagram_username)
    await page.click('[name="password"]')
    await page.fill('[name="password"]', instagram_password)
    async with page.expect_navigation():
        await page.click('button[type="submit"]')
    page_authenticated = page
    print(await page_authenticated.title())
    return page_authenticated
