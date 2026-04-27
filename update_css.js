const fs = require('fs');
const path = 'C:/Users/sean.guo1/WorkBuddy/20260423171332/家常菜点菜系统.html';
let c = fs.readFileSync(path, 'utf8');

const NEW_CSS = `<style>
/* ===== 家常菜点菜系统 - 烟火气主题 ===== */
::root{--p:#C84B31;--pl:#E87040;--pd:#9B3422;--bg:#FDF6EC;--card:#FFFDF8;--tx:#2D1810;--sub:#8B6B5A;--bd:#EDD9C4;--tagbg:#FFF0D6;--tagc:#9B5E2A;--ok:#4A9E6B;--err:#C84B31;--sh:0 3px 14px rgba(200,75,49,.10);--r:16px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"PingFang SC","Microsoft YaHei","SimSun",sans-serif;background:var(--bg);color:var(--tx);min-height:100vh;background-image:url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23C84B31' fill-opacity='0.025'%3E%3Cpath d='M50 50c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10s-10-4.477-10-10 4.477-10 10-10zM10 10c0-5.523 4.477-10 10-10s10 4.477 10 10-4.477 10-10 10c0 5.523-4.477 10-10 10S0 25.523 0 20s4.477-10 10-10zm10 8c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8zm40 40c4.418 0 8-3.582 8-8s-3.582-8-8-8-8 3.582-8 8 3.582 8 8 8z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")}
.hd{background:linear-gradient(160deg,#8B2E1A 0%,#C84B31 50%,#9B3422 100%);color:#fff;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:200;box-shadow:0 3px 20px rgba(139,46,26,.35);border-bottom:2px solid rgba(255,255,255,.12)}
.hd-t{font-size:20px;font-weight:900;letter-spacing:4px;text-shadow:0 2px 8px rgba(0,0,0,.3)}
.hd-icon{font-size:22px;margin-right:6px}
.cart-btn{background:rgba(255,255,255,.18);border:2px solid rgba(255,255,255,.4);color:#fff;border-radius:24px;padding:6px 15px;font-size:13px;cursor:pointer;display:flex;align-items:center;gap:6px;transition:all .2s;backdrop-filter:blur(4px)}
.cart-btn:hover{background:rgba(255,255,255,.32);border-color:rgba(255,255,255,.7)}
.badge{background:#FBBF24;color:#6B3A0A;border-radius:10px;padding:1px 7px;font-size:12px;font-weight:800;min-width:20px;text-align:center}
.top-banner{background:linear-gradient(90deg,#C84B31,#E87040,#FBBF24);color:#fff;text-align:center;padding:6px 16px;font-size:12px;letter-spacing:1px;font-weight:600;text-shadow:0 1px 3px rgba(0,0,0,.2);position:sticky;top:54px;z-index:195}
.fb{background:#FFFDF8;border-bottom:2px solid var(--bd);padding:10px 14px;position:sticky;top:82px;z-index:190;box-shadow:0 2px 8px rgba(200,75,49,.06)}
.sr{display:flex;gap:8px;margin-bottom:8px}
.si{flex:1;border:1.5px solid var(--bd);border-radius:22px;padding:7px 14px;font-size:13px;outline:none;transition:border .2s,box-shadow .2s;background:#fff}
.si:focus{border-color:var(--p);box-shadow:0 0 0 3px rgba(200,75,49,.1)}
.si::placeholder{color:#C4A882}
.fs{border:1.5px solid var(--bd);border-radius:22px;padding:7px 10px;font-size:12px;outline:none;cursor:pointer;background:#fff}
.ct{display:flex;gap:5px;overflow-x:auto;padding-bottom:2px}
.ct::-webkit-scrollbar{display:none}
.ctb{white-space:nowrap;border:1.5px solid var(--bd);border-radius:20px;padding:5px 14px;font-size:12px;cursor:pointer;background:#fff;transition:all .18s;color:var(--sub);font-weight:500}
.ctb.on{background:linear-gradient(135deg,var(--p),var(--pl));border-color:var(--p);color:#fff;font-weight:700;box-shadow:0 2px 8px rgba(200,75,49,.3)}
.ctb:hover:not(.on){border-color:var(--pl);color:var(--p)}
.main{max-width:1280px;margin:0 auto;padding:16px 14px}
.main-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;padding-bottom:10px;border-bottom:2px dashed var(--bd)}
.main-title{font-size:15px;font-weight:800;color:var(--pd);display:flex;align-items:center;gap:6px;letter-spacing:1px}
.main-count{font-size:12px;color:var(--sub);background:var(--tagbg);border-radius:12px;padding:2px 10px;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;align-content:start;min-height:60vh}
.card{background:var(--card);border-radius:var(--r);box-shadow:var(--sh);cursor:pointer;transition:transform .22s cubic-bezier(.34,1.56,.64,1),box-shadow .22s;overflow:hidden;display:flex;flex-direction:column;border:1px solid rgba(237,217,196,.6);position:relative}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--p),var(--pl),#FBBF24);opacity:0;transition:opacity .2s;z-index:2}
.card:hover{transform:translateY(-5px) scale(1.02);box-shadow:0 10px 28px rgba(200,75,49,.18)}
.card:hover::before{opacity:1}
.card-img{background:linear-gradient(145deg,#FFF5EB 0%,#FDF0E6 50%,#FFF8F2 100%);height:96px;display:flex;align-items:center;justify-content:center;font-size:48px;position:relative;border-bottom:1px solid var(--bd)}
.card-img::after{content:'';position:absolute;bottom:0;left:0;right:0;height:14px;background:linear-gradient(to top,rgba(253,246,236,.9),transparent)}
.card-badge{position:absolute;top:7px;left:7px;font-size:10px;font-weight:800;letter-spacing:.5px;border-radius:8px;padding:2px 7px;box-shadow:0 2px 6px rgba(0,0,0,.15);z-index:3}
.card-badge.hot{background:linear-gradient(135deg,#FF4444,#CC2222);color:#fff}
.card-badge.new{background:linear-gradient(135deg,#4A9E6B,#3A7E55);color:#fff}
.card-badge.pop{background:linear-gradient(135deg,#FBBF24,#D4A020);color:#6B3A0A}
.card-body{padding:10px 11px;flex:1;display:flex;flex-direction:column;gap:3px}
.card-name{font-size:14px;font-weight:800;color:var(--tx);line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.card-cat{font-size:11px;color:var(--sub);font-weight:600;letter-spacing:.3px}
.card-desc{font-size:11px;color:var(--sub);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-top:1px}
.card-tag{font-size:10px;background:var(--tagbg);color:var(--tagc);border-radius:8px;padding:2px 7px;display:inline-block;margin-top:3px;font-weight:600;border:1px solid rgba(155,94,42,.12)}
.card-foot{display:flex;align-items:center;justify-content:space-between;margin-top:auto;padding:9px 11px 10px;border-top:1px dashed var(--bd)}
.price-wrap{display:flex;align-items:baseline;gap:2px}
.price{font-size:19px;font-weight:900;color:var(--p)}
.price-unit{font-size:11px;color:var(--sub);font-weight:600}
.add-btn{background:linear-gradient(135deg,var(--p),var(--pl));color:#fff;border:none;border-radius:14px;padding:5px 14px;font-size:12px;font-weight:800;cursor:pointer;transition:all .18s;box-shadow:0 3px 10px rgba(200,75,49,.3);letter-spacing:.5px}
.add-btn:hover{background:linear-gradient(135deg,var(--pd),var(--p));box-shadow:0 4px 14px rgba(200,75,49,.45);transform:scale(1.06)}
.add-btn:active{transform:scale(.95)}
.empty{grid-column:1/-1;text-align:center;padding:60px 0;color:var(--sub);font-size:14px;display:flex;flex-direction:column;align-items:center;gap:10px}
.empty-icon{font-size:52px;opacity:.4}
`;

const OLD_START = c.indexOf('<style>');
const OLD_END_MARKER = '/* MODAL */';
const OLD_END = c.indexOf(OLD_END_MARKER);

const before = c.substring(0, OLD_START);
const after = c.substring(OLD_END);
const newContent = before + NEW_CSS + '\n' + after;

fs.writeFileSync(path, newContent, 'utf8');
console.log('Done! New len=' + newContent.length + ', old len=' + c.length);
