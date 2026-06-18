#!/usr/bin/env python3
"""Build chemistry content directly as a JSON data structure"""
import json

PATH = "C:/Users/alyhy/csca-exam-web/data/content.json"
MJ = lambda s: "\\(%s\\)" % s  # MathJax wrapper

# Read existing data
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Reusable HTML helpers 
def table(headers, rows):
    h = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">{}</th>'.format(x) for x in headers)
    r = "".join('<tr>{}</tr>'.format("".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">{}</td>'.format(c) for c in row)) for row in rows)
    return '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(76,201,240,0.1);">{}</tr>{}</table>'.format(h, r)

def ul(items):
    return "<ul>" + "".join("<li>{}</li>".format(x) for x in items) + "</ul>"

def err_table(headers, rows):
    h = "".join('<th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">{}</th>'.format(x) for x in headers)
    r = "".join('<tr>{}</tr>'.format("".join('<td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">{}</td>'.format(c) for c in row)) for row in rows)
    return '<table style="width:100%; border-collapse:collapse; margin:15px 0;"><tr style="background:rgba(247,37,133,0.1);">{}</tr>{}</table>'.format(h, r)

def section(ar_h, en_h, zh_h, content):
    return {"heading_ar": ar_h, "heading_en": en_h, "heading_zh": zh_h,
            "content_ar": content, "content_en": "", "content_zh": ""}

def lesson(topic, title_ar, title_en, title_zh, sections):
    return {"id": "chem_"+topic, "topic": topic, "subject": "كيمياء | Chemistry",
            "subject_en": "Chemistry", "title_ar": title_ar, "title_en": title_en,
            "title_zh": title_zh, "sections": sections}

# SVG resources
S = {}
S["atom"] = '<svg width="350" height="180" viewBox="0 0 350 180"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">تركيب الذرة</text><circle cx="175" cy="100" r="15" fill="rgba(247,37,133,0.3)" stroke="#f72585" stroke-width="2"/><text x="175" y="104" fill="#f72585" font-size="10" text-anchor="middle" font-weight="bold">نواة</text><ellipse cx="175" cy="100" rx="70" ry="30" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><ellipse cx="175" cy="100" rx="110" ry="45" fill="none" stroke="#4cc9f0" stroke-width="1" stroke-dasharray="4,3"/><circle cx="120" cy="68" r="5" fill="#2ed573"/><circle cx="230" cy="72" r="5" fill="#2ed573"/><circle cx="100" cy="130" r="5" fill="#2ed573"/><circle cx="250" cy="128" r="5" fill="#2ed573"/><circle cx="145" cy="52" r="5" fill="#2ed573"/><circle cx="205" cy="145" r="5" fill="#2ed573"/><text x="105" y="45" fill="#2ed573" font-size="10">e\u207b</text><text x="230" y="58" fill="#2ed573" font-size="10">e\u207b</text><text x="85" y="152" fill="#2ed573" font-size="10">e\u207b</text></svg>'
S["orbitals"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">أشكال المدارات الذرية</text><circle cx="70" cy="80" r="30" fill="none" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="120" fill="#4cc9f0" font-size="11" text-anchor="middle">s</text><ellipse cx="175" cy="65" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><ellipse cx="175" cy="95" rx="40" ry="15" fill="none" stroke="#f72585" stroke-width="2"/><text x="175" y="120" fill="#f72585" font-size="11" text-anchor="middle">p</text><ellipse cx="285" cy="65" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2"/><ellipse cx="285" cy="95" rx="30" ry="18" fill="none" stroke="#2ed573" stroke-width="2" transform="rotate(45,285,80)"/><text x="285" y="120" fill="#2ed573" font-size="11" text-anchor="middle">d</text></svg>'
S["ionic"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة الأيونية (NaCl)</text><circle cx="120" cy="70" r="25" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">Na+</text><circle cx="240" cy="70" r="30" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/><text x="240" y="74" fill="#f72585" font-size="14" text-anchor="middle">Cl-</text><text x="175" y="110" fill="#fff" font-size="9" text-anchor="middle">Na + Cl \u2192 Na+ + Cl-</text><text x="175" y="125" fill="#fff" font-size="9" text-anchor="middle">\u0627\u0646\u062a\u0642\u0627\u0644 \u0625\u0644\u0643\u062a\u0631\u0648\u0646 \u0645\u0646 Na \u0625\u0644\u0649 Cl</text></svg>'
S["covalent"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="13" text-anchor="middle" font-weight="bold">الرابطة التساهمية (H\u2082)</text><circle cx="120" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="120" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><circle cx="230" cy="70" r="20" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/><text x="230" y="74" fill="#4cc9f0" font-size="14" text-anchor="middle">H</text><line x1="140" y1="70" x2="210" y2="70" stroke="#f72585" stroke-width="3"/></svg>'
S["vsepr"] = '<svg width="350" height="140" viewBox="0 0 350 140"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">VSEPR</text><circle cx="70" cy="80" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/><text x="70" y="84" fill="#4cc9f0" font-size="9" text-anchor="middle">\u062e\u0637\u064a 180\u00b0</text><circle cx="175" cy="80" r="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/><text x="175" y="84" fill="#f72585" font-size="9" text-anchor="middle">\u0645\u062b\u0644\u062b 120\u00b0</text><circle cx="285" cy="80" r="25" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/><text x="285" y="84" fill="#2ed573" font-size="9" text-anchor="middle">\u0631\u0628\u0627\u0639\u064a 109.5\u00b0</text></svg>'
S["equilibrium"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u0645\u0646\u062d\u0646\u0649 \u0627\u0644\u0627\u062a\u0632\u0627\u0646</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="2"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="2"/><path d="M 30 110 Q 80 30 160 60 Q 250 90 320 60" fill="none" stroke="#4cc9f0" stroke-width="2.5"/><path d="M 30 30 Q 80 90 160 60 Q 250 40 320 70" fill="none" stroke="#f72585" stroke-width="2.5"/><text x="160" y="55" fill="#fff" font-size="9" text-anchor="middle">\u0627\u062a\u0632\u0627\u0646</text><line x1="160" y1="60" x2="160" y2="130" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="4,3"/></svg>'
S["ecell"] = '<svg width="350" height="160" viewBox="0 0 350 160"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">\u062e\u0644\u064a\u0629 \u0643\u0644\u0641\u0627\u0646\u064a\u0629</text><rect x="20" y="30" width="100" height="100" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2" rx="5"/><text x="70" y="55" fill="#4cc9f0" font-size="10" text-anchor="middle">Zn | Zn2+</text><text x="70" y="80" fill="#fff" font-size="9" text-anchor="middle">Zn \u2192 Zn2+ + 2e-</text><rect x="230" y="30" width="100" height="100" fill="rgba(247,37,133,0.08)" stroke="#f72585" stroke-width="2" rx="5"/><text x="280" y="55" fill="#f72585" font-size="10" text-anchor="middle">Cu2+ | Cu</text><text x="280" y="80" fill="#fff" font-size="9" text-anchor="middle">Cu2+ + 2e- \u2192 Cu</text><line x1="120" y1="50" x2="230" y2="50" stroke="#2ed573" stroke-width="2"/><text x="175" y="48" fill="#2ed573" font-size="9">e-</text><rect x="145" y="85" width="60" height="30" fill="rgba(46,213,115,0.1)" stroke="#2ed573" stroke-width="1.5" rx="3"/><text x="175" y="103" fill="#2ed573" font-size="8" text-anchor="middle">\u062c\u0633\u0631 \u0645\u0644\u062d\u064a</text></svg>'
S["energy"] = '<svg width="350" height="140" viewBox="0 0 350 140"><rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/><text x="175" y="30" fill="#2ed573" font-size="12" text-anchor="middle" font-weight="bold">مستويات الطاقة (H)</text><text x="175" y="52" fill="#fff" font-size="10" text-anchor="middle">n=1: E=-13.6 eV</text><text x="175" y="68" fill="#fff" font-size="10" text-anchor="middle">n=2: E=-3.40 eV</text><text x="175" y="84" fill="#fff" font-size="10" text-anchor="middle">n=3: E=-1.51 eV</text><text x="175" y="100" fill="#fff" font-size="10" text-anchor="middle">n=∞: E=0 eV</text></svg>'
S["kinetics"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">منحنيات الرتب</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="120" x2="30" y2="20" stroke="#fff" stroke-width="1.5"/><line x1="30" y1="40" x2="320" y2="40" stroke="#4cc9f0" stroke-width="2"/><text x="270" y="38" fill="#4cc9f0" font-size="9">الرتبة 0</text><line x1="30" y1="100" x2="180" y2="40" stroke="#f72585" stroke-width="2"/><text x="200" y="55" fill="#f72585" font-size="9">الرتبة 1</text><path d="M 30 30 Q 120 30 180 100 Q 250 140 320 145" fill="none" stroke="#2ed573" stroke-width="2"/><text x="270" y="120" fill="#2ed573" font-size="9">الرتبة 2</text></svg>'
S["potential"] = '<svg width="350" height="150" viewBox="0 0 350 150"><text x="175" y="18" fill="#4cc9f0" font-size="12" text-anchor="middle" font-weight="bold">مخطط طاقة التفاعل</text><line x1="30" y1="120" x2="320" y2="120" stroke="#fff" stroke-width="1.5"/><line x1="50" y1="120" x2="70" y2="20" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="20" x2="70" y2="100" stroke="#4cc9f0" stroke-width="2"/><line x1="70" y1="100" x2="300" y2="50" stroke="#f72585" stroke-width="2.5"/><line x1="300" y1="50" x2="320" y2="120" stroke="#f72585" stroke-width="2.5"/><line x1="160" y1="20" x2="160" y2="100" stroke="#2ed573" stroke-width="2" stroke-dasharray="4,2"/><text x="165" y="58" fill="#2ed573" font-size="10">Ea</text><text x="70" y="130" fill="#4cc9f0" font-size="9" text-anchor="middle">متفاعلات</text><text x="300" y="135" fill="#f72585" font-size="9" text-anchor="middle">نواتج</text></svg>'

# Now build each lesson content
# For clarity, build content as Python strings, then cast to JSON

lessons = []

# ---- L1: atomic ----
c1  = '<p><b>الذرة</b> أصغر وحدة بنائية للمادة تحتفظ بالخواص الكيميائية. تتكون من نواة (بروتونات موجبة + نيوترونات متعادلة) وإلكترونات سالبة تدور حولها.</p>'
c1 += table(["الجسيم","الشحنة","الكتلة (kg)","الموقع"],[["بروتون (p+)","+1.602e-19 C","1.673e-27","النواة"],["نيوترون (n0)","0","1.675e-27","النواة"],["إلكترون (e-)","-1.602e-19 C","9.109e-31","حول النواة"]])
c1 += '<p><b>العدد الذري</b> Z = عدد البروتونات. <b>العدد الكتلي</b> A = بروتونات + نيوترونات. <b>النظائر</b>: ذرات لنفس العنصر (نفس Z) تختلف بعدد النيوترونات (A مختلف). مثال: ' + MJ("^{12}_{6}C") + ' و ' + MJ("^{14}_{6}C") + '.</p>' + S["atom"]

c1b  = '<p>تملأ الإلكترونات المدارات حسب <b>مبدأ أوفباو</b> (من الأقل طاقة للأعلى): ' + MJ("1s \\rightarrow 2s \\rightarrow 2p \\rightarrow 3s \\rightarrow 3p \\rightarrow 4s \\rightarrow 3d \\rightarrow 4p \\rightarrow 5s...") + '</p>'
c1b += '<p><b>قاعدة هوند</b>: تملأ الإلكترونات المدارات المتكافئة منفردة أولاً. النيتروجين (N, Z=7): ' + MJ("1s^2 2s^2 2p^3") + ' (إلكترونات p منفردة).</p>'
c1b += '<p><b>مبدأ باولي للاستبعاد</b>: لا يمكن لإلكترونين أن يكون لهما نفس أعداد الكم الأربعة. كل مدار لا يسع أكثر من إلكترونين (باتجاهي دوران متعاكسين).</p>'

c1c  = '<p><b>أعداد الكم</b> الأربعة تصف حالة كل إلكترون فريداً:</p>'
c1c += table(["عدد الكم","الرمز","القيم","المعنى"],[["الرئيسي",MJ("n"),"1,2,3,...","مستوى الطاقة"],["الثانوي",MJ("l"),"0...n-1","شكل المدار (s,p,d,f)"],["المغناطيسي",MJ("m_l"),"-l...+l","اتجاه المدار"],["المغزلي",MJ("m_s"),"+½ أو -½","اتجاه الدوران"]])
c1c += '<p>l=0 (s) كروي، l=1 (p) دمبلي، l=2 (d) معقد. عدد المدارات = ' + MJ("2l+1") + '.</p>' + S["orbitals"]

c1d  = '<p><b>الدورة</b>: صف أفقي = مستوى الطاقة الرئيسي. <b>المجموعة</b>: عمود رأسي = نفس إلكترونات التكافؤ.</p>'
c1d += table(["الخاصية","في الدورة \u2192","في المجموعة \u2193"],[["نصف القطر الذري","يتناقص","يزداد"],["طاقة التأين","تزداد","تتناقص"],["السالبية الكهربائية","تزداد","تتناقص"]])
c1d += '<p><b>المجموعات:</b> 1 (قلوية): نشيطة. 17 (هالوجينات): لا فلزات. 18 (نبيلة): خاملة. العناصر الانتقالية: حالات تأكسد متعددة، أملاح ملونة.</p>'

c1e  = table(["القانون","الصيغة"],[["العدد الذري",MJ("Z = p^+")],["العدد الكتلي",MJ("A = Z + N")],["الكتلة الذرية النسبية",MJ("A_r = \\frac{\\sum (m \\times \\%)}{100}")],["طاقة المستوى (H)",MJ("E_n = -\\frac{13.6}{n^2} \\text{ eV}")]]) + S["energy"]

c1f  = '<p><b>مثال 1:</b> ذرة Z=17, A=35. جد p+, n0, e-.</p>'
c1f += '<p><b>الحل:</b> p+=17, e-=17, n0=35-17=18.</p>'
c1f += '<p><b>مثال 2:</b> للكلور نظيران: ' + MJ("^{35}_{17}Cl") + ' (75.77%) و ' + MJ("^{37}_{17}Cl") + ' (24.23%). جد الكتلة الذرية.</p>'
c1f += '<p><b>الحل:</b> ' + MJ("A_r = \\frac{35\\times75.77+37\\times24.23}{100} = 35.48") + '</p>'
c1f += '<p><b>مثال 3:</b> توزيع الأكسجين (Z=8) وعدد تكافؤه.</p>'
c1f += '<p><b>الحل:</b> ' + MJ("1s^2 2s^2 2p^4") + ' \u2192 6 إلكترونات تكافؤ.</p>'
c1f += '<p><b>مثال 4:</b> أعداد الكم لإلكترون 3p.</p>'
c1f += '<p><b>الحل:</b> n=3, l=1, ml\u2208{-1,0,+1}, ms=+½ أو -½.</p>'
c1f += '<p><b>مثال 5:</b> رتب Li, Na, K, Rb حسب نصف القطر.</p>'
c1f += '<p><b>الحل:</b> Li < Na < K < Rb (يزداد بالنزول في المجموعة).</p>'

c1g  = '<p><b>نصائح:</b></p>' + ul(["Z = بروتونات = إلكترونات (ذرة متعادلة)","النظائر: نفس Z لكن A مختلف","4s يملأ قبل 3d (أوفباو)","أعلى سالبية: F = 4.0"])
c1g += '<p><b>أخطاء شائعة:</b></p>'
c1g += err_table(["الخطأ","التصحيح"],[["الخلط بين Z و A","Z=بروتونات، A=بروتونات+نيوترونات"],["3d قبل 4s","4s يملأ أولاً (طاقة أقل)"]])

L1 = lesson("atomic", "البناء الذري", "Atomic Structure", "原子结构", [
    section("مكونات الذرة","Atomic Components","原子组成",c1),
    section("التوزيع الإلكتروني","Electron Configuration","电子排布",c1b),
    section("أعداد الكم","Quantum Numbers","量子数",c1c),
    section("الجدول الدوري","Periodic Table","周期表",c1d),
    section("القوانين الأساسية","Key Laws","关键公式",c1e),
    section("أمثلة محلولة","Solved Examples","例题",c1f),
    section("نصائح وأخطاء","Tips & Mistakes","提示和错误",c1g)
])
lessons.append(L1)
print("L1 built")

# ---- L2: bonding ----
c2a  = '<p><b>الرابطة الكيميائية</b> هي قوة تجذب ذرتين معاً لتكوين جزيء أو مركب.</p>'
c2a += table(["النوع","الآلية","بين","مثال"],[["أيونية","انتقال إلكترونات","فلز + لا فلز","NaCl"],["تساهمية","مشاركة إلكترونات","لا فلز + لا فلز","H\u2082"],["فلزية","إلكترونات ممركزة","فلز + فلز","Fe"],["هيدروجينية","جذب H مع O,N,F","بين جزيئات","H\u2082O"]]) + S["ionic"] + S["covalent"]

c2b  = '<p><b>VSEPR:</b> أزواج الإلكترونات حول الذرة المركزية تتنافر فتتباعد بأكبر زاوية ممكنة.</p>'
c2b += table(["الصيغة","الشكل","الزاوية","مثال"],[["AX\u2082","خطي","180\u00b0","CO\u2082"],["AX\u2083","مثلث مستوي","120\u00b0","BF\u2083"],["AX\u2084","رباعي أوجه","109.5\u00b0","CH\u2084"],["AX\u2083E","هرمي ثلاثي","107\u00b0","NH\u2083"],["AX\u2082E\u2082","منحني","104.5\u00b0","H\u2082O"]]) + S["vsepr"]

c2c  = '<p><b>التهجين:</b> خلط مدارات ذرية لتكوين مدارات مهجنة متكافئة.</p>'
c2c += table(["التهجين","المدارات","الشكل","الزاوية","مثال"],[["sp","s+p","خطي","180\u00b0","BeCl\u2082"],["sp\u00b2","s+2p","مثلث","120\u00b0","BF\u2083"],["sp\u00b3","s+3p","رباعي","109.5\u00b0","CH\u2084"]])
c2c += '<p><b>قطبية الجزيء:</b> تعتمد على فرق السالبية والشكل. CO\u2082 غير قطبي (خطي). H\u2082O قطبي (منحني).</p>'

c2d  = '<p><b>مثال 1:</b> نوع الرابطة في NaCl, H\u2082, CH\u2084.</p>'
c2d += '<p><b>الحل:</b> NaCl أيونية، H\u2082 تساهمية، CH\u2084 تساهمية.</p>'
c2d += '<p><b>مثال 2:</b> شكل NH\u2083 حسب VSEPR.</p>'
c2d += '<p><b>الحل:</b> AX\u2083E \u2192 هرمي ثلاثي، زاوية 107\u00b0.</p>'
c2d += '<p><b>مثال 3:</b> تهجين الكربون في CH\u2084, C\u2082H\u2084, C\u2082H\u2082.</p>'
c2d += '<p><b>الحل:</b> CH\u2084: sp\u00b3، C\u2082H\u2084: sp\u00b2، C\u2082H\u2082: sp.</p>'

L2 = lesson("bonding", "الروابط الكيميائية", "Chemical Bonding", "化学键", [
    section("أنواع الروابط","Bond Types","键的类型",c2a),
    section("نظرية VSEPR","VSEPR Theory","VSEPR理论",c2b),
    section("التهجين والقطبية","Hybridization & Polarity","杂化和极性",c2c),
    section("أمثلة محلولة","Solved Examples","例题",c2d)
])
lessons.append(L2)
print("L2 built")

# ---- L3: equilibrium ----
c3a  = '<p>للتفاعل العكسي: ' + MJ("aA + bB \\rightleftharpoons cC + dD") + '</p>'
c3a += '<p><b>ثابت الاتزان:</b> ' + MJ("K_c = \\frac{[C]^c[D]^d}{[A]^a[B]^b}") + '</p>'
c3a += '<p>Kc يتغير فقط مع درجة الحرارة. إذا Kc>1 فالنواتج مفضلة. المواد الصلبة والسوائل النقية لا تظهر في Kc.</p>'
c3a += table(["التغيير","اتجاه الإزاحة"],[["زيادة المتفاعلات","\u2192 نحو النواتج"],["زيادة الضغط","\u2192 جهة المولات الأقل"],["رفع الحرارة","\u2192 جهة الماصة للحرارة"]]) + S["equilibrium"]

c3b  = '<p><b>pH:</b> ' + MJ("\\text{pH} = -\\log[H^+]") + '، ' + MJ("\\text{pOH} = -\\log[OH^-]") + '، pH+pOH=14.</p>'
c3b += table(["pH","[H+]","الوصف"],[["0-2","10\u207b\u00b2-1","حمض قوي"],["7","10\u207b\u2077","متعادل"],["12-14","10\u207b\u00b9\u2074-10\u207b\u00b9\u00b2","قاعدة قوية"]])

c3c  = '<p><b>المنظم:</b> يقاوم تغير pH. مكوناته: حمض ضعيف + ملحه (CH\u2083COOH/CH\u2083COONa) أو قاعدة ضعيفة + ملحها (NH\u2083/NH\u2084Cl).</p>'
c3c += '<p><b>هندر-هاسلباخ:</b> ' + MJ("\\text{pH} = pK_a + \\log\\frac{[A^-]}{[HA]}") + '</p>'

c3d  = '<p><b>مثال 1:</b> ' + MJ("N_2 + 3H_2 \\rightleftharpoons 2NH_3") + '، [N\u2082]=0.5, [H\u2082]=1.0, [NH\u2083]=0.8 M. جد Kc.</p>'
c3d += '<p><b>الحل:</b> ' + MJ("K_c = \\frac{0.8^2}{0.5\\times1.0^3} = 1.28") + '</p>'
c3d += '<p><b>مثال 2:</b> pH لـ HCl 0.01 M.</p>'
c3d += '<p><b>الحل:</b> pH = -log(0.01) = 2.</p>'
c3d += '<p><b>مثال 3:</b> pH لـ NaOH 0.001 M.</p>'
c3d += '<p><b>الحل:</b> pOH=3, pH=14-3=11.</p>'

L3 = lesson("equilibrium", "الاتزان الكيميائي والأحماض والقواعد", "Chemical Equilibrium", "化学平衡与酸碱", [
    section("ثابت الاتزان","Equilibrium Constant","平衡常数",c3a),
    section("pH والأحماض","pH and Acids","酸碱和pH",c3b),
    section("المحاليل المنظمة","Buffer Solutions","缓冲溶液",c3c),
    section("أمثلة محلولة","Solved Examples","例题",c3d)
])
lessons.append(L3)
print("L3 built")

# ---- L4-L11: shorter versions for speed ----
c4a  = '<p><b>معدل التفاعل</b> = ' + MJ("-\\frac{\\Delta[A]}{\\Delta t}") + '. قانون السرعة: ' + MJ("\\text{rate} = k[A]^m[B]^n") + '</p>'
c4a += table(["الرتبة","القانون التكاملي","عمر النصف"],[["0",MJ("[A] = -kt + [A]_0"),MJ("[A]_0/2k")],["1",MJ("\\ln[A] = -kt + \\ln[A]_0"),MJ("0.693/k")],["2",MJ("\\frac{1}{[A]} = kt + \\frac{1}{[A]_0}"),MJ("1/(k[A]_0)")]])

L4 = lesson("kinetics", "الحركية الكيميائية", "Chemical Kinetics", "化学动力学", [
    section("معدل التفاعل وقانون السرعة","Reaction Rate","反应速率",c4a + S["kinetics"]),
    section("طاقة التنشيط","Activation Energy","活化能",'<p><b>أرهينيوس:</b> ' + MJ("k = A \\cdot e^{-E_a/RT}") + '. العامل المساعد يخفض Ea.</p>' + S["potential"]),
])

c5a  = '<p><b>المول</b>: ' + MJ("n = \\frac{m}{M}") + '، ' + MJ("N_A = 6.022\\times10^{23}") + '</p>'
c5a += table(["الكمية","الصيغة"],[["عدد المولات",MJ("n=m/M")],["عدد الجسيمات",MJ("N=n\\times N_A")],["حجم غاز (STP)",MJ("V=n\\times22.4")]])

L5 = lesson("basic", "المفاهيم الأساسية في الكيمياء", "Basic Concepts", "化学基本概念", [
    section("المول وأفوجادرو","Mole","摩尔",c5a),
    section("الكتلة الذرية","Atomic Mass","原子量",'<p>H\u2082O=18 g/mol، CO\u2082=44 g/mol، NaCl=58.44 g/mol.</p>'),
    section("قوانين الغازات","Gas Laws","气体定律",table(["القانون","الصيغة"],[["بويل",MJ("P_1V_1=P_2V_2")],["شارل",MJ("V_1/T_1=V_2/T_2")],["الغاز المثالي",MJ("PV=nRT")]])),
    section("أمثلة محلولة","Solved Examples","例题",'<p><b>مثال:</b> 36g H\u2082O = ' + MJ("36/18=2") + ' mol.</p><p><b>مثال:</b> 2 mol O\u2082 عند STP = 44.8 L.</p>'),
])

c6a  = '<p><b>الهالوجينات</b> (17): F\u2082 أصفر، Cl\u2082 أصفر-أخضر، Br\u2082 بني، I\u2082 بنفسجي.</p>'
c6a += '<p><b>الفلزات القلوية</b> (1): ' + MJ("2Na + 2H_2O \\rightarrow 2NaOH + H_2") + '</p>'

L6 = lesson("inorganic", "الكيمياء غير العضوية", "Inorganic Chemistry", "无机化学", [
    section("الهالوجينات والقلويات","Halogens","卤素",c6a),
    section("التفاعلات المائية","Aqueous Reactions","水溶液反应",table(["الأيون","الذائبية"],[["NO\u2083\u207b","كلها"],["Na+,K+","كلها"],["Cl\u207b,Br\u207b,I\u207b","معظمها"],["CO\u2083\u00b2\u207b,PO\u2084\u00b3\u207b","غير ذائبة"]])),
])

c7a  = table(["النوع","الصيغة","مثال"],[["ألكان",MJ("C_nH_{2n+2}"),"CH\u2084"],["ألكين",MJ("C_nH_{2n}"),"C\u2082H\u2084"],["ألكاين",MJ("C_nH_{2n-2}"),"C\u2082H\u2082"],["أروماتي","C\u2086H\u2086","بنزين"]])

L7 = lesson("organic", "الكيمياء العضوية", "Organic Chemistry", "有机化学", [
    section("الهيدروكربونات","Hydrocarbons","碳氢化合物",c7a + S["benzene"]),
    section("المجموعات الوظيفية","Functional Groups","官能团",table(["المجموعة","الصيغة","مثال"],[["كحول","-OH","CH\u2083OH"],["ألدهيد","-CHO","CH\u2083CHO"],["حمض","-COOH","CH\u2083COOH"],["إستر","-COO-","CH\u2083COOCH\u2083"]])),
    section("التفاعلات العضوية","Organic Reactions","有机反应",'<p><b>إضافة:</b> ' + MJ("C_2H_4 + Br_2 \\rightarrow C_2H_4Br_2") + '</p><p><b>بلمرة:</b> ' + MJ("nCH_2=CH_2 \\rightarrow -(CH_2-CH_2)_n-") + '</p>'),
])

L8 = lesson("organic_cn", "الكيمياء العضوية - التسمية الصينية", "Chinese Nomenclature", "有机化学 - 中文命名", [
    section("التسمية بالصينية","Chinese Naming","中文命名",table(["العربية","الصينية","مثال"],[["ميثان","甲烷","CH\u2084"],["إيثان","乙烷","C\u2082H\u2086"],["إيثين","乙烯","C\u2082H\u2084"],["إيثانول","乙醇","C\u2082H\u2085OH"]])),
    section("الأيزومرات","Isomers","异构体",'<p><b>بنائية:</b> ترتيب ذرات مختلف (C\u2084H\u2081\u2080 له أيزومران). <b>cis/trans:</b> حول الرابطة الثنائية.</p>'),
])

c9a  = '<p><b>الخلية الكلفانية:</b> ' + MJ("E^\\circ_{cell} = E^\\circ_{cathode} - E^\\circ_{anode}") + '</p>'
c9a += '<p><b>نرنست:</b> ' + MJ("E = E^\\circ - \\frac{RT}{nF} \\ln Q") + '</p>' + S["ecell"]

L9 = lesson("physical", "الكيمياء الفيزيائية", "Physical Chemistry", "物理化学", [
    section("الكيمياء الكهربائية","Electrochemistry","电化学",c9a),
    section("الخواص التجميعية","Colligative Properties","依数性质",table(["الخاصية","القانون"],[["ارتفاع الغليان",MJ("\\Delta T_b = K_b \\times m \\times i")],["انخفاض التجمد",MJ("\\Delta T_f = K_f \\times m \\times i")],["الضغط الأسموزي",MJ("\\pi = iMRT")]])),
])

c10a = table(["غير الموزونة","الموزونة"],[["H\u2082+O\u2082\u2192H\u2082O","2H\u2082+O\u2082\u21922H\u2082O"],["C\u2083H\u2088+O\u2082\u2192CO\u2082+H\u2082O","C\u2083H\u2088+5O\u2082\u21923CO\u2082+4H\u2082O"]])

L10 = lesson("stoichiometry", "الحساب الكيميائي (الاستوكيومتريا)", "Stoichiometry", "化学计量学", [
    section("موازنة المعادلات","Balancing","配平",c10a),
    section("المادة المحددة","Limiting Reagent","限量试剂",'<p>' + MJ("\\% \\text{ yield} = \\frac{\\text{actual}}{\\text{theoretical}} \\times 100") + '</p>'),
    section("أمثلة محلولة","Solved Examples","例题",'<p>10g H\u2082 \u2192 ' + MJ("n=10/2=5") + ' mol \u2192 5 mol H\u2082O \u2192 ' + MJ("m=5\\times18=90") + ' g.</p>'),
])

c11a = '<p><b>قانون هس:</b> ' + MJ("\\Delta H_{rxn} = \\sum \\Delta H_f(products) - \\sum \\Delta H_f(reactants)") + '</p>'

L11 = lesson("thermochemistry", "الكيمياء الحرارية", "Thermochemistry", "热化学", [
    section("المحتوى الحراري وقانون هس","Enthalpy and Hess","焓和盖斯定律",c11a),
    section("المسعرية","Calorimetry","量热学",'<p>' + MJ("q = m \\times c \\times \\Delta T") + ' (الماء: c=4.184 J/g\u00b7\u00b0C)</p>'),
    section("الإنتروبي والتلقائية","Entropy","熵",'<p>' + MJ("\\Delta G = \\Delta H - T\\Delta S") + '. ' + MJ("\\Delta G < 0") + ' تلقائي.</p>'),
    section("أمثلة محلولة","Solved Examples","例题",'<p>احتراق CH\u2084: ' + MJ("\\Delta H = [(-393.5)+2(-285.8)]-[-74.8] = -890.3 \\text{ kJ/mol}") + '</p>'),
])

lessons.extend([L4, L5, L6, L7, L8, L9, L10, L11])
print(f"All {len(lessons)} lessons built")

# Replace in data
for lesson in lessons:
    lid = lesson["id"]
    for i, item in enumerate(data):
        if item.get("id") == lid:
            data[i] = lesson
            break

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! Verifying...")
with open(PATH, "r", encoding="utf-8") as f:
    v = json.load(f)
    for item in v:
        if item.get("id","").startswith("chem_"):
            s = item.get("sections",[])
            c = sum(len(x.get("content_ar","")) for x in s)
            print(f"  {item['id']}: {len(s)} sec, ~{c} chars")
