# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist

from src.kth_largest import kth_largest

app = FastAPI(title="Algo-warmup API")


class KthRequest(BaseModel):
    nums: conlist(int, min_items=1)   # список ≥ 1 эл.
    k: int

    model_config = {"json_schema_extra": {"examples": [{"nums": [5,1,9,6], "k": 2}]}}  # пример для Swagger


class KthResponse(BaseModel):
    value: int


@app.post("/kth", response_model=KthResponse)
async def kth(req: KthRequest):
    if not 1 <= req.k <= len(req.nums):
        raise HTTPException(status_code=422, detail="k out of range")
    return {"value": kth_largest(req.nums, req.k)}

