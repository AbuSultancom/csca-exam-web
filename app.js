/* === CSCA Trilingual Platform - Core App === */
let currentLang = 'ar';
let translations = {};

// Initialize language
function initLang() {
    const stored = localStorage.getItem('csca_lang');
    const urlLang = new URLSearchParams(window.location.search).get('lang');
    currentLang = urlLang || stored || 'ar';
    if (['ar', 'en', 'zh'].includes(currentLang)) {
        localStorage.setItem('csca_lang', currentLang);
    } else {
        currentLang = 'ar';
        localStorage.setItem('csca_lang', 'ar');
    }
    document.documentElement.lang = currentLang;
    document.body.lang = currentLang;
}

// Switch language and reload
function switchLang(lang) {
    currentLang = lang;
    localStorage.setItem('csca_lang', lang);
    const url = new URL(window.location);
    url.searchParams.set('lang', lang);
    window.location.href = url.toString();
}

// Get translated text
function t(key) {
    const keys = key.split('.');
    let val = translations;
    for (const k of keys) {
        if (val && val[k]) val = val[k];
        else return key;
    }
    if (val && val[currentLang]) return val[currentLang];
    if (val && val['ar']) return val['ar'];
    return key;
}

// Apply translations to all elements with data-i18n attribute
function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const translated = t(key);
        if (translated && translated !== key) {
            el.innerHTML = translated;
        }
    });
    // Update language switcher buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        const lang = btn.getAttribute('data-lang');
        if (lang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

// Load translations and apply
async function loadTranslations() {
    try {
        const res = await fetch('data/translations.json');
        translations = await res.json();
        applyTranslations();
        return true;
    } catch (e) {
        console.error('Failed to load translations:', e);
        return false;
    }
}

// === Language Switcher Component ===
function renderLangSwitcher() {
    const container = document.getElementById('lang-switcher');
    if (!container) return;
    container.innerHTML = '';
    ['ar', 'en', 'zh'].forEach(lang => {
        const btn = document.createElement('button');
        btn.className = `lang-btn${lang === currentLang ? ' active' : ''}`;
        btn.setAttribute('data-lang', lang);
        btn.textContent = lang === 'ar' ? '🇸🇦 عربي' : lang === 'en' ? '🇬🇧 EN' : '🇨🇳 中文';
        btn.onclick = () => switchLang(lang);
        container.appendChild(btn);
    });
}

// Render stats
function renderStats(questionsCount = 327, lessonsCount = 19, linesCount = 8500) {
    document.querySelectorAll('#stat-lessons .stat-number').forEach(el => el.textContent = lessonsCount);
    document.querySelectorAll('#stat-lessons .stat-label').forEach(el => el.textContent = t('stats.lessons'));
    document.querySelectorAll('#stat-questions .stat-number').forEach(el => el.textContent = questionsCount);
    document.querySelectorAll('#stat-questions .stat-label').forEach(el => el.textContent = t('stats.questions'));
    document.querySelectorAll('#stat-subjects .stat-number').forEach(el => el.textContent = 3);
    document.querySelectorAll('#stat-subjects .stat-label').forEach(el => el.textContent = t('stats.subjects'));
    document.querySelectorAll('#stat-lines .stat-number').forEach(el => el.textContent = `${linesCount.toLocaleString()}+`);
    document.querySelectorAll('#stat-lines .stat-label').forEach(el => el.textContent = t('stats.lines'));
}

// === Init ===
document.addEventListener('DOMContentLoaded', async () => {
    initLang();
    await loadTranslations();
    renderLangSwitcher();
});
