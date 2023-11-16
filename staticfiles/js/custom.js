
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search_input');
    const items = document.querySelectorAll('.box');
    const noResults = document.querySelector('.no_results');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.toLowerCase();
        let resultsFound = false;

        items.forEach(function(item) {
            const itemName = item.querySelector('h4').textContent.toLowerCase();

            if (itemName.includes(query)) {
                item.style.display = 'flex';
                resultsFound = true;
            } else {
                item.style.display = 'none';
            }
        });

        if (resultsFound) {
            noResults.style.display = 'none';
        } else {
            noResults.style.display = 'block';
        }
    });
});

