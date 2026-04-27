"""
修复 index.html 中丢失的 SPLASH 欢迎页 CSS，并适配粉白主题
"""
import re

# ========== Step 1: 从原始 git commit 提取 SPLASH CSS ==========
import subprocess

result = subprocess.run(
    ['git', 'show', '153333b:家常菜点菜系统.html'],
    capture_output=True,
    cwd=r'C:\Users\sean.guo1\WorkBuddy\20260423171332'
)
raw = result.stdout
# 尝试解码
try:
    text = raw.decode('utf-16-le') if raw[:2] == b'\xff\xfe' else raw.decode('utf-8-sig', errors='replace')
except:
    text = raw.decode('utf-8', errors='replace')

# 找 SPLASH CSS 起始和结束位置
s_start = text.find('#splash')
s_rest = text[s_start:]
# 找 .hd 开头的位置（SPLASH CSS 结束）
m = re.search(r'\n\.hd\b', s_rest[50:])
s_end = s_start + m.start() if m else len(text)
splash_css = text[s_start:s_end]

print(f"提取到 SPLASH CSS: {len(splash_css)} 字符")

# ========== Step 2: 读取当前 index.html ==========
with open(r'C:\Users\sean.guo1\WorkBuddy\20260423171332\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ========== Step 3: 替换 CSS 变量（适配粉白主题） ==========
# 原始变量 -> 粉白主题变量
replacements = [
    ('var(--s-bg)', '#1a0a10'),          # 欢迎页深色背景 -> 深粉黑
    ('var(--s-g1)', '#E8628A'),           # 主色 -> 粉红
    ('var(--s-g2)', '#F093B0'),           # 浅粉
    ('var(--s-g3)', '#FBBFD2'),           # 更浅粉
    ('var(--s-g4)', '#C94070'),           # 深粉
    ('var(--s-text)', '#fff'),            # 白色文字
    ('var(--s-sub)', 'rgba(255,200,220,.7)'),  # 半透明白粉文字
    ('rgba(0,0,0,.4)', 'rgba(201,64,112,.3)'), # 食物阴影改为粉色系
    ('rgba(255,255,255,.08)', 'rgba(255,255,255,.12)'),  # 玻璃效果调亮
    ('rgba(255,255,255,.15)', 'rgba(255,255,255,.2)'),
    ('rgba(255,255,255,.1)', 'rgba(255,255,255,.15)'),
    ('rgba(255,255,255,.06)', 'rgba(255,255,255,.1)'),
]

adapted_css = splash_css
for old, new in replacements:
    adapted_css = adapted_css.replace(old, new)

# 修复 orb 颜色
adapted_css = adapted_css.replace(
    'background:var(--s-g1)',
    'background:#E8628A'
)
adapted_css = adapted_css.replace(
    'background:var(--s-g2)',
    'background:#F093B0'
)
adapted_css = adapted_css.replace(
    'background:var(--s-g4)',
    'background:#C94070'
)

# 修复文字颜色引用
adapted_css = adapted_css.replace(
    'color:var(--s-text)',
    'color:#fff'
)
adapted_css = adapted_css.replace(
    'color:var(--s-sub)',
    'color:rgba(255,200,220,.75)'
)

print(f"适配后 CSS: {len(adapted_css)} 字符")

# ========== Step 4: 找到 style 块末尾，在 </style> 前注入 SPLASH CSS ==========
style_end = html.rfind('</style>')
if style_end == -1:
    print("ERROR: 找不到 </style>")
    exit(1)

# 在 </style> 前插入（\n\n 分隔）
new_html = html[:style_end] + '\n\n/* ===== SPLASH WELCOME SCREEN ===== */\n' + adapted_css + '\n' + html[style_end:]

# ========== Step 5: 同时确保 :root 中有 s-bg 等变量 ==========
# 在 :root 块后添加 splash 专用变量
if '--s-bg:' not in new_html:
    root_end = new_html.find('}')
    insert_pos = root_end + 1
    splash_vars = '\n/* SPLASH screen variables */\n:root{--s-bg:#1a0a10;--s-g1:#E8628A;--s-g2:#F093B0;--s-g3:#FBBFD2;--s-g4:#C94070;--s-text:#fff;--s-sub:rgba(255,200,220,.75)}\n'
    new_html = new_html[:insert_pos] + splash_vars + new_html[insert_pos:]

with open(r'C:\Users\sean.guo1\WorkBuddy\20260423171332\index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("✅ SPLASH CSS 注入成功！")
print(f"文件大小: {len(new_html)} 字符")
