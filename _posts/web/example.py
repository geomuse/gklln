import asyncio
from playwright.async_api import async_playwright

async def scrape_liberty_times():
    """
    使用 Playwright 爬取自由时报首页的新闻标题和链接。
    """
    async with async_playwright() as p:
        # Launch the Firefox browser in headless mode
        browser = await p.firefox.launch(headless=True)
        # 创建一个新页面
        page = await browser.new_page()

        try:
            # 访问自由时报主页
            print("正在访问自由时报网站...")
            await page.goto("https://news.ltn.com.tw/list/breakingnews/world")

            # 等待新闻列表加载完成。
            # 这里我们使用一个 CSS 选择器，等待一个包含新闻链接的元素出现。
            # 如果网站结构变化，你可能需要更新这个选择器。
            await page.wait_for_selector('ul.list > li > a')

            # 定位所有新闻链接元素
            # Playwright 的 `locator` 是获取元素的推荐方式，它会自动等待元素加载。
            news_items = page.locator('ul.list > li > a')

            # 获取元素总数，以便循环遍历
            count = await news_items.count()
            print(f"找到 {count} 篇新闻。")

            # 遍历每个新闻元素并提取信息
            for i in range(count):
                item = news_items.nth(i)
                title = await item.text_content()
                link = await item.get_attribute('href')

                # 打印提取到的标题和链接
                print(f"标题: {title.strip()}")
                print(f"链接: {link}")

        except Exception as e:
            print(f"爬取过程中发生错误: {e}")
        finally:
            # 确保浏览器在任何情况下都会被关闭
            await browser.close()
            print("浏览器已关闭。")

# 运行主函数
if __name__ == "__main__":
    
    asyncio.run(scrape_liberty_times())