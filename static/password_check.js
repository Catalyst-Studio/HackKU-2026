const passwordInput = document.getElementById("password");
const requirementsList = document.getElementById("requirements-list");

passwordInput.onfocus = () => { requirementsList.classList.remove("d-none"); };
passwordInput.onblur = () => { requirementsList.classList.add("d-none"); };

function checkPassword() {
    const passwordInput = document.getElementById('password');
    const passwordConfirmInput = document.getElementById('password-confirm');
    let password = '';
    let passwordConfirm = '';
    if (passwordConfirmInput == null) {
        return true
    } else {
        password = passwordInput.value;
        passwordConfirm = passwordConfirmInput.value;
    }

    const hasUppercaseIndicator = document.getElementById("uppercase");
    const hasLowercaseIndicator = document.getElementById("lowercase");
    const hasNumberIndicator = document.getElementById("number");
    const hasSpecialIndicator = document.getElementById("special");
    const hasLengthIndicator = document.getElementById("length");

    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const hasSpecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password);
    const hasLength = password.length >= 8;

    if (hasUppercase) {
        hasUppercaseIndicator.classList.add("text-success");
        hasUppercaseIndicator.classList.remove("text-danger");
    } else {
        hasUppercaseIndicator.classList.remove("text-success");
        hasUppercaseIndicator.classList.add("text-danger");
    }

    if (hasLowercase) {
        hasLowercaseIndicator.classList.add("text-success");
        hasLowercaseIndicator.classList.remove("text-danger");
    } else {
        hasLowercaseIndicator.classList.remove("text-success");
        hasLowercaseIndicator.classList.add("text-danger");
    }

    if (hasNumber) {
        hasNumberIndicator.classList.add("text-success");
        hasNumberIndicator.classList.remove("text-danger");
    } else {
        hasNumberIndicator.classList.remove("text-success");
        hasNumberIndicator.classList.add("text-danger");
    }

    if (hasSpecial) {
        hasSpecialIndicator.classList.add("text-success");
        hasSpecialIndicator.classList.remove("text-danger");
    } else {
        hasSpecialIndicator.classList.remove("text-success");
        hasSpecialIndicator.classList.add("text-danger");
    }

    if (hasLength) {
        hasLengthIndicator.classList.add("text-success");
        hasLengthIndicator.classList.remove("text-danger");
    } else {
        hasLengthIndicator.classList.remove("text-success");
        hasLengthIndicator.classList.add("text-danger");
    }

    if (hasUppercase && hasLowercase && hasNumber && hasSpecial && hasLength) {
        passwordInput.classList.remove('is-invalid');
        passwordInput.classList.add('is-valid');
        if (password === passwordConfirm ) {
            passwordConfirmInput.classList.add('is-valid');
            passwordConfirmInput.classList.remove('is-invalid');
            return true
        } else {
            passwordConfirmInput.classList.remove('is-valid');
            passwordConfirmInput.classList.add('is-invalid');
            return false
        }
    } else {
        passwordInput.classList.remove('is-valid');
        passwordInput.classList.add('is-invalid');
        if ((password === passwordConfirm) && (passwordConfirm.length >= 1)) {
            passwordConfirmInput.classList.add('is-valid');
            passwordConfirmInput.classList.remove('is-invalid');
            return true
        } else {
            passwordConfirmInput.classList.remove('is-valid');
            passwordConfirmInput.classList.add('is-invalid');
            return false
        }
    }
}