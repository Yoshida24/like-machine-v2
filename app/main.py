from fastapi import FastAPI, BackgroundTasks
from app.modules.scraper.instagram import batch_like, status

app = FastAPI()


@app.get("/")
async def root():
    return "Hello"


@app.post("/tasks/like")
async def like(background_tasks: BackgroundTasks, hashtag: str, limit: int = 10):
    background_tasks.add_task(
        batch_like.post,
        hashtag=hashtag,
        limit=limit,
    )

    return f"""info: request accepted.
    hashtag={hashtag}
    limit={limit}"""


@app.get("/status")
async def status_get(background_tasks: BackgroundTasks):
    background_tasks.add_task(status.get)
    return f"""info: request accepted."""
