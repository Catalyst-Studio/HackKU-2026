function togglePasswordVisibility() {
  const passwordInput = document.getElementById('password');
  const eyeIcon = document.getElementById('eye-icon');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    eyeIcon.classList.replace('iconoir-eye-closed', 'iconoir-eye');
  } else {
    passwordInput.type = 'password';
    eyeIcon.classList.replace('iconoir-eye', 'iconoir-eye-closed');
  }
}

function togglePasswordVisibilityConfirm() {
  const passwordInput = document.getElementById('password-confirm');
  const eyeIcon = document.getElementById('eye-icon-confirm');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    eyeIcon.classList.replace('iconoir-eye-closed', 'iconoir-eye');
  } else {
    passwordInput.type = 'password';
    eyeIcon.classList.replace('iconoir-eye', 'iconoir-eye-closed');
  }
}