"""語錄卡落地頁實拍動圖片段（2026-11-25）。麻豆 0812 4K 直式影片，裁 4:5、15fps、930×1163，輕微提彩度。"""
import subprocess, os, shutil, sys
from concurrent.futures import ThreadPoolExecutor
V = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/語錄卡/毛片/麻豆_影片_0812/"
FPS = 15
C = {  # name: (src, t0, t1, speed, crop_y 0-1)
 'q_draw':  (V + 'C0191.mp4', 0.8, 5.2, 1.1, 0.30),
 'q_stand': (V + 'C0172.mp4', 0.8, 5.6, 1.1, 0.45),
 'q_flip':  (V + 'C0199.mp4', 17.5, 22.0, 1.1, 0.40),
}
def run(item):
    n, (src, t0, t1, sp, c) = item
    od = os.path.dirname(os.path.abspath(__file__)) + f'/clips/{n}'; shutil.rmtree(od, ignore_errors=True); os.makedirs(od)
    vf = f"setpts=PTS/{sp},fps={FPS},crop=iw:iw*1.25:0:(ih-iw*1.25)*{c},scale=930:1163:flags=lanczos,eq=saturation=1.12:contrast=1.04"
    subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t0), '-t', str(t1 - t0), '-i', src, '-vf', vf, '-q:v', '2', f'{od}/%03d.jpg'], check=True, stdin=subprocess.DEVNULL)
    return n, len(os.listdir(od))
sel = sys.argv[1:] or list(C)
with ThreadPoolExecutor(3) as ex:
    for r in ex.map(run, [(k, C[k]) for k in sel]): print(r)
