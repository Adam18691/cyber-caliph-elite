# FILE: app.py - v143 TURBO EXTREME - 54min content + 6min links = 60min - 25sec - 0.00000000000001
import os, sys, tempfile, subprocess
sys.dont_write_bytecode=True
try:
    from PIL import Image
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
except: pass
import requests

LINKS_6 = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% OFF", "name": "Kie.AI"}
}

from flask import Flask, request, jsonify, send_file, Response
app=Flask(__name__)

@app.route('/')
def index():
    resp=Response("<h1>v143 TURBO EXTREME 54+6=60min - 25sec - 0.00000000000001</h1>",mimetype='text/html')
    resp.headers['X-Tayybat']="0.00000000000001"
    resp.headers['X-Version']="v143-TURBO-EXTREME"
    return resp

@app.route('/health')
def health():
    return jsonify({"status":"ok","version":"v143 TURBO EXTREME 54+6=60min - 25sec - 0.00000000000001","structure":"54min content (9min x6) + 6min links (1min x6) = 60min","speed":"0.00000000000001","forbidden_count":11,"time":"25sec"})

@app.route('/wake')
def wake():
    return jsonify({"status":"awake","version":"v143"})

def make_link_img(text, url, discount, path, idx):
    from PIL import Image, ImageDraw
    # 320x180 for EXTREME TURBO - 8x faster than 1280x720
    img=Image.new('RGB',(320,180),color=[(0,100,0),(0,80,120),(120,0,0),(100,0,100),(120,80,0),(0,100,100)][idx%6])
    draw=ImageDraw.Draw(img)
    draw.rectangle([0,0,320,25],fill=(0,0,0))
    draw.text((5,5),f"LINK {idx+1}/6 - {text} - {discount}",fill=(255,255,0))
    draw.text((5,35),url[:40],fill=(255,255,255))
    draw.text((5,60),f"Waeldeban186 - {discount}",fill=(255,215,0))
    img.save(path,quality=60,optimize=True)
    return path

def make_content_img(txt, path):
    from PIL import Image, ImageDraw
    img=Image.new('RGB',(320,180),color=(139,69,19))
    draw=ImageDraw.Draw(img)
    draw.text((5,5),f"TAYYBAT {txt}",fill=(255,215,0))
    img.save(path,quality=60,optimize=True)
    return path

def build_54_6_extreme(temp_dir, content_paths):
    list_file = os.path.join(temp_dir, "list.txt")
    keys=list(LINKS_6.keys())
    content_per_block = 9*60
    link_per_block = 60
    imgs_per_block = max(1, len(content_paths)//6) if content_paths else 1
    with open(list_file, 'w') as f:
        for b in range(6):
            if content_paths:
                s=b*imgs_per_block
                e=s+imgs_per_block
                block_imgs=content_paths[s:e] or content_paths[:imgs_per_block]
                sec_per = content_per_block / len(block_imgs)
                for p in block_imgs:
                    f.write(f"file '{p}'\n")
                    f.write(f"duration {sec_per}\n")
            else:
                p=os.path.join(temp_dir,f"c{b}.jpg")
                make_content_img(f"Block {b+1}/6 - 9 MIN",p)
                f.write(f"file '{p}'\n")
                f.write(f"duration {content_per_block}\n")
            info=LINKS_6[keys[b]]
            lp=os.path.join(temp_dir,f"l{b}.jpg")
            make_link_img(info['name'],info['url'],info['discount'],lp,b)
            f.write(f"file '{lp}'\n")
            f.write(f"duration {link_per_block}\n")
        f.write(f"file '{lp}'\n")
    out=os.path.join(temp_dir,"tayybat_54_6_60min_EXTREME_0.00000000000001.mp4")
    # EXTREME TURBO: 320x180, 8fps, ultrafast, crf 35, smallest size
    cmd=["ffmpeg","-y","-f","concat","-safe","0","-i",list_file,"-vf","scale=640:360","-c:v","libx264","-preset","ultrafast","-crf","35","-pix_fmt","yuv420p","-r","8",out]
    subprocess.run(cmd, check=False, timeout=300, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out

@app.route('/generate-video-tayybat', methods=['POST'])
def gen():
    try:
        data=request.get_json(force=True) if request.is_json else {}
        images=data.get('images',[])
        if not images and 'jobs' in data:
            jobs=data['jobs']
            images=[j.get('file') or j.get('url') for j in jobs if isinstance(j,dict) and (j.get('file') or j.get('url'))]
        temp_dir=tempfile.mkdtemp(prefix="v143_")
        local=[]
        for i,url in enumerate(images[:6]):  # only 6 images for extreme speed
            try:
                if url and url.startswith('http'):
                    r=requests.get(url,timeout=3)
                    if r.status_code==200:
                        p=os.path.join(temp_dir,f"c{i}.jpg")
                        open(p,'wb').write(r.content)
                        local.append(p)
            except: continue
        out=build_54_6_extreme(temp_dir, local)
        return send_file(out,as_attachment=True,download_name="tayybat_54c_6l_60min_EXTREME_0.00000000000001.mp4",mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:2000]}),500

@app.route('/api/video/montage-60', methods=['POST'])
def m60(): return gen()
@app.route('/api/links')
def links(): return jsonify({"links":LINKS_6,"structure":"54+6=60","version":"v143-EXTREME","status":"ok"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
