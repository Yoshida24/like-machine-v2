from fastapi import FastAPI, BackgroundTasks
from playwright.async_api import async_playwright

import requests
from pprint import pprint
import time

# env
instagram_username = ""
instagram_password = ""

FRIENDLY_NAME = ("LIKEマシーン",)
line_notify_token = ""
line_notify_endpoint = "https://notify-api.line.me/api/notify"

# Constants
url = "https://www.instagram.com/"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"


def notify(notification_message):
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": notification_message}
    response = requests.post(line_notify_endpoint, headers=headers, data=data)


async def login(page, instagram_username: str, instagram_password: str):
    # Login
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


async def insta_account_status(page):
    await page.goto("https://www.instagram.com/" + instagram_username + "/")
    info = await page.locator(".x78zum5.x1q0g3np.xieb3on").text_content()
    return info


async def crawl_and_like_posts(page_authenticated, hashtag: str, limit: int):
    # Search
    notify(f"検索タグ #{hashtag}")
    await page_authenticated.goto(
        "https://www.instagram.com/explore/tags/" + hashtag + "/"
    )
    print(await page_authenticated.title())

    # Open First Post
    await page_authenticated.click("._ac7v:nth-child(1) ._aabd:nth-child(1) ._aagv")

    # Like Posts
    for _ in range(limit):
        time.sleep(3)
        # like_btn = page.locator('._aamw:has([aria-label="いいね！"])')
        like_btn = page_authenticated.locator("._aamw").nth(0)
        already_liked = (
            await page_authenticated.locator('[aria-label="「いいね！」を取り消す"]').count() > 0
        )
        print(already_liked)
        if already_liked:
            print("LIKEしなかった : " + page_authenticated.url)
            notify("LIKEしなかった : " + page_authenticated.url)
        else:
            await like_btn.click()
            print("LIKEした : " + page_authenticated.url)
            notify("LIKEした : " + page_authenticated.url)

        print(page_authenticated.url)

        next_btn = page_authenticated.locator('._abl- [aria-label="次へ"]').nth(0)
        print(await next_btn.text_content())
        await next_btn.click()
        print(page_authenticated.url)


async def arun_batch_like(
    instagram_username: str, instagram_password: str, hashtag: str, limit: int
):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(user_agent=user_agent, locale="ja-JP")

        page_authenticated = await login(
            page=page,
            instagram_username=instagram_username,
            instagram_password=instagram_password,
        )

        await crawl_and_like_posts(
            page_authenticated=page_authenticated, hashtag=hashtag, limit=limit
        )


async def get_info():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(user_agent=user_agent, locale="ja-JP")

        info = await insta_account_status(page=page)
        return info


app = FastAPI()


@app.get("/")
async def root():
    return "Hello"


@app.post("/accounts/{account}/like")
async def like(
    background_tasks: BackgroundTasks, account: str, hashtag: str, limit: int = 10
):
    background_tasks.add_task(
        arun_batch_like,
        instagram_username=instagram_username,
        instagram_password=instagram_password,
        limit=limit,
        hashtag=hashtag,
    )

    return f"""info: request accespted.
    account={account}
    instagram_username={instagram_username}
    hashtag={hashtag}
    limit={limit}"""


@app.get("/accounts/{account}/status")
async def status(account: str):
    info = await get_info()
    return info
