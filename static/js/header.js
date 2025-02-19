
// Impede de fazer pesquisas vazias
function checkSearchQuery() {
    const searchQuery = document.querySelector('input[name="search_query"]').value.trim();
    if (searchQuery === '') {
        return false;
    }
    return true;
}