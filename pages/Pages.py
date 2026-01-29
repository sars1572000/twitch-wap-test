
def streamer_page(driver):
    from pages.streamer_page  import StreamerPage
    return StreamerPage(driver)

def home_page(driver):
    from pages.home_page import HomePage
    return HomePage(driver)
