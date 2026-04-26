import pytest
from utils.ai_analyzer import analyze_failure
from utils.logger import log_failure
from utils.self_healing import click_with_healing

@pytest.mark.asyncio
async def test_login(page):

    try:
        await page.goto("https://google.com")

        await click_with_healing(
            page,
            "#wrong-id",
            ["text=Login", "button"]
        )

    except Exception as e:
        ai_reason = analyze_failure(str(e))
        log_failure("test_login", str(e), ai_reason)

        print("\n🤖 AI Analysis:\n", ai_reason)

        assert False