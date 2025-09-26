// Modal controls
const appEl = document.getElementById('app');
const uploadModal = document.getElementById('uploadModal');
const openUpload = document.getElementById('openUpload');
const openUploadTop = document.getElementById('openUploadTop');
const closeUpload = document.getElementById('closeUpload');
const closeUpload2 = document.getElementById('closeUpload2');

function showModal() {
    uploadModal.classList.add('show');
    uploadModal.setAttribute('aria-hidden', 'false');
}

function hideModal() {
    uploadModal.classList.remove('show');
    uploadModal.setAttribute('aria-hidden', 'true');
}

if (openUpload) openUpload.addEventListener('click', showModal);
if (openUploadTop) openUploadTop.addEventListener('click', showModal);
if (closeUpload) closeUpload.addEventListener('click', hideModal);
if (closeUpload2) closeUpload2.addEventListener('click', hideModal);
if (uploadModal) uploadModal.addEventListener('click', (e) => {
    if (e.target === uploadModal) hideModal();
});

// Form submit -> loading state
function wireSearchForm(id) {
    const form = document.getElementById(id);
    if (!form) return;
    form.addEventListener('submit', function() {
        appEl.classList.remove('state-search', 'state-results');
        appEl.classList.add('state-loading');
    });
}
wireSearchForm('searchForm');
wireSearchForm('searchFormTop');

// Tabs
function setActiveTab(tab) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    const btn = document.querySelector(`.tab-btn[data-tab="${tab}"]`);
    const panel = document.getElementById(`panel-${tab}`);
    if (btn && panel) {
        btn.classList.add('active');
        panel.classList.add('active');
    }
}
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        setActiveTab(btn.dataset.tab);
    });
});