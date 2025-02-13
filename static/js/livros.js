
// Comentarios
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.novo-comentario form');
    const popup = document.getElementById('login-popup');
    const closePopup = document.querySelector('.close-popup');

    if (form && popup) {
        form.addEventListener('submit', function(event) {
            const isAuthenticated = form.getAttribute('data-authenticated') === 'true';
            if (!isAuthenticated) {
                event.preventDefault();  // Prevent form submission
                popup.style.display = 'flex';  // Show the popup
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

// Favoritos
document.getElementById('favorite-btn').addEventListener('click', function() {
    const livroId = this.getAttribute('data-livro-id');
    fetch(`/livro/${livroId}/favoritar/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            this.textContent = data.is_favorited ? 'Unfavorite' : 'Favorite';
        }
    });
});

// Links dos sites
function openModal(bookId) {
    let modal = document.getElementById("customModal" + bookId);
    if (modal) {
        modal.style.display = "flex";
    }
}

function closeModal(bookId) {
    let modal = document.getElementById("customModal" + bookId);
    if (modal) {
        modal.style.display = "none";
    }
}

window.onclick = function(event) {
    let modals = document.querySelectorAll(".custom-modal");
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};