#!/usr/bin/env python3
"""
Rewrite 8 math lessons with full detail: tables, SVG graphics, examples.
"""
import json
import shutil
from pathlib import Path

DATA = Path("C:/Users/alyhy/csca-exam-web/data/content.json")
BACKUP = DATA.with_suffix(".json.bak")

# Read original
data = json.loads(DATA.read_text(encoding="utf-8"))

def ms(heading_ar, heading_en, content_ar, content_en="", heading_zh="", content_zh=""):
    return {
        "heading_ar": heading_ar,
        "heading_en": heading_en,
        "heading_zh": heading_zh,
        "content_ar": content_ar,
        "content_en": content_en,
        "content_zh": content_zh,
    }

# ============================================================
# LESSON 1: math_sets
# ============================================================
sets_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للمجموعات",
        "Basic Definitions and Concepts of Sets",
        """<p><b>المجموعة</b> هي تجميع لأشياء محددة جيداً تُسمى <b>عناصر</b> (elements). نكتب المجموعة باستخدام الأقواس المعقوفة { }. مثال: \(A = \{1, 2, 3, 4, 5\}\).</p>
<p><b>المصطلحات الأساسية:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المصطلح</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المعنى</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ينتمي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \\in A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a\) عنصر في المجموعة \(A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا ينتمي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \\notin A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a\) ليس عنصراً في \(A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموعة الخالية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\emptyset\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة بلا عناصر</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة جزئية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\subseteq B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كل عنصر في \(A\) موجود في \(B\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد العناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A|\) أو \(n(A)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد عناصر المجموعة \(A\)</td></tr>
</table>
<p><b>طرق تمثيل المجموعات:</b> طريقة السرد مثل \(A = \\{1,2,3\\}\) وطريقة قاعدة المجموعة \(A = \\{x \\mid x \\text{ عدد صحيح موجب و } x \\leq 5\\}\).</p>
<svg width="350" height="220" viewBox="0 0 350 220" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="200" fill="none" stroke="#4361ee" stroke-width="2" rx="10"/>
<text x="310" y="30" fill="#4361ee" font-size="13" font-family="sans-serif" text-anchor="end">U</text>
<circle cx="130" cy="110" r="70" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2.5"/>
<circle cx="220" cy="110" r="70" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2.5"/>
<text x="105" y="60" fill="#4cc9f0" font-size="14" font-family="sans-serif" font-weight="bold">A</text>
<text x="235" y="60" fill="#f72585" font-size="14" font-family="sans-serif" font-weight="bold">B</text>
<text x="130" y="110" fill="#fff" font-size="13" font-family="sans-serif" text-anchor="middle">A∩B</text>
<text x="60" y="130" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle">A−B</text>
<text x="290" y="130" fill="#f72585" font-size="12" font-family="sans-serif" text-anchor="middle">B−A</text>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية لعمليات المجموعات",
        "Basic Laws and Formulas of Set Operations",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">العملية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاتحاد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\cup B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر تنتمي لـ \(A\) أو \(B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\{1,2\\} \\cup \\{2,3\\} = \\{1,2,3\\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التقاطع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\cap B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر في \(A\) و \(B\) معاً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\{1,2\\} \\cap \\{2,3\\} = \\{2\\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الفرق</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A - B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر في \(A\) وليست في \(B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\{1,2\\} - \\{2,3\\} = \\{1\\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المتممة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A'\) أو \(A^c\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر في \(U\) وليست في \(A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A' = U - A\)</td></tr>
</table>
<p><b>قوانين المجموعات الهامة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التجميعي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\cup (B \\cup C) = (A \\cup B) \\cup C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التبادلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\cup B = B \\cup A\)، \(A \\cap B = B \\cap A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التوزيع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ديمورجان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((A \\cup B)' = A' \\cap B'\)</td></tr>
</table>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">قانون ديمورجان: (A∪B)' = A'∩B'</text>
<rect x="5" y="30" width="165" height="120" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="80" y="45" fill="#4361ee" font-size="10" font-family="sans-serif" text-anchor="middle">A∪B</text>
<circle cx="70" cy="95" r="40" fill="rgba(76,201,240,0.3)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="110" cy="95" r="40" fill="rgba(76,201,240,0.3)" stroke="#f72585" stroke-width="2"/>
<rect x="180" y="30" width="165" height="120" fill="rgba(76,201,240,0.15)" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="255" y="45" fill="#4361ee" font-size="10" font-family="sans-serif" text-anchor="middle">A'∩B' (مظللة)</text>
<circle cx="245" cy="95" r="40" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="285" cy="95" r="40" fill="#1a1a2e" stroke="#f72585" stroke-width="2"/>
</svg>"""
    ),
    ms(
        "المنتج الديكارتي ومبدأ العد",
        "Cartesian Product and Counting Principle",
        """<p><b>المنتج الديكارتي:</b> \(A \\times B = \\{(a, b) \\mid a \\in A, b \\in B\\}\) مجموعة الأزواج المرتبة.</p>
<p>\(|A \\times B| = |A| \\times |B|\).</p>
<p><b>مبدأ العد الأساسي:</b> إذا لدينا \(n_1\) طريقة للخطوة الأولى و \(n_2\) للثانية، فعدد الطرق الكلي = \(n_1 \\times n_2 \\times ... \\times n_k\).</p>
<p><b>عدد المجموعات الجزئية:</b> لمجموعة عدد عناصرها \(n\) هو \(2^n\).</p>
<p><b>مبدأ الإستدعاء (لمجموعتين):</b> \(|A \\cup B| = |A| + |B| - |A \\cap B|\).</p>
<p><b>مبدأ الإستدعاء (لثلاث مجموعات):</b> \(|A \\cup B \\cup C| = |A|+|B|+|C| - |A\\cap B| - |A\\cap C| - |B\\cap C| + |A\\cap B\\cap C|\).</p>
<svg width="360" height="180" viewBox="0 0 360 180" xmlns="http://www.w3.org/2000/svg">
<text x="180" y="20" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">المنتج الديكارتي A × B</text>
<ellipse cx="60" cy="60" rx="40" ry="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="45" y="55" fill="#4cc9f0" font-size="11" font-family="sans-serif">A={1,2}</text>
<ellipse cx="300" cy="60" rx="40" ry="25" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/>
<text x="280" y="55" fill="#f72585" font-size="11" font-family="sans-serif">B={a,b}</text>
<path d="M 85 60 L 270 60" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="5,3"/>
<rect x="30" y="100" width="300" height="70" fill="rgba(46,213,115,0.08)" stroke="#2ed573" stroke-width="1.5" rx="8"/>
<text x="180" y="120" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle">A×B = {(1,a),(1,b),(2,a),(2,b)}</text>
<text x="180" y="145" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle">|A×B| = 2×2 = 4</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل على المجموعات",
        "Detailed Solved Examples on Sets",
        """<p><b>مثال 1:</b> \(A = \\{1,2,3,4,5\\}\), \(B = \\{4,5,6,7\\}\), \(U = \\{1,...,10\\}\). جد \(A \\cup B\), \(A \\cap B\), \(A - B\), \(A'\).</p>
<p><b>الحل:</b> \(A \\cup B = \\{1,2,3,4,5,6,7\\}\). \(A \\cap B = \\{4,5\\}\). \(A - B = \\{1,2,3\\}\). \(A' = \\{6,7,8,9,10\\}\).</p>
<p><b>مثال 2:</b> في فصل 80 طالباً، 50 يدرسون رياضيات، 40 فيزياء، 25 كليهما. كم لا يدرس أياً منهما؟</p>
<p><b>الحل:</b> \(|M \\cup P| = 50+40-25 = 65\). \(80-65 = 15\) طالباً.</p>
<p><b>مثال 3:</b> \(A = \\{x,y\\}\), \(B = \\{1,2,3\\}\). جد \(A \\times B\).</p>
<p><b>الحل:</b> \(A \\times B = \\{(x,1),(x,2),(x,3),(y,1),(y,2),(y,3)\\}\). \(|A \\times B| = 2 \\times 3 = 6\).</p>
<p><b>مثال 4:</b> تحقق من \((A \\cup B)' = A' \\cap B'\) حيث \(U=\\{1,...,6\\}\), \(A=\\{1,2,3\\}\), \(B=\\{3,4,5\\}\).</p>
<p><b>الحل:</b> \(A \\cup B = \\{1,2,3,4,5\\}\) → \((A \\cup B)' = \\{6\\}\). \(A'=\\{4,5,6\\}\), \(B'=\\{1,2,6\\}\) → \(A' \\cap B' = \\{6\\}\). ✓</p>
<svg width="300" height="180" viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="280" height="160" fill="none" stroke="#4361ee" stroke-width="2" rx="10"/>
<text x="280" y="28" fill="#4361ee" font-size="11" font-family="sans-serif" text-anchor="end">U=80</text>
<circle cx="110" cy="95" r="50" fill="rgba(76,201,240,0.12)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="190" cy="95" r="50" fill="rgba(247,37,133,0.12)" stroke="#f72585" stroke-width="2"/>
<text x="90" y="60" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle">M=50</text>
<text x="210" y="60" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">P=40</text>
<text x="150" y="95" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">25</text>
<text x="70" y="125" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle">25</text>
<text x="230" y="125" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">15</text>
<text x="260" y="155" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">خارج=15</text>
</svg>"""
    ),
    ms(
        "جداول مقارنة لأنواع المجموعات",
        "Comparison Tables of Set Types",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>منتهية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد محدود من العناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A=\\{1,2,3\\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>غير منتهية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد غير محدود</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\mathbb{N}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>خالية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا تحتوي على عناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\emptyset\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>وحيدة</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عنصر واحد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A=\\{5\\}\)</td></tr>
</table>
<svg width="360" height="240" viewBox="0 0 360 240" xmlns="http://www.w3.org/2000/svg">
<rect x="5" y="5" width="170" height="110" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="90" y="20" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">A∪B</text>
<circle cx="70" cy="65" r="35" fill="rgba(76,201,240,0.25)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="110" cy="65" r="35" fill="rgba(76,201,240,0.25)" stroke="#f72585" stroke-width="2"/>
<rect x="185" y="5" width="170" height="110" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="270" y="20" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">A∩B</text>
<circle cx="250" cy="65" r="35" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="290" cy="65" r="35" fill="rgba(76,201,240,0.08)" stroke="#f72585" stroke-width="2"/>
<circle cx="270" cy="65" r="15" fill="rgba(46,213,115,0.4)" stroke="#2ed573" stroke-width="2"/>
<rect x="5" y="125" width="170" height="110" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="90" y="140" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">A−B</text>
<circle cx="70" cy="185" r="35" fill="rgba(76,201,240,0.25)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="110" cy="185" r="35" fill="rgba(76,201,240,0.08)" stroke="#f72585" stroke-width="2"/>
<rect x="185" y="125" width="170" height="110" fill="rgba(76,201,240,0.15)" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="270" y="140" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">A'</text>
<circle cx="270" cy="185" r="35" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
</svg>"""
    ),
    ms(
        "نصائح CSCA للمجموعات والأخطاء الشائعة",
        "CSCA Tips for Sets and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 <b>ميز بين ∈ و ⊆:</b> \(a \\in A\) عنصر، \(A \\subseteq B\) مجموعة جزئية.</li>
<li>📌 <b>ارسم مخطط فين:</b> ابدأ بملء منطقة التقاطع أولاً.</li>
<li>📌 <b>استخدم مبدأ الإستدعاء:</b> \(|A \\cup B| = |A| + |B| - |A \\cap B|\).</li>
<li>📌 <b>لثلاث مجموعات:</b> استخدم الصيغة الموسعة.</li>
<li>📌 <b>قوانين ديمورجان:</b> \((A \\cup B)' = A' \\cap B'\) و \((A \\cap B)' = A' \\cup B'\).</li>
<li>📌 <b>تذكر:</b> \(\\emptyset \\neq \\{\\emptyset\\}\).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين ∈ و ⊆</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">∈ للعناصر، ⊆ للمجموعات</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان طرح A∩B في |A∪B|</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اطرح التقاطع دائماً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">A−B = B−A</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">غير صحيح، الفرق غير تبادلي</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">∅ = {∅}</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">∅ خالية، {∅} تحوي عنصراً</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية على المجموعات",
        "Additional Exercises on Sets",
        """<p><b>التمرين 1:</b> \(A = \\{x \\in \\mathbb{Z} \\mid -3 < x \\leq 4\\}\), \(B = \\{x \\in \\mathbb{N} \\mid x \\leq 5\\}\). جد \(A \\cup B\), \(A \\cap B\), \(A - B\).</p>
<p><b>الحل:</b> \(A=\\{-2,-1,0,1,2,3,4\\}\), \(B=\\{1,2,3,4,5\\}\). \(A \\cup B = \\{-2,-1,0,1,2,3,4,5\\}\). \(A \\cap B = \\{1,2,3,4\\}\). \(A - B = \\{-2,-1,0\\}\).</p>
<p><b>التمرين 2:</b> استطلاع 100 شخص: 60 يحبون الشاي، 50 القهوة، 30 كليهما. كم لا يحب أياً منهما؟</p>
<p><b>الحل:</b> \(|T \\cup C| = 60+50-30 = 80\). \(100-80 = 20\).</p>
<p><b>التمرين 3:</b> أثبت \((A \\cap B) \\cup (A \\cap B') = A\).</p>
<p><b>الحل:</b> \((A \\cap B) \\cup (A \\cap B') = A \\cap (B \\cup B') = A \\cap U = A\). ✓</p>
<p><b>التمرين 4:</b> \(|A|=10\), \(|B|=7\), \(|A \\cap B|=3\). جد \(|A \\cup B|\) و \(|A-B|\).</p>
<p><b>الحل:</b> \(|A \\cup B| = 10+7-3 = 14\). \(|A-B| = 10-3 = 7\).</p>
<p><b>التمرين 5:</b> مجموعة S تحوي 4 عناصر. كم مجموعة جزئية تحوي ≥ 2 عنصر؟</p>
<p><b>الحل:</b> \(2^4 = 16\) كلياً. \(C(4,0) + C(4,1) = 1+4 = 5\). \(16-5 = 11\).</p>"""
    ),
]

# ============================================================
# LESSON 2: math_inequalities
# ============================================================
ineq_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للمتباينات",
        "Basic Definitions and Concepts of Inequalities",
        """<p><b>المتباينة</b> (Inequality) هي عبارة رياضية تربط مقدارين باستخدام أحد الرموز: \(<, >, \\leq, \\geq\).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المعنى</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(<\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أصغر من</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x < 3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(>\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أكبر من</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x > -1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\leq\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أصغر أو يساوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x \\leq 5\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\geq\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أكبر أو يساوي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x \\geq 0\)</td></tr>
</table>
<p><b>المجالات (Intervals):</b> تمثيل مجموعة الحلول على خط الأعداد.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">نوع المجال</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المتباينة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مغلق \([a,b]\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \\leq x \\leq b\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يشمل a و b</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مفتوح \((a,b)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a < x < b\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا يشمل a ولا b</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نصف مفتوح \([a,b)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \\leq x < b\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يشمل a فقط</td></tr>
</table>
<svg width="350" height="120" viewBox="0 0 350 120" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">تمثيل المتباينات على خط الأعداد</text>
<!-- Number line -->
<line x1="30" y1="60" x2="320" y2="60" stroke="#fff" stroke-width="2"/>
<text x="30" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">-3</text>
<text x="100" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">-2</text>
<text x="175" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">-1</text>
<text x="250" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">0</text>
<text x="320" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">1</text>
<!-- x > -2 -->
<line x1="100" y1="50" x2="320" y2="50" stroke="#4cc9f0" stroke-width="4"/>
<circle cx="100" cy="50" r="6" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<text x="175" y="45" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle">x > -2</text>
<!-- x ≤ 0 -->
<line x1="30" y1="40" x2="250" y2="40" stroke="#f72585" stroke-width="4"/>
<circle cx="250" cy="40" r="6" fill="#f72585" stroke="#f72585" stroke-width="2"/>
<text x="130" y="35" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">x ≤ 0</text>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية للمتباينات",
        "Basic Laws and Formulas of Inequalities",
        """<p><b>خواص المتباينات:</b></p>
<ul>
<li>إذا كان \(a < b\) و \(c > 0\) فإن \(ac < bc\) (الضرب بعدد موجب يحافظ على الإشارة).</li>
<li>إذا كان \(a < b\) و \(c < 0\) فإن \(ac > bc\) (الضرب بعدد سالب يعكس الإشارة).</li>
<li>إذا كان \(a < b\) فإن \(a + c < b + c\) (الجمع لا يغير الإشارة).</li>
<li>إذا كان \(a < b\) و \(b < c\) فإن \(a < c\) (خاصية التعدي).</li>
</ul>
<p><b>المتباينات الخطية:</b> تحل بعزل المتغير مثل المعادلات، مع عكس الإشارة عند الضرب أو القسمة على عدد سالب.</p>
<p><b>المتباينات التربيعية:</b> نستخدم جدول الإشارات بعد إيجاد الجذور.</p>
<p><b>المتباينات ذات القيمة المطلقة:</b></p>
<ul>
<li>\(|x| < a \\iff -a < x < a\) (لـ \(a > 0\)).</li>
<li>\(|x| > a \\iff x < -a\) أو \(x > a\) (لـ \(a > 0\)).</li>
<li>\(|x| \\leq a \\iff -a \\leq x \\leq a\).</li>
<li>\(|x| \\geq a \\iff x \\leq -a\) أو \(x \\geq a\).</li>
</ul>
<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">القيمة المطلقة |x|</text>
<line x1="30" y1="90" x2="320" y2="90" stroke="#fff" stroke-width="2"/>
<text x="175" y="80" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">0</text>
<!-- |x| < a -->
<line x1="100" y1="75" x2="250" y2="75" stroke="#4cc9f0" stroke-width="5"/>
<circle cx="100" cy="75" r="6" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="250" cy="75" r="6" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<text x="175" y="65" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle">|x| < a: -a < x < a</text>
<!-- |x| > a -->
<line x1="30" y1="125" x2="100" y2="125" stroke="#f72585" stroke-width="5"/>
<line x1="250" y1="125" x2="320" y2="125" stroke="#f72585" stroke-width="5"/>
<circle cx="100" cy="125" r="6" fill="#1a1a2e" stroke="#f72585" stroke-width="2"/>
<circle cx="250" cy="125" r="6" fill="#1a1a2e" stroke="#f72585" stroke-width="2"/>
<text x="60" y="120" fill="#f72585" font-size="10" font-family="sans-serif">x < -a</text>
<text x="290" y="120" fill="#f72585" font-size="10" font-family="sans-serif">x > a</text>
<text x="175" y="145" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">|x| > a: x < -a أو x > a</text>
</svg>"""
    ),
    ms(
        "المتباينات النسبية وطرق حلها",
        "Rational Inequalities and Solving Methods",
        """<p><b>حل المتباينات النسبية:</b></p>
<p>الخطوات: ① انقل كل الحدود لطرف واحد. ② وحد المقامات. ③ جد النقاط الحرجة (جذور البسط والمقام). ④ استخدم جدول الإشارات. ⑤ استبعد النقاط التي تجعل المقام صفراً.</p>
<p><b>جدول الإشارات:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المنطقة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">\((-\\infty, x_1)\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">\((x_1, x_2)\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">\((x_2, \\infty)\)</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إشارة العامل الأول</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(+\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(+\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إشارة العامل الثاني</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(+\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إشارة التابع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(+\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(+\)</td></tr>
</table>
<p><b>المتباينات ذات القيمة المطلقة:</b></p>
<p>لحل \(|ax + b| < c\): اكتب \(-c < ax + b < c\) ثم حل.</p>
<p>لحل \(|ax + b| > c\): اكتب \(ax + b < -c\) أو \(ax + b > c\) ثم حل.</p>
<svg width="350" height="130" viewBox="0 0 350 130" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="110" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/>
<text x="175" y="35" fill="#2ed573" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">خطوات حل المتباينة التربيعية</text>
<text x="175" y="55" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">1. انقل جميع الحدود لطرف واحد: ax²+bx+c (>/<) 0</text>
<text x="175" y="72" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">2. حلل المعادلة التربيعية: (x−r₁)(x−r₂) = 0</text>
<text x="175" y="89" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">3. ضع الجذور على خط الأعداد وحدد الفترات</text>
<text x="175" y="106" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">4. اختبر نقطة من كل فترة لتحديد الإشارة</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل على المتباينات",
        "Detailed Solved Examples on Inequalities",
        """<p><b>مثال 1: متباينة خطية</b></p>
<p>حل: \(3(2x - 1) \\geq 5x + 4\).</p>
<p><b>الحل:</b> \(6x - 3 \\geq 5x + 4\) → \(6x - 5x \\geq 4 + 3\) → \(x \\geq 7\). \[\\boxed{x \\in [7, \\infty)}\]</p>

<p><b>مثال 2: متباينة تربيعية</b></p>
<p>حل: \(x^2 - 4 < 0\).</p>
<p><b>الحل:</b> \((x - 2)(x + 2) < 0\). النقاط الحرجة: \(x = -2, x = 2\).</p>
<p>جدول الإشارات: موجب خارج \([-2,2]\) وسالب داخله.</p>
<p>\[\\boxed{x \\in (-2, 2)}\]</p>

<p><b>مثال 3: متباينة نسبية</b></p>
<p>حل: \(\\frac{x - 1}{x + 2} > 0\).</p>
<p><b>الحل:</b> النقاط الحرجة: \(x = 1\) (بسط)، \(x = -2\) (مقام، مستبعد).</p>
<p>\[\\boxed{x \\in (-\\infty, -2) \\cup (1, \\infty)}\]</p>

<p><b>مثال 4: قيمة مطلقة</b></p>
<p>حل: \(|2x - 1| \\leq 3\).</p>
<p><b>الحل:</b> \(-3 \\leq 2x - 1 \\leq 3\) → \(-2 \\leq 2x \\leq 4\) → \(-1 \\leq x \\leq 2\).</p>
<p>\[\\boxed{x \\in [-1, 2]}\]</p>

<p><b>مثال 5: متباينة مركبة</b></p>
<p>حل: \(|x - 3| > 2\).</p>
<p><b>الحل:</b> \(x - 3 < -2\) أو \(x - 3 > 2\) → \(x < 1\) أو \(x > 5\).</p>
<p>\[\\boxed{x \\in (-\\infty, 1) \\cup (5, \\infty)}\]</p>

<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">تمثيل حلول المتباينات</text>
<line x1="30" y1="50" x2="320" y2="50" stroke="#fff" stroke-width="2"/>
<text x="175" y="65" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">0  1  2  3  4  5  6  7</text>
<!-- x ≥ 7 -->
<line x1="265" y1="45" x2="320" y2="45" stroke="#4cc9f0" stroke-width="4"/>
<circle cx="265" cy="45" r="6" fill="#4cc9f0" stroke="#4cc9f0" stroke-width="2"/>
<text x="175" y="40" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle">x ≥ 7</text>
<!-- x < 1 or x > 5 -->
<line x1="30" y1="105" x2="100" y2="105" stroke="#f72585" stroke-width="4"/>
<line x1="255" y1="105" x2="320" y2="105" stroke="#f72585" stroke-width="4"/>
<circle cx="100" cy="105" r="6" fill="#1a1a2e" stroke="#f72585" stroke-width="2"/>
<circle cx="255" cy="105" r="6" fill="#1a1a2e" stroke="#f72585" stroke-width="2"/>
<text x="175" y="125" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">x < 1  أو  x > 5</text>
</svg>"""
    ),
    ms(
        "جداول مقارنة: أنواع المتباينات",
        "Comparison Tables: Types of Inequalities",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الصيغة العامة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">طريقة الحل</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>خطية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(ax + b > 0\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عزل المتغير، عكس الإشارة عند الضرب بسالب</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>تربيعية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(ax^2+bx+c > 0\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تحليل، إيجاد الجذور، جدول الإشارات</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>نسبية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{P(x)}{Q(x)} > 0\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نقل، توحيد مقامات، جدول إشارات، استبعاد Q=0</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>قيمة مطلقة</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|ax+b| > c\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تحويل إلى متباينات بدون قيمة مطلقة</td></tr>
</table>"""
    ),
    ms(
        "نصائح CSCA للمتباينات والأخطاء الشائعة",
        "CSCA Tips for Inequalities and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 اكتب الحل على صورة مجال دائماً.</li>
<li>📌 ارسم خط الأعداد لتجنب الأخطاء.</li>
<li>📌 في المتباينات النسبية، استبعد النقاط التي تجعل المقام صفراً.</li>
<li>📌 للقيمة المطلقة: \(|x| < a \\iff -a < x < a\).</li>
<li>📌 في المتباينات التربيعية، إذا كان \(\\Delta < 0\) والتابع موجب دائماً (a>0) فالحل \(\\mathbb{R}\).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان عكس الإشارة عند الضرب بعدد سالب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إذا ضربت بـ -1، اعكس الإشارة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ضرب متباينة نسبية بالمقام دون مراعاة إشارته</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">استخدم جدول الإشارات بدلاً من الضرب</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان أن \(|x| \\geq 0\) دائماً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القيمة المطلقة لا يمكن أن تكون سالبة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين \(|x| < a\) و \(|x| > a\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">< : بين -a و a، > : خارج ذلك</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية على المتباينات",
        "Additional Exercises on Inequalities",
        """<p><b>التمرين 1:</b> حل \(5x - 3 \\leq 2x + 9\).</p>
<p><b>الحل:</b> \(5x - 2x \\leq 9 + 3\) → \(3x \\leq 12\) → \(x \\leq 4\). \([\\boxed{-\\infty, 4}]\)</p>

<p><b>التمرين 2:</b> حل \(x^2 - 5x + 6 \\geq 0\).</p>
<p><b>الحل:</b> \((x-2)(x-3) \\geq 0\). \[\\boxed{(-\\infty, 2] \\cup [3, \\infty)}\]</p>

<p><b>التمرين 3:</b> حل \(\\frac{2x+1}{x-3} < 0\).</p>
<p><b>الحل:</b> النقاط الحرجة: \(x = -0.5\) (بسط)، \(x = 3\) (مقام). \[\\boxed{(-0.5, 3)}\]</p>

<p><b>التمرين 4:</b> حل \(|3x + 2| \\geq 5\).</p>
<p><b>الحل:</b> \(3x+2 \\leq -5\) أو \(3x+2 \\geq 5\). \(3x \\leq -7\) أو \(3x \\geq 3\). \(x \\leq -\\frac{7}{3}\) أو \(x \\geq 1\).</p>

<p><b>التمرين 5:</b> جد مجال الدالة \(f(x) = \\sqrt{x^2 - 9}\).</p>
<p><b>الحل:</b> \(x^2 - 9 \\geq 0\) → \((x-3)(x+3) \\geq 0\). \[\\boxed{(-\\infty, -3] \\cup [3, \\infty)}\]</p>"""
    ),
]

# ============================================================
# LESSON 3: math_functions
# ============================================================
func_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للدوال",
        "Basic Definitions and Concepts of Functions",
        """<p><b>الدالة</b> (Function) هي علاقة تربط كل عنصر \(x\) في المجال \(X\) بعنصر واحد فقط \(y\) في المدى \(Y\). نكتب \(y = f(x)\).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المصطلح</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجال (Domain)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قيم \(x\) الممكنة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(D_f\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المدى (Range)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قيم \(y = f(x)\) الناتجة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(R_f\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الصورة (Image)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(a)\) قيمة الدالة عند \(a\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(a)\)</td></tr>
</table>
<p><b>أنواع الدوال:</b></p>
<ul>
<li><b>خطية:</b> \(f(x) = mx + b\) (ميلها \(m\) وتقطع \(y\) عند \(b\)).</li>
<li><b>تربيعية:</b> \(f(x) = ax^2 + bx + c\) (رسمها قطع مكافئ).</li>
<li><b>تكعيبية:</b> \(f(x) = ax^3 + bx^2 + cx + d\).</li>
<li><b>نسبية:</b> \(f(x) = \\frac{P(x)}{Q(x)}\).</li>
<li><b>جذرية:</b> \(f(x) = \\sqrt{x}\).</li>
<li><b>أسية:</b> \(f(x) = a^x\).</li>
<li><b>لوغاريتمية:</b> \(f(x) = \\log_a(x)\).</li>
</ul>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">تمثيل سهمي للدالة f: X → Y</text>
<ellipse cx="70" cy="90" rx="50" ry="55" fill="rgba(76,201,240,0.12)" stroke="#4cc9f0" stroke-width="2"/>
<text x="70" y="40" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">X (المجال)</text>
<circle cx="55" cy="75" r="10" fill="#4cc9f0" opacity="0.5"/><text x="55" y="79" fill="#fff" font-size="9" text-anchor="middle">1</text>
<circle cx="55" cy="105" r="10" fill="#4cc9f0" opacity="0.5"/><text x="55" y="109" fill="#fff" font-size="9" text-anchor="middle">2</text>
<circle cx="55" cy="135" r="10" fill="#4cc9f0" opacity="0.5"/><text x="55" y="139" fill="#fff" font-size="9" text-anchor="middle">3</text>
<ellipse cx="280" cy="90" rx="50" ry="55" fill="rgba(247,37,133,0.12)" stroke="#f72585" stroke-width="2"/>
<text x="280" y="40" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">Y (المدى)</text>
<circle cx="265" cy="75" r="10" fill="#f72585" opacity="0.5"/><text x="265" y="79" fill="#fff" font-size="9" text-anchor="middle">a</text>
<circle cx="265" cy="105" r="10" fill="#f72585" opacity="0.5"/><text x="265" y="109" fill="#fff" font-size="9" text-anchor="middle">b</text>
<circle cx="265" cy="135" r="10" fill="#f72585" opacity="0.5"/><text x="265" y="139" fill="#fff" font-size="9" text-anchor="middle">c</text>
<line x1="65" y1="75" x2="255" y2="75" stroke="#2ed573" stroke-width="1.5" marker-end="url(#arrowf)"/>
<line x1="65" y1="105" x2="255" y2="105" stroke="#2ed573" stroke-width="1.5" marker-end="url(#arrowf)"/>
<line x1="65" y1="135" x2="255" y2="135" stroke="#2ed573" stroke-width="1.5" marker-end="url(#arrowf)"/>
<defs><marker id="arrowf" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#2ed573"/></marker></defs>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية للدوال",
        "Basic Laws and Formulas for Functions",
        """<p><b>مجال الدالة:</b> مجموعة قيم \(x\) التي تجعل الدالة معرفة (قيمة حقيقية). نستبعد:</p>
<ul>
<li>المقام = صفر (للدوال النسبية).</li>
<li>ما تحت الجذر الزوجي < 0 (للأعداد الحقيقية).</li>
<li>ما تحت اللوغاريتم ≤ 0.</li>
</ul>
<p><b>اختبار الخط الرأسي:</b> إذا قطع خط رأسي التابع في أكثر من نقطة، فليس دالة.</p>
<p><b>الدالة الزوجية والفردية:</b></p>
<ul>
<li>زوجية: \(f(-x) = f(x)\) (متناظرة حول محور \(y\)).</li>
<li>فردية: \(f(-x) = -f(x)\) (متناظرة حول نقطة الأصل).</li>
</ul>
<p><b>تركيب الدوال:</b> \((f \\circ g)(x) = f(g(x))\). الشرط: \(g(x) \\in D_f\).</p>
<p><b>الدالة العكسية:</b> \(f^{-1}(y) = x\) إذا \(f(x) = y\). الشرط: الدالة one-to-one.</p>
<p><b>لإيجاد العكس:</b> بدل \(x\) و \(y\)، ثم حل لـ \(y\).</p>
<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="120" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/>
<text x="175" y="32" fill="#2ed573" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">تركيب الدوال (f∘g)(x) = f(g(x))</text>
<text x="175" y="55" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">الخطوة 1: احسب g(x) = t (الناتج الوسيط)</text>
<text x="175" y="75" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">الخطوة 2: احسب f(t) = f(g(x)) (الناتج النهائي)</text>
<text x="175" y="100" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">مثال: f(x)=x², g(x)=x+1 → f(g(x)) = (x+1)²</text>
<text x="175" y="120" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">ملاحظة: (f∘g)(x) ≠ (g∘f)(x) عموماً</text>
</svg>"""
    ),
    ms(
        "أنواع الدوال وخصائصها",
        "Types of Functions and Their Properties",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المجال</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المدى</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثابتة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(x)=c\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\{c\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">خطية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(x)=mx+b\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تربيعية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(x)=ax^2+bx+c\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\([y_v, \infty)\) أو \((-\infty, y_v]\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جذرية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(x)=\sqrt{x}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\([0, \infty)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\([0, \infty)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسبية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f(x)=1/x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\setminus\{0\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{R}\setminus\{0\}\)</td></tr>
</table>
<svg width="350" height="180" viewBox="0 0 350 180" xmlns="http://www.w3.org/2000/svg">
<!-- Axes -->
<line x1="175" y1="15" x2="175" y2="170" stroke="#fff" stroke-width="1.5"/>
<line x1="20" y1="95" x2="330" y2="95" stroke="#fff" stroke-width="1.5"/>
<text x="180" y="15" fill="#fff" font-size="10">y</text><text x="325" y="98" fill="#fff" font-size="10">x</text>
<!-- Parabola f(x)=x² -->
<path d="M 175 95 Q 145 30 100 175" fill="none" stroke="#4cc9f0" stroke-width="2.5"/>
<path d="M 175 95 Q 205 30 250 175" fill="none" stroke="#4cc9f0" stroke-width="2.5"/>
<text x="260" y="110" fill="#4cc9f0" font-size="10" font-family="sans-serif">f(x)=x²</text>
<!-- Line f(x)=x -->
<line x1="50" y1="55" x2="300" y2="135" stroke="#f72585" stroke-width="2.5"/>
<text x="310" y="130" fill="#f72585" font-size="10" font-family="sans-serif">f(x)=x</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل على الدوال",
        "Detailed Solved Examples on Functions",
        """<p><b>مثال 1: إيجاد مجال الدالة</b></p>
<p>جد مجال \(f(x) = \\frac{x+1}{x^2 - 4}\).</p>
<p><b>الحل:</b> المقام \(x^2 - 4 \\neq 0\) → \(x^2 \\neq 4\) → \(x \\neq \\pm 2\).</p>
<p>\[\\boxed{D_f = \\mathbb{R} - \\{-2, 2\\}}\]</p>

<p><b>مثال 2: حساب قيمة دالة</b></p>
<p>إذا كانت \(f(x) = 3x - 5\)، جد \(f(2)\) و \(f(a+1)\).</p>
<p><b>الحل:</b> \(f(2) = 3(2) - 5 = 1\). \(f(a+1) = 3(a+1) - 5 = 3a - 2\).</p>

<p><b>مثال 3: الدالة العكسية</b></p>
<p>جد الدالة العكسية لـ \(f(x) = 2x + 3\).</p>
<p><b>الحل:</b> \(y = 2x + 3\) → بدل: \(x = 2y + 3\) → \(2y = x - 3\) → \(y = \\frac{x-3}{2}\).</p>
<p>\[\\boxed{f^{-1}(x) = \\frac{x-3}{2}}\]</p>

<p><b>مثال 4: تركيب الدوال</b></p>
<p>إذا كانت \(f(x) = x^2\) و \(g(x) = x + 1\)، جد \((f \\circ g)(x)\) و \((g \\circ f)(x)\).</p>
<p><b>الحل:</b> \((f \\circ g)(x) = f(g(x)) = f(x+1) = (x+1)^2 = x^2 + 2x + 1\).</p>
<p>\((g \\circ f)(x) = g(f(x)) = g(x^2) = x^2 + 1\).</p>
<p>لاحظ: \((f \\circ g)(x) \\neq (g \\circ f)(x)\).</p>

<p><b>مثال 5: مجال دالة جذرية</b></p>
<p>جد مجال \(f(x) = \\sqrt{x - 2}\).</p>
<p><b>الحل:</b> \(x - 2 \\geq 0\) → \(x \\geq 2\).</p>
<p>\[\\boxed{D_f = [2, \\infty)},\\quad R_f = [0, \\infty)\]</p>

<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="120" fill="rgba(76,201,240,0.06)" stroke="#4cc9f0" stroke-width="2" rx="8"/>
<text x="175" y="35" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">خطوات إيجاد الدالة العكسية</text>
<text x="175" y="58" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">1. اكتب y = f(x)</text>
<text x="175" y="75" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">2. بدل x و y (x = f(y))</text>
<text x="175" y="92" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">3. حل المعادلة لإيجاد y بدلالة x</text>
<text x="175" y="109" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">4. اكتب f⁻¹(x) = ...</text>
<text x="175" y="125" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">تحقق: f(f⁻¹(x)) = x و f⁻¹(f(x)) = x</text>
</svg>"""
    ),
    ms(
        "نصائح CSCA للدوال والأخطاء الشائعة",
        "CSCA Tips for Functions and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 حدد مجال الدالة أولاً قبل أي عملية.</li>
<li>📌 اختبر if الدالة one-to-one (باستخدام الخط الأفقي) قبل البحث عن العكس.</li>
<li>📌 في تركيب الدوال، احسب الدالة الداخلية أولاً.</li>
<li>📌 تذكر أن \(f^{-1}(x) \\neq \\frac{1}{f(x)}\).</li>
<li>📌 في الدوال الزوجية والفردية: زوجية \(f(-x)=f(x)\)، فردية \(f(-x)=-f(x)\).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين (f∘g)(x) و (g∘f)(x)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">احسب من الداخل للخارج</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">f⁻¹(x) = 1/f(x)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">f⁻¹(x) ≠ 1/f(x)، هذا خطأ شائع</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان استبعاد قيم المقام الصفري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المقام ≠ 0 دوماً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدم مراعاة مجال الدالة الداخلية في التركيب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تأكد أن g(x) في مجال f</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية على الدوال",
        "Additional Exercises on Functions",
        """<p><b>التمرين 1:</b> جد مجال \(f(x) = \\frac{3x}{x^2 - 9}\).</p>
<p><b>الحل:</b> \(x^2-9 \\neq 0\) → \(x \\neq \\pm 3\). \[\\boxed{\\mathbb{R} - \\{-3, 3\\}}\]</p>

<p><b>التمرين 2:</b> إذا كانت \(f(x) = x^2 + 2x\) و \(g(x) = 3x - 1\)، جد \((f \\circ g)(2)\).</p>
<p><b>الحل:</b> \(g(2) = 3(2)-1 = 5\). \(f(5) = 25 + 10 = 35\). \[\\boxed{35}\]</p>

<p><b>التمرين 3:</b> جد الدالة العكسية لـ \(f(x) = \\frac{x+1}{x-2}\).</p>
<p><b>الحل:</b> \(y = \\frac{x+1}{x-2}\) → \(x = \\frac{y+1}{y-2}\) → \(x(y-2) = y+1\) → \(xy-2x = y+1\) → \(xy-y = 2x+1\) → \(y(x-1) = 2x+1\) → \(y = \\frac{2x+1}{x-1}\).</p>
<p>\[\\boxed{f^{-1}(x) = \\frac{2x+1}{x-1},\\ x \\neq 1}\]</p>

<p><b>التمرين 4:</b> حدد إذا كانت \(f(x) = x^3 - x\) زوجية أم فردية أم لا.</p>
<p><b>الحل:</b> \(f(-x) = (-x)^3 - (-x) = -x^3 + x = -(x^3 - x) = -f(x)\). إذاً فردية.</p>

<p><b>التمرين 5:</b> جد مجال ومدى \(f(x) = \\sqrt{4 - x^2}\).</p>
<p><b>الحل:</b> \(4-x^2 \\geq 0\) → \(x^2 \\leq 4\) → \(-2 \\leq x \\leq 2\). \[\\boxed{D = [-2,2],\\ R = [0,2]}\]</p>"""
    ),
]

# ============================================================
# LESSON 4: math_geometry
# ============================================================
geom_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية في الهندسة",
        "Basic Definitions and Concepts in Geometry",
        """<p><b>الهندسة</b> (Geometry) تدرس الأشكال والخواص المكانية. النقطة والخط والمستوى مفاهيم أولية.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المفهوم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الزاوية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تقاس بالدرجات (°) أو الراديان (rad). \(180° = \\pi\\ \\text{rad}\).</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المثلث</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموع زواياه = 180°.</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المضلع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموع الزوايا الداخلية = \((n-2) \\times 180°\).</td></tr>
</table>
<p><b>تصنيف المثلثات:</b></p>
<ul>
<li><b>حسب الأضلاع:</b> متساوي الأضلاع (\(3\) أضلاع متساوية)، متساوي الساقين (ضلعان متساويان)، مختلف الأضلاع.</li>
<li><b>حسب الزوايا:</b> حاد الزوايا (كل < 90°)، قائم (زاوية = 90°)، منفرج (زاوية > 90°).</li>
</ul>
<svg width="350" height="180" viewBox="0 0 350 180" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="18" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">أنواع المثلثات</text>
<!-- Equilateral -->
<polygon points="50,145 110,145 80,95" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="80" y="160" fill="#4cc9f0" font-size="10" font-family="sans-serif" text-anchor="middle">متساوي الأضلاع</text>
<!-- Right -->
<polygon points="160,145 240,145 160,85" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/>
<rect x="160" y="125" width="15" height="15" fill="none" stroke="#f72585" stroke-width="1.5"/>
<text x="200" y="160" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">قائم الزاوية</text>
<!-- Isosceles -->
<polygon points="265,145 315,145 290,95" fill="rgba(46,213,115,0.15)" stroke="#2ed573" stroke-width="2"/>
<text x="290" y="160" fill="#2ed573" font-size="10" font-family="sans-serif" text-anchor="middle">متساوي الساقين</text>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية في الهندسة",
        "Basic Laws and Formulas in Geometry",
        """<p><b>نظرية فيثاغورس:</b> في المثلث القائم: \(a^2 + b^2 = c^2\) حيث \(c\) الوتر.</p>
<p><b>تطابق المثلثات:</b> SSS, SAS, ASA, AAS, RHS.</p>
<p><b>تشابه المثلثات:</b> AAA (زوايا متساوية)، SAS (ضلعان متناسبان والزاوية المحصورة)، SSS (الأضلاع الثلاثة متناسبة).</p>

<p><b>قوانين المساحات والحجوم الأساسية:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشكل</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المساحة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الحجم</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مربع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(s^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(s^3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مستطيل</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(L \\times W\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(L \\times W \\times H\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مثلث</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{1}{2} \\times b \\times h\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">دائرة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كرة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(4\\pi r^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{4}{3}\\pi r^3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أسطوانة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(2\\pi r^2 + 2\\pi r h\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r^2 h\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مخروط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r l + \\pi r^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{1}{3}\\pi r^2 h\)</td></tr>
</table>"""
    ),
    ms(
        "الهندسة التحليلية والإحداثيات",
        "Analytic Geometry and Coordinates",
        """<p><b>قوانين الهندسة التحليلية:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المسافة بين نقطتين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نقطة المنتصف</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(M = \\left(\\frac{x_1+x_2}{2}, \\frac{y_1+y_2}{2}\\right)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ميل الخط المستقيم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(m = \\frac{y_2 - y_1}{x_2 - x_1}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معادلة الخط (ميل-مقطع)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(y = mx + b\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معادلة الخط (نقطة-ميل)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(y - y_1 = m(x - x_1)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخطوط المتعامدة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(m_1 \\times m_2 = -1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخطوط المتوازية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(m_1 = m_2\)</td></tr>
</table>
<svg width="350" height="200" viewBox="0 0 350 200" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="180" x2="320" y2="180" stroke="#fff" stroke-width="1.5"/>
<line x1="175" y1="10" x2="175" y2="190" stroke="#fff" stroke-width="1.5"/>
<text x="320" y="195" fill="#fff" font-size="12">x</text><text x="180" y="15" fill="#fff" font-size="12">y</text>
<!-- Line through points -->
<line x1="75" y1="150" x2="275" y2="80" stroke="#4cc9f0" stroke-width="2.5"/>
<circle cx="125" cy="125" r="4" fill="#f72585"/><text x="130" y="120" fill="#f72585" font-size="10">(x₁,y₁)</text>
<circle cx="225" cy="105" r="4" fill="#f72585"/><text x="230" y="100" fill="#f72585" font-size="10">(x₂,y₂)</text>
<text x="175" y="50" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">m = (y₂−y₁)/(x₂−x₁)</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل في الهندسة",
        "Detailed Solved Examples in Geometry",
        """<p><b>مثال 1: نظرية فيثاغورس</b></p>
<p>مثلث قائم وتره 13 سم وأحد أضلاعه 5 سم. جد مساحته.</p>
<p><b>الحل:</b> الضلع الآخر = \(\\sqrt{13^2 - 5^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\) سم.</p>
<p>المساحة = \(\\frac{1}{2} \\times 5 \\times 12 = 30\) سم². \[\\boxed{30\\ \\text{سم}^2}\]</p>

<p><b>مثال 2: حجم ومساحة كرة</b></p>
<p>كرة نصف قطرها 6 سم. جد حجمها ومساحة سطحها.</p>
<p><b>الحل:</b> الحجم = \(\\frac{4}{3}\\pi \\times 216 = 288\\pi \\approx 904.32\) سم³.</p>
<p>المساحة = \(4\\pi \\times 36 = 144\\pi \\approx 452.16\) سم².</p>

<p><b>مثال 3: المسافة بين نقطتين</b></p>
<p>جد المسافة بين \(A(1, 2)\) و \(B(4, 6)\).</p>
<p><b>الحل:</b> \(d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\).</p>

<p><b>مثال 4: معادلة خط مستقيم</b></p>
<p>جد معادلة الخط المار بالنقطتين (1, 3) و (4, 11).</p>
<p><b>الحل:</b> \(m = \\frac{11-3}{4-1} = \\frac{8}{3}\). \(y - 3 = \\frac{8}{3}(x - 1)\).</p>
<p>\[\\boxed{y = \\frac{8}{3}x + \\frac{1}{3}}\]</p>

<p><b>مثال 5: الزاوية الثالثة في مثلث</b></p>
<p><b>الحل:</b> \(180° - 47° - 85° = 48°\).</p>

<svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
<polygon points="50,130 170,130 50,20" fill="rgba(76,201,240,0.12)" stroke="#4cc9f0" stroke-width="2"/>
<rect x="50" y="110" width="15" height="15" fill="none" stroke="#f72585" stroke-width="1.5"/>
<text x="30" y="20" fill="#4cc9f0" font-size="11" font-family="sans-serif">a=5</text>
<text x="100" y="140" fill="#f72585" font-size="11" font-family="sans-serif">b=12</text>
<text x="130" y="60" fill="#2ed573" font-size="11" font-family="sans-serif">c=13</text>
</svg>"""
    ),
    ms(
        "جداول مقارنة: قوانين المساحات والحجوم",
        "Comparison Tables: Area and Volume Formulas",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الشكل</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المساحة الجانبية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المساحة الكلية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الحجم</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مكعب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(4s^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(6s^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(s^3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">متوازي مستطيلات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(2h(L+W)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(2(LW+LH+WH)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(LWH\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أسطوانة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(2\\pi r h\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(2\\pi r^2 + 2\\pi r h\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r^2 h\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كرة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(4\\pi r^2\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{4}{3}\\pi r^3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مخروط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r l\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\pi r^2 + \\pi r l\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{1}{3}\\pi r^2 h\)</td></tr>
</table>
<p>حيث: \(l\) = الارتفاع الجانبي للمخروط = \(\\sqrt{r^2 + h^2}\).</p>"""
    ),
    ms(
        "نصائح CSCA في الهندسة والأخطاء الشائعة",
        "CSCA Tips for Geometry and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 احفظ قوانين المساحات والحجوم جيداً.</li>
<li>📌 في المثلث القائم: الوتر هو أطول ضلع.</li>
<li>📌 ارسم شكلاً توضيحياً دائماً.</li>
<li>📌 انتبه للوحدات: حول كل القياسات لنفس الوحدة.</li>
<li>📌 نصف القطر ≠ القطر. نصف القطر = القطر ÷ 2.</li>
<li>📌 في الدائرة: المساحة = \(\\pi r^2\) والمحيط = \(2\\pi r\).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين مساحة الدائرة ومحيطها</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المساحة \(\\pi r^2\)، المحيط \(2\\pi r\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان تربيع نصف القطر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(r^2\) وليس \(r\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان القسمة على 3 في حجم المخروط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{1}{3}\\pi r^2 h\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تطبيق فيثاغورس على مثلث غير قائم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فيثاغورس للقائم فقط</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية في الهندسة",
        "Additional Exercises in Geometry",
        """<p><b>التمرين 1:</b> جد مساحة مثلث قاعدته 8 سم وارتفاعه 6 سم.</p>
<p><b>الحل:</b> المساحة = \(\\frac{1}{2} \\times 8 \\times 6 = 24\) سم².</p>

<p><b>التمرين 2:</b> أسطوانة نصف قطر قاعدتها 3 سم وارتفاعها 10 سم. جد حجمها.</p>
<p><b>الحل:</b> \(V = \\pi (3)^2 (10) = 90\\pi \\approx 282.6\) سم³.</p>

<p><b>التمرين 3:</b> جد المسافة بين النقطتين (-2, 1) و (3, 5).</p>
<p><b>الحل:</b> \(d = \\sqrt{(3-(-2))^2 + (5-1)^2} = \\sqrt{25+16} = \\sqrt{41}\).</p>

<p><b>التمرين 4:</b> جد معادلة المستقيم المار بـ (2, -3) وميله 4.</p>
<p><b>الحل:</b> \(y + 3 = 4(x - 2)\) → \(y = 4x - 11\).</p>

<p><b>التمرين 5:</b> مخروط نصف قطر قاعدته 5 سم وارتفاعه 12 سم. جد حجمه.</p>
<p><b>الحل:</b> \(V = \\frac{1}{3}\\pi(25)(12) = 100\\pi \\approx 314\) سم³.</p>"""
    ),
]

# ============================================================
# LESSON 5: math_calculus
# ============================================================
calc_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للتفاضل والتكامل",
        "Basic Definitions and Concepts of Calculus",
        """<p>التفاضل والتكامل (Calculus) يدرس التغير المستمر. الفروع الرئيسية: <b>التفاضل</b> (معدل التغير) و<b>التكامل</b> (التراكم).</p>
<p><b>النهايات (Limits):</b> \(\\lim_{x \\to a} f(x) = L\) تعني أن \(f(x)\) تقترب من \(L\) كلما اقترب \(x\) من \(a\).</p>
<p><b>الاتصال (Continuity):</b> الدالة \(f\) متصلة عند \(x=a\) إذا: \(f(a)\) معرفة، \(\\lim_{x\\to a} f(x)\) موجود، و \(\\lim_{x\\to a} f(x) = f(a)\).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المفهوم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف الرياضي</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المعنى الهندسي</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النهاية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\lim_{x\\to a} f(x) = L\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قيمة \(f\) تقترب من \(L\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المشتقة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(f'(a) = \lim_{h\\to 0} \\frac{f(a+h)-f(a)}{h}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ميل المماس عند \(a\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التكامل المحدد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int_a^b f(x)dx\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المساحة تحت المنحني</td></tr>
</table>"""
    ),
    ms(
        "قواعد الاشتقاق الأساسية",
        "Basic Differentiation Rules",
        """<p><b>المشتقة:</b> \(f'(x) = \\frac{dy}{dx} = \\lim_{h\\to 0} \\frac{f(x+h)-f(x)}{h}\).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القاعدة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ثابت</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{d}{dx}(c) = 0\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\frac{d}{dx}(5) = 0\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القوة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{d}{dx}(x^n) = nx^{n-1}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\frac{d}{dx}(x^5) = 5x^4\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((f\\pm g)' = f' \\pm g'\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((x^2+x)' = 2x+1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الضرب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((f\\cdot g)' = f'g + fg'\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((x^2\\sin x)' = 2x\\sin x + x^2\\cos x\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القسمة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\left(\\frac{f}{g}\\right)' = \\frac{f'g - fg'}{g^2}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\frac{d}{dx}(\\frac{x}{x+1}) = \\frac{1}{(x+1)^2}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">السلسلة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((f\\circ g)' = f'(g(x))\\cdot g'(x)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\frac{d}{dx}\\sin(2x) = 2\\cos(2x)\)</td></tr>
</table>"""
    ),
    ms(
        "قواعد التكامل الأساسية",
        "Basic Integration Rules",
        """<p><b>التكامل غير المحدد:</b> \(\\int f(x) dx = F(x) + C\) حيث \(F'(x) = f(x)\) و \(C\) ثابت التكامل.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القاعدة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القوة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int x^n dx = \\frac{x^{n+1}}{n+1}+C\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int x^3 dx = \\frac{x^4}{4}+C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اللوغاريتم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int \\frac{1}{x} dx = \\ln|x|+C\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int_1^2 \\frac{1}{x} dx = \\ln 2\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الأسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int e^x dx = e^x + C\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int e^{2x} dx = \\frac{e^{2x}}{2}+C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الجيب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int \\sin x dx = -\\cos x + C\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int_0^{\\pi} \\sin x dx = 2\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جيب التمام</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int \\cos x dx = \\sin x + C\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int \\cos(3x) dx = \\frac{\\sin(3x)}{3}+C\)</td></tr>
</table>
<p><b>النظرية الأساسية للتكامل:</b> \(\\int_a^b f(x) dx = F(b) - F(a)\) حيث \(F'(x) = f(x)\).</p>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="15" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">التكامل = المساحة تحت المنحني</text>
<path d="M 40 140 Q 100 20 160 80 Q 220 140 300 30" fill="none" stroke="#4cc9f0" stroke-width="2.5"/>
<!-- Area under curve -->
<path d="M 80 140 Q 140 60 200 100 Q 260 140 280 60 L 280 140 Z" fill="rgba(76,201,240,0.2)" stroke="none"/>
<line x1="80" y1="140" x2="80" y2="148" stroke="#f72585" stroke-width="2"/>
<text x="80" y="158" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">a</text>
<line x1="280" y1="140" x2="280" y2="148" stroke="#f72585" stroke-width="2"/>
<text x="280" y="158" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">b</text>
<text x="180" y="130" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">∫₂ f(x) dx</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل في التفاضل والتكامل",
        "Detailed Solved Examples in Calculus",
        """<p><b>مثال 1: الاشتقاق</b></p>
<p>جد مشتقة \(f(x) = 3x^4 - 2x^3 + 5x - 7\).</p>
<p><b>الحل:</b> \(f'(x) = 12x^3 - 6x^2 + 5\).</p>

<p><b>مثال 2: قاعدة السلسلة</b></p>
<p>جد مشتقة \(h(x) = (2x^2 + 1)^5\).</p>
<p><b>الحل:</b> \(h'(x) = 5(2x^2+1)^4 \\cdot 4x = 20x(2x^2+1)^4\).</p>

<p><b>مثال 3: التكامل غير المحدد</b></p>
<p>جد \(\\int (6x^2 - 4x + 3) dx\).</p>
<p><b>الحل:</b> \(= \\frac{6x^3}{3} - \\frac{4x^2}{2} + 3x + C = 2x^3 - 2x^2 + 3x + C\).</p>

<p><b>مثال 4: التكامل المحدد</b></p>
<p>جد \(\\int_0^2 (x^2 + 1) dx\).</p>
<p><b>الحل:</b> \([\\frac{x^3}{3} + x]_0^2 = (\\frac{8}{3} + 2) - (0 + 0) = \\frac{14}{3}\).</p>

<p><b>مثال 5: نهاية</b></p>
<p>جد \(\\lim_{x \\to 3} \\frac{x^2 - 9}{x - 3}\).</p>
<p><b>الحل:</b> \(\\frac{x^2-9}{x-3} = \\frac{(x-3)(x+3)}{x-3} = x+3\). إذن \(\lim_{x\\to 3} (x+3) = 6\).</p>

<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="130" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/>
<text x="175" y="32" fill="#2ed573" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">💡 تطبيقات المشتقة في CSCA</text>
<text x="175" y="55" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">1. معادلة المماس: y − f(a) = f′(a)(x − a)</text>
<text x="175" y="72" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">2. النقاط الحرجة: f′(x) = 0</text>
<text x="175" y="89" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">3. اختبار المشتقة الثانية: f″(a) > 0 → صغرى، f″(a) < 0 → عظمى</text>
<text x="175" y="106" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">4. التزايد/التناقص: f′ > 0 → تزايد، f′ < 0 → تناقص</text>
<text x="175" y="125" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">5. نقطة الانقلاب: f″(x) = 0 وتغير الإشارة</text>
</svg>"""
    ),
    ms(
        "جداول مقارنة في التفاضل والتكامل",
        "Comparison Tables in Calculus",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">العملية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الاشتقاق (Differentiation)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التكامل (Integration)</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المعنى</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معدل التغير</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التراكم/المساحة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الرمز</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{d}{dx}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\int dx\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x^n\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(nx^{n-1}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{x^{n+1}}{n+1}+C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\sin x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\cos x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\cos x + C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\cos x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(-\sin x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\sin x + C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(e^x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(e^x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(e^x + C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\ln x\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{1}{x}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(x\\ln x - x + C\)</td></tr>
</table>
<p>لاحظ أن الاشتقاق والتكامل عمليتان عكسيتان (النظرية الأساسية).</p>"""
    ),
    ms(
        "نصائح CSCA للتفاضل والتكامل والأخطاء الشائعة",
        "CSCA Tips for Calculus and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 احفظ قواعد الاشتقاق الأساسية جيداً.</li>
<li>📌 استخدم قاعدة السلسلة عند اشتقاق الدوال المركبة: اشتق الخارج × اشتق الداخل.</li>
<li>📌 لا تنسَ ثابت التكامل \(C\) في التكامل غير المحدد.</li>
<li>📌 في التكامل المحدد: \(F(b) - F(a)\) (وليس العكس).</li>
<li>📌 تذكر: \(\int x^n = \\frac{x^{n+1}}{n+1}\) لـ \(n \\neq -1\).</li>
<li>📌 \(\int \\frac{1}{x} dx = \\ln|x| + C\) (حالة خاصة).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان قاعدة السلسلة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اشتق الدالة الخارجية × مشتقة الداخلية</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\int x^n = \\frac{x^{n+1}}{n+1}\) حتى \(n=-1\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لـ \(n=-1\): \(\int \\frac{1}{x} dx = \\ln|x|+C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان ثابت التكامل C</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أضف C دائماً في التكامل غير المحدد</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين الاشتقاق والتكامل</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاشتقاق: ينقص الأس بمقدار 1؛ التكامل: يزيد الأس</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية في التفاضل والتكامل",
        "Additional Exercises in Calculus",
        """<p><b>التمرين 1:</b> جد مشتقة \(f(x) = 5x^3 - 2x^2 + 7x - 1\).</p>
<p><b>الحل:</b> \(f'(x) = 15x^2 - 4x + 7\).</p>

<p><b>التمرين 2:</b> جد \(\\int (4x^3 - 6x + 2) dx\).</p>
<p><b>الحل:</b> \(x^4 - 3x^2 + 2x + C\).</p>

<p><b>التمرين 3:</b> جد \(\\int_1^3 (2x + 1) dx\).</p>
<p><b>الحل:</b> \([x^2 + x]_1^3 = (9+3) - (1+1) = 10\).</p>

<p><b>التمرين 4:</b> جد مشتقة \(f(x) = \\sin(3x^2 + 1)\).</p>
<p><b>الحل:</b> \(f'(x) = \\cos(3x^2+1) \\cdot 6x = 6x \\cos(3x^2+1)\).</p>

<p><b>التمرين 5:</b> جد \(\\lim_{x\\to 2} \\frac{x^2 + x - 6}{x - 2}\).</p>
<p><b>الحل:</b> \(\\frac{(x-2)(x+3)}{x-2} = x+3\). \(\lim_{x\\to 2} (x+3) = 5\).</p>"""
    ),
]

# ============================================================
# LESSON 6: math_probability
# ============================================================
prob_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للاحتمالات",
        "Basic Definitions and Concepts of Probability",
        """<p><b>الاحتمال</b> (Probability) هو قياس إمكانية حدوث حدث ما. قيمته بين 0 (مستحيل) و 1 (مؤكد).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المصطلح</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فضاء العينة \(S\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة كل النتائج الممكنة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رمي نرد: \(S=\\{1,2,3,4,5,6\\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحدث \(E\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة جزئية من \(S\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(E=\\{2,4,6\\}\) (عدد زوجي)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاحتمال \(P(E)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\frac{|E|}{|S|}\) (للمنتظم)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(\\text{زوجي}) = \\frac{3}{6} = \\frac{1}{2}\)</td></tr>
</table>
<p><b>خواص الاحتمال:</b> \(P(\\emptyset) = 0\)، \(P(S) = 1\)، \(0 \\leq P(E) \\leq 1\)، \(P(E') = 1 - P(E)\).</p>"""
    ),
    ms(
        "القوانين الأساسية في الاحتمالات",
        "Basic Laws of Probability",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون الجمع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحدثان المتنافيان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A \\cap B) = 0\) → \(P(A \\cup B) = P(A) + P(B)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاحتمال الشرطي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A|B) = \\frac{P(A \\cap B)}{P(B)}\) حيث \(P(B) > 0\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحدثان المستقلان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A \\cap B) = P(A) \\cdot P(B)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدة الضرب العامة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A \\cap B) = P(A) \\cdot P(B|A)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون الاحتمال الكلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(B) = \\sum_i P(A_i) \\cdot P(B|A_i)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قاعدة بايز</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A|B) = \\frac{P(B|A)P(A)}{P(B)}\)</td></tr>
</table>
<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">P(A∪B) = P(A) + P(B) − P(A∩B)</text>
<rect x="30" y="35" width="290" height="100" fill="none" stroke="#4361ee" stroke-width="2" rx="8"/>
<text x="290" y="50" fill="#4361ee" font-size="10" font-family="sans-serif" text-anchor="end">S</text>
<circle cx="120" cy="85" r="40" fill="rgba(76,201,240,0.2)" stroke="#4cc9f0" stroke-width="2"/>
<text x="100" y="55" fill="#4cc9f0" font-size="11" font-family="sans-serif">A</text>
<circle cx="215" cy="85" r="40" fill="rgba(247,37,133,0.2)" stroke="#f72585" stroke-width="2"/>
<text x="235" y="55" fill="#f72585" font-size="11" font-family="sans-serif">B</text>
<text x="168" y="88" fill="#fff" font-size="12" font-family="sans-serif" text-anchor="middle">A∩B</text>
</svg>"""
    ),
    ms(
        "التوزيعات الاحتمالية",
        "Probability Distributions",
        """<p><b>المتغير العشوائي \(X\):</b> دالة من فضاء العينة إلى الأعداد الحقيقية.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التوزيع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">دالة الاحتمال</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\(E(X)\)</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">\(Var(X)\)</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ذو الحدين \(B(n,p)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(X=k)=C(n,k)p^k(1-p)^{n-k}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(np\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(np(1-p)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بواسون \(P(\\lambda)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(X=k)=\\frac{e^{-\\lambda}\\lambda^k}{k!}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\lambda\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\lambda\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">طبيعي \(N(\\mu,\\sigma^2)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">منحنى جرسي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\mu\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\sigma^2\)</td></tr>
</table>
<p><b>قاعدة 68-95-99.7 للتوزيع الطبيعي:</b></p>
<ul>
<li>\(68\\%\) من البيانات ضمن \(\\mu \\pm \\sigma\).</li>
<li>\(95\\%\) من البيانات ضمن \(\\mu \\pm 2\\sigma\).</li>
<li>\(99.7\\%\) من البيانات ضمن \(\\mu \\pm 3\\sigma\).</li>
</ul>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 20 130 Q 120 130 175 40 Q 230 130 330 130" fill="none" stroke="#4cc9f0" stroke-width="2.5"/>
<line x1="175" y1="40" x2="175" y2="140" stroke="#fff" stroke-width="1" stroke-dasharray="4,4"/>
<text x="175" y="150" fill="#fff" font-size="10" font-family="sans-serif" text-anchor="middle">μ</text>
<line x1="120" y1="130" x2="120" y2="135" stroke="#f72585" stroke-width="1.5"/>
<text x="120" y="148" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">μ-σ</text>
<line x1="230" y1="130" x2="230" y2="135" stroke="#f72585" stroke-width="1.5"/>
<text x="230" y="148" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">μ+σ</text>
<text x="175" y="65" fill="#2ed573" font-size="10" font-family="sans-serif" text-anchor="middle">68%</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل في الاحتمالات",
        "Detailed Solved Examples in Probability",
        """<p><b>مثال 1: رمي نردين</b></p>
<p>ما احتمال أن يكون مجموع وجهي نردين متجانسين يساوي 7؟</p>
<p><b>الحل:</b> عدد النتائج = \(6 \\times 6 = 36\).</p>
<p>النتائج المواتية: \((1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\) → 6 نتائج.</p>
<p>\(P = \\frac{6}{36} = \\frac{1}{6}\).</p>

<p><b>مثال 2: سحب بدون إرجاع</b></p>
<p>صندوق يحوي 5 كرات حمراء و 3 زرقاء. سحبت كرتان بدون إرجاع. ما احتمال أن تكونا حمراوين؟</p>
<p><b>الحل:</b> \(P = \\frac{5}{8} \\times \\frac{4}{7} = \\frac{20}{56} = \\frac{5}{14}\).</p>

<p><b>مثال 3: الاستقلال</b></p>
<p>إذا كان \(P(A) = 0.4\)، \(P(B) = 0.5\)، \(P(A \\cap B) = 0.2\). هل A و B مستقلان؟</p>
<p><b>الحل:</b> \(P(A) \\cdot P(B) = 0.4 \\times 0.5 = 0.2 = P(A \\cap B)\). ← مستقلان.</p>

<p><b>مثال 4: الاحتمال الشرطي</b></p>
<p>إذا كان 60% من الطلاب يدرسون الرياضيات، 30% يدرسون الفيزياء، و 20% يدرسون كليهما. ما احتمال أن طالباً يدرس الفيزياء علماً أنه يدرس الرياضيات؟</p>
<p><b>الحل:</b> \(P(P|M) = \\frac{P(M \\cap P)}{P(M)} = \\frac{0.2}{0.6} = \\frac{1}{3}\).</p>

<p><b>مثال 5: التوزيع ذو الحدين</b></p>
<p>نرمي قطعة نقود 5 مرات. ما احتمال الحصول على 3 صور بالضبط؟</p>
<p><b>الحل:</b> \(n=5, k=3, p=\\frac{1}{2}\). \(P = C(5,3)(\\frac{1}{2})^3(\\frac{1}{2})^2 = 10 \\times \\frac{1}{32} = \\frac{10}{32} = \\frac{5}{16}\).</p>

<svg width="300" height="120" viewBox="0 0 300 120" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="280" height="100" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/>
<text x="150" y="35" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">مثال: سحب كرتين بدون إرجاع</text>
<circle cx="70" cy="70" r="18" fill="#f72585"/><text x="70" y="74" fill="#fff" font-size="11" text-anchor="middle">حمراء</text>
<circle cx="120" cy="70" r="18" fill="#f72585"/><text x="120" y="74" fill="#fff" font-size="11" text-anchor="middle">حمراء</text>
<circle cx="170" cy="70" r="18" fill="#f72585"/><text x="170" y="74" fill="#fff" font-size="11" text-anchor="middle">حمراء</text>
<circle cx="220" cy="70" r="18" fill="#f72585"/><text x="220" y="74" fill="#fff" font-size="11" text-anchor="middle">حمراء</text>
<circle cx="270" cy="70" r="18" fill="#f72585"/><text x="270" y="74" fill="#fff" font-size="11" text-anchor="middle">حمراء</text>
</svg>"""
    ),
    ms(
        "جداول مقارنة في الاحتمالات",
        "Comparison Tables in Probability",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المفهوم</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">متنافيان (Mutually Exclusive)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا يمكن حدوثهما معاً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رمي نرد: الحصول على 3 و 5 معاً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مستقلان (Independent)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">وقوع أحدهما لا يؤثر على الآخر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رمي نردين: نتيجة كل نرد مستقلة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تابعان (Dependent)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">وقوع أحدهما يؤثر على الآخر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">سحب كرتين بدون إرجاع</td></tr>
</table>
<p><b>مقارنة بين السحب مع الإرجاع وبدون إرجاع:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مع الإرجاع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">بدون إرجاع</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاستقلال</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مستقل</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تابع</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاحتمال يبقى ثابتاً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نعم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الصيغة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(p^k(1-p)^{n-k}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">متغير</td></tr>
</table>"""
    ),
    ms(
        "نصائح CSCA للاحتمالات والأخطاء الشائعة",
        "CSCA Tips for Probability and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 حدد فضاء العينة بوضوح قبل حساب أي احتمال.</li>
<li>📌 ميز بين السحب مع الإرجاع (مستقل) وبدون إرجاع (تابع).</li>
<li>📌 استخدم الاحتمال المتمم \(P(E') = 1 - P(E)\) عندما يكون الحل أسهل.</li>
<li>📌 في مسائل ذي الحدين: تثبت من \(n\) محدد، استقلال، احتمال ثابت.</li>
<li>📌 "و" → ضرب (تقاطع)، "أو" → جمع (اتحاد) مع طرح التقاطع.</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان طرح التقاطع في قانون الجمع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(P(A\\cup B) = P(A)+P(B)-P(A\\cap B)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين P(A&#124;B) و P(B&#124;A)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">معناهما مختلف تماماً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">اعتبار حدثين مستقلين لصغر P(A∩B)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاستقلال: P(A∩B) = P(A)×P(B)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">P(A&#124;B) = P(A∩B)/P(A)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">P(A&#124;B) = P(A∩B)/P(B)</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية في الاحتمالات",
        "Additional Exercises in Probability",
        """<p><b>التمرين 1:</b> رمي حجري نرد. ما احتمال أن يكون المجموع ≥ 10؟</p>
<p><b>الحل:</b> النتائج المواتية: (4,6),(5,5),(5,6),(6,4),(6,5),(6,6) ← 6. \(P = \\frac{6}{36} = \\frac{1}{6}\).</p>

<p><b>التمرين 2:</b> صندوق به 4 كرات حمراء و 6 زرقاء. سحب كرتين مع الإرجاع. ما احتمال أن تكونا حمراوين؟</p>
<p><b>الحل:</b> \(P = \\frac{4}{10} \\times \\frac{4}{10} = \\frac{16}{100} = \\frac{4}{25}\).</p>

<p><b>التمرين 3:</b> إذا كان \(P(A)=0.3, P(B)=0.4, P(A\\cap B)=0.1\). جد \(P(A\\cup B)\) و \(P(A|B)\).</p>
<p><b>الحل:</b> \(P(A\\cup B) = 0.3+0.4-0.1 = 0.6\). \(P(A|B) = \\frac{0.1}{0.4} = 0.25\).</p>

<p><b>التمرين 4:</b> احتمال إصابة هدف = 0.7. ما احتمال إصابته مرتين في 3 محاولات؟</p>
<p><b>الحل:</b> \(P = C(3,2)(0.7)^2(0.3)^1 = 3 \\times 0.49 \\times 0.3 = 0.441\).</p>

<p><b>التمرين 5:</b> في اختبار CSCA، 80% من الطلاب ينجحون. إذا اختير 3 طلاب عشوائياً، ما احتمال نجاح اثنين فقط؟</p>
<p><b>الحل:</b> \(P = C(3,2)(0.8)^2(0.2)^1 = 3 \\times 0.64 \\times 0.2 = 0.384\).</p>"""
    ),
]

# ============================================================
# LESSON 7: math_sequences
# ============================================================
seq_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للمتتاليات",
        "Basic Definitions and Concepts of Sequences",
        """<p><b>المتتالية</b> (Sequence) هي دالة مجالها الأعداد الطبيعية (أو مجموعة جزئية). نكتب \(a_1, a_2, a_3, ...\) حيث \(a_n\) هو الحد العام.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>حسابية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الفرق \(d\) ثابت: \(a_{n+1} - a_n = d\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">2, 5, 8, 11, ... (\(d=3\))</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>هندسية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النسبة \(r\) ثابتة: \(a_{n+1}/a_n = r\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">1, 2, 4, 8, ... (\(r=2\))</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>عودية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تعرف بدلالة الحدود السابقة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">فيبوناتشي: \(a_n = a_{n-1} + a_{n-2}\)</td></tr>
</table>
<svg width="350" height="150" viewBox="0 0 350 150" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">المتتالية الحسابية (d=3): 2, 5, 8, 11, 14</text>
<circle cx="50" cy="70" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="50" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">2</text>
<circle cx="125" cy="70" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="125" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">5</text>
<circle cx="200" cy="70" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="200" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">8</text>
<circle cx="275" cy="70" r="25" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="275" y="74" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">11</text>
<text x="85" y="50" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">+3</text>
<text x="160" y="50" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">+3</text>
<text x="238" y="50" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">+3</text>
<text x="175" y="125" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">الحد العام: aₙ = 2 + (n−1)×3 = 3n−1</text>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية للمتتاليات",
        "Basic Laws and Formulas for Sequences",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المتتالية الحسابية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المتتالية الهندسية</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحد العام \(a_n\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_n = a_1 + (n-1)d\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_n = a_1 \\cdot r^{n-1}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموع \(n\) حد \(S_n\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(S_n = \\frac{n}{2}[2a_1 + (n-1)d]\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(S_n = a_1 \\cdot \\frac{1-r^n}{1-r}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">صيغة أخرى للمجموع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(S_n = \\frac{n}{2}(a_1 + a_n)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموع اللانهائي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">غير موجود (يتباعد)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(S_\\infty = \\frac{a_1}{1-r}\) لـ \(|r| < 1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط الحسابي: \(\\frac{a+b}{2}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط الهندسي: \(\\sqrt{ab}\)</td></tr>
</table>
<svg width="350" height="140" viewBox="0 0 350 140" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">المتسلسلة الهندسية اللانهائية</text>
<rect x="10" y="30" width="330" height="100" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="8"/>
<text x="175" y="52" fill="#fff" font-size="12" font-family="sans-serif" text-anchor="middle">S∞ = a₁ + a₁r + a₁r² + ... = a₁/(1−r)</text>
<text x="175" y="72" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">الشرط: |r| < 1</text>
<text x="175" y="95" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">مثال: ½ + ¼ + ⅛ + ... = ½/(1−½) = 1</text>
<text x="175" y="115" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle">إذا كان |r| ≥ 1، المتسلسلة تتباعد</text>
</svg>"""
    ),
    ms(
        "نهايات المتتاليات والتقارب",
        "Limits of Sequences and Convergence",
        """<p><b>نهاية المتتالية:</b> \(\\lim_{n\\to\\infty} a_n = L\) إذا تقاربت قيم \(a_n\) من \(L\) كلما كبر \(n\).</p>
<ul>
<li>إذا كانت النهاية موجودة (منتهية) → المتتالية <b>متقاربة</b>.</li>
<li>إذا كانت النهاية غير موجودة (أو لا نهائية) → المتتالية <b>متباعدة</b>.</li>
</ul>
<p><b>نهايات خاصة:</b></p>
<ul>
<li>\(\lim_{n\\to\\infty} \\frac{1}{n} = 0\)</li>
<li>\(\lim_{n\\to\\infty} r^n = 0\) إذا \(|r| < 1\)</li>
<li>\(\lim_{n\\to\\infty} r^n\) غير موجود إذا \(|r| > 1\) (يتباعد)</li>
<li>\(\lim_{n\\to\\infty} \\left(1 + \\frac{1}{n}\\right)^n = e\)</li>
</ul>
<p><b>نظرية الساندويتش (Squeeze):</b> إذا \(b_n \\leq a_n \\leq c_n\) و \(\lim b_n = \\lim c_n = L\)، فإن \(\lim a_n = L\).</p>
<p><b>المتتالية الحسابية:</b> تتباعد دائماً (إلا إذا \(d = 0\)).</p>
<p><b>المتتالية الهندسية:</b> تتقارب إلى 0 إذا \(|r| < 1\)، تتقارب إلى \(a_1\) إذا \(r = 1\)، تتباعد إذا \(|r| > 1\).</p>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل على المتتاليات",
        "Detailed Solved Examples on Sequences",
        """<p><b>مثال 1: متتالية حسابية</b></p>
<p>متتالية حسابية حدها الثالث = 10 والخامس = 16. جد \(d\)، \(a_1\)، و \(a_{10}\).</p>
<p><b>الحل:</b> \(a_3 = a_1 + 2d = 10\)، \(a_5 = a_1 + 4d = 16\).</p>
<p>\(a_5 - a_3 = 2d = 6\) → \(d = 3\). \(a_1 = 10 - 2(3) = 4\). \(a_{10} = 4 + 9(3) = 31\).</p>

<p><b>مثال 2: متتالية هندسية</b></p>
<p>متتالية هندسية حدها الأول = 3 وأساسها = 2. جد \(a_6\) و \(S_6\).</p>
<p><b>الحل:</b> \(a_6 = 3 \\times 2^5 = 3 \\times 32 = 96\).</p>
<p>\(S_6 = 3 \\times \\frac{1-2^6}{1-2} = 3 \\times \\frac{1-64}{-1} = 3 \\times 63 = 189\).</p>

<p><b>مثال 3: متسلسلة هندسية لانهائية</b></p>
<p>جد مجموع المتسلسلة: \(\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + ...\).</p>
<p><b>الحل:</b> \(a_1 = \\frac{1}{2}\)، \(r = \\frac{1}{2}\).</p>
<p>\(S_\\infty = \\frac{1/2}{1-1/2} = \\frac{1/2}{1/2} = 1\).</p>

<p><b>مثال 4: إيجاد عدد الحدود</b></p>
<p>كم حداً من المتتالية الحسابية 3, 7, 11, ... يلزم ليكون المجموع 210؟</p>
<p><b>الحل:</b> \(a_1=3, d=4\). \(S_n = \\frac{n}{2}[6 + (n-1)4] = \\frac{n}{2}[4n+2] = n(2n+1) = 210\).</p>
<p>\(2n^2 + n - 210 = 0\). \(n = \\frac{-1 \\pm \\sqrt{1+1680}}{4} = \\frac{-1 \\pm 41}{4}\). \(n = 10\).</p>

<p><b>مثال 5: تطبيق المتتالية الهندسية</b></p>
<p>كرة ترتد إلى نصف ارتفاعها الساقط. إذا سقطت من ارتفاع 64 سم، ما المسافة الكلية التي تقطعها قبل أن تتوقف؟</p>
<p><b>الحل:</b> سلسلة هندسية: \(a_1 = 64\) (نزول)، ثم \(r = \\frac{1}{2}\).</p>
<p>المسافة الكلية = \(64 + 2(32 + 16 + 8 + ...) = 64 + 2 \\times \\frac{32}{1-1/2} = 64 + 2 \\times 64 = 192\) سم.</p>"""
    ),
    ms(
        "جداول مقارنة: المتتاليات الحسابية والهندسية",
        "Comparison Tables: Arithmetic vs Geometric Sequences",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الخاصية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">حسابية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">هندسية</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العامل الثابت</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الفرق \(d\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">النسبة \(r\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العلاقة بين الحدود</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_{n+1} = a_n + d\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_{n+1} = a_n \\cdot r\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحد العام \(a_n\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_1 + (n-1)d\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a_1 \\cdot r^{n-1}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">السلوك للنهاية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يتباعد (إلا \(d=0\))</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">يتقارب لـ 0 إذا \(|r|<1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\frac{a+b}{2}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\sqrt{ab}\)</td></tr>
</table>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<rect x="5" y="5" width="170" height="150" fill="rgba(76,201,240,0.06)" stroke="#4cc9f0" stroke-width="2" rx="5"/>
<text x="90" y="22" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">حسابية (d=2)</text>
<line x1="30" y1="45" x2="30" y2="140" stroke="#fff" stroke-width="1"/>
<line x1="20" y1="130" x2="160" y2="130" stroke="#fff" stroke-width="1"/>
<circle cx="30" cy="130" r="3" fill="#4cc9f0"/><text x="30" y="145" fill="#4cc9f0" font-size="8" text-anchor="middle">1</text>
<circle cx="50" cy="110" r="3" fill="#4cc9f0"/><text x="50" y="145" fill="#4cc9f0" font-size="8" text-anchor="middle">2</text>
<circle cx="70" cy="90" r="3" fill="#4cc9f0"/><text x="70" y="145" fill="#4cc9f0" font-size="8" text-anchor="middle">3</text>
<circle cx="90" cy="70" r="3" fill="#4cc9f0"/><text x="90" y="145" fill="#4cc9f0" font-size="8" text-anchor="middle">4</text>
<circle cx="110" cy="50" r="3" fill="#4cc9f0"/><text x="110" y="145" fill="#4cc9f0" font-size="8" text-anchor="middle">5</text>
<rect x="180" y="5" width="165" height="150" fill="rgba(247,37,133,0.06)" stroke="#f72585" stroke-width="2" rx="5"/>
<text x="263" y="22" fill="#f72585" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">هندسية (r=0.5)</text>
<line x1="210" y1="45" x2="210" y2="140" stroke="#fff" stroke-width="1"/>
<line x1="200" y1="130" x2="340" y2="130" stroke="#fff" stroke-width="1"/>
<circle cx="210" cy="130" r="3" fill="#f72585"/><text x="210" y="145" fill="#f72585" font-size="8" text-anchor="middle">1</text>
<circle cx="230" cy="110" r="3" fill="#f72585"/><text x="230" y="145" fill="#f72585" font-size="8" text-anchor="middle">2</text>
<circle cx="250" cy="95" r="3" fill="#f72585"/><text x="250" y="145" fill="#f72585" font-size="8" text-anchor="middle">3</text>
<circle cx="270" cy="85" r="3" fill="#f72585"/><text x="270" y="145" fill="#f72585" font-size="8" text-anchor="middle">4</text>
<circle cx="290" cy="78" r="3" fill="#f72585"/><text x="290" y="145" fill="#f72585" font-size="8" text-anchor="middle">5</text>
</svg>"""
    ),
    ms(
        "نصائح CSCA للمتتاليات والأخطاء الشائعة",
        "CSCA Tips for Sequences and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 حدد نوع المتتالية أولاً: حسابية (فرق ثابت) أم هندسية (نسبة ثابتة).</li>
<li>📌 احفظ قانون الحد العام والمجموع لكل نوع.</li>
<li>📌 للمتسلسلة الهندسية اللانهائية: تحقق من \(|r| < 1\) قبل تطبيق القانون.</li>
<li>📌 فرق بين <b>المتتالية</b> (ترتيب الأعداد) و <b>المتسلسلة</b> (مجموع الأعداد).</li>
<li>📌 في المتتالية الهندسية: \(a_n = a_1 r^{n-1}\) وليس \(r^n\).</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين d و r</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">d = الفرق، r = النسبة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">استخدام قانون الحسابية في الهندسية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حدد النوع أولاً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(r^{n-1}\) للحد n (تكتب \(r^n\))</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحد n هو \(a_1 r^{n-1}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان شرط \(|r|<1\) للمتسلسلة اللانهائية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">إذا \(|r|≥1\)، المتسلسة تتباعد</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية على المتتاليات",
        "Additional Exercises on Sequences",
        """<p><b>التمرين 1:</b> متتالية حسابية حدها الأول 7 والرابع 19. جد d و a₁₀.</p>
<p><b>الحل:</b> \(a_4 = 7 + 3d = 19\) → \(3d = 12\) → \(d = 4\). \(a_{10} = 7 + 9(4) = 43\).</p>

<p><b>التمرين 2:</b> متتالية هندسية حدها الأول 4 وأساسها 3. جد a₅ و S₅.</p>
<p><b>الحل:</b> \(a_5 = 4 \\times 3^4 = 4 \\times 81 = 324\). \(S_5 = 4 \\times \\frac{1-3^5}{1-3} = 4 \\times \\frac{1-243}{-2} = 4 \\times 121 = 484\).</p>

<p><b>التمرين 3:</b> جد مجموع المتسلسلة: \(1 + \\frac{1}{3} + \\frac{1}{9} + ...\).</p>
<p><b>الحل:</b> \(a_1=1, r=\\frac{1}{3}\). \(S_\\infty = \\frac{1}{1-1/3} = \\frac{1}{2/3} = \\frac{3}{2}\).</p>

<p><b>التمرين 4:</b> متتالية حسابية: a₂ = 8, a₆ = 20. جد a₁₅.</p>
<p><b>الحل:</b> \(a_6 - a_2 = 4d = 12\) → \(d=3\). \(a_1 = a_2 - d = 5\). \(a_{15} = 5 + 14(3) = 47\).</p>

<p><b>التمرين 5:</b> جد الوسط الهندسي للعددين 4 و 9.</p>
<p><b>الحل:</b> \(\\sqrt{4 \\times 9} = \\sqrt{36} = 6\).</p>"""
    ),
]

# ============================================================
# LESSON 8: statistics (id=8)
# ============================================================
stats_sections = [
    ms(
        "التعريفات والمفاهيم الأساسية للإحصاء",
        "Basic Definitions and Concepts of Statistics",
        """<p><b>الإحصاء</b> (Statistics) هو علم جمع وتحليل وتفسير البيانات.</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المصطلح</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجتمع (Population)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جميع الأفراد أو العناصر محل الدراسة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">العينة (Sample)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة جزئية من المجتمع تمثله</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المتغير (Variable)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">خاصية أو صفة تقاس (عددية أو فئوية)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التكرار (Frequency)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد مرات ظهور قيمة معينة</td></tr>
</table>
<p><b>مقاييس النزعة المركزية:</b> الوسط الحسابي (Mean)، الوسيط (Median)، المنوال (Mode).</p>
<svg width="350" height="160" viewBox="0 0 350 160" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="15" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">توزيع متماثل: Mean = Median = Mode</text>
<path d="M 30 130 Q 175 10 320 130" fill="none" stroke="#4cc9f0" stroke-width="2"/>
<line x1="175" y1="130" x2="175" y2="140" stroke="#f72585" stroke-width="2"/>
<text x="175" y="150" fill="#f72585" font-size="10" font-family="sans-serif" text-anchor="middle">Mean, Median, Mode</text>
<text x="175" y="45" fill="#2ed573" font-size="10" font-family="sans-serif" text-anchor="middle">توزيع متماثل</text>
</svg>"""
    ),
    ms(
        "القوانين والصيغ الأساسية للإحصاء",
        "Basic Laws and Formulas for Statistics",
        """<p><b>مقاييس النزعة المركزية:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المقياس</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط الحسابي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموع القيم ÷ عددها</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\bar{x} = \\frac{\\sum x_i}{n}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسيط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القيمة الوسطى بعد الترتيب</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المنوال</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القيمة الأكثر تكراراً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td></tr>
</table>
<p><b>مقاييس التشتت:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المقياس</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المدى</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">أكبر قيمة − أصغر قيمة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(R = \\max - \\min\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التباين (مجتمع)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">متوسط مربعات الانحرافات</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\sigma^2 = \\frac{\\sum (x_i-\\mu)^2}{N}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التباين (عينة)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">—</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(s^2 = \\frac{\\sum (x_i-\\bar{x})^2}{n-1}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الانحراف المعياري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">جذر التباين</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\\sigma = \\sqrt{\\sigma^2}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المدى الربيعي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Q3 − Q1</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(IQR = Q_3 - Q_1\)</td></tr>
</table>"""
    ),
    ms(
        "الربيعيات والمئينات والمخطط الصندوقي",
        "Quartiles, Percentiles and Box Plot",
        """<p><b>الربيعيات (Quartiles):</b> تقسم البيانات إلى أربعة أجزاء متساوية.</p>
<ul>
<li><b>Q1</b> (الربيع الأول): 25% من البيانات أقل منه.</li>
<li><b>Q2</b> (الربيع الثاني = الوسيط): 50% من البيانات أقل منه.</li>
<li><b>Q3</b> (الربيع الثالث): 75% من البيانات أقل منه.</li>
</ul>
<p><b>المئين (Percentile) k:</b> القيمة التي عندها \(k\\%\) من البيانات أقل منها.</p>
<p><b>المخطط الصندوقي (Box Plot):</b> يعرض Q1, Q2 (الوسيط), Q3, القيم القصوى، والشواذ (outliers).</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المقياس</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الاستخدام</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Q1 − 1.5×IQR</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحد الأدنى للقيم غير الشاذة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">Q3 + 1.5×IQR</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الحد الأعلى للقيم غير الشاذة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">خارج هذا النطاق</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قيم شاذة (Outliers)</td></tr>
</table>
<svg width="350" height="130" viewBox="0 0 350 130" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="18" fill="#4cc9f0" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">المخطط الصندوقي (Box Plot)</text>
<line x1="30" y1="60" x2="320" y2="60" stroke="#fff" stroke-width="2"/>
<!-- Box -->
<rect x="90" y="45" width="150" height="30" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<line x1="165" y1="45" x2="165" y2="75" stroke="#f72585" stroke-width="2"/>
<line x1="90" y1="60" x2="50" y2="60" stroke="#2ed573" stroke-width="2"/>
<line x1="240" y1="60" x2="300" y2="60" stroke="#2ed573" stroke-width="2"/>
<text x="50" y="80" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">min</text>
<text x="90" y="90" fill="#4cc9f0" font-size="9" font-family="sans-serif" text-anchor="middle">Q1</text>
<text x="165" y="90" fill="#f72585" font-size="9" font-family="sans-serif" text-anchor="middle">Med</text>
<text x="240" y="90" fill="#4cc9f0" font-size="9" font-family="sans-serif" text-anchor="middle">Q3</text>
<text x="300" y="80" fill="#2ed573" font-size="9" font-family="sans-serif" text-anchor="middle">max</text>
</svg>"""
    ),
    ms(
        "أمثلة محلولة بالتفصيل في الإحصاء",
        "Detailed Solved Examples in Statistics",
        """<p><b>مثال 1: حساب الوسط والوسيط والمنوال</b></p>
<p>البيانات: 4, 8, 6, 5, 8, 10, 7.</p>
<p><b>الحل:</b> الوسط = \(\\frac{4+8+6+5+8+10+7}{7} = \\frac{48}{7} \\approx 6.86\).</p>
<p>الترتيب: 4, 5, 6, <b>7</b>, 8, 8, 10. الوسيط = 7.</p>
<p>المنوال = 8 (يتكرر مرتين).</p>

<p><b>مثال 2: حساب التباين والانحراف المعياري (مجتمع)</b></p>
<p>البيانات: 2, 4, 6, 8. \(\\mu = \\frac{20}{4} = 5\).</p>
<p>\(\\sigma^2 = \\frac{(2-5)^2+(4-5)^2+(6-5)^2+(8-5)^2}{4} = \\frac{9+1+1+9}{4} = \\frac{20}{4} = 5\).</p>
<p>\(\\sigma = \\sqrt{5} \\approx 2.236\).</p>

<p><b>مثال 3: المدى الربيعي IQR</b></p>
<p>البيانات: 1, 3, 5, 7, 9, 11, 13.</p>
<p><b>الحل:</b> Q1 = 3 (الربع الأول), Q3 = 11 (الربع الثالث). IQR = 11 - 3 = 8.</p>

<p><b>مثال 4: كشف القيم الشاذة</b></p>
<p>باستخدام المثال السابق: الحد الأدنى = Q1 − 1.5×IQR = 3 − 12 = -9.</p>
<p>الحد الأعلى = Q3 + 1.5×IQR = 11 + 12 = 23.</p>
<p>جميع القيم (1 إلى 13) ضمن [-9, 23] → لا توجد قيم شاذة.</p>

<p><b>مثال 5: حساب معامل الاختلاف</b></p>
<p>مجموعتان: A: \(\\mu_A = 50, \\sigma_A = 5\). B: \(\\mu_B = 100, \\sigma_B = 10\).</p>
<p><b>الحل:</b> \(CV_A = \\frac{5}{50} = 0.1 = 10\\%\). \(CV_B = \\frac{10}{100} = 0.1 = 10\\%\).</p>
<p>نسب التشتت متساوية رغم اختلاف المقاييس المطلقة.</p>"""
    ),
    ms(
        "جداول مقارنة في الإحصاء",
        "Comparison Tables in Statistics",
        """<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">المقياس</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">يتأثر بالقيم المتطرفة؟</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);;">الاستخدام الأفضل</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط الحسابي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نعم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بيانات متماثلة بدون قيم شاذة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسيط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بيانات ملتوية أو ذات قيم شاذة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المنوال</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">بيانات فئوية أو اسمية</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المدى</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نعم بشدة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نظرة سريعة على انتشار البيانات</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">IQR</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مقارنة انتشار مجموعات البيانات</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الانحراف المعياري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نعم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المقياس الأكثر استخداماً للتشتت</td></tr>
</table>"""
    ),
    ms(
        "نصائح CSCA للإحصاء والأخطاء الشائعة",
        "CSCA Tips for Statistics and Common Mistakes",
        """<p><b>نصائح هامة:</b></p>
<ul>
<li>📌 في التوزيع المتماثل: الوسط = الوسيط = المنوال.</li>
<li>📌 التواء يميني (Right-skewed): الوسط > الوسيط > المنوال.</li>
<li>📌 التواء يساري (Left-skewed): الوسط < الوسيط < المنوال.</li>
<li>📌 تباين العينة يستخدم (n−1) وليس n (تصحيح بيسل).</li>
<li>📌 الانحراف المعياري = جذر التباين دائماً.</li>
<li>📌 CV = \(\\frac{\\sigma}{\\mu}\) يقارن تشتت مجموعات بوحدات مختلفة.</li>
</ul>
<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);;">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">استخدام n بدلاً من (n−1) في تباين العينة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التباين للعينة: n−1</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين التباين والانحراف المعياري</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الانحراف المعياري = √التباين</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان ترتيب البيانات قبل إيجاد الوسيط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">رتب البيانات أولاً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قسمة مجموع القيم على (n−1) في الوسط</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الوسط = المجموع ÷ n</td></tr>
</table>"""
    ),
    ms(
        "تمارين إضافية في الإحصاء",
        "Additional Exercises in Statistics",
        """<p><b>التمرين 1:</b> البيانات: 12, 15, 18, 20, 22, 25, 30. جد الوسط والوسيط والمنوال.</p>
<p><b>الحل:</b> الوسط = \(\\frac{12+15+18+20+22+25+30}{7} = \\frac{142}{7} \\approx 20.29\). الوسيط = 20. لا يوجد منوال.</p>

<p><b>التمرين 2:</b> جد التباين والانحراف المعياري للبيانات: 3, 7, 11 (مجتمع).</p>
<p><b>الحل:</b> \(\\mu = 7\). \(\\sigma^2 = \\frac{(3-7)^2+(7-7)^2+(11-7)^2}{3} = \\frac{16+0+16}{3} = \\frac{32}{3} \\approx 10.67\). \(\\sigma \\approx 3.27\).</p>

<p><b>التمرين 3:</b> البيانات: 2, 4, 6, 8, 10, 12. جد Q1, Q3, IQR.</p>
<p><b>الحل:</b> Q1 = 4, Q3 = 10. IQR = 10 - 4 = 6.</p>

<p><b>التمرين 4:</b> إذا كان الوسط = 25 والانحراف المعياري = 5، جد معامل الاختلاف.</p>
<p><b>الحل:</b> \(CV = \\frac{5}{25} = 0.2 = 20\\%\).</p>

<p><b>التمرين 5:</b> في دراسة، أوزان 5 طلاب: 55, 60, 65, 70, 75 كجم. جد الوسط والانحراف المعياري (عينة).</p>
<p><b>الحل:</b> \(\\bar{x} = 65\). \(s^2 = \\frac{(55-65)^2+...+(75-65)^2}{4} = \\frac{100+25+0+25+100}{4} = \\frac{250}{4} = 62.5\). \(s \\approx 7.9\).</p>"""
    ),
]

# ============================================================
# Apply all lessons
# ============================================================
lesson_map = {
    "math_sets": sets_sections,
    "math_inequalities": ineq_sections,
    "math_functions": func_sections,
    "math_geometry": geom_sections,
    "math_calculus": calc_sections,
    "math_probability": prob_sections,
    "math_sequences": seq_sections,
}

stats_id = 8  # numeric ID for statistics

print("Starting rewrite of 8 math lessons...")
print(f"Found {len(data)} entries in content.json")

updates = 0
for entry in data:
    lid = entry.get("id")
    if lid in lesson_map:
        entry["sections"] = lesson_map[lid]
        updates += 1
        print(f"✓ Updated: {entry['title_ar']} ({len(lesson_map[lid])} sections)")
    elif lid == stats_id:
        entry["sections"] = stats_sections
        updates += 1
        print(f"✓ Updated: statistics ({len(stats_sections)} sections)")

print(f"\nUpdated {updates} lessons total")

# Save backup
print("Creating backup...")
shutil.copy2(DATA, BACKUP)

# Write updated JSON
print("Writing updated content.json...")
DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

# Print stats
print("\n" + "="*60)
print("STATISTICS (character counts):")
print("="*60)
total_ar = 0
for entry in data:
    lid = entry.get("id")
    if lid in lesson_map or lid == stats_id:
        ar_chars = sum(len(s.get("content_ar", "")) for s in entry["sections"])
        name = entry.get("title_ar", str(lid))
        svg_count = sum(s.get("content_ar", "").count("<svg") for s in entry["sections"])
        table_count = sum(s.get("content_ar", "").count("<table") for s in entry["sections"])
        section_count = len(entry["sections"])
        print(f"  {name:25s}: {ar_chars:6d} chars, {section_count} sections, {svg_count} SVGs, {table_count} tables")
        total_ar += ar_chars

print(f"\n  TOTAL Arabic chars: {total_ar}")
print(f"  TOTAL file size: {DATA.stat().st_size} bytes")
print(f"  Backup saved to: {BACKUP}")
print("Done!")
