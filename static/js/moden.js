// Sidebar toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggleBtn');
    const sidebar = document.getElementById('sidebar');
    const container = document.querySelector('.container');

    if (toggleBtn && sidebar && container) {
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            container.classList.toggle('sidebar-open');
        });

        // Close sidebar when a link is clicked on mobile
        const sidebarLinks = sidebar.querySelectorAll('a');
        sidebarLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 768) {
                    sidebar.classList.add('collapsed');
                    container.classList.remove('sidebar-open');
                }
            });
        });
    }
});
