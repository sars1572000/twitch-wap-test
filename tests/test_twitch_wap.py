import pytest
from pages.BasePage import BasePage
from pages import Pages

Base_URL = "https://m.twitch.tv/"


@pytest.mark.wap
def test_twitch_starcraft_ii_streamer_page(mobile_chrome_driver, logger):
    driver = mobile_chrome_driver
    base_page = BasePage(driver)
    logger.info("Starting Twitch StarCraft II WAP test")
    logger.info("Step 1: Navigating to Twitch")
    base_page.open_link(Base_URL)
    # Verify we're on Twitch
    assert "twitch" in driver.title.lower(), "Failed to navigate to Twitch"
    logger.info("✓ Successfully navigated to Twitch")
    home_page = Pages.home_page(driver)
    # Step 2: Click in the search icon
    logger.info("Step 2: Clicking search button")
    home_page.click_search_icon()
    logger.info("✓ Search button clicked")
    # Step 3: Input StarCraft II
    logger.info("Step 3: Searching for StarCraft II")
    home_page.search_for("StarCraft II")
    home_page.click_first_search_result()
    home_page.wait_for_search_results()
    logger.info("✓ Search results loaded for StarCraft II")
    # Step 4: Scroll down 2 times
    logger.info("Step 4: Scrolling down 2 times")
    home_page.scroll_down(2)
    logger.info("✓ Scrolled down 2 times")
    # Step 5: Select one streamer
    logger.info("Step 5: Selecting first available streamer")
    home_page.select_first_streamer()
    # Step 6: On the streamer page wait until all is load and take a screenshot
    logger.info("Step 6: Waiting for streamer page to load and taking screenshot")
    streamer_page = Pages.streamer_page(driver)
    streamer_page.wait_for_page_load()
    # Take screenshot
    screenshot_path = streamer_page.take_screenshot("starcraft_streamer_final.png")
    assert screenshot_path is not None, "Failed to take screenshot"
    logger.info(f"✓ Screenshot saved: {screenshot_path}")

    logger.info("Twitch StarCraft II WAP test completed successfully")



if __name__ == "__main__":
    pytest.main(["-q"])