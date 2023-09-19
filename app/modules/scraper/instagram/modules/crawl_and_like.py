from playwright.async_api import Page
from app.modules.notification import line

import time
import os


async def crawl_and_like_posts(
    page_authenticated: Page, hashtag: str, limit: int
) -> None:
    # Search
    start_msg = os.linesep.join([
        "",
        f"✅ Batch job started.",f"🔍 hashtag:{hashtag}",
    ])
    line.notify(start_msg)
    await page_authenticated.goto(
        "https://www.instagram.com/explore/tags/" + hashtag + "/"
    )
    print(await page_authenticated.title())

    # Open First Post
    await page_authenticated.click("._ac7v:nth-child(1) ._aabd:nth-child(1) ._aagv")

    # Counter
    like_success = 0

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
        else:
            await like_btn.click()
            print("LIKEした : " + page_authenticated.url)
            like_success += 1

        print(page_authenticated.url)

        next_btn = page_authenticated.locator('._abl- [aria-label="次へ"]').nth(0)
        print(await next_btn.text_content())
        await next_btn.click()
        print(page_authenticated.url)

    success_msg = os.linesep.join(
        [
            "",
            "✅ Batch job successed.",
            "",
            f"🔍 hashtag:{str(hashtag)}",
            f"💚 successfully liked:{str(like_success)}",
            f"💔 failed to like:{str(limit - like_success)}",
        ]
    )
    line.notify(success_msg)
