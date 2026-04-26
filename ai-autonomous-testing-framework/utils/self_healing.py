async def click_with_healing(page, primary, fallbacks):

    try:
        await page.locator(primary).click()
        return primary

    except:
        for locator in fallbacks:
            try:
                await page.locator(locator).click()
                return locator
            except:
                continue

        raise Exception("All locators failed")