// script.js - search functionality for Arabic CCSA study site
// Simple client‑side search that filters lesson cards and questions based on input

document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.trim().toLowerCase();
        // Filter lesson cards (if present on the page)
        const cards = document.querySelectorAll('.lesson-card');
        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            card.style.display = text.includes(query) ? '' : 'none';
        });
        // Filter questions table (if present)
        const rows = document.querySelectorAll('.question-row');
        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    });
});
