from tenacity import retry, wait_exponential, stop_after_attempt
import httpx
from src.core.config import settings


@retry(wait=wait_exponential(multiplier=1, min=1, max=10), stop=stop_after_attempt(3))
async def embed_text(text: str) -> dict:
    if not settings.OPENAI_API_KEY:
        return {"embedding": []}
    headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}"}
    async with httpx.AsyncClient(timeout=30) as client:
        # exemplo placeholder — ajuste ao modelo de embedding desejado
        resp = await client.post(
            "https://api.openai.com/v1/embeddings",
            headers=headers,
            json={"model": "text-embedding-3-small", "input": text},
        )
        resp.raise_for_status()
        return resp.json()
