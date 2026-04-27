import re

f = open(r'C:\Users\sean.guo1\WorkBuddy\20260423171332\index.html', encoding='utf-8')
content = f.read()
f.close()

style_start = content.find('<style>')
style_end = content.find('</style>') + len('</style>')

new_css = """<style>
/* ===== 家常菜点菜系统 - 清新粉白主题 ===== */
:root{--p:#E8628A;--pl:#F093B0;--pd:#C94070;--bg:#FFF5F8;--card:#FFFFFF;--tx:#3D1F2D;--sub:#9B7088;--bd:#F5D5E2;--tagbg:#FCEEF3;--tagc:#C94070;--ok:#4A9E6B;--err:#E8628A;--sh:0 3px 14px rgba(232,98,138,.10);--r:16px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"PingFang SC","Microsoft YaHei","SimSun",sans-serif;background:var(--bg);color:var(--tx);min-height:100vh;background-image:url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23E8628A' fill-opacity='0.04'%3E%3Cpath d='M50 50c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10s-10-4.477-10-10 4.477-10 10-10zM10 10c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10S0 25.523 0 20s4.477-10 10-10zm10 8c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8zm40 40c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")}
.hd{background:linear-gradient(160deg,#C94070 0%,#E8628A 50%,#F093B0 100%);color:#fff;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:200;box-shadow:0 3px 20px rgba(201,64,112,.25);border-bottom:2px solid rgba(255,255,255,.18)}
.hd-t{font-size:20px;font-weight:900;letter-spacing:4px;text-shadow:0 2px 8px rgba(0,0,0,.15)}
.hd-icon{font-size:22px;margin-right:6px}
.cart-btn{background:rgba(255,255,255,.28);border:2px solid rgba(255,255,255,.7);color:#fff;border-radius:24px;padding:6px 15px;font-size:13px;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .2s;backdrop-filter:blur(4px);font-weight:700}
.cart-btn:hover{background:rgba(255,255,255,.48);border-color:#fff}
.badge{background:#fff;color:var(--pd);border-radius:10px;padding:1px 7px;font-size:12px;font-weight:800;min-width:20px;text-align:center}
.top-banner{background:linear-gradient(90deg,#E8628A,#F093B0,#FBBFD2);color:#fff;text-align:center;padding:6px 16px;font-size:12px;letter-spacing:1px;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,.1);position:sticky;top:54px;z-index:195}
.fb{background:#fff;border-bottom:2px solid var(--bd);padding:10px 14px;position:sticky;top:82px;z-index:190;box-shadow:0 2px 8px rgba(232,98,138,.06)}
.sr{display:flex;gap:8px;margin-bottom:8px}
.si{flex:1;border:1.5px solid var(--bd);border-radius:22px;padding:7px 14px;font-size:13px;outline:none;transition:border .2s,box-shadow .2s;background:#fff;color:var(--tx)}
.si:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(232,98,138,.12)}
.si::placeholder{color:#D4A8BC}
.fs{border:1.5px solid var(--bd);border-radius:22px;padding:7px 10px;font-size:12px;outline:none;cursor:pointer;background:#fff;color:var(--tx)}
.ct{display:flex;gap:5px;overflow-x:auto;padding-bottom:2px}
.ct::-webkit-scrollbar{display:none}
.ctb{white-space:nowrap;border:1.5px solid var(--bd);border-radius:20px;padding:5px 14px;font-size:12px;cursor:pointer;background:#fff;transition:all .18s;color:var(--sub);font-weight:600}
.ctb.on{background:linear-gradient(135deg,var(--p),var(--pl));border-color:var(--p);color:#fff;font-weight:700;box-shadow:0 2px 10px rgba(232,98,138,.35)}
.ctb:hover:not(.on){border-color:var(--p);color:var(--p);background:#FFF0F5}
.main{max-width:1280px;margin:0 auto;padding:16px 14px}
.main-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;padding-bottom:10px;border-bottom:2px dashed var(--bd)}
.main-title{font-size:15px;font-weight:800;color:var(--pd);display:flex;align-items:center;gap:6px;letter-spacing:1px}
.main-count{font-size:12px;color:var(--sub);background:var(--tagbg);border-radius:12px;padding:2px 10px;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;align-content:start;min-height:60vh}
.card{background:var(--card);border-radius:var(--r);box-shadow:var(--sh);cursor:pointer;transition:transform .22s cubic-bezier(.34,1.56,.64,1),box-shadow .22s;overflow:hidden;display:flex;flex-direction:column;border:1px solid rgba(245,213,226,.8);position:relative}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--p),var(--pl),#FBBFD2);opacity:0;transition:opacity .2s;z-index:2}
.card:hover{transform:translateY(-5px) scale(1.02);box-shadow:0 10px 28px rgba(232,98,138,.18)}
.card:hover::before{opacity:1}
.card-img{background:linear-gradient(145deg,#FFF0F5 0%,#FCEEF3 50%,#FFF5F8 100%);height:96px;display:flex;align-items:center;justify-content:center;font-size:48px;position:relative;border-bottom:1px solid var(--bd)}
.card-img::after{content:'';position:absolute;bottom:0;left:0;right:0;height:14px;background:linear-gradient(to top,rgba(255,245,248,.9),transparent)}
.card-badge{position:absolute;top:7px;left:7px;font-size:10px;font-weight:800;letter-spacing:.5px;border-radius:8px;padding:2px 7px;box-shadow:0 2px 6px rgba(0,0,0,.12);z-index:3}
.card-badge.hot{background:linear-gradient(135deg,#FF6B8A,#E8628A);color:#fff}
.card-badge.new{background:linear-gradient(135deg,#4A9E6B,#3A7E55);color:#fff}
.card-badge.pop{background:linear-gradient(135deg,#FBBF24,#D4A020);color:#5A3A0A}
.card-body{padding:10px 11px;flex:1;display:flex;flex-direction:column;gap:3px}
.card-name{font-size:14px;font-weight:800;color:var(--tx);line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card-cat{font-size:11px;color:var(--sub);font-weight:600;letter-spacing:.3px}
.card-desc{font-size:11px;color:var(--sub);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-top:1px}
.card-tag{font-size:10px;background:var(--tagbg);color:var(--tagc);border-radius:8px;padding:2px 7px;display:inline-block;margin-top:3px;font-weight:600;border:1px solid rgba(201,64,112,.12)}
.card-foot{display:flex;align-items:center;justify-content:space-between;margin-top:auto;padding:9px 11px 10px;border-top:1px dashed var(--bd)}
.price-wrap{display:flex;align-items:baseline;gap:2px}
.price{font-size:19px;font-weight:900;color:var(--p)}
.price-unit{font-size:11px;color:var(--sub);font-weight:600}
.add-btn{background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:14px;padding:5px 14px;font-size:12px;font-weight:800;cursor:pointer;transition:all .18s;box-shadow:0 3px 10px rgba(232,98,138,.3);letter-spacing:.5px}
.add-btn:hover{background:linear-gradient(135deg,var(--pd),var(--p));box-shadow:0 4px 14px rgba(232,98,138,.45);transform:scale(1.06)}
.add-btn:active{transform:scale(.95)}
.empty{grid-column:1/-1;text-align:center;padding:60px 0;color:var(--sub);font-size:14px;display:flex;flex-direction:column;align-items:center;gap:10px}
.empty-icon{font-size:52px;opacity:.4}
/* MODAL */
.ov{position:fixed;inset:0;background:rgba(61,31,45,.45);z-index:400;display:none;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(3px)}
.ov.open{display:flex}
.modal{background:#fff;border-radius:20px;max-width:540px;width:100%;max-height:90vh;overflow-y:auto;animation:mup .25s cubic-bezier(.34,1.56,.64,1);box-shadow:0 20px 60px rgba(201,64,112,.18)}
@keyframes mup{from{transform:translateY(28px) scale(.96);opacity:0}to{transform:none;opacity:1}}
.modal-hd{padding:16px 18px 12px;border-bottom:2px solid var(--bd);display:flex;align-items:center;justify-content:space-between;gap:10px}
.modal-title{font-size:17px;font-weight:800;color:var(--tx);letter-spacing:.5px}
.modal-close{background:none;border:none;font-size:22px;cursor:pointer;color:var(--sub);line-height:1;padding:2px 4px;border-radius:50%;transition:all .15s}
.modal-close:hover{background:#FCEEF3;color:var(--p)}
.modal-body{padding:16px 18px}
.meta-row{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:12px}
.mc{background:linear-gradient(135deg,var(--tagbg),#fff);border-radius:10px;padding:4px 10px;font-size:12px;font-weight:600;color:var(--tagc);border:1px solid var(--bd)}
.st{font-size:12px;font-weight:700;color:var(--pd);margin:12px 0 6px;letter-spacing:1px;text-transform:uppercase}
.chips{display:flex;flex-wrap:wrap;gap:5px}
.chip{border-radius:10px;padding:3px 9px;font-size:11px;font-weight:600}
.chip.I{background:var(--tagbg);color:var(--tagc)}
.chip.S{background:#e0f2fe;color:#0369a1}
.nut{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:8px}
.nut-item{background:linear-gradient(145deg,var(--tagbg),#fff);border-radius:12px;padding:8px 4px;text-align:center;border:1px solid var(--bd)}
.nut-v{font-size:15px;font-weight:900;color:var(--p)}
.nut-k{font-size:10px;color:var(--sub);margin-top:2px}
/* CART */
.cart-ov{position:fixed;inset:0;z-index:500;display:none}
.cart-ov.open{display:block}
.cart-bg{position:absolute;inset:0;background:rgba(61,31,45,.45);backdrop-filter:blur(4px)}
.cart-drawer{position:absolute;right:0;top:0;bottom:0;width:min(400px,100vw);background:#fff;box-shadow:-8px 0 32px rgba(201,64,112,.18);display:flex;flex-direction:column;animation:sin .3s cubic-bezier(.34,1.56,.64,1);border-left:2px solid var(--bd)}
@keyframes sin{from{transform:translateX(100%)}to{transform:none}}
.cart-hd{padding:16px 18px;border-bottom:2px solid var(--bd);font-size:17px;font-weight:800;display:flex;align-items:center;justify-content:space-between;color:var(--tx)}
.cart-items{flex:1;overflow-y:auto;padding:12px 16px}
.ci{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px dashed var(--bd)}
.ci-name{flex:1;font-size:14px;font-weight:700;color:var(--tx)}
.ci-price{font-size:14px;color:var(--p);font-weight:900;min-width:52px;text-align:right}
.qty-ctrl{display:flex;align-items:center;gap:6px}
.qb{background:var(--tagbg);border:1.5px solid var(--bd);border-radius:50%;width:26px;height:26px;cursor:pointer;font-size:15px;display:flex;align-items:center;justify-content:center;transition:all .15s;color:var(--p);font-weight:700}
.qb:hover{border-color:var(--p);background:var(--p);color:#fff}
.qty-n{font-size:14px;font-weight:800;min-width:18px;text-align:center;color:var(--tx)}
.cart-ft{padding:16px;border-top:2px solid var(--bd)}
.cart-total{display:flex;justify-content:space-between;margin-bottom:12px;font-size:16px;font-weight:800;color:var(--tx)}
.total-price{color:var(--p);font-size:20px;font-weight:900}
.order-btn{width:100%;background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:24px;padding:14px;font-size:16px;font-weight:800;cursor:pointer;transition:all .2s;box-shadow:0 4px 16px rgba(232,98,138,.35);letter-spacing:1px;margin-bottom:8px}
.order-btn:hover{background:linear-gradient(135deg,var(--pd),var(--p));box-shadow:0 6px 20px rgba(232,98,138,.45);transform:translateY(-1px)}
.clear-btn{width:100%;background:none;border:1.5px solid var(--bd);border-radius:24px;padding:10px;font-size:13px;cursor:pointer;color:var(--sub);transition:all .15s;font-weight:600}
.clear-btn:hover{border-color:var(--err);color:var(--err)}
.cart-empty{text-align:center;padding:50px 0;color:var(--sub);display:flex;flex-direction:column;align-items:center;gap:8px}
/* ADMIN */
.admin-ov{position:fixed;inset:0;background:rgba(61,31,45,.45);z-index:600;display:none;align-items:center;justify-content:center;padding:16px;backdrop-filter:blur(3px)}
.admin-ov.open{display:flex}
.admin-modal{background:#fff;border-radius:20px;max-width:520px;width:100%;max-height:92vh;overflow-y:auto;animation:mup .25s cubic-bezier(.34,1.56,.64,1);box-shadow:0 20px 60px rgba(201,64,112,.18)}
.admin-hd{padding:16px 18px 12px;border-bottom:2px solid var(--bd);display:flex;align-items:center;justify-content:space-between}
.admin-hd h2{font-size:16px;font-weight:800;color:var(--tx)}
.admin-body{padding:14px 17px}
.form-row{margin-bottom:12px}
.form-row label{display:block;font-size:12px;font-weight:700;margin-bottom:5px;color:var(--sub);letter-spacing:.5px;text-transform:uppercase}
.form-row input,.form-row select,.form-row textarea{width:100%;border:1.5px solid var(--bd);border-radius:12px;padding:8px 12px;font-size:13px;outline:none;transition:border .2s,box-shadow .2s;font-family:inherit;background:#fff;color:var(--tx)}
.form-row input:focus,.form-row select:focus,.form-row textarea:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(232,98,138,.1)}
.form-2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.form-btn-row{display:flex;gap:10px;margin-top:14px}
.fb-save{flex:1;background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:20px;padding:11px;font-size:14px;font-weight:800;cursor:pointer;box-shadow:0 3px 12px rgba(232,98,138,.3);transition:all .2s}
.fb-save:hover{background:linear-gradient(135deg,var(--pd),var(--p));box-shadow:0 4px 16px rgba(232,98,138,.4)}
.fb-cancel{background:#fff;border:1.5px solid var(--bd);border-radius:20px;padding:11px 18px;font-size:14px;cursor:pointer;color:var(--sub);font-weight:600;transition:all .15s}
.fb-cancel:hover{border-color:var(--p);color:var(--p)}
/* TOAST */
.toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(80px);background:linear-gradient(135deg,var(--p),var(--pd));color:#fff;padding:10px 24px;border-radius:24px;font-size:13px;font-weight:700;z-index:9999;opacity:0;transition:all .3s cubic-bezier(.34,1.56,.64,1);white-space:nowrap;box-shadow:0 4px 20px rgba(232,98,138,.4)}
.toast.show{transform:translateX(-50%) translateY(0);opacity:1}
/* ORDER CONFIRM */
.order-confirm{position:fixed;inset:0;background:rgba(61,31,45,.45);z-index:700;display:none;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px)}
.order-confirm.open{display:flex}
.oc-box{background:#fff;border-radius:24px;max-width:400px;width:100%;padding:36px 28px;text-align:center;animation:mup .28s cubic-bezier(.34,1.56,.64,1);box-shadow:0 20px 60px rgba(201,64,112,.18)}
.oc-icon{font-size:60px;margin-bottom:14px}
.oc-title{font-size:20px;font-weight:900;color:var(--tx);margin-bottom:10px;letter-spacing:.5px}
.oc-sub{font-size:13px;color:var(--sub);margin-bottom:24px;line-height:1.6}
.oc-ok{background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:20px;padding:13px 28px;font-size:15px;font-weight:800;cursor:pointer;width:100%;box-shadow:0 4px 16px rgba(232,98,138,.35);transition:all .2s}
.oc-ok:hover{background:linear-gradient(135deg,var(--pd),var(--p));box-shadow:0 6px 20px rgba(232,98,138,.45);transform:scale(1.02)}
/* Fab */
.fab{position:fixed;right:20px;bottom:24px;background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:50%;width:52px;height:52px;font-size:24px;cursor:pointer;box-shadow:0 6px 20px rgba(232,98,138,.4);display:flex;align-items:center;justify-content:center;z-index:300;transition:all .22s;letter-spacing:-1px}
.fab:hover{background:linear-gradient(135deg,var(--pd),var(--p));transform:scale(1.1);box-shadow:0 8px 28px rgba(232,98,138,.5)}
@media(max-width:600px){
  .grid{grid-template-columns:repeat(2,1fr);gap:8px}
  .card-img{height:80px;font-size:38px}
  .modal{max-height:95vh;border-radius:18px 18px 0 0;margin-top:auto;width:100%;max-width:100%}
  .ov{align-items:flex-end;padding:0}
  .top-banner{font-size:11px;padding:5px 12px}
}
</style>"""

after_first_style = content[style_end:]
new_content = content[:style_start] + new_css + after_first_style

f = open(r'C:\Users\sean.guo1\WorkBuddy\20260423171332\index.html', 'w', encoding='utf-8')
f.write(new_content)
f.close()
print('Done! New length:', len(new_content))
