document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll('form[action$="delete/"] button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            if (!confirm("Are you sure you want to delete this item?")) {
                event.preventDefault();
            }
        });
    });
});
