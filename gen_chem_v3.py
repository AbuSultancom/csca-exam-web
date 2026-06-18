#!/usr/bin/env python3
"""Build chemistry lessons content and save to content.json"""
import json

PATH = "C:/Users/alyhy/csca-exam-web/data/content.json"

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# SVG definitions as raw strings to avoid escaping issues
SVG = {}

SVG["atom"] = '<svg width="350" height="180" viewBox="0 0 350 180"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">تركيب الذرة</text><circle cx="175" cy="100" r="15" fill="rgba(247,37,133,0.3)" stroke="#f72585" stroke-width="2"/><text x="175" y="104" fill="#f72585" font-size="10" text-anchor="middle" font-weight="bold">نواة</text><ellipse cx="175" cy="100" rx="70" ry="30" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="175" cy="100" rx="110" ry="45" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><circle cx="120" cy="68" r="5" fill="#2ed573"/><circle cx="230" cy="72" r="5" fill="#2ed573"/><circle cx="100" cy="130" r="5" fill="#2ed573"/><circle cx="250" cy="128" r="5" fill="#2ed573"/><text x="105" y="45" fill="#2ed573" font-size="10">e\u207b</text><text x="230" y="58" fill="#2ed573" font-size="10">e\u207b</text></svg>'

SVG["orbitals"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">أشكال المدارات الذرية</text><circle cx="70" cy="80" r="30" fill="none" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="120" fill="#4cc9f0" font-size="11" text-anchor="middle">s</text><ellipse cx="175" cy="65" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><ellipse cx="175" cy="95" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><text x="175" y="120" fill="#f72585" font-size="11" text-anchor="middle">p</text><ellipse cx="285" cy="65" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2"/><ellipse cx="285" cy="95" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2" transform="rotate(45,285,80)"/><text x="285" y="120" fill="#2ed573" font-size="11" text-anchor="middle">d</text></svg>'

SVG["ionic"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة الأيونية (NaCl)</text><circle cx="120" cy="70" r="25" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">Na+</text><circle cx="240" cy="70" r="30" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/><text x="240" y="74" fill="#f72585" font-size="14" text-anchor="middle">Cl-</text><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">Na + Cl \u2192 Na+ + Cl-</text><text x="175" y="125" fill="#fff" font-size="9" text-anchor="middle">انتقال إلكترون من Na إلى Cl</text></svg>'

SVG["vsepr"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">الأشكال الهندسية VSEPR</text><circle cx="70" cy="80" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="84" fill="#4cc9f0" font-size="9" text-anchor="middle">خطي 180\u00b0</text><circle cx="175" cy="80" r="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/><text x="175" y="84" fill="#f72585" font-size="9" text-anchor="middle">مثلث 120\u00b0</text><circle cx="285" cy="80" r="25" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/><text x="285" y="84" fill="#2ed573" font-size="9" text-anchor="middle">رباعي 109.5\u00b0</text></svg>'

SVG["equilibrium"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">منحنى الاتزان الكيميائي</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="2"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="2"/><path d="M 30 110 Q 80 30 160 60 Q 250 90 320 60" fill="none" stroke="#4cc9f0" stroke-width="2.5"/><path d="M 30 30 Q 80 90 160 60 Q 250 40 320 70" fill="none" stroke="#f72585" stroke-width="2.5"/><text x="160" y="55" fill="#fff" font-size="9" text-anchor="middle">اتزان</text><line x1="160" y1="60" x2="160" y2="130" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="4,3"/><text x="160" y="138" fill="#2ed573" font-size="9" text-anchor="middle">الزمن</text><text x="18" y="70" fill="#fff" font-size="9" text-anchor="middle" transform="rotate(-90,18,70)">التركيز</text></svg>'

SVG["potential"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">مخطط طاقة التفاعل</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="50" y1="120" x2="70" y2="20" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="20" x2="70" y2="100" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="100" x2="300" y2="50" stroke="#f72585" stroke-width="2.5"/><line x1="300" y1="50" x2="320" y2="120" stroke="#f72585" stroke-width="2.5"/><line x1="160" y1="20" x2="160" y2="100" stroke="#2ed573" stroke-width="2" stroke-dasharray="4,2"/><text x="165" y="58" fill="#2ed573" font-size="10" text-anchor="middle">Ea</text><text x="70" y="130" fill="#4cc9f0" font-size="9" text-anchor="middle">متفاعلات</text><text x="300" y="138" fill="#f72585" font-size="9" text-anchor="middle">نواتج</text></svg>'

SVG["kinetics"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">منحنيات الرتب المختلفة</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="40" x2="320" y2="40" stroke="#4cc9f0" stroke-width="2"/><text x="280" y="38" fill="#4cc9f0" font-size="9" text-anchor="middle">الرتبة 0</text><line x1="30" y1="100" x2="180" y2="40" stroke="#f72585" stroke-width="2"/><text x="200" y="55" fill="#f72585" font-size="9" text-anchor="middle">الرتبة 1</text><path d="M 30 30 Q 120 30 180 100 Q 250 140 320 145" fill="none" stroke="#2ed573" stroke-width="2"/><text x="280" y="120" fill="#2ed573" font-size="9" text-anchor="middle">الرتبة 2</text><text x="18" y="70" fill="#fff" font-size="9" text-anchor="middle" transform="rotate(-90,18,70)">[A]</text><text x="175" y="138" fill="#fff" font-size="9" text-anchor="middle">الزمن</text></svg>'

SVG["ecell"] = '<svg width="350" height="160" viewBox="0 0 350 160"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">خلية كلفانية</text><rect x="20" y="30" width="100" height="100" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2" rx="5"/><text x="70" y="55" fill="#4cc9f0" font-size="10" text-anchor="middle">Zn | Zn2+</text><text x="70" y="80" fill="#fff" font-size="9" text-anchor="middle">Zn \u2192 Zn2+ + 2e-</text><text x="70" y="110" fill="#4cc9f0" font-size="9" text-anchor="middle">(\u0623\u0646\u0648\u062f: \u062a\u0623\u0643\u0633\u062f)</text><rect x="230" y="30" width="100" height="100" fill="rgba(247,37,133,0.08)" stroke="#f72585" stroke-width="2" rx="5"/><text x="280" y="55" fill="#f72585" font-size="10" text-anchor="middle">Cu2+ | Cu</text><text x="280" y="80" fill="#fff" font-size="9" text-anchor="middle">Cu2+ + 2e- \u2192 Cu</text><text x="280" y="110" fill="#f72585" font-size="9" text-anchor="middle">(\u0643\u0627\u062b\u0648\u062f: \u0627\u062e\u062a\u0632\u0627\u0644)</text><line x1="120" y1="50" x2="230" y2="50" stroke="#2ed573" stroke-width="2"/><text x="175" y="48" fill="#2ed573" font-size="9" text-anchor="middle">e-</text><rect x="145" y="85" width="60" height="30" fill="rgba(46,213,115,0.1)" stroke="#2ed573" stroke-width="1.5" rx="3"/><text x="175" y="103" fill="#2ed573" font-size="8" text-anchor="middle">\u062c\u0633\u0631 \u0645\u0644\u062d\u064a</text></svg>'

SVG["benzene"] = '<svg width="200" height="140" viewBox="0 0 200 140"><text x="100" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0627\u0644\u0628\u0646\u0632\u064a\u0646 (C\u2086H\u2086)</text><polygon points="100,30 150,60 150,100 100,130 50,100 50,60" fill="rgba(76,201,240,0.1)" stroke="#4cc9f0" stroke-width="2"/><circle cx="100" cy="80" r="20" fill="none" stroke="#f72585" stroke-width="1.5" stroke-dasharray="4,3"/><text x="152" y="63" fill="#fff" font-size="9">H</text><text x="152" y="105" fill="#fff" font-size="9">H</text><text x="48" y="105" fill="#fff" font-size="9">H</text><text x="48" y="63" fill="#fff" font-size="9">H</text><text x="100" y="28" fill="#fff" font-size="9">H</text><text x="100" y="138" fill="#fff" font-size="9">H</text></svg>'

SVG["energy"] = '<svg width="350" height="140" viewBox="0 0 350 140"><rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/><text x="175" y="30" fill="#2ed573" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u0633\u062a\u0648\u064a\u0627\u062a \u0627\u0644\u0637\u0627\u0642\u0629 (\u0630\u0631\u0629 \u0627\u0644\u0647\u064a\u062f\u0631\u0648\u062c\u064a\u0646)</text><text x="175" y="52" fill="#fff" font-size="10" text-anchor="middle">n=1: E = -13.6 eV</text><text x="175" y="68" fill="#fff" font-size="10" text-anchor="middle">n=2: E = -3.40 eV</text><text x="175" y="84" fill="#fff" font-size="10" text-anchor="middle">n=3: E = -1.51 eV</text><text x="175" y="100" fill="#fff" font-size="10" text-anchor="middle">n=\u221e: E = 0 eV (\u062a\u0623\u064a\u0646)</text><text x="175" y="122" fill="#2ed573" font-size="9" text-anchor="middle">\u0627\u0644\u0641\u0631\u0642 = 13.6 eV</text></svg>'

# Build lessons as JSON-compatible dicts
def mk_sections(sections_data):
    """Convert list of (ar_heading, en_heading, zh_heading, content) tuples to sections"""
    result = []
    for h_ar, h_en, h_zh, content in sections_data:
        result.append({
            "heading_ar": h_ar,
            "heading_en": h_en,
            "heading_zh": h_zh,
            "content_ar": content,
            "content_en": "",
            "content_zh": ""
        })
    return result

def mk_lesson(topic, title_ar, title_en, title_zh, sections_data):
    return {
        "id": "chem_" + topic,
        "topic": topic,
        "subject": "كيمياء | Chemistry",
        "subject_en": "Chemistry",
        "title_ar": title_ar,
        "title_en": title_en,
        "title_zh": title_zh,
        "sections": mk_sections(sections_data)
    }

# MathJax helpers
L = lambda x: "\\(%s\\)" % x
R = lambda x: "\\" + x  # For LaTeX commands

# Build the HTML content strings
# Lesson 1: chem_atomic
L1_secs = [
    ("مكونات الذرة - تعريفات أساسية", "Atomic Components", "原子组成",
     '<p><b>الذرة</b> (Atom) هي أصغر وحدة بنائية للمادة. تتكون من <b>نواة</b> (بروتونات موجبة + نيوترونات متعادلة) وإلكترونات سالبة تدور حولها.</p>'
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الجسيم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشحنة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الكتلة (kg)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الموقع</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بروتون (p+)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">+1.602e-19 C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.673e-27</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النواة</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نيوترون (n0)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1.675e-27</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النواة</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إلكترون (e-)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-1.602e-19 C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">9.109e-31</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حول النواة</td></tr>'
     '</table>'
     '<p><b>العدد الذري</b> Z = عدد البروتونات. <b>العدد الكتلي</b> A = بروتونات + نيوترونات. <b>النظائر</b>: نفس Z (نفس العنصر) لكن A مختلف (نيوترونات مختلفة). مثال: ' + L('^{12}_{6}C') + ' و ' + L('^{14}_{6}C') + '.</p>'
     + SVG["atom"]),
    ("التوزيع الإلكتروني", "Electron Configuration", "电子排布",
     '<p>تملأ الإلكترونات المدارات حسب <b>مبدأ أوفباو</b> (من الأقل طاقة للأعلى): ' + L('1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s \\rightarrow 3d \\rightarrow 4p \\rightarrow 5s...') + '</p>'
     '<p><b>قاعدة هوند</b>: تملأ الإلكترونات المدارات المتكافئة منفردة أولاً. مثال: النيتروجين (Z=7): ' + L('1s^2 2s^2 2p^3') + '</p>'
     '<p><b>مبدأ باولي</b>: لا يمكن لإلكترونين أن يكون لهما نفس أعداد الكم الأربعة. كل مدار يسع إلكترونين فقط.</p>'
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">العنصر</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">Z</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التوزيع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">تكافؤ</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">H</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('1s^1') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">6</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('1s^2 2s^2 2p^2') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">4</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Fe</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">26</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('[Ar] 3d^6 4s^2') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2</td></tr>'
     '</table>'),
    ("أعداد الكم", "Quantum Numbers", "量子数",
     '<p>أربعة أعداد كم تصف حالة كل إلكترون:</p>'
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">عدد الكم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القيم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المعنى</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرئيسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('n') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1,2,3,...</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مستوى الطاقة</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الثانوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('l') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">0...n-1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">شكل المدار</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المغناطيسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('m_l') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">-l...+l</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اتجاه المدار</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المغزلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('m_s') + '</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\u00b1\u00bd</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اتجاه الدوران</td></tr>'
     '</table>'
     '<p>l=0 (s) كروي، l=1 (p) دمبلي، l=2 (d) معقد. عدد المدارات = ' + L('2l+1') + '.</p>'
     + SVG["orbitals"]),
    ("الجدول الدوري والخواص الدورية", "Periodic Table", "周期表",
     '<p><b>الدورة</b> (Period): صف أفقي = مستوى الطاقة الرئيسي. <b>المجموعة</b> (Group): عمود رأسي = نفس عدد إلكترونات التكافؤ.</p>'
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">في الدورة \u2192</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">في المجموعة \u2193</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نصف القطر الذري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يتناقص</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يزداد</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">طاقة التأين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تزداد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تتناقص</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">السالبية الكهربائية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تزداد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تتناقص</td></tr>'
     '</table>'
     '<p><b>أهم المجموعات:</b> 1 (قلوية): نشيطة جداً. 17 (هالوجينات): لا فلزات نشيطة. 18 (نبيلة): خاملة. العناصر الانتقالية: حالات تأكسد متعددة، أملاح ملونة.</p>'),
    ("قوانين وصيغ أساسية", "Key Formulas", "关键公式",
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العدد الذري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('Z = p^+') + '</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العدد الكتلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('A = Z + N') + '</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الكتلة الذرية النسبية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('A_r = \\frac{\\sum (m \\times \\%)}{100}') + '</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">طاقة المستوى (H)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">' + L('E_n = -\\frac{13.6}{n^2} \\text{ eV}') + '</td></tr>'
     '</table>'
     + SVG["energy"]),
    ("أمثلة محلولة", "Solved Examples", "例题",
     '<p><b>مثال 1:</b> ذرة Z=17, A=35. جد عدد p+, n0, e-.</p>'
     '<p><b>الحل:</b> p+=17, e-=17, n0 = 35-17 = 18.</p>'
     '<p><b>مثال 2:</b> للكلور نظيران: ' + L('^{35}_{17}Cl') + ' (75.77%) و ' + L('^{37}_{17}Cl') + ' (24.23%). جد الكتلة الذرية النسبية.</p>'
     '<p><b>الحل:</b> ' + L('A_r = \\frac{35\\times75.77 + 37\\times24.23}{100} = 35.48') + '</p>'
     '<p><b>مثال 3:</b> توزيع الأكسجين (Z=8) وعدد تكافؤه.</p>'
     '<p><b>الحل:</b> ' + L('1s^2 2s^2 2p^4') + ' \u2192 6 إلكترونات تكافؤ.</p>'
     '<p><b>مثال 4:</b> أعداد الكم لإلكترون في مدار 3p.</p>'
     '<p><b>الحل:</b> n=3, l=1, ml\u2208{-1,0,+1}, ms=\u00b1\u00bd. مثال: (3,1,0,+1/2).</p>'
     '<p><b>مثال 5:</b> رتب Li, Na, K, Rb حسب نصف القطر الذري.</p>'
     '<p><b>الحل:</b> Li < Na < K < Rb (يزداد نصف القطر بالنزول في المجموعة).</p>'),
    ("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
     '<p><b>نصائح:</b></p><ul><li>Z = عدد البروتونات = عدد الإلكترونات في الذرة المتعادلة</li>'
     '<li>النظائر: نفس Z لكن A مختلف</li>'
     '<li>' + L('4s') + ' يملأ قبل ' + L('3d') + ' (أوفباو)</li>'
     '<li>أعلى سالبية كهربائية للفلور (F) = 4.0</li></ul>'
     '<p><b>أخطاء شائعة:</b></p>'
     '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين Z و A</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Z = بروتونات، A = بروتونات + نيوترونات</td></tr>'
     '<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">3d قبل 4s</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">4s يملأ أولاً (طاقة أقل)</td></tr>'
     '</table>'),
]

L1 = mk_lesson("atomic", "البناء الذري", "Atomic Structure", "原子结构", L1_secs)

# Replace
for i, item in enumerate(data):
    if item.get("id") == "chem_atomic":
        data[i] = L1
        break

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
with open(PATH, "r", encoding="utf-8") as f:
    verify = json.load(f)
    for item in verify:
        if item.get("id") == "chem_atomic":
            n = len(item.get("sections", []))
            ch = sum(len(s.get("content_ar","")) for s in item["sections"])
            print("chem_atomic: %d sections, ~%d chars - VALID" % (n, ch))
            break
