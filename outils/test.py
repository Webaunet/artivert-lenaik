import sys,os,glob,json
from playwright.sync_api import sync_playwright
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages=sorted(glob.glob(root+"/*.html"))
W=[360,414,768,821,980,981,1280,1920]
JS="""()=>{const o=[];const vh=innerHeight;
if(document.documentElement.scrollWidth>innerWidth)o.push('overflow-x '+document.documentElement.scrollWidth);
document.querySelectorAll('body *').forEach(e=>{const cs=getComputedStyle(e);if(cs.display==='none'||cs.visibility==='hidden')return;
const t=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());
if(t&&parseFloat(cs.fontSize)<15.9)o.push('font '+parseFloat(cs.fontSize)+' '+e.tagName+'.'+e.className);
if((e.tagName==='A'||e.tagName==='BUTTON')&&!e.closest('p')){const r=e.getBoundingClientRect();if(r.width>0&&(r.height<43.5||r.width<43.5))o.push('tap '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(e.textContent.trim().slice(0,20)||e.id))}
if(e.tagName==='IMG'&&e.naturalWidth&&!e.classList.contains('hero__img')&&(e.getBoundingClientRect().width>e.naturalWidth+1))o.push('upscaled '+e.getAttribute('src'));});
document.querySelectorAll('section,.hero').forEach(s=>{const h=s.getBoundingClientRect().height;o.push('H '+(s.id||s.className.split(' ')[0])+' '+Math.round(h/vh*100)+'%')});
const f=document.querySelector('footer');if(f)o.push('H footer '+Math.round(f.getBoundingClientRect().height/vh*100)+'%');
const logo=document.querySelector('.logo'),call=document.querySelector('.hdr__call'),nav=document.querySelector('.nav');
if(innerWidth>980&&logo&&call&&nav){const a=logo.getBoundingClientRect(),b=nav.getBoundingClientRect(),c=call.getBoundingClientRect();if(a.right>b.left||b.right>c.left)o.push('header overlap')}
return o}"""
bad=0
with sync_playwright() as p:
    b=p.chromium.launch()
    for pg in pages:
        for w in W:
            c=b.new_context(viewport={"width":w,"height":800 if w<1000 else 900})
            page=c.new_page();page.goto("file://"+pg);page.wait_for_timeout(300)
            r=page.evaluate(JS)
            for x in r:
                if not x.startswith("H "): print(os.path.basename(pg),w,x);bad+=1
                elif "-v" in sys.argv: print(os.path.basename(pg),w,x)
            c.close()
    b.close()
for pg in pages:
    src=open(pg,encoding="utf-8").read()
    import re
    tot=0
    for m in set(re.findall(r'(?:href|src)="([^"#:]+?)"',src)):
        if m.startswith("http"):continue
        f=os.path.join(root,m)
        if not os.path.exists(f):print(os.path.basename(pg),"lien mort",m);bad+=1
        elif m.startswith("images/"):tot+=os.path.getsize(f)
    if tot>1.5*1024*1024:print(os.path.basename(pg),"poids images",tot//1024,"Ko");bad+=1
print("OK" if not bad else f"{bad} anomalies")
