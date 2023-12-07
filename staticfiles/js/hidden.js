function toggleTable() {
    event.preventDefault();
    var tableContainer = document.getElementById('tableContainer');
    var viewAllLink = document.getElementById('viewAllLink');

    if (tableContainer.style.display === 'none') {
        tableContainer.style.display = 'block';
        viewAllLink.textContent = 'Show Less';
    } else {
        tableContainer.style.display = 'none';
        viewAllLink.textContent = 'View All';
    }
}
