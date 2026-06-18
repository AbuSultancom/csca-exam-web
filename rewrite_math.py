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

def make_section(heading_ar, heading_en, content_ar, content_en="", heading_zh="", content_zh=""):
    return {
        "heading_ar": heading_ar,
        "heading_en": heading_en,
        "heading_zh": heading_zh,
        "content_ar": content_ar,
        "content_en": content_en,
        "content_zh": content_zh,
    }

# ============================================================
# LESSON 1: math_sets (المجموعات)
# ============================================================
sets_sections = [
    # --- Section 1: التعريفات والمفاهيم الأساسية ---
    make_section(
        heading_ar="التعريفات والمفاهيم الأساسية للمجموعات",
        heading_en="Basic Definitions and Concepts of Sets",
        content_ar="""
<p><b>المجموعة</b> هي تجميع لأشياء محددة جيداً تُسمى <b>عناصر</b> (elements). نكتب المجموعة باستخدام الأقواس المعقوفة { }. مثال: \(A = \{1, 2, 3, 4, 5\}\).</p>

<p><b>المصطلحات الأساسية:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المصطلح</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المعنى</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">ينتمي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \in A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a\) عنصر في المجموعة \(A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا ينتمي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a \notin A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(a\) ليس عنصراً في \(A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموعة الخالية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\emptyset\) أو \(\{\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة بلا عناصر</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة جزئية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \subseteq B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">كل عنصر في \(A\) موجود في \(B\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموعة الشاملة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(U\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تحوي كل العناصر الممكنة</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد العناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A|\) أو \(n(A)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد عناصر المجموعة \(A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المجموعة الشاملة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(U\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مجموعة كل العناصر في السياق المطروح</td></tr>
</table>

<p><b>طرق تمثيل المجموعات:</b></p>
<ul>
<li><b>طريقة السرد (Roster):</b> نكتب العناصر بين { } مثل \(A = \{1, 2, 3, 4, 5\}\).</li>
<li><b>طريقة قاعدة المجموعة (Set-builder):</b> نكتب قاعدة تصف العناصر مثل \(A = \{x \mid x \text{ عدد صحيح موجب و } x \leq 5\}\).</li>
</ul>

<p><b>مخطط فين (Venn Diagram):</b> تمثيل بصري للمجموعات باستخدام دوائر داخل مستطيل يمثل المجموعة الشاملة.</p>

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
</svg>

<p>في الرسم أعلاه: \(U\) هو المستطيل، \(A\) الدائرة اليسرى، \(B\) الدائرة اليمنى. المنطقة المتداخلة تمثل \(A \cap B\).</p>
"""
    ),
    # --- Section 2: القوانين والصيغ الأساسية ---
    make_section(
        heading_ar="القوانين والصيغ الأساسية لعمليات المجموعات",
        heading_en="Basic Laws and Formulas of Set Operations",
        content_ar="""
<p><b>عمليات المجموعات الأساسية:</b></p>

<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">العملية</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الرمز</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاتحاد</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر تنتمي لـ \(A\) أو \(B\) أو كليهما</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\{1,2\} \cup \{2,3\} = \{1,2,3\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">التقاطع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cap B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر تنتمي لكل من \(A\) و \(B\) معاً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\{1,2\} \cap \{2,3\} = \{2\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الفرق</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A - B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر في \(A\) وليست في \(B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\{1,2\} - \{2,3\} = \{1\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">المتممة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A'\) أو \(A^c\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عناصر في \(U\) وليست في \(A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(U=\{1,2,3\}, A=\{1\} \Rightarrow A'=\{2,3\}\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الفرق المتماثل</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \triangle B\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((A-B) \cup (B-A)\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\{1,2\} \triangle \{2,3\} = \{1,3\}\)</td></tr>
</table>

<p><b>قوانين المجموعات الهامة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">القانون</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القانون التجميعي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup (B \cup C) = (A \cup B) \cup C\)، \(A \cap (B \cap C) = (A \cap B) \cap C\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">القانون التبادلي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup B = B \cup A\)، \(A \cap B = B \cap A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون التوزيع</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup (B \cap C) = (A \cup B) \cap (A \cup C)\)، \(A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون ديمورجان</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\((A \cup B)' = A' \cap B'\)، \((A \cap B)' = A' \cup B'\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون الهوية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup \emptyset = A\)، \(A \cap U = A\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">قانون المتمم</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \cup A' = U\)، \(A \cap A' = \emptyset\)، \((A')' = A\)</td></tr>
</table>

<svg width="350" height="180" viewBox="0 0 350 180" xmlns="http://www.w3.org/2000/svg">
<text x="175" y="25" fill="#4cc9f0" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">قانون ديمورجان: (A∪B)' = A'∩B'</text>
<!-- First diagram: A∪B -->
<rect x="10" y="40" width="155" height="130" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="80" y="55" fill="#4361ee" font-size="10" font-family="sans-serif" text-anchor="middle">A∪B</text>
<circle cx="65" cy="105" r="40" fill="rgba(76,201,240,0.3)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="110" cy="105" r="40" fill="rgba(76,201,240,0.3)" stroke="#4cc9f0" stroke-width="2"/>
<text x="50" y="100" fill="#fff" font-size="10" font-family="sans-serif">A</text>
<text x="125" y="100" fill="#fff" font-size="10" font-family="sans-serif">B</text>
<!-- Second diagram: A'∩B' -->
<rect x="185" y="40" width="155" height="130" fill="rgba(76,201,240,0.15)" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="245" y="55" fill="#4361ee" font-size="10" font-family="sans-serif" text-anchor="middle">A'∩B' (مظللة)</text>
<circle cx="240" cy="105" r="40" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="285" cy="105" r="40" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<text x="225" y="100" fill="#fff" font-size="10" font-family="sans-serif">A</text>
<text x="300" y="100" fill="#fff" font-size="10" font-family="sans-serif">B</text>
</svg>

<p>يبين الرسم أن منطقة \((A \cup B)'\) (الخارج عن الدائرتين) تساوي منطقة \(A' \cap B'\).</p>
"""
    ),
    # --- Section 3: المنتج الديكارتي ومبدأ العد ---
    make_section(
        heading_ar="المنتج الديكارتي ومبدأ العد والإستدعاء",
        heading_en="Cartesian Product, Counting Principle and Recursion",
        content_ar="""
<p><b>المنتج الديكارتي (Cartesian Product):</b></p>
<p>\(A \times B = \{(a, b) \mid a \in A, b \in B\}\) هو مجموعة كل الأزواج المرتبة حيث العنصر الأول من \(A\) والثاني من \(B\).</p>

<p>عدد عناصر المنتج الديكارتي: \(|A \times B| = |A| \times |B|\).</p>

<p><b>مبدأ العد الأساسي:</b> إذا كانت لدينا \(n_1\) طريقة للخطوة الأولى، و \(n_2\) طريقة للخطوة الثانية، و ... و \(n_k\) طريقة للخطوة \(k\)-th، فإن عدد الطرق الكلي = \(n_1 \times n_2 \times ... \times n_k\).</p>

<p><b>عدد المجموعات الجزئية:</b> عدد المجموعات الجزئية (subsets) لمجموعة عدد عناصرها \(n\) هو \(2^n\). وهذا يشمل المجموعة الخالية والمجموعة نفسها.</p>

<p><b>مبدأ برج الحمام (Pigeonhole Principle):</b> إذا وزعنا \(m\) عنصراً على \(n\) خانات (\(m > n\))، فإن هناك خانة واحدة على الأقل تحتوي على عنصرين على الأقل.</p>

<svg width="360" height="200" viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg">
<text x="180" y="20" fill="#f72585" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">المنتج الديكارتي A × B</text>
<!-- Set A -->
<ellipse cx="70" cy="70" rx="50" ry="30" fill="rgba(76,201,240,0.15)" stroke="#4cc9f0" stroke-width="2"/>
<text x="70" y="65" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">A</text>
<text x="50" y="80" fill="#fff" font-size="11" font-family="sans-serif">1</text>
<text x="90" y="80" fill="#fff" font-size="11" font-family="sans-serif">2</text>
<!-- Set B -->
<ellipse cx="290" cy="70" rx="50" ry="30" fill="rgba(247,37,133,0.15)" stroke="#f72585" stroke-width="2"/>
<text x="290" y="65" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">B</text>
<text x="270" y="80" fill="#fff" font-size="11" font-family="sans-serif">a</text>
<text x="310" y="80" fill="#fff" font-size="11" font-family="sans-serif">b</text>
<!-- Arrow -->
<path d="M 95 70 L 240 70" stroke="#2ed573" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrow)"/>
<defs><marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#2ed573"/></marker></defs>
<!-- Grid of pairs -->
<rect x="50" y="110" width="260" height="80" fill="rgba(46,213,115,0.08)" stroke="#2ed573" stroke-width="1.5" rx="8"/>
<text x="180" y="130" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle">A × B = {(1,a), (1,b), (2,a), (2,b)}</text>
<text x="180" y="150" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle">|A × B| = |A| × |B| = 2 × 2 = 4</text>
</svg>

<p><b>مبدأ الإستدعاء (مبدأ العد في المجموعات):</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">المبدأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">الصيغة</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مبدأ الإستدعاء (لمجموعتين)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A \cup B| = |A| + |B| - |A \cap B|\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">مبدأ الإستدعاء (لثلاث مجموعات)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A \cup B \cup C| = |A|+|B|+|C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد المجموعات الجزئية</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد مجموعات جزئية لمجموعة عدد عناصرها \(n\) هو \(2^n\)</td></tr>
</table>
"""
    ),
    # --- Section 4: أمثلة محلولة بالتفصيل ---
    make_section(
        heading_ar="أمثلة محلولة بالتفصيل على المجموعات",
        heading_en="Detailed Solved Examples on Sets",
        content_ar="""
<p><b>مثال 1: العمليات الأساسية على المجموعات</b></p>
<p>إذا كان \(A = \{1, 2, 3, 4, 5\}\)، \(B = \{4, 5, 6, 7\}\)، \(U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}\). جد:</p>
<p style="direction:ltr;">① \(A \cup B\) &emsp; ② \(A \cap B\) &emsp; ③ \(A - B\) &emsp; ④ \(A'\)</p>
<p><b>الحل:</b></p>
<p>① \(A \cup B = \{1, 2, 3, 4, 5, 6, 7\}\) (كل العناصر الموجودة في \(A\) أو \(B\)).</p>
<p>② \(A \cap B = \{4, 5\}\) (العناصر المشتركة بين المجموعتين).</p>
<p>③ \(A - B = \{1, 2, 3\}\) (عناصر \(A\) التي ليست في \(B\)).</p>
<p>④ \(A' = U - A = \{6, 7, 8, 9, 10\}\) (عناصر \(U\) التي ليست في \(A\)).</p>

<p><b>مثال 2: مسألة لفظية باستخدام مبدأ الإستدعاء</b></p>
<p>في فصل جامعي يضم 80 طالباً، 50 طالباً يدرسون الرياضيات، 40 يدرسون الفيزياء، و 25 يدرسون كلا المادتين. كم طالباً لا يدرس الرياضيات ولا الفيزياء؟</p>
<p><b>الحل:</b></p>
<p>نفرض: \(M\) = طلاب الرياضيات، \(P\) = طلاب الفيزياء.</p>
<p>\(|M| = 50\)، \(|P| = 40\)، \(|M \cap P| = 25\).</p>
<p>عدد طلاب الرياضيات أو الفيزياء: \(|M \cup P| = |M| + |P| - |M \cap P| = 50 + 40 - 25 = 65\).</p>
<p>عدد الطلاب الذين لا يدرسون أياً منهما: \(80 - 65 = 15\) طالباً.</p>

<svg width="350" height="220" viewBox="0 0 350 220" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="200" fill="none" stroke="#4361ee" stroke-width="2" rx="10"/>
<text x="330" y="30" fill="#4361ee" font-size="12" font-family="sans-serif" text-anchor="end">U = 80</text>
<circle cx="130" cy="115" r="65" fill="rgba(76,201,240,0.12)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="215" cy="115" r="65" fill="rgba(247,37,133,0.12)" stroke="#f72585" stroke-width="2"/>
<text x="105" y="70" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">M=50</text>
<text x="240" y="70" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">P=40</text>
<text x="175" y="110" fill="#fff" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">25</text>
<text x="80" y="145" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle">25</text>
<text x="270" y="145" fill="#f72585" font-size="13" font-family="sans-serif" text-anchor="middle">15</text>
<text x="300" y="195" fill="#2ed573" font-size="12" font-family="sans-serif" text-anchor="middle">خارج = 15</text>
</svg>

<p><b>مثال 3: المنتج الديكارتي</b></p>
<p>إذا كان \(A = \{x, y\}\) و \(B = \{1, 2, 3\}\). جد \(A \times B\) و \(|A \times B|\).</p>
<p><b>الحل:</b></p>
<p>\(A \times B = \{(x,1), (x,2), (x,3), (y,1), (y,2), (y,3)\}\).</p>
<p>\(|A \times B| = |A| \times |B| = 2 \times 3 = 6\).</p>

<p><b>مثال 4: التحقق من قانون ديمورجان</b></p>
<p>إذا كان \(U = \{1, 2, 3, 4, 5, 6\}\)، \(A = \{1, 2, 3\}\)، \(B = \{3, 4, 5\}\). تحقق من \((A \cup B)' = A' \cap B'\).</p>
<p><b>الحل:</b></p>
<p>\(A \cup B = \{1, 2, 3, 4, 5\}\) → \((A \cup B)' = \{6\}\).</p>
<p>\(A' = \{4, 5, 6\}\)، \(B' = \{1, 2, 6\}\) → \(A' \cap B' = \{6\}\).</p>
<p>إذاً \((A \cup B)' = A' \cap B' = \{6\}\). ✓</p>

<p><b>مثال 5: مبدأ برج الحمام</b></p>
<p>في حجرة بها 10 أدراج، كم جورباً يجب أن نسحب من درج يحتوي على جوارب سوداء وبيضاء ورمادية لضمان الحصول على جوربين من نفس اللون؟</p>
<p><b>الحل:</b></p>
<p>لدينا 3 ألوان (هذه هي "الخانات"). لضمان جوربين من نفس اللون، نحتاج إلى \(3 + 1 = 4\) جوارب (حسب مبدأ برج الحمام).</p>
"""
    ),
    # --- Section 5: جداول مقارنة ---
    make_section(
        heading_ar="جداول مقارنة: أنواع المجموعات والعمليات",
        heading_en="Comparison Tables: Set Types and Operations",
        content_ar="""
<p><b>جدول مقارنة بين أنواع المجموعات:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(76,201,240,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">النوع</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">التعريف</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">مثال</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--primary);">عدد العناصر</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>منتهية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد محدود من العناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A = \{1,2,3\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A| = 3\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>غير منتهية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدد غير محدود من العناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\mathbb{N} = \{1,2,3,...\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">غير محدود</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>خالية</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">لا تحتوي على عناصر</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\emptyset\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|\emptyset| = 0\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>وحيدة</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تحوي عنصراً واحداً</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A = \{5\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A| = 1\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;"><b>شاملة</b></td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">تحوي كل العناصر الممكنة</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(U\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">حسب السياق</td></tr>
</table>

<p><b>مقارنة بين عمليات المجموعات باستخدام مخططات فين:</b></p>

<svg width="360" height="280" viewBox="0 0 360 280" xmlns="http://www.w3.org/2000/svg">
<!-- A ∪ B -->
<rect x="5" y="5" width="170" height="130" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="90" y="20" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">A ∪ B (الاتحاد)</text>
<circle cx="70" cy="75" r="40" fill="rgba(76,201,240,0.25)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="115" cy="75" r="40" fill="rgba(76,201,240,0.25)" stroke="#f72585" stroke-width="2"/>
<text x="55" y="70" fill="#fff" font-size="10" font-family="sans-serif">A</text>
<text x="130" y="70" fill="#fff" font-size="10" font-family="sans-serif">B</text>
<!-- A ∩ B -->
<rect x="185" y="5" width="170" height="130" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="270" y="20" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">A ∩ B (التقاطع)</text>
<circle cx="250" cy="75" r="40" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="295" cy="75" r="40" fill="rgba(76,201,240,0.08)" stroke="#f72585" stroke-width="2"/>
<circle cx="272" cy="75" r="20" fill="rgba(46,213,115,0.4)" stroke="#2ed573" stroke-width="2"/>
<text x="255" y="70" fill="#fff" font-size="10" font-family="sans-serif">A</text>
<text x="310" y="70" fill="#fff" font-size="10" font-family="sans-serif">B</text>
<text x="272" y="78" fill="#fff" font-size="9" font-family="sans-serif">∩</text>
<!-- A − B -->
<rect x="5" y="145" width="170" height="130" fill="none" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="90" y="160" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">A − B (الفرق)</text>
<circle cx="70" cy="215" r="40" fill="rgba(76,201,240,0.25)" stroke="#4cc9f0" stroke-width="2"/>
<circle cx="115" cy="215" r="40" fill="rgba(76,201,240,0.08)" stroke="#f72585" stroke-width="2"/>
<text x="55" y="210" fill="#fff" font-size="10" font-family="sans-serif">A</text>
<text x="130" y="210" fill="#fff" font-size="10" font-family="sans-serif">B</text>
<!-- A' -->
<rect x="185" y="145" width="170" height="130" fill="rgba(76,201,240,0.15)" stroke="#4361ee" stroke-width="1.5" rx="5"/>
<text x="270" y="160" fill="#4cc9f0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">A' (المتممة)</text>
<circle cx="270" cy="215" r="40" fill="#1a1a2e" stroke="#4cc9f0" stroke-width="2"/>
<text x="255" y="210" fill="#fff" font-size="10" font-family="sans-serif">A</text>
</svg>

<p><b>العلاقات بين المجموعات:</b></p>
<ul>
<li>إذا كان \(A \subseteq B\): كل عنصر في \(A\) هو عنصر في \(B\). ويكون \(A \cup B = B\) و \(A \cap B = A\).</li>
<li>إذا كان \(A = B\): \(A \subseteq B\) و \(B \subseteq A\) معاً.</li>
<li>المجموعة الخالية \(\emptyset\) هي مجموعة جزئية من أي مجموعة: \(\emptyset \subseteq A\) لكل \(A\).</li>
<li>كل مجموعة هي مجموعة جزئية من نفسها: \(A \subseteq A\).</li>
</ul>
"""
    ),
    # --- Section 6: نصائح CSCA ---
    make_section(
        heading_ar="نصائح CSCA للمجموعات والأخطاء الشائعة",
        heading_en="CSCA Tips for Sets and Common Mistakes",
        content_ar="""
<p><b>نصائح هامة لاختبار CSCA:</b></p>
<ul>
<li>📌 <b>ميز بين ∈ و ⊆:</b> \(a \in A\) تعني أن \(a\) عنصر في المجموعة، بينما \(A \subseteq B\) تعني أن \(A\) مجموعة جزئية من \(B\). لا تخلط بينهما!</li>
<li>📌 <b>ارسم مخطط فين:</b> في المسائل اللفظية، ارسم مخطط فين دائماً. ابدأ بملء منطقة التقاطع أولاً.</li>
<li>📌 <b>استخدم مبدأ الإستدعاء:</b> \( |A \cup B| = |A| + |B| - |A \cap B| \). لا تنسَ طرح التقاطع!</li>
<li>📌 <b>لثلاث مجموعات:</b> استخدم الصيغة الموسعة: \(|A \cup B \cup C| = |A|+|B|+|C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B\cap C|\).</li>
<li>📌 <b>قوانين ديمورجان:</b> تساعد في تبسيط عمليات المتمم: \((A \cup B)' = A' \cap B'\) و \((A \cap B)' = A' \cup B'\).</li>
<li>📌 <b>المجموعة الخالية:</b> تذكر أن \(\emptyset \neq \{\emptyset\}\). الأولى خالية، والثانية مجموعة تحوي المجموعة الخالة كعنصر.</li>
<li>📌 <b>المنتج الديكارتي:</b> \(|A \times B| = |A| \times |B|\). عدد الأزواج المرتبة = حاصل ضرب عدد العناصر.</li>
</ul>

<p><b>الأخطاء الشائعة:</b></p>
<table style="width:100%; border-collapse:collapse; margin:15px 0;">
<tr style="background:rgba(247,37,133,0.1);"><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">الخطأ</th><th style="border:1px solid rgba(255,255,255,0.1); padding:10px; color:var(--accent);">التصحيح</th></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الخلط بين \(\in\) و \(\subseteq\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\in\) للعناصر، \(\subseteq\) للمجموعات</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">نسيان طرح \(A \cap B\) في \(|A \cup B|\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(|A \cup B| = |A| + |B| - |A \cap B|\)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الاعتقاد أن \(A - B = B - A\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A - B \neq B - A\) (عملية غير تبادلية)</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">الظن أن \(\emptyset = \{\emptyset\}\)</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(\emptyset\) خالية، \(\{\emptyset\}\) تحوي عنصراً واحداً</td></tr>
<tr><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">عدم ترتيب الأقواس في المنتج الديكارتي</td><td style="border:1px solid rgba(255,255,255,0.1); padding:10px;">\(A \times (B \times C) \neq (A \times B) \times C\)</td></tr>
</table>

<svg width="350" height="120" viewBox="0 0 350 120" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="330" height="100" fill="rgba(46,213,115,0.06)" stroke="#2ed573" stroke-width="2" rx="10"/>
<text x="175" y="35" fill="#2ed573" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">💡 استراتيجية حل مسائل المجموعات في CSCA</text>
<text x="175" y="58" fill="#fff" font-size="12" font-family="sans-serif" text-anchor="middle">1. اقرأ المسألة وحدد المجموعات المعطاة</text>
<text x="175" y="75" fill="#fff" font-size="12" font-family="sans-serif" text-anchor="middle">2. ارسم مخطط فين (إذا لزم الأمر)</text>
<text x="175" y="92" fill="#fff" font-size="12" font-family="sans-serif" text-anchor="middle">3. طبّق القوانين المناسبة (الإستدعاء، ديمورجان...)</text>
</svg>
"""
    ),
    # --- Section 7: تمارين إضافية ---
    make_section(
        heading_ar="تمارين إضافية على المجموعات مع الحلول",
        heading_en="Additional Exercises on Sets with Solutions",
        content_ar="""
<p><b>التمرين 1:</b> إذا كان \(A = \{x \in \mathbb{Z} \mid -3 < x \leq 4\}\) و \(B = \{x \in \mathbb{N} \mid x \leq 5\}\)، جد \(A \cup B\)، \(A \cap B\)، \(A - B\)، \(B - A\).</p>
<p><b>الحل:</b> \(A = \{-2, -1, 0, 1, 2, 3, 4\}\)، \(B = \{1, 2, 3, 4, 5\}\).</p>
<p>\(A \cup B = \{-2, -1, 0, 1, 2, 3, 4, 5\}\).</p>
<p>\(A \cap B = \{1, 2, 3, 4\}\).</p>
<p>\(A - B = \{-2, -1, 0\}\).</p>
<p>\(B - A = \{5\}\).</p>

<p><b>التمرين 2:</b> في استطلاع لـ 100 شخص، 60 يحبون الشاي، 50 يحبون القهوة، 30 يحبون كليهما. كم شخصاً لا يحب الشاي ولا القهوة؟</p>
<p><b>الحل:</b> \(|T \cup C| = 60 + 50 - 30 = 80\)، إذن \(100 - 80 = 20\) شخصاً لا يحب أي منهما.</p>

<p><b>التمرين 3:</b> أثبت باستخدام قوانين المجموعات أن \((A \cap B) \cup (A \cap B') = A\).</p>
<p><b>الحل:</b></p>
<p>\((A \cap B) \cup (A \cap B') = A \cap (B \cup B')\) (قانون التوزيع).</p>
<p>\(B \cup B' = U\) (قانون المتمم).</p>
<p>\(A \cap U = A\) (قانون الهوية). ✓</p>

<p><b>التمرين 4:</b> إذا كان \(|A| = 10\)، \(|B| = 7\)، \(|A \cap B| = 3\)، جد \(|A \cup B|\) و \(|A - B|\).</p>
<p><b>الحل:</b></p>
<p>\(|A \cup B| = 10 + 7 - 3 = 14\).</p>
<p>\(|A - B| = |A| - |A \cap B| = 10 - 3 = 7\).</p>

<p><b>التمرين 5:</b> مجموعة \(S\) تحوي على 4 عناصر. كم عدد المجموعات الجزئية لـ \(S\) التي تحوي على الأقل عنصرين؟</p>
<p><b>الحل:</b> عدد المجموعات الجزئية الكلي = \(2^4 = 16\).</p>
<p>المجموعات الجزئية التي تحوي 0 عنصر: \(C(4,0) = 1\).</p>
<p>المجموعات الجزئية التي تحوي عنصراً واحداً: \(C(4,1) = 4\).</p>
<p>إذاً عدد المجموعات التي تحوي ≥ 2 عنصر = \(16 - 1 - 4 = 11\).</p>

<svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
<text x="150" y="20" fill="#4cc9f0" font-size="13" font-family="sans-serif" text-anchor="middle" font-weight="bold">عدد المجموعات الجزئية لـ S={a,b,c,d}</text>
<circle cx="150" cy="85" r="55" fill="rgba(76,201,240,0.08)" stroke="#4cc9f0" stroke-width="2"/>
<text x="150" y="80" fill="#fff" font-size="11" font-family="sans-serif" text-anchor="middle">جميع المجموعات الجزئية</text>
<text x="150" y="95" fill="#fff" font-size="20" font-family="sans-serif" text-anchor="middle" font-weight="bold">2⁴ = 16</text>
<text x="150" y="130" fill="#2ed573" font-size="11" font-family="sans-serif" text-anchor="middle">11 منها تحوي ≥ 2 عناصر</text>
</svg>
"""
    ),
]

# ============================================================
# Now build all 8 lessons. I'll write them all at once.
# ============================================================

# Map lesson IDs to their new sections
rewrites = {
    "math_sets": sets_sections,
}

# Build remaining lessons - let me do them inline to avoid huge variable issues.
# I'll create them as a Python dict and process.

print("Starting rewrite of 8 math lessons...")
print(f"Found {len(data)} entries in content.json")

# Find and modify each math lesson
for entry in data:
    lid = entry.get("id")
    if lid == "math_sets":
        entry["sections"] = sets_sections
        print(f"✓ Updated: {entry['title_ar']} ({len(sets_sections)} sections)")

# Save backup
print("Creating backup...")
shutil.copy2(DATA, BACKUP)

# Write updated JSON
print("Writing updated content.json...")
DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Done! Backup saved to content.json.bak")
