#!/usr/bin/env python3
"""Build all chemistry content directly into content.json"""
import json
import sys

PATH = "C:/Users/alyhy/csca-exam-web/data/content.json"

# Read existing data
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Helper: L wraps text in MathJax inline
def L(s):
    return "\\(%s\\)" % s

# SVG assets (minified inline SVGs)
S = {}
S["atom"] = '<svg width="350" height="180" viewBox="0 0 350 180"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">تركيب الذرة (نموذج رذرفورد)</text><circle cx="175" cy="100" r="15" fill="rgba(247,37,133,0.3)" stroke="#f72585" stroke-width="2"/><text x="175" y="104" fill="#f72585" font-size="10" text-anchor="middle" font-weight="bold">نواة</text><ellipse cx="175" cy="100" rx="70" ry="30" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="175" cy="100" rx="110" ry="45" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><circle cx="120" cy="68" r="5" fill="#2ed573"/><circle cx="230" cy="72" r="5" fill="#2ed573"/><circle cx="100" cy="130" r="5" fill="#2ed573"/><circle cx="250" cy="128" r="5" fill="#2ed573"/><circle cx="145" cy="52" r="5" fill="#2ed573"/><circle cx="205" cy="145" r="5" fill="#2ed573"/><text x="105" y="45" fill="#2ed573" font-size="10">e⁻</text><text x="230" y="58" fill="#2ed573" font-size="10">e⁻</text><text x="85" y="152" fill="#2ed573" font-size="10">e⁻</text></svg>'
S["orbitals"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">أشكال المدارات الذرية</text><circle cx="70" cy="80" r="30" fill="none" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="120" fill="#4cc9f0" font-size="11" text-anchor="middle">s</text><ellipse cx="175" cy="65" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><ellipse cx="175" cy="95" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><text x="175" y="120" fill="#f72585" font-size="11" text-anchor="middle">p</text><ellipse cx="285" cy="65" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2"/><ellipse cx="285" cy="95" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2" transform="rotate(45,285,80)"/><text x="285" y="120" fill="#2ed573" font-size="11" text-anchor="middle">d</text></svg>'
S["ionic"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة الأيونية (NaCl)</text><circle cx="120" cy="70" r="25" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">Na+</text><circle cx="240" cy="70" r="30" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/><text x="240" y="74" fill="#f72585" font-size="14" text-anchor="middle">Cl-</text><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">Na + Cl \u2192 Na+ + Cl-</text><text x="175" y="125" fill="#fff" font-size="9" text-anchor="middle">\u0627\u0646\u062a\u0642\u0627\u0644 \u0625\u0644\u0643\u062a\u0631\u0648\u0646 \u0645\u0646 Na \u0625\u0644\u0649 Cl</text></svg>'
S["covalent"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة التساهمية (H\u2082)</text><circle cx="120" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><circle cx="230" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="230" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><line x1="140" y1="70" x2="210" y2="70" stroke="#f72585" stroke-width="3"/><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">\u0645\u0634\u0627\u0631\u0643\u0629 \u0632\u0648\u062c \u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a \u0628\u064a\u0646 \u0630\u0631\u062a\u064a H</text></svg>'
S["vsepr"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0627\u0644\u0623\u0634\u0643\u0627\u0644 \u0627\u0644\u0647\u0646\u062f\u0633\u064a\u0629 VSEPR</text><circle cx="70" cy="80" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="84" fill="#4cc9f0" font-size="9" text-anchor="middle">\u062e\u0637\u064a 180\u00b0</text><circle cx="175" cy="80" r="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/><text x="175" y="84" fill="#f72585" font-size="9" text-anchor="middle">\u0645\u062b\u0644\u062b 120\u00b0</text><circle cx="285" cy="80" r="25" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/><text x="285" y="84" fill="#2ed573" font-size="9" text-anchor="middle">\u0631\u0628\u0627\u0639\u064a 109.5\u00b0</text></svg>'
S["equilibrium"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u0646\u062d\u0646\u0649 \u0627\u0644\u0627\u062a\u0632\u0627\u0646 \u0627\u0644\u0643\u064a\u0645\u064a\u0627\u0626\u064a</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="2"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="2"/><path d="M 30 110 Q 80 30 160 60 Q 250 90 320 60" fill="none" stroke="#4cc9f0" stroke-width="2.5"/><path d="M 30 30 Q 80 90 160 60 Q 250 40 320 70" fill="none" stroke="#f72585" stroke-width="2.5"/><text x="160" y="55" fill="#fff" font-size="9" text-anchor="middle">\u0627\u062a\u0632\u0627\u0646</text><line x1="160" y1="60" x2="160" y2="130" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="4,3"/><text x="160" y="138" fill="#2ed573" font-size="9" text-anchor="middle">\u0627\u0644\u0632\u0645\u0646</text><text x="18" y="70" fill="#fff" font-size="9" text-anchor="middle" transform="rotate(-90,18,70)">\u0627\u0644\u062a\u0631\u0643\u064a\u0632</text></svg>'
S["potential"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u062e\u0637\u0637 \u0637\u0627\u0642\u0629 \u0627\u0644\u062a\u0641\u0627\u0639\u0644</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="50" y1="120" x2="70" y2="20" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="20" x2="70" y2="100" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="100" x2="300" y2="50" stroke="#f72585" stroke-width="2.5"/><line x1="300" y1="50" x2="320" y2="120" stroke="#f72585" stroke-width="2.5"/><line x1="160" y1="20" x2="160" y2="100" stroke="#2ed573" stroke-width="2" stroke-dasharray="4,2"/><text x="165" y="58" fill="#2ed573" font-size="10">Ea</text><text x="70" y="130" fill="#4cc9f0" font-size="9" text-anchor="middle">reactants</text><text x="300" y="135" fill="#f72585" font-size="9" text-anchor="middle">products</text></svg>'
S["kinetics"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u0646\u062d\u0646\u064a\u0627\u062a \u0627\u0644\u0631\u062a\u0628 \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="40" x2="320" y2="40" stroke="#4cc9f0" stroke-width="2"/><text x="270" y="38" fill="#4cc9f0" font-size="9">\u0627\u0644\u0631\u062a\u0628\u0629 0</text><line x1="30" y1="100" x2="180" y2="40" stroke="#f72585" stroke-width="2"/><text x="200" y="55" fill="#f72585" font-size="9">\u0627\u0644\u0631\u062a\u0628\u0629 1</text><path d="M 30 30 Q 120 30 180 100 Q 250 140 320 145" fill="none" stroke="#2ed573" stroke-width="2"/><text x="270" y="120" fill="#2ed573" font-size="9">\u0627\u0644\u0631\u062a\u0628\u0629 2</text><text x="18" y="70" fill="#fff" font-size="9" text-anchor="middle" transform="rotate(-90,18,70)">[A]</text><text x="175" y="138" fill="#fff" font-size="9" text-anchor="middle">t</text></svg>'
S["ecell"] = '<svg width="350" height="160" viewBox="0 0 350 160"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u062e\u0644\u064a\u0629 \u0643\u0644\u0641\u0627\u0646\u064a\u0629</text><rect x="20" y="30" width="100" height="100" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2" rx="5"/><text x="70" y="55" fill="#4cc9f0" font-size="10" text-anchor="middle">Zn | Zn2+</text><text x="70" y="80" fill="#fff" font-size="9" text-anchor="middle">Zn \u2192 Zn2+ + 2e-</text><text x="70" y="110" fill="#4cc9f0" font-size="9" text-anchor="middle">(-) \u0623\u0646\u0648\u062f</text><rect x="230" y="30" width="100" height="100" fill="rgba(247,37,133,0.08)" stroke="#f72585" stroke-width="2" rx="5"/><text x="280" y="55" fill="#f72585" font-size="10" text-anchor="middle">Cu2+ | Cu</text><text x="280" y="80" fill="#fff" font-size="9" text-anchor="middle">Cu2+ + 2e- \u2192 Cu</text><text x="280" y="110" fill="#f72585" font-size="9" text-anchor="middle">(+) \u0643\u0627\u062b\u0648\u062f</text><line x1="120" y1="50" x2="230" y2="50" stroke="#2ed573" stroke-width="2"/><text x="175" y="48" fill="#2ed573" font-size="9">e-</text><rect x="145" y="85" width="60" height="30" fill="rgba(46,213,115,0.1)" stroke="#2ed573" stroke-width="1.5" rx="3"/><text x="175" y="103" fill="#2ed573" font-size="8" text-anchor="middle">\u062c\u0633\u0631 \u0645\u0644\u062d\u064a</text></svg>'
S["benzene"] = '<svg width="200" height="140" viewBox="0 0 200 140"><text x="100" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0627\u0644\u0628\u0646\u0632\u064a\u0646 (C\u2086H\u2086)</text><polygon points="100,30 150,60 150,100 100,130 50,100 50,60" fill="rgba(76,201,240,0.1)" stroke="#4cc9f0" stroke-width="2"/><circle cx="100" cy="80" r="20" fill="none" stroke="#f72585" stroke-width="1.5" stroke-dasharray="4,3"/><text x="152" y="63" fill="#fff" font-size="9">H</text><text x="152" y="105" fill="#fff" font-size="9">H</text><text x="48" y="105" fill="#fff" font-size="9">H</text><text x="48" y="63" fill="#fff" font-size="9">H</text><text x="100" y="28" fill="#fff" font-size="9">H</text><text x="100" y="138" fill="#fff" font-size="9">H</text></svg>'
S["energy"] = '<svg width="350" height="140" viewBox="0 0 350 140"><rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/><text x="175" y="30" fill="#2ed573" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u0633\u062a\u0648\u064a\u0627\u062a \u0627\u0644\u0637\u0627\u0642\u0629 (\u0630\u0631\u0629 H)</text><text x="175" y="52" fill="#fff" font-size="10" text-anchor="middle">n=1: E = -13.6 eV</text><text x="175" y="68" fill="#fff" font-size="10" text-anchor="middle">n=2: E = -3.40 eV</text><text x="175" y="84" fill="#fff" font-size="10" text-anchor="middle">n=3: E = -1.51 eV</text><text x="175" y="100" fill="#fff" font-size="10" text-anchor="middle">n=\u221e: E = 0 eV</text></svg>'

# Build HTML table helper
def T(headers, rows):
    h = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">%s</th>' % x for x in headers)
    r = "".join('<tr>%s</tr>' % "".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">%s</td>' % c for c in row) for row in rows)
    return '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);">%s</tr>%s</table>' % (h, r)

def UL(items):
    return "<ul>" + "".join("<li>%s</li>" % x for x in items) + "</ul>"

def MIST(headers, rows):
    h = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">%s</th>' % x for x in headers)
    r = "".join('<tr>%s</tr>' % "".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">%s</td>' % c for c in row) for row in rows)
    return '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(247,37,133,0.1);">%s</tr>%s</table>' % (h, r)

def sec(ar_h, en_h, zh_h, content):
    return {"heading_ar": ar_h, "heading_en": en_h, "heading_zh": zh_h, "content_ar": content, "content_en": "", "content_zh": ""}

def LSN(topic, title_ar, title_en, title_zh, sections):
    return {"id": "chem_"+topic, "topic": topic, "subject": "كيمياء | Chemistry", "subject_en": "Chemistry",
            "title_ar": title_ar, "title_en": title_en, "title_zh": title_zh, "sections": sections}

# Now define ALL 11 lessons

all_lessons = []

# ===== L1: atomic =====
all_lessons.append(LSN("atomic", "البناء الذري", "Atomic Structure", "原子结构", [
sec("مكونات الذرة", "Atomic Components", "原子组成",
'<p><b>الذرة</b> أصغر وحدة بنائية للمادة تحتفظ بالخواص الكيميائية. تتكون من نواة (بروتونات موجبة + نيوترونات متعادلة) وإلكترونات سالبة تدور حولها في مدارات محددة.</p>'
+T(["الجسيم","الشحنة","الكتلة (kg)","الموقع"],[["بروتون (p+)","+1.602e-19 C","1.673e-27","النواة"],["نيوترون (n0)","0","1.675e-27","النواة"],["إلكترون (e-)","-1.602e-19 C","9.109e-31","حول النواة"]])
+'<p><b>العدد الذري</b> Z = عدد البروتونات. <b>العدد الكتلي</b> A = بروتونات + نيوترونات. <b>النظائر</b>: ذرات لنفس العنصر (نفس Z) تختلف بعدد النيوترونات (A مختلف). مثال: '
+L('^{12}_{6}C')+' و '+L('^{14}_{6}C')+'.</p>'+S["atom"]),
sec("التوزيع الإلكتروني", "Electron Configuration", "电子排布",
'<p>تملأ الإلكترونات المدارات حسب <b>مبدأ أوفباو</b> (من الأقل طاقة للأعلى): '+L('1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s \\rightarrow 3d \\rightarrow 4p \\rightarrow 5s...')+'</p>'
+'<p><b>قاعدة هوند</b>: تملأ الإلكترونات المدارات المتكافئة منفردة أولاً. النيتروجين (N, Z=7): '+L('1s^2 2s^2 2p^3')+' (إلكترونات p منفردة).</p>'
+'<p><b>مبدأ باولي للاستبعاد</b>: لا يمكن لإلكترونين أن يكون لهما نفس أعداد الكم الأربعة. كل مدار لا يسع أكثر من إلكترونين (باتجاهي دوران متعاكسين).</p>'),
sec("أعداد الكم الأربعة", "Quantum Numbers", "量子数",
'<p><b>أعداد الكم</b> (Quantum Numbers) أربعة أعداد تصف حالة كل إلكترون فريداً:</p>'
+T(["عدد الكم","الرمز","القيم الممكنة","المعنى الفيزيائي"],
  [["الرئيسي",L('n'),"1, 2, 3, ...","مستوى الطاقة الرئيسي"],
   ["الثانوي (السمتي)",L('l'),"0, 1, ..., n-1","شكل المدار (s,p,d,f)"],
   ["المغناطيسي",L('m_l'),"-l, ..., 0, ..., +l","اتجاه المدار في الفضاء"],
   ["المغزلي",L('m_s'),"+½ أو -½","اتجاه دوران الإلكترون"]])
+'<p>l=0 (s) كروي، l=1 (p) دمبلي، l=2 (d) معقد، l=3 (f) أكثر تعقيداً. عدد المدارات لكل قيمة l هو '+L('2l+1')+'.</p>'+S["orbitals"]),
sec("الجدول الدوري والخواص الدورية", "Periodic Table", "周期表",
'<p><b>الدورة</b> (Period): صف أفقي يمثل مستوى الطاقة الرئيسي. <b>المجموعة</b> (Group): عمود رأسي، العناصر لها نفس عدد إلكترونات التكافؤ.</p>'
+T(["الخاصية","في الدورة ←","في المجموعة ↓"],[["نصف القطر الذري","يتناقص","يزداد"],["طاقة التأين","تزداد","تتناقص"],["السالبية الكهربائية","تزداد","تتناقص"],["الألفة الإلكترونية","تزداد","تتناقص"]])),
sec("القوانين والصيغ الأساسية", "Key Laws and Formulas", "关键公式",
+T(["القانون","الصيغة","الشرح"],[["العدد الذري",L('Z = p^+'),"يميز العنصر"],["العدد الكتلي",L('A = Z + N'),"p+ + n0"],["الكتلة الذرية النسبية",L('A_r = \\frac{\\sum (m \\times \\text{%})}{100}'),"متوسط النظائر"],["طاقة المستوى n (H)",L('E_n = -\\frac{13.6}{n^2} \\text{ eV}'),"لذرة الهيدروجين"],["الكتلة (amu)","1 amu = 1.66e-27 kg","1/12 كتلة C-12"]])+S["energy"]),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> ذرة عنصر عددها الذري 17 وعددها الكتلي 35. احسب عدد البروتونات والنيوترونات والإلكترونات.</p>'
+'<p><b>الحل:</b> Z=17 → بروتونات=17، إلكترونات=17. N = A-Z = 35-17 = 18 نيوتروناً.</p>'
+'<p><b>مثال 2:</b> للكلور نظيران: '+L('^{35}_{17}Cl')+' (75.77%) و '+L('^{37}_{17}Cl')+' (24.23%). احسب الكتلة الذرية النسبية.</p>'
+'<p><b>الحل:</b> '+L('A_r = \\frac{35 \\times 75.77 + 37 \\times 24.23}{100} = 35.48')+'</p>'
+'<p><b>مثال 3:</b> اكتب التوزيع الإلكتروني للأكسجين (Z=8) وحدد عدد إلكترونات التكافؤ.</p>'
+'<p><b>الحل:</b> '+L('1s^2 2s^2 2p^4')+' → إلكترونات التكافؤ (n=2): 6 إلكترونات.</p>'
+'<p><b>مثال 4:</b> ما أعداد الكم الأربعة لإلكترون في مدار 3p؟</p>'
+'<p><b>الحل:</b> n=3, l=1 (p), ml يمكن أن يكون -1, 0, أو +1, ms=+½ أو -½. مثال: (3,1,0,+½).</p>'
+'<p><b>مثال 5:</b> رتب حسب زيادة نصف القطر الذري: Li, Na, K, Rb.</p>'
+'<p><b>الحل:</b> جميعها في المجموعة 1. نصف القطر يزداد بالنزول: Li < Na < K < Rb.</p>'),
sec("نصائح وأخطاء شائعة", "Tips and Common Mistakes", "提示和错误",
'<p><b>نصائح هامة:</b></p>'+UL(["Z = عدد البروتونات = عدد الإلكترونات (ذرة متعادلة)","النظائر: نفس Z لكن A مختلف","4s يملأ قبل 3d (قاعدة أوفباو)","أعلى سالبية كهربائية للفلور (F) = 4.0"])
+'<p><b>أخطاء شائعة:</b></p>'+MIST(["الخطأ","التصحيح"],[["الخلط بين Z و A","Z = بروتونات، A = بروتونات + نيوترونات"],["اعتبار أن 3d يملأ قبل 4s","4s طاقة أقل ← يملأ أولاً"],["نسيان أن ml يعتمد على l","ml من -l إلى +l"]]))
]))

# ===== L2: bonding =====
all_lessons.append(LSN("bonding", "الروابط الكيميائية", "Chemical Bonding", "化学键", [
sec("أنواع الروابط الكيميائية", "Types of Bonds", "键的类型",
'<p><b>الرابطة الكيميائية</b> هي قوة تجذب ذرتين معاً لتكوين جزيء أو مركب. الأنواع الرئيسية:</p>'
+T(["النوع","الآلية","بين","مثال"],[["أيونية","انتقال إلكترونات","فلز + لا فلز","NaCl"],["تساهمية","مشاركة إلكترونات","لا فلز + لا فلز","H₂"],["فلزية","إلكترونات ممركزة","فلز + فلز","Fe"],["هيدروجينية","جذب H مع O,N,F","بين جزيئات","H₂O"]])+S["ionic"]+S["covalent"]),
sec("نظرية VSEPR", "VSEPR Theory", "VSEPR理论",
'<p><b>VSEPR</b>: أزواج الإلكترونات حول الذرة المركزية تتنافر فتتباعد بأكبر زاوية ممكنة.</p>'
+T(["الصيغة","الشكل","الزاوية","مثال"],[["AX₂","خطي","180°","CO₂"],["AX₃","مثلث مستوي","120°","BF₃"],["AX₄","رباعي أوجه","109.5°","CH₄"],["AX₃E","هرمي ثلاثي","107°","NH₃"],["AX₂E₂","منحني","104.5°","H₂O"]])+S["vsepr"]),
sec("التهجين والقطبية", "Hybridization and Polarity", "杂化和极性",
'<p><b>التهجين</b>: خلط مدارات ذرية لتكوين مدارات مهجنة متكافئة.</p>'
+T(["التهجين","المدارات","الشكل","الزاوية","مثال"],[["sp","s+p","خطي","180°","BeCl₂"],["sp²","s+2p","مثلث مستوي","120°","BF₃"],["sp³","s+3p","رباعي أوجه","109.5°","CH₄"]])
+'<p><b>قطبية الجزيء:</b> تعتمد على فرق السالبية الكهربائية وشكل الجزيء. CO₂ غير قطبي (خطي، العزم=0). H₂O قطبي (منحني، العزم≠0).</p>'),
sec("قوانين أساسية للروابط", "Key Bonding Laws", "化学键定律",
'<p><b>قاعدة الثمانية (Octet Rule):</b> تميل الذرات للوصول إلى 8 إلكترونات في غلافها الخارجي (ماعدا H: 2 إلكترون).</p>'
+T(["الرابطة","طول الرابطة (pm)","طاقة الرابطة (kJ/mol)"],[["C-C (أحادية)","154","348"],["C=C (ثنائية)","134","614"],["C≡C (ثلاثية)","121","839"],["H-H","74","436"],["O-H","96","463"]])),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> حدد نوع الرابطة في NaCl, H₂, CH₄.</p>'
+'<p><b>الحل:</b> NaCl أيونية، H₂ تساهمية أحادية، CH₄ تساهمية (روابط C-H).</p>'
+'<p><b>مثال 2:</b> ما الشكل الهندسي لـ NH₃ حسب VSEPR؟</p>'
+'<p><b>الحل:</b> NH₃: AX₃E → هرمي ثلاثي، زاوية 107°.</p>'
+'<p><b>مثال 3:</b> حدد تهجين الكربون في CH₄, C₂H₄, C₂H₂.</p>'
+'<p><b>الحل:</b> CH₄: sp³, C₂H₄: sp², C₂H₂: sp.</p>'
+'<p><b>مثال 4:</b> هل CO₂ قطبي أم لا؟</p>'
+'<p><b>الحل:</b> CO₂ خطي (O=C=O) → غير قطبي رغم قطبية كل رابطة C-O على حدة.</p>'),
sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
'<p><b>نصائح:</b></p>'+UL(["الأيونية: بين فلز ولا فلز (فرق سالبية كبير)","التساهمية: بين لا فلزات (فرق سالبية صغير)","قطبية الجزيء = تعتمد على الشكل + فرق السالبية"]))
]))

# ===== L3: equilibrium =====
all_lessons.append(LSN("equilibrium", "الاتزان الكيميائي والأحماض والقواعد", "Chemical Equilibrium", "化学平衡与酸碱", [
sec("ثابت الاتزان ومبدأ لوشاتيليه", "Equilibrium Constant", "平衡常数",
'<p>للتفاعل العكسي: '+L('aA + bB \\rightleftharpoons cC + dD')+'</p>'
+'<p><b>ثابت الاتزان:</b> '+L('K_c = \\frac{[C]^c[D]^d}{[A]^a[B]^b}')+'</p>'
+'<p>Kc يتغير فقط مع درجة الحرارة. إذا Kc > 1 فالنواتج مفضلة. المواد الصلبة والسوائل النقية لا تظهر في Kc (قيمتها 1).</p>'
+'<p><b>مبدأ لوشاتيليه:</b> إذا أثر تغيير على نظام في حالة اتزان، يزيح النظام اتزانه ليعاكس التغيير.</p>'
+T(["التغيير","اتجاه الإزاحة"],[["زيادة تركيز المتفاعلات","← نحو النواتج"],["زيادة الضغط","← نحو الجهة ذات المولات الأقل"],["رفع درجة الحرارة","← نحو الجهة الماصة للحرارة"]])+S["equilibrium"]),
sec("الأحماض والقواعد و pH", "Acids, Bases and pH", "酸碱和pH",
'<p><b>Arrhenius:</b> حمض = يعطي H⁺، قاعدة = تعطي OH⁻. <b>Brønsted-Lowry:</b> حمض = مانح بروتون (H⁺)، قاعدة = مستقبل بروتون.</p>'
+'<p>'+L('\\text{pH} = -\\log[H^+]')+'، '+L('\\text{pOH} = -\\log[OH^-]')+'، '+L('\\text{pH} + \\text{pOH} = 14')+' عند 25°C.</p>'
+T(["pH","[H+] (M)","الوصف"],[["0-2","1 - 10⁻²","حمض قوي"],["3-6","10⁻³ - 10⁻⁶","حمض ضعيف"],["7","10⁻⁷","متعادل"],["8-11","10⁻⁸ - 10⁻¹¹","قاعدة ضعيفة"],["12-14","10⁻¹² - 10⁻¹⁴","قاعدة قوية"]])
+'<p><b>الأحماض القوية:</b> HCl, HNO₃, H₂SO₄ (تتأين كلياً). <b>الأحماض الضعيفة:</b> CH₃COOH, HF (تتأين جزئياً).</p>'),
sec("المحاليل المنظمة (Buffers)", "Buffer Solutions", "缓冲溶液",
'<p><b>المحلول المنظم</b> يقاوم التغير في pH عند إضافة كميات صغيرة من حمض أو قاعدة. يتكون من حمض ضعيف وقاعدته المترافقة (مثل CH₃COOH/CH₃COONa) أو قاعدة ضعيفة وحمضها المترافق (مثل NH₃/NH₄Cl).</p>'
+'<p><b>معادلة هندر-هاسلباخ:</b> '+L('\\text{pH} = pK_a + \\log\\frac{[A^-]}{[HA]}')+'</p>'),
sec("منتجات الذوبان (Ksp)", "Solubility Products", "溶度积",
'<p>للمركب الشحيح الذوبان '+L('A_xB_y(s) \\rightleftharpoons xA^{y+} + yB^{x-}')+'</p>'
+'<p>'+L('K_{sp} = [A^{y+}]^x[B^{x-}]^y')+'</p>'
+T(["المركب","Ksp (25°C)"],[["AgCl","1.8×10⁻¹⁰"],["BaSO₄","1.1×10⁻¹⁰"],["CaCO₃","3.4×10⁻⁹"],["Fe(OH)₃","2.8×10⁻³⁹"]])),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> للتفاعل '+L('N_2 + 3H_2 \\rightleftharpoons 2NH_3')+'، التركيزات عند الاتزان: [N₂]=0.5M, [H₂]=1.0M, [NH₃]=0.8M. احسب Kc.</p>'
+'<p><b>الحل:</b> '+L('K_c = \\frac{[NH_3]^2}{[N_2][H_2]^3} = \\frac{0.8^2}{0.5 \\times 1.0^3} = \\frac{0.64}{0.5} = 1.28')+'</p>'
+'<p><b>مثال 2:</b> احسب pH لمحلول HCl تركيزه 0.01 M.</p>'
+'<p><b>الحل:</b> HCl حمض قوي → '+L('[H^+] = 0.01 M')+' → pH = -log(0.01) = 2.</p>'
+'<p><b>مثال 3:</b> احسب pH لمحلول NaOH تركيزه 0.001 M.</p>'
+'<p><b>الحل:</b> '+L('[OH^-] = 10^{-3} M')+' → pOH = 3 → pH = 14-3 = 11.</p>'
+'<p><b>مثال 4:</b> محلول منظم CH₃COOH/CH₃COONa بنسبة [A⁻]/[HA]=2, pKa=4.76. جد pH.</p>'
+'<p><b>الحل:</b> '+L('\\text{pH} = 4.76 + \\log(2) = 4.76 + 0.30 = 5.06')+'</p>'),
]))

# Add remaining lessons...
print("Debug: L1-L3 built, adding remaining...")

# ===== L4: kinetics =====
all_lessons.append(LSN("kinetics", "الحركية الكيميائية", "Chemical Kinetics", "化学动力学", [
sec("معدل التفاعل وقانون السرعة", "Reaction Rate", "反应速率",
'<p><b>معدل التفاعل</b> = '+L('-\\frac{\\Delta[A]}{\\Delta t}')+' (للمتفاعلات) أو '+L('+\\frac{\\Delta[B]}{\\Delta t}')+' (للنواتج). الوحدة: M/s.</p>'
+'<p><b>قانون السرعة:</b> '+L('\\text{rate} = k[A]^m[B]^n')+' حيث m,n رتب التفاعل (تحدد تجريبياً).</p>'
+T(["الرتبة","القانون التكاملي","الرسم الخطي"],[["0",L('[A] = -kt + [A]_0'),"[A] vs t"],["1",L('\\ln[A] = -kt + \\ln[A]_0'),"ln[A] vs t"],["2",L('\\frac{1}{[A]} = kt + \\frac{1}{[A]_0}'),"1/[A] vs t"]])+S["kinetics"]),
sec("طاقة التنشيط ومعادلة أرهينيوس", "Activation Energy", "活化能",
'<p><b>طاقة التنشيط Ea</b>: الحد الأدنى من الطاقة اللازمة لبدء التفاعل.</p>'
+'<p><b>معادلة أرهينيوس:</b> '+L('k = A \\cdot e^{-E_a/RT}')+' أو '+L('\\ln k = \\ln A - \\frac{E_a}{R} \\cdot \\frac{1}{T}')+'</p>'
+'<p><b>العامل المساعد (Catalyst):</b> يخفض Ea فيسرع التفاعل دون أن يستهلك. الإنزيمات محفزات حيوية تخفض Ea بشكل كبير.</p>'+S["potential"]),
sec("عمر النصف وآليات التفاعل", "Half-Life", "半衰期",
'<p><b>عمر النصف t₁/₂</b>: الزمن اللازم لانخفاض التركيز إلى النصف.</p>'
+T(["الرتبة","t₁/₂","ملاحظة"],[["0",L('[A]_0/2k'),"يعتمد على [A]₀"],["1",L('0.693/k'),"ثابت (لا يعتمد على التركيز)"],["2",L('1/(k[A]_0)'),"يعتمد على [A]₀"]]))]))

# ===== L5: basic =====
all_lessons.append(LSN("basic", "المفاهيم الأساسية في الكيمياء", "Basic Concepts", "化学基本概念", [
sec("المول وعدد أفوجادرو", "Mole", "摩尔",
'<p><b>المول</b>: كمية المادة التي تحتوي على عدد أفوجادرو من الوحدات.</p>'
+'<p>'+L('N_A = 6.022 \\times 10^{23} \\text{ particles/mol}')+'</p>'
+T(["المطلوب","الصيغة"],[["عدد المولات (n)",L('n = \\frac{m}{M}')],["عدد الجسيمات",L('N = n \\times N_A')],["حجم الغاز (STP)",L('V = n \\times 22.4 \\text{ L/mol}')]])),
sec("الكتلة الذرية والجزيئية", "Atomic Mass", "原子量",
'<p><b>الكتلة المولية</b> = كتلة 1 مول بوحدة g/mol.</p>'
+T(["المركب","الحساب","الكتلة المولية"],[["H₂O","2×1.008+16.00","18.016 g/mol"],["CO₂","12.01+2×16.00","44.01 g/mol"],["NaCl","22.99+35.45","58.44 g/mol"]])),
sec("قوانين الغازات", "Gas Laws", "气体定律",
+T(["القانون","الصيغة","الثابت"],[["بويل",L('P_1V_1 = P_2V_2'),"T, n"],["شارل",L('\\frac{V_1}{T_1} = \\frac{V_2}{T_2}'),"P, n"],["الغاز المثالي",L('PV = nRT'),"R=0.0821"]]))]))

# ===== L6: inorganic =====
all_lessons.append(LSN("inorganic", "الكيمياء غير العضوية", "Inorganic Chemistry", "无机化学", [
sec("الهالوجينات والفلزات القلوية", "Halogens", "卤素",
'<p><b>الهالوجينات</b> (المجموعة 17): F₂ (غاز أصفر)، Cl₂ (غاز أصفر-أخضر)، Br₂ (سائل بني)، I₂ (صلب بنفسجي). النشاط الكيميائي يقل كلما نزلنا في المجموعة.</p>'
+'<p><b>الفلزات القلوية</b> (المجموعة 1): تتفاعل بعنف مع الماء. '+L('2Na + 2H_2O \\rightarrow 2NaOH + H_2')+'. النشاط يزداد للنزول (Li < Na < K < Rb < Cs).</p>'),
sec("التفاعلات في المحاليل المائية", "Aqueous Reactions", "水溶液反应",
'<p><b>قواعد الذائبية:</b></p>'
+T(["الأيون","الذائبية","الاستثناءات"],[["NO₃⁻","كلها ذائبة","لا يوجد"],["Na⁺, K⁺","كلها ذائبة","لا يوجد"],["Cl⁻, Br⁻, I⁻","معظمها ذائبة","Ag⁺, Pb²⁺"],["SO₄²⁻","معظمها ذائبة","Ba²⁺, Pb²⁺"],["CO₃²⁻, PO₄³⁻","غير ذائبة","مع أيونات القلويات"]]))]))

# ===== L7: organic =====
all_lessons.append(LSN("organic", "الكيمياء العضوية", "Organic Chemistry", "有机化学", [
sec("الهيدروكربونات", "Hydrocarbons", "碳氢化合物",
+T(["النوع","الصيغة العامة","الرابطة","مثال"],[["ألكان",L('C_nH_{2n+2}'),"أحادية (σ)","CH₄"],["ألكين",L('C_nH_{2n}'),"ثنائية (σ+π)","C₂H₄"],["ألكاين",L('C_nH_{2n-2}'),"ثلاثية (σ+2π)","C₂H₂"],["أروماتي","C₆H₆","رنين","البنزين"]])+S["benzene"]),
sec("المجموعات الوظيفية", "Functional Groups", "官能团",
+T(["المجموعة","الصيغة","اللاحقة","مثال"],[["كحول","-OH","-ول","CH₃OH"],["ألدهيد","-CHO","-ال","CH₃CHO"],["كيتون",">C=O","-ون","CH₃COCH₃"],["حمض كربوكسيلي","-COOH","-حمض","CH₃COOH"],["إستر","-COO-","-وات","CH₃COOCH₃"],["أمين","-NH₂","-أمين","CH₃NH₂"]]))]))

# ===== L8: organic_cn =====
all_lessons.append(LSN("organic_cn", "الكيمياء العضوية - التسمية الصينية", "Chinese Nomenclature", "有机化学 - 中文命名", [
sec("التسمية بالصينية", "Chinese Naming", "中文命名",
'<p>في نظام التسمية الصيني للمركبات العضوية:</p>'
+T(["المجموعة","اللاحقة الصينية","مثال"],[["ألكان","-烷 (wán)","甲烷 CH₄"],["ألكين","-烯 (xī)","乙烯 C₂H₄"],["ألكاين","-炔 (quē)","乙炔 C₂H₂"],["كحول","-醇 (chún)","乙醇 C₂H₅OH"],["ألدهيد","-醛 (quán)","乙醛 CH₃CHO"],["حمض","-酸 (suān)","乙酸 CH₃COOH"]]))]))

# ===== L9: physical =====
all_lessons.append(LSN("physical", "الكيمياء الفيزيائية", "Physical Chemistry", "物理化学", [
sec("الكيمياء الكهربائية", "Electrochemistry", "电化学",
'<p><b>الخلايا الكلفانية</b>: تحول الطاقة الكيميائية إلى طاقة كهربائية. الأنود: يتأكسد (قطب سالب). الكاثود: يختزل (قطب موجب).</p>'
+'<p>'+L('E^\\circ_{cell} = E^\\circ_{cathode} - E^\\circ_{anode}')+'</p>'
+'<p><b>معادلة نرنست:</b> '+L('E = E^\\circ - \\frac{RT}{nF} \\ln Q')+'</p>'+S["ecell"]),
sec("الخواص التجميعية", "Colligative Properties", "依数性质",
+T(["الخاصية","القانون"],[["انخفاض ضغط البخار",L('P_1 = X_1P_1^\\circ')+" (راؤول)"],["ارتفاع درجة الغليان",L('\\Delta T_b = K_b \\times m \\times i')],["انخفاض درجة التجمد",L('\\Delta T_f = K_f \\times m \\times i')],["الضغط الأسموزي",L('\\pi = iMRT')]]))]))

# ===== L10: stoichiometry =====
all_lessons.append(LSN("stoichiometry", "الحساب الكيميائي (الاستوكيومتريا)", "Stoichiometry", "化学计量学", [
sec("موازنة المعادلات", "Balancing", "配平",
'<p><b>موازنة المعادلة الكيميائية</b>: يجب أن يتساوى عدد ذرات كل عنصر في كلا الطرفين. نستخدم معاملات عددية صحيحة.</p>'
+T(["غير الموزونة","الموزونة"],[["H₂ + O₂ → H₂O","2H₂ + O₂ → 2H₂O"],["Fe + O₂ → Fe₂O₃","4Fe + 3O₂ → 2Fe₂O₃"],["C₃H₈ + O₂ → CO₂ + H₂O","C₃H₈ + 5O₂ → 3CO₂ + 4H₂O"]])),
sec("المادة المحددة والمردود", "Limiting Reagent", "限量试剂",
'<p><b>المادة المحددة</b>: المادة التي تستهلك أولاً وتحدد كمية الناتج. تحول جميع المواد إلى مولات، ثم استخدم النسبة المولية.</p>'
+'<p><b>المردود النظري</b>: أقصى كمية ناتج ممكنة (محسوبة من المادة المحددة). <b>المردود الفعلي</b>: الكمية المحصلة عملياً.</p>'
+'<p>'+L('\\% \\text{ yield} = \\frac{\\text{actual}}{\\text{theoretical}} \\times 100')+'</p>'))]))

# ===== L11: thermochemistry =====
all_lessons.append(LSN("thermochemistry", "الكيمياء الحرارية", "Thermochemistry", "热化学", [
sec("المحتوى الحراري وقانون هس", "Enthalpy and Hess", "焓和盖斯定律",
'<p><b>التغير في المحتوى الحراري ΔH</b>: حرارة التفاعل عند ضغط ثابت. ΔH > 0 ماص للحرارة (Endothermic)، ΔH < 0 ناشر للحرارة (Exothermic).</p>'
+'<p><b>قانون هس</b>: ΔH للتفاعل الكلي = مجموع ΔH للتفاعلات الجزئية، بغض النظر عن المسار.</p>'
+'<p>'+L('\\Delta H_{rxn} = \\sum \\Delta H_f(products) - \\sum \\Delta H_f(reactants)')+'</p>'),
sec("المسعرية والحرارة النوعية", "Calorimetry", "量热学",
'<p><b>الحرارة النوعية c</b>: كمية الحرارة اللازمة لرفع درجة حرارة 1 g من المادة بمقدار 1°C. الماء: c = 4.184 J/g·°C.</p>'
+'<p>'+L('q = m \\times c \\times \\Delta T')+'</p>'
+'<p><b>مسعر القنبلة</b>: حجم ثابت (q = ΔU). <b>مسعر بسيط</b>: ضغط ثابت (q = ΔH).</p>'))))

# Now replace in data
for lesson in all_lessons:
    lid = lesson["id"]
    found = False
    for i, item in enumerate(data):
        if item.get("id") == lid:
            data[i] = lesson
            found = True
            break
    if not found:
        print(f"WARNING: {lid} not found!")

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nDone! {len(all_lessons)} lessons updated.")

# Verify
with open(PATH, "r", encoding="utf-8") as f:
    v = json.load(f)
    for item in v:
        lid = item.get("id","")
        if lid.startswith("chem_"):
            s = item.get("sections",[])
            c = sum(len(x.get("content_ar","")) for x in s)
            print(f"  {lid}: {len(s)} sec, ~{c} chars")
