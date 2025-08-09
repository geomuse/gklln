from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # 设置 headless=False 可看到界面
    page = browser.new_page()
    page.goto("https://example.com")
    print("网页标题是：", page.title())
    browser.close()