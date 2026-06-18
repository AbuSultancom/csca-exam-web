#!/usr/bin/env python3
"""Generate ALL 11 chemistry lessons for content.json"""
import json

PATH = "C:/Users/alyhy/csca-exam-web/data/content.json"

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# SVG resources
SVG = {}
SVG["atom"] = '<svg width="350" height="180" viewBox="0 0 350 180"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">تركيب الذرة</text><circle cx="175" cy="100" r="15" fill="rgba(247,37,133,0.3)" stroke="#f72585" stroke-width="2"/><text x="175" y="104" fill="#f72585" font-size="10" text-anchor="middle" font-weight="bold">نواة</text><ellipse cx="175" cy="100" rx="70" ry="30" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="175" cy="100" rx="110" ry="45" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><circle cx="120" cy="68" r="5" fill="#2ed573"/><circle cx="230" cy="72" r="5" fill="#2ed573"/><circle cx="100" cy="130" r="5" fill="#2ed573"/><circle cx="250" cy="128" r="5" fill="#2ed573"/><text x="105" y="45" fill="#2ed573" font-size="10">e-</text><text x="230" y="58" fill="#2ed573" font-size="10">e-</text></svg>'
SVG["orbitals"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">أشكال المدارات الذرية</text><circle cx="70" cy="80" r="30" fill="none" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="120" fill="#4cc9f0" font-size="11" text-anchor="middle">s</text><ellipse cx="175" cy="65" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><ellipse cx="175" cy="95" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><text x="175" y="120" fill="#f72585" font-size="11" text-anchor="middle">p</text><ellipse cx="285" cy="65" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2"/><ellipse cx="285" cy="95" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2" transform="rotate(45,285,80)"/><text x="285" y="120" fill="#2ed573" font-size="11" text-anchor="middle">d</text></svg>'
SVG["ionic"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة الأيونية (NaCl)</text><circle cx="120" cy="70" r="25" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">Na+</text><circle cx="240" cy="70" r="30" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/><text x="240" y="74" fill="#f72585" font-size="14" text-anchor="middle">Cl-</text><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">Na + Cl \u2192 Na+ + Cl-</text><text x="175" y="125" fill="#fff" font-size="9" text-anchor="middle">انتقال إلكترون من Na إلى Cl</text></svg>'
SVG["covalent"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة التساهمية (H2)</text><circle cx="120" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><circle cx="230" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="230" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><line x1="140" y1="70" x2="210" y2="70" stroke="#f72585" stroke-width="3"/><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">مشاركة زوج إلكتروني بين ذرتي هيدروجين</text></svg>'
SVG["vsepr"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">الأشكال الهندسية VSEPR</text><circle cx="70" cy="80" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="84" fill="#4cc9f0" font-size="9" text-anchor="middle">خطي 180</text><circle cx="175" cy="80" r="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/><text x="175" y="84" fill="#f72585" font-size="9" text-anchor="middle">مثلث 120</text><circle cx="285" cy="80" r="25" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/><text x="285" y="84" fill="#2ed573" font-size="9" text-anchor="middle">رباعي 109.5</text></svg>'
SVG["equilibrium"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">منحنى الاتزان الكيميائي</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="2"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="2"/><path d="M 30 110 Q 80 30 160 60 Q 250 90 320 60" fill="none" stroke="#4cc9f0" stroke-width="2.5"/><path d="M 30 30 Q 80 90 160 60 Q 250 40 320 70" fill="none" stroke="#f72585" stroke-width="2.5"/><text x="160" y="55" fill="#fff" font-size="9" text-anchor="middle">اتزان</text><line x1="160" y1="60" x2="160" y2="130" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="4,3"/><text x="160" y="138" fill="#2ed573" font-size="9" text-anchor="middle">الزمن</text></svg>'
SVG["potential"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">مخطط طاقة التفاعل</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="50" y1="120" x2="70" y2="20" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="20" x2="70" y2="100" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="100" x2="300" y2="50" stroke="#f72585" stroke-width="2.5"/><line x1="300" y1="50" x2="320" y2="120" stroke="#f72585" stroke-width="2.5"/><line x1="160" y1="20" x2="160" y2="100" stroke="#2ed573" stroke-width="2" stroke-dasharray="4,2"/><text x="165" y="58" fill="#2ed573" font-size="10">Ea</text><text x="70" y="130" fill="#4cc9f0" font-size="9" text-anchor="middle">متفاعلات</text><text x="300" y="138" fill="#f72585" font-size="9" text-anchor="middle">نواتج</text></svg>'
SVG["kinetics"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">منحنيات الرتب</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="40" x2="320" y2="40" stroke="#4cc9f0" stroke-width="2"/><text x="280" y="38" fill="#4cc9f0" font-size="9">الرتبة 0</text><line x1="30" y1="100" x2="180" y2="40" stroke="#f72585" stroke-width="2"/><text x="200" y="55" fill="#f72585" font-size="9">الرتبة 1</text><path d="M 30 30 Q 120 30 180 100 Q 250 140 320 145" fill="none" stroke="#2ed573" stroke-width="2"/><text x="280" y="120" fill="#2ed573" font-size="9">الرتبة 2</text></svg>'
SVG["ecell"] = '<svg width="350" height="160" viewBox="0 0 350 160"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">خلية كلفانية</text><rect x="20" y="30" width="100" height="100" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2" rx="5"/><text x="70" y="55" fill="#4cc9f0" font-size="10" text-anchor="middle">Zn | Zn2+</text><text x="70" y="80" fill="#fff" font-size="9" text-anchor="middle">Zn \u2192 Zn2+ + 2e-</text><rect x="230" y="30" width="100" height="100" fill="rgba(247,37,133,0.08)" stroke="#f72585" stroke-width="2" rx="5"/><text x="280" y="55" fill="#f72585" font-size="10" text-anchor="middle">Cu2+ | Cu</text><text x="280" y="80" fill="#fff" font-size="9" text-anchor="middle">Cu2+ + 2e- \u2192 Cu</text><line x1="120" y1="50" x2="230" y2="50" stroke="#2ed573" stroke-width="2"/><text x="175" y="48" fill="#2ed573" font-size="9">e-</text><rect x="145" y="85" width="60" height="30" fill="rgba(46,213,115,0.1)" stroke="#2ed573" stroke-width="1.5" rx="3"/><text x="175" y="103" fill="#2ed573" font-size="8" text-anchor="middle">جسر ملحي</text></svg>'
SVG["benzene"] = '<svg width="200" height="140" viewBox="0 0 200 140"><text x="100" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">البنزين (C6H6)</text><polygon points="100,30 150,60 150,100 100,130 50,100 50,60" fill="rgba(76,201,240,0.1)" stroke="#4cc9f0" stroke-width="2"/><circle cx="100" cy="80" r="20" fill="none" stroke="#f72585" stroke-width="1.5" stroke-dasharray="4,3"/><text x="152" y="63" fill="#fff" font-size="9">H</text><text x="152" y="105" fill="#fff" font-size="9">H</text><text x="48" y="105" fill="#fff" font-size="9">H</text><text x="48" y="63" fill="#fff" font-size="9">H</text><text x="100" y="28" fill="#fff" font-size="9">H</text><text x="100" y="138" fill="#fff" font-size="9">H</text></svg>'
SVG["energy"] = '<svg width="350" height="140" viewBox="0 0 350 140"><rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/><text x="175" y="30" fill="#2ed573" font-size="12" text-anchor="middle" font-weight="bold">مستويات الطاقة</text><text x="175" y="52" fill="#fff" font-size="10" text-anchor="middle">n=1: E = -13.6 eV</text><text x="175" y="68" fill="#fff" font-size="10" text-anchor="middle">n=2: E = -3.40 eV</text><text x="175" y="84" fill="#fff" font-size="10" text-anchor="middle">n=3: E = -1.51 eV</text><text x="175" y="100" fill="#fff" font-size="10" text-anchor="middle">n=\u221e: E = 0 eV</text></svg>'

L = lambda s: "\\(%s\\)" % s  # MathJax inline

def sec(h_ar, h_en, h_zh, content):
    return {"heading_ar": h_ar, "heading_en": h_en, "heading_zh": h_zh,
            "content_ar": content, "content_en": "", "content_zh": ""}

def mk(topic, title_ar, title_en, title_zh, sections):
    return {"id": "chem_" + topic, "topic": topic, "subject": "كيمياء | Chemistry",
            "subject_en": "Chemistry", "title_ar": title_ar, "title_en": title_en,
            "title_zh": title_zh, "sections": sections}

def T(headers, rows, style="width:100%; border-collapse:collapse; margin:15px 0;"):
    """Build HTML table"""
    th = style
    h_cells = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">%s</th>' % h for h in headers)
    r_cells = lambda row: "".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">%s</td>' % c for c in row)
    rows_html = "".join('<tr>%s</tr>' % r_cells(r) for r in rows)
    return '<table style="%s"><tr style="background:rgba(76,201,240,0.1);">%s</tr>%s</table>' % (style, h_cells, rows_html)

def UL(items):
    return "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"

def TIP(headers, rows):
    th = "width:100%; border-collapse:collapse; margin:15px 0;"
    h_cells = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">%s</th>' % h for h in headers)
    r_cells = lambda row: "".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">%s</td>' % c for c in row)
    rows_html = "".join('<tr>%s</tr>' % r_cells(r) for r in rows)
    return '<table style="%s"><tr style="background:rgba(247,37,133,0.1);">%s</tr>%s</table>' % (th, h_cells, rows_html)

# ================================================================
# L1: chem_atomic
# ================================================================
L1 = mk("atomic", "البناء الذري", "Atomic Structure", "原子结构", [
sec("مكونات الذرة", "Atomic Components", "原子组成",
'<p><b>الذرة</b> أصغر وحدة بنائية للمادة. تتكون من نواة (بروتونات موجبة + نيوترونات متعادلة) وإلكترونات سالبة تدور حولها.</p>'
+ T(["الجسيم","الشحنة","الكتلة (kg)","الموقع"],
    [["بروتون (p+)","+1.602e-19 C","1.673e-27","النواة"],
     ["نيوترون (n0)","0","1.675e-27","النواة"],
     ["إلكترون (e-)","-1.602e-19 C","9.109e-31","حول النواة"]])
+'<p><b>العدد الذري</b> Z = عدد البروتونات. <b>العدد الكتلي</b> A = بروتونات + نيوترونات. <b>النظائر</b>: ذرات لنفس العنصر (نفس Z) تختلف بعدد النيوترونات (A مختلف). مثال: '+L('^{12}_{6}C')+' و '+L('^{14}_{6}C')+'.</p>'+SVG["atom"]),
sec("التوزيع الإلكتروني", "Electron Configuration", "电子排布",
'<p>تملأ الإلكترونات حسب <b>مبدأ أوفباو</b>: '+L('1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s \\rightarrow 3d \\rightarrow 4p \\rightarrow 5s...')+'</p>'
+'<p><b>قاعدة هوند</b>: تملأ الإلكترونات المدارات المتكافئة منفردة أولاً. النيتروجين (Z=7): '+L('1s^2 2s^2 2p^3')+' (إلكترونات p منفردة).</p>'
+'<p><b>مبدأ باولي</b>: لا يمكن لإلكترونين أن يكون لهما نفس أعداد الكم الأربعة.</p>'
+T(["العنصر","Z","التوزيع","تكافؤ"],[["H","1",L('1s^1'),"1"],["C","6",L('1s^2 2s^2 2p^2'),"4"],["Fe","26",L('[Ar] 3d^6 4s^2'),"2"]])),
sec("أعداد الكم", "Quantum Numbers", "量子数",
'<p>أربعة أعداد كم تصف حالة كل إلكترون:</p>'
+T(["عدد الكم","الرمز","القيم","المعنى"],
  [["الرئيسي",L('n'),"1,2,3,...","مستوى الطاقة"],
   ["الثانوي",L('l'),"0...n-1","شكل المدار (s,p,d,f)"],
   ["المغناطيسي",L('m_l'),"-l...+l","اتجاه المدار"],
   ["المغزلي",L('m_s'),"\\u00b1\\u00bd","اتجاه الدوران"]])
+'<p>l=0 (s) كروي، l=1 (p) دمبلي، l=2 (d) معقد. عدد المدارات = '+L('2l+1')+'.</p>'+SVG["orbitals"]),
sec("الجدول الدوري والخواص الدورية", "Periodic Table", "周期表",
'<p><b>الدورة</b> = مستوى الطاقة. <b>المجموعة</b> = نفس إلكترونات التكافؤ.</p>'
+T(["الخاصية","في الدورة \\u2192","في المجموعة \\u2193"],
  [["نصف القطر الذري","يتناقص","يزداد"],
   ["طاقة التأين","تزداد","تتناقص"],
   ["السالبية الكهربائية","تزداد","تتناقص"]])
+'<p><b>المجموعات:</b> 1 (قلوية): نشيطة. 17 (هالوجينات): لا فلزات نشيطة. 18 (نبيلة): خاملة. العناصر الانتقالية: حالات تأكسد متعددة، أملاح ملونة.</p>'),
sec("القوانين الأساسية", "Key Laws", "关键公式",
T(["القانون","الصيغة"],
  [["العدد الذري",L('Z = p^+')],
   ["العدد الكتلي",L('A = Z + N')],
   ["الكتلة الذرية النسبية",L('A_r = \\frac{\\sum (m \\times \\%)}{100}')],
   ["طاقة الهيدروجين",L('E_n = -\\frac{13.6}{n^2} \\text{ eV}')]])+SVG["energy"]),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> ذرة Z=17, A=35. جد البروتونات والنيوترونات والإلكترونات.</p>'
+'<p><b>الحل:</b> بروتونات=17, إلكترونات=17, نيوترونات=35-17=18.</p>'
+'<p><b>مثال 2:</b> للكلور نظيران: '+L('^{35}_{17}Cl')+' (75.77%) و '+L('^{37}_{17}Cl')+' (24.23%). جد الكتلة الذرية.</p>'
+'<p><b>الحل:</b> '+L('A_r = \\frac{35\\times75.77+37\\times24.23}{100} = 35.48')+'</p>'
+'<p><b>مثال 3:</b> توزيع الأكسجين (Z=8) وعدد تكافؤه.</p>'
+'<p><b>الحل:</b> '+L('1s^2 2s^2 2p^4')+' \\u2192 6 إلكترونات تكافؤ.</p>'
+'<p><b>مثال 4:</b> أعداد الكم لإلكترون 3p.</p>'
+'<p><b>الحل:</b> n=3, l=1, ml\\u2208{-1,0,+1}, ms=\\u00b1\\u00bd.</p>'
+'<p><b>مثال 5:</b> رتب Li, Na, K, Rb حسب نصف القطر.</p>'
+'<p><b>الحل:</b> Li < Na < K < Rb.</p>'),
sec("نصائح وأخطاء", "Tips and Mistakes", "提示和错误",
'<p><b>نصائح:</b></p>'+UL(["Z = بروتونات = إلكترونات (ذرة متعادلة)",
"النظائر: نفس Z، مختلف N",
L('4s')+" يملأ قبل "+L('3d'),
"أعلى سالبية كهربائية للفلور = 4.0"])
+'<p><b>أخطاء شائعة:</b></p>'
+TIP(["الخطأ","التصحيح"],[["الخلط بين Z و A","Z=بروتونات، A=بروتونات+نيوترونات"],["3d قبل 4s","4s يملأ أولاً (طاقة أقل)"]]))
])

# ================================================================
# L2: chem_bonding
# ================================================================
L2 = mk("bonding", "الروابط الكيميائية", "Chemical Bonding", "化学键", [
sec("أنواع الروابط", "Bond Types", "键的类型",
'<p><b>الرابطة الكيميائية</b> قوة تجذب ذرتين معاً لتكوين جزيء.</p>'
+T(["النوع","الآلية","بين","مثال"],
  [["أيونية","انتقال إلكترونات","فلز + لا فلز","NaCl"],
   ["تساهمية","مشاركة إلكترونات","لا فلز + لا فلز","H2"],
   ["فلزية","إلكترونات ممركزة","فلز + فلز","Fe"],
   ["هيدروجينية","جذب H مع O,N,F","بين جزيئات","H2O"]])
+SVG["ionic"]+SVG["covalent"]),
sec("نظرية VSEPR", "VSEPR Theory", "VSEPR理论",
'<p><b>VSEPR</b>: أزواج الإلكترونات تتنافر فتتباعد بأكبر زاوية.</p>'
+T(["الصيغة","الشكل","الزاوية","مثال"],
  [["AX2","خطي","180\\u00b0","CO2"],
   ["AX3","مثلث مستوي","120\\u00b0","BF3"],
   ["AX4","رباعي أوجه","109.5\\u00b0","CH4"],
   ["AX3E","هرمي ثلاثي","107\\u00b0","NH3"],
   ["AX2E2","منحني","104.5\\u00b0","H2O"]])+SVG["vsepr"]),
sec("التهجين والقطبية", "Hybridization", "杂化",
'<p><b>التهجين</b>: خلط مدارات ذرية لتكوين مدارات مهجنة.</p>'
+T(["التهجين","المدارات","الشكل","الزاوية","مثال"],
  [[L('sp'),"s+p","خطي","180\\u00b0","BeCl2"],
   [L('sp^2'),"s+2p","مثلث","120\\u00b0","BF3"],
   [L('sp^3'),"s+3p","رباعي","109.5\\u00b0","CH4"]])
+'<p><b>قطبية الجزيء</b>: تعتمد على فرق السالبية وشكل الجزيء. CO2 غير قطبي (خطي). H2O قطبي (منحني).</p>'),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> نوع الرابطة في NaCl, H2, CH4.</p>'
+'<p><b>الحل:</b> NaCl أيونية، H2 و CH4 تساهمية.</p>'
+'<p><b>مثال 2:</b> شكل NH3 حسب VSEPR.</p>'
+'<p><b>الحل:</b> AX3E \\u2192 هرمي ثلاثي، زاوية 107\\u00b0.</p>'
+'<p><b>مثال 3:</b> تهجين الكربون في CH4, C2H4, C2H2.</p>'
+'<p><b>الحل:</b> '+L('sp^3, sp^2, sp')+' على الترتيب.</p>'
+'<p><b>مثال 4:</b> هل CO2 قطبي؟</p>'
+'<p><b>الحل:</b> لا، خطي (O=C=O) \\u2192 عزم ثنائي القطب = 0.</p>')
])

# ================================================================
# L3: chem_equilibrium
# ================================================================
L3 = mk("equilibrium", "الاتزان الكيميائي والأحماض والقواعد", "Chemical Equilibrium", "化学平衡与酸碱", [
sec("ثابت الاتزان ومبدأ لوشاتيليه", "Equilibrium Constant", "平衡常数",
'<p>للتفاعل: '+L('aA + bB \\rightleftharpoons cC + dD')+'</p>'
+'<p><b>ثابت الاتزان:</b> '+L('K_c = \\frac{[C]^c[D]^d}{[A]^a[B]^b}')+'</p>'
+'<p><b>ملاحظات:</b> Kc يتغير فقط بدرجة الحرارة. إذا Kc>1 فالنواتج مفضلة. المواد الصلبة والسوائل النقية لا تظهر في Kc.</p>'
+T(["التغيير","اتجاه الإزاحة"],
  [["زيادة المتفاعلات","\\u2192 نحو النواتج"],
   ["زيادة الضغط","\\u2192 جهة المولات الأقل"],
   ["رفع الحرارة","\\u2192 جهة الماصة للحرارة"]])
+SVG["equilibrium"]),
sec("الأحماض والقواعد و pH", "Acids, Bases and pH", "酸碱和pH",
'<p><b>Arrhenius:</b> حمض=H+, قاعدة=OH-. <b>Br\\u00f8nsted:</b> حمض=مانح بروتون، قاعدة=مستقبل بروتون.</p>'
+'<p>'+L('\\text{pH} = -\\log[H^+]')+'، '+L('\\text{pOH} = -\\log[OH^-]')+'، pH+pOH=14 عند 25\\u00b0C.</p>'
+T(["pH","[H+] (M)","الوصف"],
  [["0-2","10^-2 - 1","حمض قوي"],
   ["3-6","10^-6 - 10^-3","حمض ضعيف"],
   ["7","10^-7","متعادل"],
   ["12-14","10^-14 - 10^-12","قاعدة قوية"]])),
sec("المحاليل المنظمة", "Buffer Solutions", "缓冲溶液",
'<p><b>المنظم</b>: يقاوم تغير pH. يتكون من حمض ضعيف+ملحه (CH3COOH/CH3COONa) أو قاعدة ضعيفة+ملحها (NH3/NH4Cl).</p>'
+'<p><b>معادلة هندر-هاسلباخ:</b> '+L('\\text{pH} = pK_a + \\log\\frac{[A^-]}{[HA]}')+'</p>'),
sec("منتجات الذوبان (Ksp)", "Solubility Products", "溶度积",
'<p>للمركب '+L('A_xB_y(s) \\rightleftharpoons xA^{y+} + yB^{x-}')+'</p>'
+'<p>'+L('K_{sp} = [A^{y+}]^x[B^{x-}]^y')+'</p>'
+T(["المركب","Ksp (25\\u00b0C)"],[["AgCl","1.8\\u00d710^-10"],["BaSO4","1.1\\u00d710^-10"],["CaCO3","3.4\\u00d710^-9"],["Fe(OH)3","2.8\\u00d710^-39"]])),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> '+L('N_2 + 3H_2 \\rightleftharpoons 2NH_3')+'، التركيزات: 0.5, 1.0, 0.8 M. جد Kc.</p>'
+'<p><b>الحل:</b> '+L('K_c = \\frac{0.8^2}{0.5\\times1.0^3}=1.28')+'</p>'
+'<p><b>مثال 2:</b> pH لمحلول HCl 0.01 M.</p>'
+'<p><b>الحل:</b> '+L('\\text{pH}=-\\log(0.01)=2')+'</p>'
+'<p><b>مثال 3:</b> pH لمحلول NaOH 0.001 M.</p>'
+'<p><b>الحل:</b> pOH=3, pH=14-3=11.</p>')
])

# ================================================================
# L4: chem_kinetics
# ================================================================
L4 = mk("kinetics", "الحركية الكيميائية", "Chemical Kinetics", "化学动力学", [
sec("معدل التفاعل وقانون السرعة", "Reaction Rate", "反应速率",
'<p><b>معدل التفاعل</b> = '+L('-\\frac{\\Delta[A]}{\\Delta t}')+' (للمتفاعلات). الوحدة: M/s.</p>'
+'<p><b>قانون السرعة:</b> '+L('\\text{rate} = k[A]^m[B]^n')+' (m,n تحدد تجريبياً).</p>'
+T(["الرتبة","القانون التكاملي","الرسم الخطي"],
  [["0",L('[A] = -kt + [A]_0'),"t vs [A]"],
   ["1",L('\\ln[A] = -kt + \\ln[A]_0'),"t vs ln[A]"],
   ["2",L('\\frac{1}{[A]} = kt + \\frac{1}{[A]_0}'),"t vs 1/[A]"]])
+SVG["kinetics"]),
sec("طاقة التنشيط وأرهينيوس", "Activation Energy", "活化能",
'<p><b>طاقة التنشيط Ea</b>: أقل طاقة لبدء التفاعل.</p>'
+'<p><b>معادلة أرهينيوس:</b> '+L('k = A \\cdot e^{-E_a/RT}')+'</p>'
+'<p><b>العامل المساعد</b>: يخفض Ea، فيسرع التفاعل دون استهلاك.</p>'
+SVG["potential"]),
sec("عمر النصف", "Half-Life", "半衰期",
'<p><b>عمر النصف t1/2</b>: زمن انخفاض التركيز للنصف.</p>'
+T(["الرتبة","t1/2","ملاحظة"],
  [["0",L('[A]_0/2k'),"يعتمد على [A]0"],
   ["1",L('0.693/k'),"ثابت (لا يعتمد على [A]0)"],
   ["2",L('1/(k[A]_0)'),"يعتمد على [A]0"]])),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> تفاعل رتبة 1، k=0.05 s-1، [A]0=2M. جد [A] بعد 20 ث.</p>'
+'<p><b>الحل:</b> '+L('\\ln[A] = -0.05\\times20 + \\ln2 = -0.307')+' \\u2192 '+L('[A] = e^{-0.307}=0.736M')+'</p>'
+'<p><b>مثال 2:</b> t1/2 لتفاعل رتبة 1، k=0.0693 s-1.</p>'
+'<p><b>الحل:</b> '+L('t_{1/2} = 0.693/0.0693 = 10')+' ثوان.</p>')
])

# ================================================================
# L5: chem_basic
# ================================================================
L5 = mk("basic", "المفاهيم الأساسية في الكيمياء", "Basic Concepts", "化学基本概念", [
sec("المول وعدد أفوجادرو", "Mole", "摩尔",
'<p><b>المول</b>: كمية مادة تحتوي على '+L('N_A = 6.022\\times10^{23}')+' وحدة (عدد أفوجادرو).</p>'
+T(["المطلوب","الصيغة"],
  [["عدد المولات (n)",L('n = \\frac{m}{M}')],
   ["عدد الجسيمات",L('N = n \\times N_A')],
   ["حجم غاز (STP)",L('V = n \\times 22.4 \\text{ L/mol}')]])),
sec("الكتلة الذرية والجزيئية", "Atomic Mass", "原子量",
'<p><b>الكتلة المولية</b>: كتلة 1 مول (g/mol). H2O = 18.016, CO2 = 44.01, NaCl = 58.44.</p>'
+T(["المركب","الحساب","الكتلة (g/mol)"],
  [["H2O","2\\u00d71.008+16.00","18.016"],
   ["CO2","12.01+2\\u00d716.00","44.01"],
   ["NaCl","22.99+35.45","58.44"]])),
sec("قوانين الغازات", "Gas Laws", "气体定律",
''+T(["القانون","الصيغة","الثابت"],
  [["بويل",L('P_1V_1 = P_2V_2'),"T,n"],
   ["شارل",L('\\frac{V_1}{T_1} = \\frac{V_2}{T_2}'),"P,n"],
   ["الغاز المثالي",L('PV = nRT'),"R=0.0821"]])
+'<p>STP (0\\u00b0C, 1 atm): الحجم المولي = 22.4 L/mol.</p>'),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> كم مولاً في 36g H2O؟</p>'
+'<p><b>الحل:</b> '+L('n = 36/18 = 2')+' mol.</p>'
+'<p><b>مثال 2:</b> حجم 2 mol O2 عند STP.</p>'
+'<p><b>الحل:</b> 2\\u00d722.4 = 44.8 L.</p>')
])

# ================================================================
# L6: chem_inorganic
# ================================================================
L6 = mk("inorganic", "الكيمياء غير العضوية", "Inorganic Chemistry", "无机化学", [
sec("الهالوجينات والفلزات القلوية", "Halogens and Alkali Metals", "卤素和碱金属",
'<p><b>الهالوجينات</b> (المجموعة 17): F2 غاز أصفر، Cl2 غاز أصفر-أخضر، Br2 سائل بني، I2 صلب بنفسجي. النشاط يقل للنزول.</p>'
+T(["الخاصية","الاتجاه \\u2193"],
  [["نصف القطر","يزداد"],
   ["النشاط الكيميائي","يقل"],
   ["نقطة الغليان","تزداد"]])
+'<p><b>الفلزات القلوية</b> (المجموعة 1): '+L('2Na + 2H_2O \\rightarrow 2NaOH + H_2')+'. النشاط يزداد للنزول.</p>'),
sec("التفاعلات في المحاليل المائية", "Aqueous Reactions", "水溶液反应",
'<p><b>قواعد الذائبية:</b></p>'
+T(["الأيون","الذائبية","استثناءات"],
  [["NO3-","كلها ذائبة","لا يوجد"],
   ["Na+, K+","كلها ذائبة","لا يوجد"],
   ["Cl-, Br-, I-","معظمها ذائبة","Ag+, Pb2+"],
   ["CO32-, PO43-","غير ذائبة","مع القلويات"]])
+'<p><b>الأكسدة-الاختزال:</b> عامل مؤكسد يكتسب إلكترونات، عامل مختزل يفقد إلكترونات.</p>'),
sec("العناصر الانتقالية", "Transition Metals", "过渡元素",
'<p>العناصر الانتقالية (المجموعات 3-12): مدارات d غير ممتلئة.</p>'
+UL(["حالات تأكسد متعددة (Fe: +2,+3, Mn: +2,+3,+4,+6,+7)",
"أملاح ملونة (CuSO4 أزرق، FeCl3 بني)",
"نشاط تحفيزي (Fe في هابر، Ni في الهدرجة)",
"تكوين مركبات معقدة"]))
])

# ================================================================
# L7: chem_organic
# ================================================================
L7 = mk("organic", "الكيمياء العضوية", "Organic Chemistry", "有机化学", [
sec("الهيدروكربونات", "Hydrocarbons", "碳氢化合物",
+T(["النوع","الصيغة العامة","الرابطة","مثال"],
  [["ألكان",L('C_nH_{2n+2}'),"أحادية","CH4"],
   ["ألكين",L('C_nH_{2n}'),"ثنائية","C2H4"],
   ["ألكاين",L('C_nH_{2n-2}'),"ثلاثية","C2H2"],
   ["أروماتي","C6H6","رنين","بنزين"]])
+SVG["benzene"]),
sec("المجموعات الوظيفية", "Functional Groups", "官能团",
+T(["المجموعة","الصيغة","اللاحقة","مثال"],
  [["كحول","-OH","-ول","CH3OH"],
   ["ألدهيد","-CHO","-ال","CH3CHO"],
   ["كيتون",">C=O","-ون","CH3COCH3"],
   ["حمض","-COOH","-حمض","CH3COOH"],
   ["إستر","-COO-","-وات","CH3COOCH3"]])),
sec("التفاعلات العضوية", "Organic Reactions", "有机反应",
'<p><b>الإضافة:</b> '+L('C_2H_4 + Br_2 \\rightarrow C_2H_4Br_2')+'</p>'
+'<p><b>الاستبدال:</b> '+L('CH_4 + Cl_2 \\rightarrow CH_3Cl + HCl')+'</p>'
+'<p><b>الإزالة:</b> '+L('C_2H_5OH \\rightarrow C_2H_4 + H_2O')+'</p>'
+'<p><b>البلمرة:</b> '+L('nCH_2=CH_2 \\rightarrow -(CH_2-CH_2)_n-')+'</p>')
])

# ================================================================
# L8: chem_organic_cn
# ================================================================
L8 = mk("organic_cn", "الكيمياء العضوية - التسمية الصينية", "Chinese Nomenclature", "有机化学 - 中文命名", [
sec("التسمية بالصينية", "Chinese Naming", "中文命名",
'<p>في نظام التسمية الصيني: ميثان (\\u7532\\u70f7)، إيثان (\\u4e59\\u70f7)، بروبان (\\u4e19\\u70f7)، بيوتان (\\u4e01\\u70f7).</p>'
+T(["المجموعة","اللاحقة الصينية","مثال"],
  [["ألكان","-\\u70f7","\\u7532\\u70f7 CH4"],
   ["ألكين","-\\u70ef","\\u4e59\\u70ef C2H4"],
   ["كحول","-\\u9187","\\u4e59\\u9187 C2H5OH"],
   ["حمض","-\\u9178","\\u4e59\\u9178 CH3COOH"]])),
sec("الأيزومرات", "Isomers", "异构体",
'<p><b>الأيزومرات البنائية</b>: ترتيب ذرات مختلف. C4H10 له أيزومران: بيوتان وأيزوبيوتان.</p>'
+'<p><b>cis/trans</b>: حول الرابطة الثنائية. <b>الأيزومرات الضوئية</b>: صور مرآة غير متطابقة (مركز كيرالي).</p>'),
sec("التفاعلات المهمة", "Important Reactions", "重要反应",
'<p><b>الأسترة:</b> '+L('CH_3COOH + C_2H_5OH \\rightarrow CH_3COOC_2H_5 + H_2O')+'</p>'
+'<p><b>التصبن:</b> إستر + قاعدة \\u2192 كحول + صابون.</p>'
+'<p><b>نزع الماء:</b> '+L('C_2H_5OH \\rightarrow C_2H_4 + H_2O')+'</p>')
])

# ================================================================
# L9: chem_physical
# ================================================================
L9 = mk("physical", "الكيمياء الفيزيائية", "Physical Chemistry", "物理化学", [
sec("الكيمياء الكهربائية", "Electrochemistry", "电化学",
'<p><b>الخلية الكلفانية:</b> تحول كيميائي \\u2192 كهربائي. الأنود: تأكسد (سالب). الكاثود: اختزال (موجب).</p>'
+'<p>'+L('E^\\circ_{cell} = E^\\circ_{cathode} - E^\\circ_{anode}')+'</p>'
+'<p><b>معادلة نرنست:</b> '+L('E = E^\\circ - \\frac{RT}{nF} \\ln Q')+'</p>'
+SVG["ecell"]),
sec("الخواص التجميعية", "Colligative Properties", "依数性质",
+T(["الخاصية","القانون"],
  [["ارتفاع الغليان",L('\\Delta T_b = K_b \\times m \\times i')],
   ["انخفاض التجمد",L('\\Delta T_f = K_f \\times m \\times i')],
   ["الضغط الأسموزي",L('\\pi = iMRT')]])
+'<p>معامل فانت هوف i: NaCl \\u2192 i=2، الجلوكوز \\u2192 i=1.</p>'),
sec("قوانين الديناميكا الحرارية", "Thermodynamics", "热力学",
'<p><b>القانون الأول:</b> '+L('\\Delta U = q + w')+'</p>'
+'<p><b>القانون الثاني:</b> الإنتروبي S يقيس الفوضى. '+L('\\Delta S_{universe} > 0')+' للتلقائية.</p>'
+'<p><b>طاقة جيبس:</b> '+L('\\Delta G = \\Delta H - T\\Delta S')+'. '+L('\\Delta G < 0')+' تلقائي.</p>')
])

# ================================================================
# L10: chem_stoichiometry
# ================================================================
L10 = mk("stoichiometry", "الحساب الكيميائي", "Stoichiometry", "化学计量学", [
sec("موازنة المعادلات", "Balancing", "配平",
'<p><b>موازنة:</b> عدد ذرات كل عنصر = في الطرفين.</p>'
+T(["غير موزونة","موزونة"],[["H2+O2\\u2192H2O","2H2+O2\\u21922H2O"],
   ["Fe+O2\\u2192Fe2O3","4Fe+3O2\\u21922Fe2O3"],
   ["C3H8+O2\\u2192CO2+H2O","C3H8+5O2\\u21923CO2+4H2O"]])),
sec("المادة المحددة والمردود", "Limiting Reagent", "限量试剂",
'<p><b>المادة المحددة</b>: تستهلك أولاً وتحدد الناتج.</p>'
+'<p><b>المردود النظري:</b> أقصى كمية ناتج. <b>الفعلي:</b> المحصل معملياً.</p>'
+'<p>'+L('\\% \\text{ yield} = \\frac{\\text{actual}}{\\text{theoretical}} \\times 100')+'</p>'),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> 10g H2 مع O2 زائد. كم g H2O ينتج؟</p>'
+'<p><b>الحل:</b> '+L('n_{H2}=10/2=5\\text{ mol}')+' \\u2192 '+L('n_{H2O}=5\\text{ mol}')+' \\u2192 '+L('m_{H2O}=5\\times18=90\\text{ g}')+'</p>'
+'<p><b>مثال 2:</b> كم mol CO2 من حرق 2 mol C3H8؟</p>'
+'<p><b>الحل:</b> '+L('n_{CO2}=2\\times3=6\\text{ mol}')+'</p>')
])

# ================================================================
# L11: chem_thermochemistry
# ================================================================
L11 = mk("thermochemistry", "الكيمياء الحرارية", "Thermochemistry", "热化学", [
sec("المحتوى الحراري وقانون هس", "Enthalpy and Hess", "焓和盖斯定律",
'<p><b>DH</b>: حرارة التفاعل عند ضغط ثابت. موجب = ماص، سالب = ناشر.</p>'
+'<p><b>قانون هس:</b> '+L('Delta H_{total} = sum Delta H_{partial}')+'</p>'
+'<p>'+L('Delta H_{rxn} = sum Delta H_f(products) - sum Delta H_f(reactants)')+'</p>'
+T(["المركب",L('Delta H_f^circ (kJ/mol)')],
  [["H2O(l)","-285.8"],["CO2(g)","-393.5"],["CH4(g)","-74.8"]])),
sec("المسعرية والحرارة النوعية", "Calorimetry", "量热学",
'<p><b>الحرارة النوعية c:</b> '+L('q = m times c times Delta T')+'</p>'
+'<p>الماء: c = 4.184 J/g.C.</p>'
+'<p><b>مسعر القنبلة:</b> حجم ثابت. <b>مسعر بسيط:</b> ضغط ثابت.</p>'),
sec("الإنتروبي والتلقائية", "Entropy", "熵",
'<p><b>الإنتروبي S</b>: مقياس العشوائية. '+L('Delta S > 0')+' = زيادة فوضى.</p>'
+UL(["صلب < سائل < غاز (S يزداد)",
"زيادة جسيمات الغاز تزيد S",
L('Delta G = Delta H - T Delta S')+"، "+L('Delta G < 0')+" تلقائي"])),
sec("أمثلة محلولة", "Solved Examples", "例题",
'<p><b>مثال 1:</b> احسب DH لحرق CH4: CH4+2O2 -> CO2+2H2O. DHf: CH4=-74.8, CO2=-393.5, H2O=-285.8.</p>'
+'<p><b>الحل:</b> '+L('Delta H = [(-393.5)+2(-285.8)]-[-74.8] = -890.3 kJ/mol')+'</p>'
+'<p><b>مثال 2:</b> 50g ماء من 25C لـ 75C. جد q.</p>'
+'<p><b>الحل:</b> '+L('q = 50 times 4.184 times 50 = 10460 J = 10.46 kJ')+'</p>')
])

# =============== REPLACE ===============
all_lessons = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11]

ids_done = 0
for lesson in all_lessons:
    lid = lesson["id"]
    found = False
    for i, item in enumerate(data):
        if item.get("id") == lid:
            data[i] = lesson
            found = True
            ids_done += 1
            break
    if not found:
        print("WARNING: %s not found!" % lid)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! %d/%d lessons replaced." % (ids_done, len(all_lessons)))

# Verify
with open(PATH, "r", encoding="utf-8") as f:
    v = json.load(f)
    for item in v:
        if item.get("id","").startswith("chem_"):
            s = item["sections"]
            c = sum(len(x.get("content_ar","")) for x in s)
            print("  %s: %d sec, ~%d chars" % (item["id"], len(s), c))
