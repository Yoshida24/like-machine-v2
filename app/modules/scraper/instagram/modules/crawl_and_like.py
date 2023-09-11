from playwright.async_api import Page
from app.modules.notification import line

import time


async def crawl_and_like_posts(
    page_authenticated: Page, hashtag: str, limit: int
) -> None:
    # Search
    line.notify(f"検索タグ #{hashtag}")
    await page_authenticated.goto(
        "https://www.instagram.com/explore/tags/" + hashtag + "/"
    )
    print(await page_authenticated.title())

    # Open First Post
    await page_authenticated.click("._ac7v:nth-child(1) ._aabd:nth-child(1) ._aagv")

    # Like Posts
    for _ in range(limit):
        time.sleep(3)
        like_btn = page_authenticated.locator("._aamw").nth(0)
        already_liked = (
            await page_authenticated.locator('[aria-label="「いいね！」を取り消す"]').count() > 0
        )
        print(already_liked)
        if already_liked:
            print("LIKEしなかった : " + page_authenticated.url)
            line.notify("LIKEしなかった : " + page_authenticated.url)
        else:
            await like_btn.click()
            print("LIKEした : " + page_authenticated.url)
            line.notify("LIKEした : " + page_authenticated.url)

        print(page_authenticated.url)

        next_btn = page_authenticated.locator('._abl- [aria-label="次へ"]').nth(0)
        print(await next_btn.text_content())
        await next_btn.click()
        print(page_authenticated.url)
