import asyncio,os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='chrome')
        pg=await b.new_page(viewport={'width':432,'height':900},device_scale_factor=2.5)
        await pg.goto('file://'+D+'/page.html'); await pg.wait_for_timeout(800); await pg.evaluate('document.fonts.ready')
        await pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=600})")
        os.makedirs(D+'/sec',exist_ok=True)
        ids=await pg.eval_on_selector_all('section','e=>e.map(x=>x.id)')
        for i in ids: await pg.locator('#'+i).screenshot(path=f'{D}/sec/{i}.png')
        await pg.screenshot(path=D+'/full.png',full_page=True)
        print(ids, await pg.evaluate('document.body.scrollHeight'))
        await b.close()
asyncio.run(main())
