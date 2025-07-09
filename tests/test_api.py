import pytest
from httpx import AsyncClient
from src import app


@pytest.mark.asyncio
async def test_kth_api():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/kth", json={"nums": [5,1,9,6], "k": 2})
    assert resp.status_code == 200
    assert resp.json() == {"value": 6}
