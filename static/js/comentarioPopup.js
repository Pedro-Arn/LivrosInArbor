document.addEventListener('DOMContentLoaded', function() {
    const commentField = document.querySelector('textarea[name="corpo"]');
    const popup = document.getElementById('login-popup');
    const closePopup = document.querySelector('.close-popup');

    if (commentField && popup) {
        commentField.addEventListener('click', function() {
            const isAuthenticated = commentField.getAttribute('data-authenticated') === 'true';
            if (!isAuthenticated) {
                popup.style.display = 'flex';
            }
        });

        closePopup.addEventListener('click', function() {
            popup.style.display = 'none';
        });

        window.addEventListener('click', function(event) {
            if (event.target === popup) {
                popup.style.display = 'none';
            }
        });
    }
});