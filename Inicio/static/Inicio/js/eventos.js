/*Add this script to initialize the cart - carrito de compras  */
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Initialize the shopping cart
var shoppingCart = new bootstrap.Offcanvas(document.getElementById('shoppingCart'))


document.addEventListener('DOMContentLoaded', function () {
    // Function to toggle password visibility
    function togglePasswordVisibility(eyeIcon, passwordInput) {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        eyeIcon.classList.toggle('bi-eye');
        eyeIcon.classList.toggle('bi-eye-slash');
    }

    // Setup for login form
    const loginEyeIcon = document.querySelector('#loginModal .bi-eye');
    const loginPassword = document.querySelector('#loginModal input[type="password"]');
    if (loginEyeIcon && loginPassword) {
        loginEyeIcon.addEventListener('click', function () {
            togglePasswordVisibility(this, loginPassword);
        });
    }

    // Setup for registration form - handling both password fields
    const registerPasswordEyeIcon = document.querySelector('#registerModal .password-field .bi-eye');
    const registerConfirmEyeIcon = document.querySelector('#registerModal .confirm-password-field .bi-eye');
    const registerPassword = document.querySelector('#registerModal .password-field input[type="password"]');
    const registerConfirmPassword = document.querySelector('#registerModal .confirm-password-field input[type="password"]');

    if (registerPasswordEyeIcon && registerPassword) {
        registerPasswordEyeIcon.addEventListener('click', function () {
            togglePasswordVisibility(this, registerPassword);
        });
    }

    if (registerConfirmEyeIcon && registerConfirmPassword) {
        registerConfirmEyeIcon.addEventListener('click', function () {
            togglePasswordVisibility(this, registerConfirmPassword);
        });
    }
});
