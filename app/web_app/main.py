from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.infra import Cache
from app.metrics import get_metrics_worldometers

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Message-Code", "content-disposition"],
)


@app.get("/")
async def root():
    cache = Cache()

    metrics = cache.get_metrics()
    if not metrics:
        worldometers = get_metrics_worldometers()

        metrics = {"worldometers": worldometers}  # TODO: usar pydantic
        cache.save_metrics(metrics)

        return metrics

    return metrics
