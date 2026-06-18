#!/usr/bin/env python3
"""Generate ALL 11 chemistry lessons for content.json"""
import json

PATH = "C:/Users/alyhy/csca-exam-web/data/content.json"

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def sec(ar_heading, en_heading, zh_heading, ar_content):
    return {
        "heading_ar": ar_heading,
        "heading_en": en_heading,
        "heading_zh": zh_heading,
        "content_ar": ar_content,
        "content_en": "",
        "content_zh": ""
    }

def make_lesson(topic, title_ar, title_en, title_zh, sections):
    return {
        "id": f"chem_{topic}",
        "topic": topic,
        "subject": "كيمياء | Chemistry",
        "subject_en": "Chemistry",
        "title_ar": title_ar,
        "title_en": title_en,
        "title_zh": title_zh,
        "sections": sections
    }

# =============== SVG Helpers ===============
def svg_energy_levels():
    return '<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/><text x="175" y="30" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">مستويات الطاقة (ذرة الهيدروجين)</text><text x="175" y="52" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">n=1: E = -13.6 eV</text><text x="175" y="68" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">n=2: E = -3.40 eV</text><text x="175" y="84" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">n=3: E = -1.51 eV</text><text x="175" y="100" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">n=∞: E = 0 eV (تأين)</text><text x="175" y="122" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">الفرق = 13.6 eV</text></svg>'

def svg_atom():
    return '<svg width="350" height="180" viewBox="0 0 350 180" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">تركيب الذرة (نموذج رذرفورد)</text><circle cx="175" cy="100" r="15" fill="rgba(247,37,133,0.3)" stroke="#f72585" stroke-width="2"/><text x="175" y="104" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">نواة</text><ellipse cx="175" cy="100" rx="70" ry="30" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="175" cy="100" rx="110" ry="45" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><circle cx="120" cy="68" r="5" fill="#2ed573"/><circle cx="230" cy="72" r="5" fill="#2ed573"/><circle cx="100" cy="130" r="5" fill="#2ed573"/><circle cx="250" cy="128" r="5" fill="#2ed573"/><circle cx="145" cy="52" r="5" fill="#2ed573"/><circle cx="205" cy="145" r="5" fill="#2ed573"/><text x="105" y="45" fill="#2ed573" font-size="10" font-family="sans-serif">e⁻</text><text x="230" y="58" fill="#2ed573" font-size="10" font-family="sans-serif">e⁻</text><text x="85" y="152" fill="#2ed573" font-size="10" font-family="sans-serif">e⁻</text></svg>'

def svg_orbitals():
    return '<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">أشكال المدارات الذرية</text><circle cx="70" cy="80" r="30" fill="none" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="120" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle">s</text><ellipse cx="175" cy="65" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><ellipse cx="175" cy="95" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><text x="175" y="120" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">p</text><ellipse cx="285" cy="65" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2"/><ellipse cx="285" cy="95" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2" transform="rotate(45,285,80)"/><text x="285" y="120" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">d</text></svg>'

def svg_ionic():
    return '<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">الرابطة الأيونية (NaCl)</text><circle cx="120" cy="70" r="25" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle">Na⁺</text><circle cx="240" cy="70" r="30" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/><text x="240" y="74" fill="#f72585" font-size="14" font-family="sans-serif" text-anchor="middle">Cl⁻</text><text x="175" y="110" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">Na + Cl → Na⁺ + Cl⁻</text><text x="175" y="125" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">انتقال إلكترون من Na إلى Cl</text></svg>'

def svg_covalent():
    return '<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">الرابطة التساهمية (H₂)</text><circle cx="120" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle">H</text><circle cx="230" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="230" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle">H</text><line x1="140" y1="70" x2="210" y2="70" stroke="#f72585" stroke-width="3"/><text x="175" y="55" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">H:H</text><text x="175" y="110" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">مشاركة إلكترونين بين ذرتي الهيدروجين</text></svg>'

def svg_vsepr():
    return '<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">الأشكال الهندسية VSEPR</text><circle cx="70" cy="80" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="84" fill="#4cc9f0" font-size="9" font-family="sans-serif" text-anchor="middle">خطي 180°</text><circle cx="175" cy="80" r="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/><text x="175" y="84" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">مثلث 120°</text><circle cx="285" cy="80" r="25" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/><text x="285" y="84" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">رباعي 109.5°</text></svg>'

def svg_equilibrium():
    return '<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">منحنى الاتزان الكيميائي</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="2"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="2"/><path d="M 30 110 Q 80 30 160 60 Q 250 90 320 60" fill="none" stroke="#4cc9f0" stroke-width="2.5"/><path d="M 30 30 Q 80 90 160 60 Q 250 40 320 70" fill="none" stroke="#f72585" stroke-width="2.5"/><text x="160" y="55" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">اتزان</text><line x1="160" y1="60" x2="160" y2="130" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="4,3"/><text x="160" y="138" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">الزمن</text><text x="18" y="70" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle" transform="rotate(-90,18,70)">التركيز</text></svg>'

def svg_potential():
    return '<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">مخطط طاقة التفاعل</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="50" y1="120" x2="70" y2="20" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="20" x2="70" y2="100" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="100" x2="300" y2="50" stroke="#f72585" stroke-width="2.5"/><line x1="300" y1="50" x2="320" y2="120" stroke="#f72585" stroke-width="2.5"/><line x1="160" y1="20" x2="160" y2="100" stroke="#2ed573" stroke-width="2" stroke-dasharray="4,2"/><text x="165" y="58" fill="#2ed573" font-size="10" font-family="sans-serif">Ea</text><text x="70" y="130" fill="#4cc9f0" font-size="9" font-family="sans-serif" text-anchor="middle">متفاعلات</text><text x="300" y="138" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">نواتج</text></svg>'

def svg_benzene():
    return '<svg width="200" height="140" viewBox="0 0 200 140" xmlns="http://www.w3.org/2000/svg"><text x="100" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">البنزين (C₆H₆)</text><polygon points="100,30 150,60 150,100 100,130 50,100 50,60" fill="rgba(76,201,240,0.1)" stroke="#4cc9f0" stroke-width="2"/><circle cx="100" cy="80" r="20" fill="none" stroke="#f72585" stroke-width="1.5" stroke-dasharray="4,3"/><text x="152" y="63" fill="#fff" font-size="9" font-family="sans-serif">H</text><text x="152" y="105" fill="#fff" font-size="9" font-family="sans-serif">H</text><text x="48" y="105" fill="#fff" font-size="9" font-family="sans-serif">H</text><text x="48" y="63" fill="#fff" font-size="9" font-family="sans-serif">H</text><text x="100" y="28" fill="#fff" font-size="9" font-family="sans-serif">H</text><text x="100" y="138" fill="#fff" font-size="9" font-family="sans-serif">H</text></svg>'

def svg_ecell():
    return '<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">خلية كلفانية</text><rect x="20" y="30" width="100" height="100" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2" rx="5"/><text x="70" y="55" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle">Zn | Zn²⁺</text><text x="70" y="80" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">Zn → Zn²⁺ + 2e⁻</text><text x="70" y="110" fill="#4cc9f0" font-size="9" font-family="sans-serif" text-anchor="middle">(أنود: تأكسد)</text><rect x="230" y="30" width="100" height="100" fill="rgba(247,37,133,0.08)" stroke="#f72585" stroke-width="2" rx="5"/><text x="280" y="55" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">Cu²⁺ | Cu</text><text x="280" y="80" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">Cu²⁺ + 2e⁻ → Cu</text><text x="280" y="110" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">(كاثود: اختزال)</text><line x1="120" y1="50" x2="230" y2="50" stroke="#2ed573" stroke-width="2"/><text x="175" y="48" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">e⁻</text><rect x="145" y="85" width="60" height="30" fill="rgba(46,213,115,0.1)" stroke="#2ed573" stroke-width="1.5" rx="3"/><text x="175" y="103" fill="#2ed573" font-size="8" font-family="sans-serif" text-anchor="middle">جسر ملحي</text></svg>'

def svg_kinetics():
    return '<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg"><text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">منحنيات الرتب المختلفة</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="40" x2="320" y2="40" stroke="#4cc9f0" stroke-width="2"/><text x="280" y="38" fill="#4cc9f0" font-size="9" font-family="sans-serif">الرتبة 0 (ثابت)</text><line x1="30" y1="100" x2="180" y2="40" stroke="#f72585" stroke-width="2"/><text x="200" y="55" fill="#f72585" font-size="9" font-family="sans-serif">الرتبة 1</text><path d="M 30 30 Q 120 30 180 100 Q 250 140 320 145" fill="none" stroke="#2ed573" stroke-width="2"/><text x="280" y="120" fill="#2ed573" font-size="9" font-family="sans-serif">الرتبة 2</text><text x="18" y="70" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle" transform="rotate(-90,18,70)">[A]</text><text x="175" y="138" fill="#fff" font-size="9" font-family="sans-serif" text-anchor="middle">الزمن</text></svg>'

# ============================================================
# LESSON 1: chem_atomic
# ============================================================
L1 = make_lesson("atomic", "البناء الذري", "Atomic Structure", "原子结构", [
    sec("مكونات الذرة - تعريفات أساسية", "Atomic Components", "原子组成",
        f'<p><b>الذرة</b> (Atom) هي أصغر وحدة بنائية للمادة تحتفظ بالخواص الكيميائية للعنصر. تتكون الذرة من <b>نواة</b> تحتوي على بروتونات (موجبة) ونيوترونات (متعادلة)، وتدور حولها <b>إلكترونات</b> (سالبة).</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الجسيم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشحنة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الكتلة (kg)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الموقع</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بروتون (p⁺)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+1.602×10⁻¹⁹ C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.673×10⁻²⁷</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النواة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نيوترون (n⁰)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.675×10⁻²⁷</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النواة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إلكترون (e⁻)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-1.602×10⁻¹⁹ C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">9.109×10⁻³¹</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حول النواة</td></tr>'
        '</table>'
        '<p><b>العدد الذري</b> Z = عدد البروتونات. <b>العدد الكتلي</b> A = بروتونات + نيوترونات. <b>النظائر</b>: نفس Z (نفس العنصر) لكن A مختلف (نيوترونات مختلفة). مثال: \\(^{12}_{6}C\\) و \\(^{14}_{6}C\\).</p>'
        f'{svg_atom()}'),
    sec("التوزيع الإلكتروني", "Electron Configuration", "电子排布",
        '<p>تملأ الإلكترونات المدارات حسب <b>مبدأ أوفباو</b> (من الأقل طاقة): \\(1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s \\rightarrow 3d \\rightarrow 4p \\rightarrow 5s...\\)</p>'
        '<p><b>قاعدة هوند</b>: تملأ الإلكترونات المدارات المتكافئة منفردة أولاً. النيتروجين (Z=7): \\(1s^2 2s^2 2p^3\\) (إلكترونات p منفردة).</p>'
        '<p><b>مبدأ باولي</b>: لا يمكن لإلكترونين أن يكون لهما نفس أعداد الكم الأربعة. كل مدار يسع إلكترونين فقط (باتجاهي دوران متعاكسين).</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">العنصر</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">Z</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التوزيع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">تكافؤ</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(1s^1\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">6</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(1s^2 2s^2 2p^2\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">4</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Fe</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">26</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\([Ar] 3d^6 4s^2\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2</td></tr>'
        '</table>'),
    sec("أعداد الكم", "Quantum Numbers", "量子数",
        '<p>أربعة أعداد كم تصف حالة كل إلكترون:</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">عدد الكم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القيم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المعنى</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرئيسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(n\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1,2,3,...</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مستوى الطاقة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الثانوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(l\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0...n-1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">شكل المدار (s,p,d,f)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المغناطيسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(m_l\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-l...+l</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اتجاه المدار</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المغزلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(m_s\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">±½</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اتجاه الدوران</td></tr>'
        '</table>'
        f'<p>\\(l=0\\) (s) كروي، \\(l=1\\) (p) دمبلي، \\(l=2\\) (d) معقد. عدد المدارات = \\(2l+1\\).</p>{svg_orbitals()}'),
    sec("الجدول الدوري والخواص", "Periodic Table", "周期表",
        '<p><b>الدورة</b> = مستوى الطاقة. <b>المجموعة</b> = نفس إلكترونات التكافؤ.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">في الدورة ←</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">في المجموعة ↓</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نصف القطر الذري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يتناقص</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يزداد</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">طاقة التأين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تزداد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تتناقص</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">السالبية الكهربائية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تزداد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تتناقص</td></tr>'
        '</table>'
        '<p><b>المجموعات:</b> 1 (قلوية): نشيطة جداً. 17 (هالوجينات): لا فلزات نشيطة. 18 (نبيلة): خاملة. العناصر الانتقالية (3-12): حالات تأكسد متعددة، أملاح ملونة.</p>'),
    sec("قوانين وصيغ أساسية", "Key Formulas", "关键公式",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العدد الذري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(Z = p^+\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العدد الكتلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(A = Z + N\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الكتلة الذرية النسبية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(A_r = \\frac{\\sum (m \\times \\%)}{100}\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">طاقة الهيدروجين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(E_n = -13.6/n^2 \\text{ eV}\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الكتلة الذرية (amu)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1 amu = 1.66×10⁻²⁷ kg</td></tr>'
        '</table>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> ذرة Z=17, A=35. جد عدد p⁺, n⁰, e⁻.</p>'
        '<p><b>الحل:</b> p⁺=17, e⁻=17, n⁰ = 35-17 = 18.</p>'
        '<p><b>مثال 2:</b> للكلور نظيران: ³⁵Cl (75.77%) و ³⁷Cl (24.23%). جد \\(A_r\\).</p>'
        '<p><b>الحل:</b> \\(A_r = \\frac{35\\times75.77+37\\times24.23}{100} = 35.48\\)</p>'
        '<p><b>مثال 3:</b> توزيع الأكسجين (Z=8) وعدد تكافؤه.</p>'
        '<p><b>الحل:</b> \\(1s^2 2s^2 2p^4\\) → 6 إلكترونات تكافؤ.</p>'
        '<p><b>مثال 4:</b> أعداد الكم لإلكترون 3p.</p>'
        '<p><b>الحل:</b> n=3, l=1, m_l∈{-1,0,+1}, m_s=±½. مثال: (3,1,0,+½).</p>'
        '<p><b>مثال 5:</b> رتب Li, Na, K, Rb حسب نصف القطر.</p>'
        '<p><b>الحل:</b> Li < Na < K < Rb.</p>'),
    sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
        '<p><b>نصائح:</b></p>'
        '<ul><li>Z = p⁺ = e⁻ (في الذرة المتعادلة)</li>'
        '<li>النظائر: نفس Z، مختلف N</li>'
        '<li>4s قبل 3d (أوفباو)</li>'
        '<li>أعلى سالبية كهربائية: F = 4.0</li></ul>'
        '<p><b>أخطاء:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين Z و A</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Z=بروتونات, A=بروتونات+نيوترونات</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">3d قبل 4s</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">4s يملأ أولاً</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">m_l لا يعتمد على l</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">m_l من -l إلى +l</td></tr>'
        '</table>'),
])

# ============================================================
# LESSON 2: chem_bonding
# ============================================================
L2 = make_lesson("bonding", "الروابط الكيميائية", "Chemical Bonding", "化学键", [
    sec("أنواع الروابط الكيميائية", "Types of Chemical Bonds", "化学键类型",
        f'<p><b>الرابطة الكيميائية</b> هي قوة تجذب ذرتين معاً لتكوين جزيء أو مركب. الأنواع الرئيسية:</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الآلية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">بين</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أيونية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">انتقال إلكترونات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فلز + لا فلز</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">NaCl</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تساهمية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مشاركة إلكترونات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا فلز + لا فلز</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂, H₂O</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فلزية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إلكترونات متمركزة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فلز + فلز</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Fe, Cu</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">هيدروجينية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جذب H مع O,N,F</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بين جزيئات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂O</td></tr>'
        '</table>'
        f'<p><b>الرابطة الأيونية</b>: تفقد ذرة فلز إلكتروناً (تصبح أيوناً موجباً) وتكسبه ذرة لا فلز (تصبح أيوناً سالباً). التجاذب الكهروستاتيكي بين الأيونات المتعاكسة هو الرابطة.</p>{svg_ionic()}'
        f'<p><b>الرابطة التساهمية</b>: تشارك ذرتان زوجاً أو أكثر من الإلكترونات. رابطة أحادية (زوج واحد) مثل H₂، ثنائية (زوجان) مثل O₂، ثلاثية (ثلاثة أزواج) مثل N₂.</p>{svg_covalent()}'),
    sec("نظرية VSEPR", "VSEPR Theory", "VSEPR理论",
        '<p><b>VSEPR</b> (Valence Shell Electron Pair Repulsion): أزواج الإلكترونات حول الذرة المركزية تتنافر، فتتباعد بأكبر زاوية ممكنة لتحديد الشكل الهندسي.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشكل</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الزاوية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AX₂</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">خطي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">180°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CO₂, BeCl₂</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AX₃</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مثلث مستوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">120°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">BF₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AX₄</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رباعي أوجه</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">109.5°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₄</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AX₃E</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">هرمي ثلاثي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">107°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">NH₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AX₂E₂</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">منحني</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">104.5°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂O</td></tr>'
        '</table>'
        f'{svg_vsepr()}'),
    sec("التهجين (Hybridization)", "Hybridization", "杂化",
        '<p><b>التهجين</b>: خلط مدارات ذرية لتكوين مدارات مهجنة جديدة متكافئة في الطاقة والشكل.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التهجين</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المدارات المخلوطة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشكل</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الزاوية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(sp\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">s + p</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">خطي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">180°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">BeCl₂</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(sp^2\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">s + 2p</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مثلث مستوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">120°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">BF₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(sp^3\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">s + 3p</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رباعي أوجه</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">109.5°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₄</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(sp^3d\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">s+3p+d</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">هرمي مزدوج</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">90°,120°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">PCl₅</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(sp^3d^2\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">s+3p+2d</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثماني أوجه</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">90°</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">SF₆</td></tr>'
        '</table>'
        '<p><b>قطبية الجزيء</b>: تعتمد على فرق السالبية الكهربائية وشكل الجزيء. جزيء قطبي: عزم ثنائي قطب ≠ 0 (مثل H₂O). جزيء غير قطبي: عزم ثنائي قطب = 0 (مثل CO₂ الخطي).</p>'),
    sec("قوانين أساسية للروابط", "Key Bonding Laws", "化学键定律",
        '<p><b>قاعدة الثمانية (Octet Rule):</b> تميل الذرات للوصول إلى 8 إلكترونات في غلافها الخارجي (ماعدا H: 2 إلكترون).</p>'
        '<p><b>طاقة الرابطة (Bond Energy):</b> الطاقة اللازمة لكسر 1 mol من الرابطة (kJ/mol). كلما زادت طاقة الرابطة، كانت أقوى وأقصر.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرابطة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">طول الرابطة (pm)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">طاقة الرابطة (kJ/mol)</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C–C (أحادية)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">154</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">348</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C=C (ثنائية)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">134</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">614</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C≡C (ثلاثية)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">121</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">839</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H–H</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">74</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">436</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">O–H</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">96</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">463</td></tr>'
        '</table>'
        '<p><b>الرابطة الأحادية</b> (σ): تداخل أمامي للمدارات، أقوى. <b>الرابطة الثنائية</b> (σ + π): رابطة σ + رابطة π جانبية.</p>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> حدد نوع الرابطة في NaCl و H₂ و CH₄.</p>'
        '<p><b>الحل:</b> NaCl: أيونية (Na فلز + Cl لا فلز). H₂: تساهمية (H-H). CH₄: تساهمية (روابط C-H).</p>'
        '<p><b>مثال 2:</b> ما الشكل الهندسي لـ NH₃ حسب VSEPR؟</p>'
        '<p><b>الحل:</b> NH₃: AX₃E → هرمي ثلاثي، زاوية 107° (زوج حر واحد يدفع الذرات).</p>'
        '<p><b>مثال 3:</b> حدد تهجين الكربون في CH₄ و C₂H₄ و C₂H₂.</p>'
        '<p><b>الحل:</b> CH₄: \\(sp^3\\). C₂H₄: \\(sp^2\\). C₂H₂: \\(sp\\).</p>'
        '<p><b>مثال 4:</b> هل CO₂ قطبي أم لا؟ ولماذا؟</p>'
        '<p><b>الحل:</b> CO₂ خطي (O=C=O)، العزم ثنائي القطب = 0 → غير قطبي رغم أن C-O قطبية.</p>'
        '<p><b>مثال 5:</b> رتب قوة الرابطة: C-C, C=C, C≡C.</p>'
        '<p><b>الحل:</b> C≡C (أقوى) > C=C > C-C (أضعف). طاقة الرابطة: 839 > 614 > 348 kJ/mol.</p>'),
    sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
        '<p><b>نصائح:</b></p><ul><li>الرابطة الأيونية: بين فلز ولا فلز (فرق سالبية كبير)</li>'
        '<li>الرابطة التساهمية: بين لا فلزات (فرق سالبية صغير)</li>'
        '<li>قطبية الجزيء: تعتمد على الشكل الهندسي + فرق السالبية</li>'
        '<li>VSEPR: عد أزواج الإلكترونات (الرابطة والحرّة) حول الذرة المركزية</li></ul>'
        '<p><b>أخطاء:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين الأيوني والتساهمي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أيوني: فلز+لا فلز، تساهمي: لا فلز+لا فلز</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جزيء خطي = قطبي دائماً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخطي قد يكون غير قطبي (CO₂)</td></tr>'
        '</table>'),
])

# ============================================================
# LESSON 3: chem_equilibrium
# ============================================================
L3 = make_lesson("equilibrium", "الاتزان الكيميائي والأحماض والقواعد", "Chemical Equilibrium, Acids and Bases", "化学平衡与酸碱", [
    sec("ثابت الاتزان ومبدأ لوشاتيليه", "Equilibrium Constant and Le Chatelier", "平衡常数",
        f'<p>للتفاعل العكسي: \\(aA + bB \\rightleftharpoons cC + dD\\)</p>'
        '<p><b>ثابت الاتزان</b>: \\(K_c = \\frac{[C]^c[D]^d}{[A]^a[B]^b}\\)</p>'
        '<p><b>ملاحظات:</b> \\(K_c\\) يتغير فقط مع درجة الحرارة. إذا \\(K_c > 1\\): النواتج مفضلة. إذا \\(K_c < 1\\): المتفاعلات مفضلة. المواد الصلبة والسوائل النقية لا تظهر في \\(K_c\\).</p>'
        '<p><b>مبدأ لوشاتيليه:</b> إذا أثر تغيير (تركيز، ضغط، حرارة) على نظام في حالة اتزان، يزيح النظام اتزانه ليعاكس التغيير.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التغيير</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">اتجاه الإزاحة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">زيادة تركيز المتفاعلات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">→ نحو النواتج</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">زيادة الضغط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">→ نحو الجهة ذات المولات الأقل</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رفع درجة الحرارة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">→ نحو الجهة الماصة للحرارة</td></tr>'
        '</table>'
        f'{svg_equilibrium()}'),
    sec("الأحماض والقواعد الأس الهيدروجيني pH", "Acids, Bases and pH", "酸碱和pH",
        '<p><b>Arrhenius:</b> حمض = يعطي H⁺، قاعدة = تعطي OH⁻.</p>'
        '<p><b>Brønsted-Lowry:</b> حمض = مانح بروتون (H⁺)، قاعدة = مستقبل بروتون.</p>'
        '<p><b>pH</b>: \\(\\text{pH} = -\\log[H^+]\\)، \\(\\text{pOH} = -\\log[OH^-]\\)، \\(\\text{pH} + \\text{pOH} = 14\\) عند 25°C.</p>'
        '<p><b>الأحماض القوية:</b> تتأين كلياً (HCl, HNO₃, H₂SO₄). <b>الأحماض الضعيفة:</b> تتأين جزئياً (CH₃COOH, HF).</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">pH</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">[H⁺] (M)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الوصف</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0-2</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">10⁻² - 1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمض قوي</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">3-6</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">10⁻⁶ - 10⁻³</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمض ضعيف</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">7</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">10⁻⁷</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">متعادل</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">8-11</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">10⁻¹¹ - 10⁻⁸</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدة ضعيفة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">12-14</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">10⁻¹⁴ - 10⁻¹²</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدة قوية</td></tr>'
        '</table>'
        '<p><b>ثابت تأين الحمض</b> \\(K_a = \\frac{[H^+][A^-]}{[HA]}\\). <b>pK_a</b> = -log K_a. كلما صغر pK_a، زادت قوة الحمض.</p>'),
    sec("المحاليل المنظمة (Buffers)", "Buffer Solutions", "缓冲溶液",
        '<p><b>المحلول المنظم</b> يقاوم التغير في pH عند إضافة حمض أو قاعدة. يتكون من حمض ضعيف وقاعدته المترافقة (أو قاعدة ضعيفة وحمضها المترافق).</p>'
        '<p><b>معادلة هندر-هاسلباخ:</b> \\(\\text{pH} = pK_a + \\log\\frac{[A^-]}{[HA]}\\)</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">نوع المنظم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المكونات</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمضي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمض ضعيف + ملحه</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃COOH / CH₃COONa</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدة ضعيفة + ملحها</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">NH₃ / NH₄Cl</td></tr>'
        '</table>'
        '<p><b>آلية عمل المنظم:</b> عند إضافة H⁺ → يتحد مع القاعدة المرافقة A⁻ لتكوين HA. عند إضافة OH⁻ → يتفاعل مع HA لتكوين A⁻ + H₂O.</p>'),
    sec("منتجات الذوبان (Ksp)", "Solubility Products", "溶度积",
        '<p>للمركب الشحيح الذوبان \\(A_xB_y(s) \\rightleftharpoons xA^{y+} + yB^{x-}\\):</p>'
        '<p>\\(K_{sp} = [A^{y+}]^x[B^{x-}]^y\\)</p>'
        '<p><b>ملاحظات:</b> كلما صغر Ksp، قلت الذائبية. <b>تأثير الأيون المشترك:</b> إضافة أيون موجود يقلل الذائبية.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المركب</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">Ksp (25°C)</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">AgCl</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.8×10⁻¹⁰</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">BaSO₄</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.1×10⁻¹⁰</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CaCO₃</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">3.4×10⁻⁹</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Fe(OH)₃</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2.8×10⁻³⁹</td></tr>'
        '</table>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> للتفاعل \\(N_2 + 3H_2 \\rightleftharpoons 2NH_3\\)، إذا \\([N_2]=0.5M, [H_2]=1.0M, [NH_3]=0.8M\\)، احسب \\(K_c\\).</p>'
        '<p><b>الحل:</b> \\(K_c = \\frac{[NH_3]^2}{[N_2][H_2]^3} = \\frac{0.8^2}{0.5 \\times 1.0^3} = \\frac{0.64}{0.5} = 1.28\\)</p>'
        '<p><b>مثال 2:</b> pH لمحلول HCl تركيزه 0.01 M.</p>'
        '<p><b>الحل:</b> HCl قوي → \\([H^+]=0.01M\\). pH = -log(0.01) = 2.</p>'
        '<p><b>مثال 3:</b> pH لمحلول NaOH تركيزه 0.001 M.</p>'
        '<p><b>الحل:</b> \\([OH^-]=10^{-3}M\\), pOH=3, pH=14-3=11.</p>'
        '<p><b>مثال 4:</b> محلول منظم CH₃COOH/CH₃COONa بنسبة [A⁻]/[HA]=2, pKa=4.76. جد pH.</p>'
        '<p><b>الحل:</b> pH = 4.76 + log(2) = 4.76 + 0.30 = 5.06.</p>'
        '<p><b>مثال 5:</b> Ksp لـ AgCl = 1.8×10⁻¹⁰. جد ذائبيته في الماء (mol/L).</p>'
        '<p><b>الحل:</b> \\(K_{sp}=s^2\\) → \\(s=\\sqrt{1.8\\times10^{-10}}=1.34\\times10^{-5} M\\)</p>'),
    sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
        '<p><b>نصائح:</b></p><ul><li>\\(K_c\\) يتغير فقط مع درجة الحرارة</li>'
        '<li>المواد الصلبة والسوائل النقية ≠ يدخلون في \\(K_c\\)</li>'
        '<li>pH للحمض القوي = -log[حمض]</li>'
        '<li>للمنظم: استخدم معادلة هندر-هاسلباخ</li></ul>'
        '<p><b>أخطاء:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إدخال المواد الصلبة في Kc</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المواد الصلبة = 1 (تستبعد)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين pH و pOH</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">pH+pOH=14</td></tr>'
        '</table>'),
])

# ============================================================
# LESSON 4: chem_kinetics
# ============================================================
L4 = make_lesson("kinetics", "الحركية الكيميائية", "Chemical Kinetics", "化学动力学", [
    sec("معدل التفاعل وقانون السرعة", "Reaction Rate and Rate Law", "反应速率",
        f'<p><b>معدل التفاعل</b> = \\(-\\frac{\\Delta[A]}{\\Delta t}\\) (للمتفاعلات) أو \\(+\\frac{\\Delta[B]}{\\Delta t}\\) (للنواتج). وحدة: M/s.</p>'
        '<p><b>قانون السرعة:</b> \\(\\text{rate} = k[A]^m[B]^n\\) حيث m,n <b>رتب التفاعل</b> (تحدد تجريبياً). k = ثابت السرعة.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الرتبة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">قانون السرعة التكاملي</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الرسم البياني (خط مستقيم)</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\([A] = -kt + [A]_0\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">[A] vs t</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\ln[A] = -kt + \\ln[A]_0\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ln[A] vs t</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\frac{1}{[A]} = kt + \\frac{1}{[A]_0}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1/[A] vs t</td></tr>'
        '</table>'
        svg_kinetics()'),
    sec("طاقة التنشيط ومعادلة أرهينيوس", "Activation Energy", "活化能",
        '<p><b>طاقة التنشيط</b> \\(E_a\\): الحد الأدنى من الطاقة اللازمة لبدء التفاعل.</p>'
        '<p><b>معادلة أرهينيوس:</b> \\(k = A \\cdot e^{-E_a/RT}\\)</p>'
        '<p>الصورة اللوغاريتمية: \\(\\ln k = \\ln A - \\frac{E_a}{R} \\cdot \\frac{1}{T}\\)</p>'
        '<p><b>العامل المساعد (Catalyst):</b> يخفض \\(E_a\\)، فيسرع التفاعل دون أن يستهلك. المواد المحفزة الحيوية (الإنزيمات) تخفض \\(E_a\\) بشكل كبير.</p>'
        '<p><b>قاعدة 10°:</b> رفع درجة الحرارة بمقدار 10°C يضاعف سرعة التفاعل تقريباً.</p>'
        f'{svg_potential()}'),
    sec("عمر النصف وآليات التفاعل", "Half-Life and Mechanisms", "半衰期",
        '<p><b>عمر النصف</b> \\(t_{1/2}\\): الزمن اللازم لانخفاض التركيز للنصف.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الرتبة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\\(t_{1/2}\\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">ملاحظة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\([A]_0/2k\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يعتمد على [A]₀</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(0.693/k\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثابت (لا يعتمد على التركيز)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(1/(k[A]_0)\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يعتمد على [A]₀</td></tr>'
        '</table>'
        '<p><b>آلية التفاعل:</b> سلسلة من الخطوات الأولية. <b>خطوة تحديد السرعة</b> (Rate-Determining Step) = أبطأ خطوة.</p>'
        '<p><b>الجزيئية (Molecularity):</b> عدد الجزيئات في الخطوة الأولية. أحادية (جزيء واحد)، ثنائية (جزيئان)، ثلاثية (ثلاثة جزيئات).</p>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> تفاعل من الرتبة الأولى، \\(k=0.05 s^{-1}\\). إذا \\([A]_0=2M\\)، جد [A] بعد 20 ثانية.</p>'
        '<p><b>الحل:</b> \\(\\ln[A] = -0.05\\times20 + \\ln2 = -1 + 0.693 = -0.307\\). \\([A] = e^{-0.307} = 0.736 M\\).</p>'
        '<p><b>مثال 2:</b> جد عمر النصف لتفاعل من الرتبة الأولى، \\(k=0.0693 s^{-1}\\).</p>'
        '<p><b>الحل:</b> \\(t_{1/2} = 0.693/0.0693 = 10\\) ثوان.</p>'
        '<p><b>مثال 3:</b> إذا تضاعفت السرعة عند رفع T من 300K لـ 310K، احسب \\(E_a\\).</p>'
        '<p><b>الحل:</b> باستخدام معادلة أرهينيوس: \\(\\ln\\frac{k_2}{k_1} = \\frac{E_a}{R}(\\frac{1}{T_1}-\\frac{1}{T_2})\\). \\(\\ln2 = \\frac{E_a}{8.314}(\\frac{1}{300}-\\frac{1}{310})\\) → \\(E_a \\approx 53.6 \\text{ kJ/mol}\\)</p>'),
    sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
        '<p><b>نصائح:</b></p><ul><li>الرتبة تحدد تجريبياً وليس من المعادلة الموزونة</li>'
        '<li>الرتبة الأولى: \\(t_{1/2}\\) ثابت (أداة مفيدة للتعرف)</li>'
        '<li>العامل المساعد لا يغير \\(\\Delta H\\) أو \\(K\\)، فقط \\(E_a\\)</li></ul>'
        '<p><b>أخطاء:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرتبة = المعاملات في المعادلة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرتبة تحدد تجريبياً</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين \\(t_{1/2}\\) للرتبة 1 و 2</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرتبة 1: 0.693/k، الرتبة 2: 1/(k[A]₀)</td></tr>'
        '</table>'),
])

# ============================================================
# LESSON 5: chem_basic
# ============================================================
L5 = make_lesson("basic", "المفاهيم الأساسية في الكيمياء", "Basic Concepts in Chemistry", "化学基本概念", [
    sec("المول وعدد أفوجادرو", "Mole and Avogadro's Number", "摩尔",
        '<p><b>المول (Mole):</b> كمية المادة التي تحتوي على عدد أفوجادرو من الوحدات. \\(N_A = 6.022\\times10^{23} \\text{ particles/mol}\\)</p>'
        '<p><b>الكتلة المولية (Molar Mass):</b> كتلة 1 مول بوحدة g/mol.</p>'
        '<p><b>القوانين:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المطلوب</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد المولات (n)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(n = \\frac{m}{M}\\) (m=الكتلة، M=الكتلة المولية)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد الجسيمات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(N = n \\times N_A\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حجم الغاز (STP)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(V = n \\times 22.4 \\text{ L/mol}\\)</td></tr>'
        '</table>'),
    sec("الكتلة الذرية والجزيئية", "Atomic and Molecular Mass", "原子量和分子量",
        '<p><b>الكتلة الذرية النسبية</b>: متوسط كتلة ذرات العنصر مقارنة بـ 1/12 كتلة ¹²C.</p>'
        '<p><b>الكتلة الجزيئية</b>: مجموع الكتل الذرية لذرات الجزيء.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المركب</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الحساب</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الكتلة الجزيئية (g/mol)</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂O</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2×1.008 + 16.00</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">18.016</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CO₂</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">12.01 + 2×16.00</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">44.01</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">NaCl</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">22.99 + 35.45</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">58.44</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₆H₁₂O₆</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">6×12.01 + 12×1.008 + 6×16.00</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">180.16</td></tr>'
        '</table>'
        '<p>1 amu = 1.6605×10⁻²⁴ g = 1/12 كتلة ذرة ¹²C.</p>'),
    sec("قوانين الغازات", "Gas Laws", "气体定律",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الثابت</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بويل (Boyle)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(P_1V_1 = P_2V_2\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">T, n</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">شارل (Charles)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\frac{V_1}{T_1} = \\frac{V_2}{T_2}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">P, n</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أفوجادرو</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\frac{V_1}{n_1} = \\frac{V_2}{n_2}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">P, T</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الغاز المثالي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(PV = nRT\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">R=0.0821 L·atm/mol·K</td></tr>'
        '</table>'
        '<p><b>STP</b> (0°C, 1 atm): الحجم المولي = 22.4 L/mol. <b>R</b> = 0.0821 L·atm/mol·K = 8.314 J/mol·K.</p>'
        '<p><b>قانون دالتون للضغوط الجزئية:</b> \\(P_{total} = P_1 + P_2 + P_3 + ...\\)</p>'),
    sec("التركيزات الكيميائية", "Chemical Concentrations", "化学浓度",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">نوع التركيز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المولارية (M)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(M = \\frac{n}{V(L)}\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المولالية (m)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(m = \\frac{n}{kg(مذيب)}\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النسبة الوزنية (% w/w)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\% = \\frac{m_{مذاب}}{m_{محلول}}\\times100\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جزء في المليون (ppm)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(ppm = \\frac{m_{مذاب}}{m_{محلول}}\\times10^6\\)</td></tr>'
        '</table>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> كم مولاً في 36 g من H₂O؟</p>'
        '<p><b>الحل:</b> \\(M_{H2O}=18\\text{ g/mol}\\). \\(n = 36/18 = 2\\) mol.</p>'
        '<p><b>مثال 2:</b> كم جزيئاً في 0.5 mol من CO₂؟</p>'
        '<p><b>الحل:</b> \\(N = 0.5 \\times 6.022\\times10^{23} = 3.011\\times10^{23}\\) جزيء.</p>'
        '<p><b>مثال 3:</b> حجم 2 mol من O₂ عند STP.</p>'
        '<p><b>الحل:</b> \\(V = 2 \\times 22.4 = 44.8\\) L.</p>'
        '<p><b>مثال 4:</b> كتلة 0.5 L من محلول NaCl 2M.</p>'
        '<p><b>الحل:</b> \\(n = 2 \\times 0.5 = 1\\) mol. \\(m = 1 \\times 58.44 = 58.44\\) g.</p>'),
])

# ============================================================
# LESSON 6: chem_inorganic
# ============================================================
L6 = make_lesson("inorganic", "الكيمياء غير العضوية", "Inorganic Chemistry", "无机化学", [
    sec("الهالوجينات والفلزات القلوية", "Halogens and Alkali Metals", "卤素和碱金属",
        '<p><b>الهالوجينات (المجموعة 17):</b> F₂ (غاز أصفر)، Cl₂ (غاز أصفر-أخضر)، Br₂ (سائل بني)، I₂ (صلب بنفسجي).</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الاتجاه في المجموعة ↓</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نصف القطر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يزداد</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النشاط الكيميائي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يقل</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نقطة الغليان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تزداد</td></tr>'
        '</table>'
        '<p><b>الفلزات القلوية (المجموعة 1):</b> تتفاعل بعنف مع الماء: \\(2Na + 2H_2O \\rightarrow 2NaOH + H_2\\). النشاط يزداد للنزول في المجموعة (Li < Na < K < Rb < Cs).</p>'),
    sec("التفاعلات في المحاليل المائية", "Reactions in Aqueous Solutions", "水溶液反应",
        '<p><b>تفاعلات الترسيب:</b> تكوين راسب صلب غير ذائب.</p>'
        '<p><b>قواعد الذائبية:</b></p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الأيون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الذائبية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الاستثناءات</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">NO₃⁻</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كلها ذائبة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا يوجد</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Na⁺, K⁺</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كلها ذائبة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا يوجد</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Cl⁻, Br⁻, I⁻</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معظمها ذائبة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Ag⁺, Pb²⁺, Hg₂²⁺</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">SO₄²⁻</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معظمها ذائبة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Ba²⁺, Pb²⁺, Sr²⁺</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CO₃²⁻, PO₄³⁻</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">غير ذائبة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مع أيونات الفلزات القلوية</td></tr>'
        '</table>'
        '<p><b>تفاعلات الأكسدة-الاختزال:</b> انتقال إلكترونات. العامل المؤكسد: يختزل (يكسب إلكترونات). العامل المختزل: يتأكسد (يفقد إلكترونات).</p>'),
    sec("العناصر الانتقالية", "Transition Elements", "过渡元素",
        '<p>العناصر الانتقالية (المجموعات 3-12): مدارات d غير ممتلئة جزئياً. <b>خصائصها:</b></p>'
        '<ul><li>حالات تأكسد متعددة (Fe: +2, +3. Mn: +2, +3, +4, +6, +7)</li>'
        '<li>أملاح ملونة (CuSO₄ أزرق، FeCl₃ بني، KMnO₄ بنفسجي)</li>'
        '<li>نشاط تحفيزي (Fe في عملية هابر، Ni في الهدرجة)</li>'
        '<li>تكوين مركبات معقدة (Coordination Compounds)</li></ul>'
        '<p><b>المركبات المعقدة:</b> أيون فلز مركزي + ليكاندات (جزيئات أو أيونات مرتبطة). <b>العدد التناسقي:</b> عدد الروابط. رباعي أوجه (CN=4)، ثماني أوجه (CN=6).</p>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> اكتب معادلة تفاعل الصوديوم مع الماء.</p>'
        '<p><b>الحل:</b> \\(2Na + 2H_2O \\rightarrow 2NaOH + H_2\\)</p>'
        '<p><b>مثال 2:</b> هل AgCl يترسب عند خلط AgNO₃ و NaCl؟</p>'
        '<p><b>الحل:</b> نعم، لأن AgCl شحيح الذوبان (وفقاً لقواعد الذائبية).</p>'
        '<p><b>مثال 3:</b> حدد العامل المؤكسد والمختزل في \\(Zn + CuSO_4 \\rightarrow ZnSO_4 + Cu\\)</p>'
        '<p><b>الحل:</b> Zn يتأكسد (مختزل)، Cu²⁺ يختزل (مؤكسد).</p>'),
])

# ============================================================
# LESSON 7: chem_organic
# ============================================================
L7 = make_lesson("organic", "الكيمياء العضوية", "Organic Chemistry", "有机化学", [
    sec("الهيدروكربونات", "Hydrocarbons", "碳氢化合物",
        f'<p><b>الألكانات</b> (Alkanes): \\(C_nH_{2n+2}\\)، روابط أحادية فقط (مشبعة). <b>الألكينات</b> (Alkenes): \\(C_nH_{2n}\\)، رابطة ثنائية. <b>الألكاينات</b> (Alkynes): \\(C_nH_{2n-2}\\)، رابطة ثلاثية.</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة العامة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الرابطة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(C_nH_{2n+2}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أحادية (σ)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₄, C₂H₆</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(C_nH_{2n}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثنائية (σ+π)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₂H₄</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكاين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(C_nH_{2n-2}\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثلاثية (σ+2π)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₂H₂</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أروماتي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(C_6H_6\\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رنين (حلقة)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">البنزين</td></tr>'
        '</table>'
        f'{svg_benzene()}'),
    sec("المجموعات الوظيفية", "Functional Groups", "官能团",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المجموعة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">اللاحقة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كحول</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-OH</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-ول (ol)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃OH</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألدهيد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-CHO</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-ال (al)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃CHO</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كيتون</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">>C=O</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-ون (one)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃COCH₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمض كربوكسيلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-COOH</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-حمض (oic acid)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃COOH</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إستر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-COO-</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-وات (oate)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃COOCH₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أمين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-NH₂</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-أمين (amine)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₃NH₂</td></tr>'
        '</table>'),
    sec("أنواع التفاعلات العضوية", "Organic Reactions", "有机反应",
        '<p><b>الإضافة (Addition):</b> إضافة جزيء إلى رابطة متعددة (مثل إضافة Br₂ إلى C₂H₄: \\(C_2H_4 + Br_2 \\rightarrow C_2H_4Br_2\\)).</p>'
        '<p><b>الاستبدال (Substitution):</b> استبدال ذرة بأخرى (هلجنة الألكان: \\(CH_4 + Cl_2 \\rightarrow CH_3Cl + HCl\\)).</p>'
        '<p><b>الإزالة (Elimination):</b> حذف جزيء صغير لتكوين رابطة متعددة (نزع ماء من كحول: \\(C_2H_5OH \\rightarrow C_2H_4 + H_2O\\)).</p>'
        '<p><b>البلمرة (Polymerization):</b> اتحاد مونومرات لتكوين بوليمر. بلمرة الإضافة: مثل البولي إيثيلين. بلمرة التكثيف: مثل النايلون.</p>'),
    sec("التسمية النظامية IUPAC", "IUPAC Nomenclature", "IUPAC命名法",
        '<p><b>خطوات التسمية:</b></p>'
        '<ol><li>حدد أطول سلسلة كربونية متصلة (السلسلة الأم).</li>'
        '<li>رقم السلسلة من أقرب نهاية للمجموعة الوظيفية أو الاستبدال.</li>'
        '<li>حدد وسمِّ الاستبدالات (مجموعات ألكيل: ميثيل، إيثيل، بروبيل...).</li>'
        '<li>اكتب الاسم: رقم-استبدال + سلسلة أم + لاحقة المجموعة الوظيفية.</li></ol>'
        '<p><b>أسماء الألكانات:</b> ميثان (C1)، إيثان (C2)، بروبان (C3)، بيوتان (C4)، بنتان (C5)، هكسان (C6).</p>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> صنف المركبات: CH₄, C₂H₄, C₂H₂, C₆H₆.</p>'
        '<p><b>الحل:</b> CH₄ ألكان، C₂H₄ ألكين، C₂H₂ ألكاين، C₆H₆ أروماتي.</p>'
        '<p><b>مثال 2:</b> ما المجموعة الوظيفية في CH₃COOH؟</p>'
        '<p><b>الحل:</b> -COOH (حمض كربوكسيلي).</p>'
        '<p><b>مثال 3:</b> اكتب معادلة تفاعل إضافة Br₂ إلى الإيثيلين.</p>'
        '<p><b>الحل:</b> \\(C_2H_4 + Br_2 \\rightarrow CH_2BrCH_2Br\\)</p>'),
])

# ============================================================
# LESSON 8: chem_organic_cn
# ============================================================
L8 = make_lesson("organic_cn", "الكيمياء العضوية - التسمية الصينية", "Organic Chemistry - Chinese Nomenclature", "有机化学 - 中文命名", [
    sec("تسمية المركبات بالصينية", "Chinese Naming", "中文命名",
        '<p><b>الأسماء الصينية للألكانات:</b> ميثان = 甲烷 (jiǎwán)، إيثان = 乙烷 (yǐwán)، بروبان = 丙烷 (bǐngwán)، بيوتان = 丁烷 (dīngwán)، بنتان = 戊烷 (wùwán)، هكسان = 己烷 (jǐwán).</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المجموعة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">اللاحقة الصينية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-烷 (wán)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">甲烷 CH₄</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-烯 (xī)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">乙烯 C₂H₄</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألكاين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-炔 (quē)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">乙炔 C₂H₂</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كحول</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-醇 (chún)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">乙醇 C₂H₅OH</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ألدهيد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-醛 (quán)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">乙醛 CH₃CHO</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كيتون</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-酮 (tóng)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">丙酮 CH₃COCH₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حمض</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-酸 (suān)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">乙酸 CH₃COOH</td></tr>'
        '</table>'),
    sec("الأيزومرات", "Isomers", "异构体",
        '<p><b>الأيزومرات البنائية:</b> نفس الصيغة الجزيئية، ترتيب ذرات مختلف. مثال: C₄H₁₀ له أيزومران: بيوتان (n-butane) وأيزوبيوتان (2-methylpropane).</p>'
        '<p><b>الأيزومرات الفراغية:</b> نفس الصيغة والترتيب لكن ترتيب فراغي مختلف. <b>cis/trans:</b> حول الرابطة الثنائية. cis: نفس الجهة، trans: جهتين متعاكستين.</p>'
        '<p><b>الأيزومرات الضوئية (Enantiomers):</b> صور مرآة غير متطابقة. تحتاج لذرة كربون غير متماثلة (مركز كيرالي: 4 مجموعات مختلفة).</p>'),
    sec("التفاعلات المهمة للامتحان", "Important Reactions", "重要反应",
        '<p><b>الأسترة (Esterification):</b> كحول + حمض كربوكسيلي ← إستر + ماء (بوجود H₂SO₄ مركز). \\(CH_3COOH + C_2H_5OH \\rightarrow CH_3COOC_2H_5 + H_2O\\)</p>'
        '<p><b>التصبن (Saponification):</b> إستر + قاعدة ← كحول + ملح حمض دهني (صابون).</p>'
        '<p><b>بلمرة الإيثيلين:</b> \\(nCH_2=CH_2 \\rightarrow -(CH_2-CH_2)_n-\\) (بولي إيثيلين).</p>'
        '<p><b>نزع الماء من الكحول:</b> \\(C_2H_5OH \\xrightarrow{H_2SO_4, \\Delta} C_2H_4 + H_2O\\)</p>'),
])

# ============================================================
# LESSON 9: chem_physical
# ============================================================
L9 = make_lesson("physical", "الكيمياء الفيزيائية", "Physical Chemistry", "物理化学", [
    sec("الكيمياء الكهربائية", "Electrochemistry", "电化学",
        f'<p><b>الخلايا الكلفانية:</b> تحول الطاقة الكيميائية ← كهربائية. <b>الأنود:</b> يتأكسد (قطب سالب). <b>الكاثود:</b> يختزل (قطب موجب).</p>'
        '<p><b>جهد الخلية القياسي:</b> \\(E^\\circ_{cell} = E^\\circ_{cathode} - E^\\circ_{anode}\\)</p>'
        '<p><b>معادلة نرنست:</b> \\(E = E^\\circ - \\frac{RT}{nF} \\ln Q\\) عند 25°C: \\(E = E^\\circ - \\frac{0.0592}{n} \\log Q\\)</p>'
        '<p><b>التحليل الكهربائي:</b> استخدام تيار كهربائي لتحليل مركب. قانون فاراداي: \\(m = \\frac{Q \\times M}{n \\times F}\\) حيث \\(F = 96500 \\text{ C/mol}\\)</p>'
        f'{svg_ecell()}'),
    sec("الخواص التجميعية", "Colligative Properties", "依数性质",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القانون</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">انخفاض ضغط البخار</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(P_1 = X_1 P_1^\\circ\\) (راؤول)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ارتفاع درجة الغليان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\Delta T_b = K_b \\times m \\times i\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">انخفاض درجة التجمد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\Delta T_f = K_f \\times m \\times i\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الضغط الأسموزي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(\\pi = iMRT\\)</td></tr>'
        '</table>'
        '<p><b>معامل فانت هوف</b> \\(i\\): عدد الأيونات من تفكك المذاب. NaCl → i=2، CaCl₂ → i=3، الجلوكوز (غير متأين) → i=1.</p>'),
    sec("قوانين الديناميكا الحرارية", "Thermodynamics Laws", "热力学定律",
        '<p><b>القانون الأول:</b> \\(\\Delta U = q + w\\) (الطاقة محفوظة). عند ضغط ثابت: \\(\\Delta H = q\\).</p>'
        '<p><b>المحتوى الحراري:</b> \\(H = U + PV\\). \\(\\Delta H > 0\\) ماص للحرارة، \\(\\Delta H < 0\\) ناشر للحرارة.</p>'
        '<p><b>القانون الثاني:</b> الإنتروبي \\(S\\) يقيس الفوضى. \\(\\Delta S_{universe} > 0\\) للتفاعلات التلقائية.</p>'
        '<p><b>القانون الثالث:</b> \\(S = 0\\) عند 0 K للبلورة المثالية.</p>'),
    sec("طاقة جيبس الحرة", "Gibbs Free Energy", "吉布斯自由能",
        '<p>\\(G = H - TS\\)، \\(\\Delta G = \\Delta H - T\\Delta S\\)</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\\(\\Delta H\\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\\(\\Delta S\\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">النتيجة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">- (ناشر)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+ (زيادة)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تلقائي عند كل درجات الحرارة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+ (ماص)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">- (نقص)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">غير تلقائي أبداً</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">- (ناشر)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">- (نقص)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تلقائي في درجات الحرارة المنخفضة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+ (ماص)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+ (زيادة)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تلقائي في درجات الحرارة المرتفعة</td></tr>'
        '</table>'
        '<p>\\(\\Delta G^\\circ = -RT \\ln K\\) (تربط الديناميكا الحرارية بالاتزان). \\(\\Delta G < 0\\): تلقائي. \\(\\Delta G = 0\\): اتزان. \\(\\Delta G > 0\\): غير تلقائي.</p>'),
])

# ============================================================
# LESSON 10: chem_stoichiometry
# ============================================================
L10 = make_lesson("stoichiometry", "الحساب الكيميائي (الاستوكيومتريا)", "Stoichiometry", "化学计量学", [
    sec("موازنة المعادلات", "Balancing Equations", "配平方程式",
        '<p><b>موازنة المعادلة:</b> يجب أن يتساوى عدد ذرات كل عنصر في الطرفين. مثال: \\(2H_2 + O_2 \\rightarrow 2H_2O\\)</p>'
        '<p><b>خطوات الموازنة:</b></p>'
        '<ol><li>اكتب المواد المتفاعلة والناتجة.</li>'
        '<li>ابدأ بالعناصر التي تظهر في مركب واحد في كل طرف.</li>'
        '<li>استخدم معاملات عددية صحيحة.</li>'
        '<li>تحقق من موازنة الأكسجين والهيدروجين أخيراً.</li></ol>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المعادلة غير الموزونة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الموزونة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂ + O₂ → H₂O</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2H₂ + O₂ → 2H₂O</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Fe + O₂ → Fe₂O₃</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">4Fe + 3O₂ → 2Fe₂O₃</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₃H₈ + O₂ → CO₂ + H₂O</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₃H₈ + 5O₂ → 3CO₂ + 4H₂O</td></tr>'
        '</table>'),
    sec("المادة المحددة والمردود", "Limiting Reagent and Yield", "限量试剂",
        '<p><b>المادة المحددة (Limiting Reagent):</b> المادة التي تستهلك أولاً وتحدد كمية الناتج. تباعاً: تحول جميع المتفاعلات إلى مولات، استخدم النسبة المولية لمعرفة المحدد.</p>'
        '<p><b>المردود النظري:</b> أقصى كمية ناتج ممكنة (محسوبة من المادة المحددة).</p>'
        '<p><b>المردود الفعلي:</b> الكمية المحصلة عملياً (غالباً أقل من النظري).</p>'
        '<p><b>النسبة المئوية للمردود:</b> \\(\\% \\text{ yield} = \\frac{\\text{actual}}{\\text{theoretical}} \\times 100\\)</p>'),
    sec("العلاقات المولية", "Mole Relationships", "摩尔关系",
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التحويل</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الطريقة</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كتلة → مولات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(n = m/M\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مولات → كتلة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(m = n \\times M\\)</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مولات A → مولات B</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النسبة المولية من المعادلة</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مولات → جسيمات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\\(N = n \\times N_A\\)</td></tr>'
        '</table>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> وازن: Fe + O₂ → Fe₂O₃.</p>'
        '<p><b>الحل:</b> 4Fe + 3O₂ → 2Fe₂O₃</p>'
        '<p><b>مثال 2:</b> كم مولاً من CO₂ ينتج من حرق 2 mol من C₃H₈؟</p>'
        '<p><b>الحل:</b> \\(C_3H_8 + 5O_2 \\rightarrow 3CO_2 + 4H_2O\\). \\(n_{CO2} = 2 \\times 3 = 6\\) mol.</p>'
        '<p><b>مثال 3:</b> يتفاعل 10 g من H₂ مع excess O₂. كم g من H₂O ينتج؟</p>'
        '<p><b>الحل:</b> \\(n_{H2} = 10/2 = 5\\) mol. \\(2H_2 + O_2 \\rightarrow 2H_2O\\). \\(n_{H2O} = 5\\) mol. \\(m_{H2O} = 5 \\times 18 = 90\\) g.</p>'),
])

# ============================================================
# LESSON 11: chem_thermochemistry
# ============================================================
L11 = make_lesson("thermochemistry", "الكيمياء الحرارية", "Thermochemistry", "热化学", [
    sec("المحتوى الحراري وقانون هس", "Enthalpy and Hess\'s Law", "焓和盖斯定律",
        '<p><b>\\(\\Delta H\\)</b>: التغير في المحتوى الحراري (حرارة التفاعل عند ضغط ثابت). \\(\\Delta H > 0\\): ماص للحرارة (Endothermic). \\(\\Delta H < 0\\): ناشر للحرارة (Exothermic).</p>'
        '<p><b>قانون هس (Hess\'s Law):</b> \\(\\Delta H\\) للتفاعل الكلي = مجموع \\(\\Delta H\\) للتفاعلات الجزئية، بغض النظر عن المسار.</p>'
        '<p><b>حرارة التكوين القياسية \\(\\Delta H_f^\\circ\\):</b> \\(\\Delta H\\) لتكوين 1 mol من مركب من عناصره في حالتها القياسية. \\(\\Delta H_{rxn}^\\circ = \\sum \\Delta H_f^\\circ(products) - \\sum \\Delta H_f^\\circ(reactants)\\)</p>'
        '<table style="width:100%; border-collapse:collapse; margin:15px 0;">'
        '<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المركب</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\\(\\Delta H_f^\\circ\\) (kJ/mol)</th></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H₂O(l)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-285.8</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CO₂(g)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-393.5</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">CH₄(g)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-74.8</td></tr>'
        '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C₂H₅OH(l)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-277.7</td></tr>'
        '</table>'),
    sec("المسعرية والحرارة النوعية", "Calorimetry and Specific Heat", "量热学和比热容",
        '<p><b>الحرارة النوعية \\(c\\):</b> كمية الحرارة لرفع 1 g بمقدار 1°C. الماء: \\(c = 4.184 \\text{ J/g·°C}\\).</p>'
        '<p><b>القانون الأساسي:</b> \\(q = m \\times c \\times \\Delta T\\)</p>'
        '<p><b>المسعر (Calorimeter):</b> جهاز لقياس انتقال الحرارة.</p>'
        '<ul><li><b>مسعر القنبلة (Bomb Calorimeter):</b> حجم ثابت → \\(q = \\Delta U\\)</li>'
        '<li><b>مسعر بسيط (Coffee Cup):</b> ضغط ثابت → \\(q = \\Delta H\\)</li></ul>'
        '<p><b>قانون حفظ الطاقة في المسعر:</b> \\(q_{system} + q_{surroundings} = 0\\)</p>'),
    sec("الإنتروبي والتلقائية", "Entropy and Spontaneity", "熵和自发性",
        '<p><b>الإنتروبي \\(S\\):</b> مقياس العشوائية أو الفوضى. \\(\\Delta S > 0\\): زيادة في العشوائية. \\(\\Delta S < 0\\): نقصان.</p>'
        '<p><b>العوامل المؤثرة على \\(\\Delta S\\):</b></p>'
        '<ul><li>تغير الحالة: صلب < سائل < غاز (\\(S_{gas} \\gg S_{liquid} > S_{solid}\\))</li>'
        '<li>زيادة عدد جسيمات الغاز تزيد \\(\\Delta S\\)</li>'
        '<li>رفع درجة الحرارة يزيد \\(S\\)</li></ul>'
        '<p><b>طاقة جيبس الحرة:</b> \\(\\Delta G = \\Delta H - T\\Delta S\\). \\(\\Delta G < 0\\): تلقائي. \\(\\Delta G = 0\\): اتزان.</p>'),
    sec("أمثلة محلولة", "Solved Examples", "例题",
        '<p><b>مثال 1:</b> احسب \\(\\Delta H\\) لحرق الميثان: \\(CH_4 + 2O_2 \\rightarrow CO_2 + 2H_2O\\). \\(\\Delta H_f^\\circ(CH_4)=-74.8, CO_2=-393.5, H_2O=-285.8\\).</p>'
        '<p><b>الحل:</b> \\(\\Delta H = [(-393.5) + 2(-285.8)] - [(-74.8) + 0] = -965.1 + 74.8 = -890.3 \\text{ kJ/mol}\\)</p>'
        '<p><b>مثال 2:</b> سخنت 50 g ماء من 25°C إلى 75°C. احسب \\(q\\). (c=4.184 J/g·°C)</p>'
        '<p><b>الحل:</b> \\(q = 50 \\times 4.184 \\times (75-25) = 50 \\times 4.184 \\times 50 = 10460 \\text{ J} = 10.46 \\text{ kJ}\\)</p>'
        '<p><b>مثال 3:</b> تفاعل \\(\\Delta H = +100 \\text{ kJ}\\), \\(\\Delta S = +200 \\text{ J/K}\\). عند أي درجة حرارة يصبح تلقائياً؟</p>'
        '<p><b>الحل:</b> يصبح تلقائياً عندما \\(\\Delta G < 0\\): \\(T > \\Delta H/\\Delta S = 100000/200 = 500 K\\).</p>'),
])

# =============== Apply all replacements ===============
lessons = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11]

for lesson_obj in lessons:
    lid = lesson_obj["id"]
    for i, item in enumerate(data):
        if item.get("id") == lid:
            data[i] = lesson_obj
            break
    else:
        print(f"WARNING: {lid} not found in data, appending")
        data.append(lesson_obj)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All 11 chemistry lessons updated!")
print("File is valid JSON!")

# Verify
with open(PATH, "r", encoding="utf-8") as f:
    verify = json.load(f)
    for item in verify:
        lid = item.get("id", "")
        if lid.startswith("chem_"):
            secs = item.get("sections", [])
            total_chars = sum(len(s.get("content_ar", "")) for s in secs)
            print(f"{lid}: {len(secs)} sections, ~{total_chars} chars")
