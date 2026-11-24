import asyncio, os, sys, shutil, json
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FR=D+'/gif/secframes'
async def main():
    sel=sys.argv[1:]
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='chrome')
        pg=await b.new_page(viewport={'width':432,'height':900},device_scale_factor=2.5)
        await pg.goto('file://'+D+'/page.html'); await pg.wait_for_timeout(800); await pg.evaluate('document.fonts.ready')
        await pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=600})")
        items=await pg.eval_on_selector_all('[data-clip]','els=>els.map(e=>[e.closest("section").id,e.dataset.clip])')
        groups={}
        for sec,clip in items: groups.setdefault(sec,[]).append(clip)
        for sec,clips in groups.items():
            if sel and sec not in sel: continue
            od=f'{FR}/{sec}'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
            n=len(os.listdir(f'{D}/gif/clips/{clips[0]}'))
            caps={c:json.load(open(f'{D}/gif/caps_{c}.json')) for c in clips if os.path.exists(f'{D}/gif/caps_{c}.json')}
            for i in range(n):
                upd=[[c,f'gif/clips/{c}/{sorted(os.listdir(f"{D}/gif/clips/{c}"))[i]}',caps[c][i] if c in caps else None] for c in clips]
                await pg.evaluate('''async (U)=>{for(const [c,u,t] of U){const im=new Image();im.src=u;await im.decode();document.querySelector(`[data-clip="${c}"]`).style.backgroundImage=`url(${u})`;if(t!==null){document.querySelector(`[data-caps="${c}"]`).innerHTML=t}};await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))}''',upd)
                await pg.locator('#'+sec).screenshot(path=f'{od}/{i+1:03d}.png')
            print(sec,clips,n,flush=True)
        if not sel or 's03b' in sel:
            od=f'{FR}/s03b'; shutil.rmtree(od,ignore_errors=True); os.makedirs(od)
            for i in range(25):
                await pg.evaluate(f"document.getAnimations().forEach(a=>{{a.pause();a.currentTime={i*100}}})")
                await pg.locator('#s03b').screenshot(path=f'{od}/{i+1:03d}.png')
            print('s03b',25)
        await b.close()
asyncio.run(main())
