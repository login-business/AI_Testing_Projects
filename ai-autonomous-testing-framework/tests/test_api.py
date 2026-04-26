import pytest
from utils.ai_analyzer import analyze_failure
from utils.logger import log_failure

@pytest.mark.asyncio
async def test_login_api(playwright):

    try:
        request = await playwright.request.new_context()

        response = await request.post(
            "https://reqres.in/api/login",
            data={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
        )

        assert response.status == 200

    except Exception as e:
        ai_reason = analyze_failure(str(e))
        log_failure("test_api", str(e), ai_reason)

        print("\n🤖 AI Analysis:\n", ai_reason)

        assert False