from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

#Test Routes go here

'''
When we visit /hello
we get "Hello, World"
'''

def test_get_hello(page, test_web_address):
    #open the webpage
    page.goto(f"http://{test_web_address}/hello")
    #locate a particular html tag
    heading_tag = page.locator("h1")
    #we expect the heading_tag will have specific string or result.
    expect(heading_tag).to_have_text("Hello, world!")

def test_get_bye(page, test_web_address):
    page.goto(f"http://{test_web_address}/bye")
    heading_two_tag = page.locator("h2")
    expect(heading_two_tag).to_have_text("Bye!")
