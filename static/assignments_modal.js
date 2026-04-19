function addClass() {
    let assignmentsModal = bootstrap.Modal.getOrCreateInstance("#assignments-modal");
    let classesModal = bootstrap.Modal.getOrCreateInstance("#classes-modal");
    assignmentsModal.hide();
    classesModal.show();
    document.getElementById("classes-modal-btn-close").onclick = function() {
        classesModal.hide();
        assignmentsModal.show();
    }; document.getElementById("classes-modal-submit").onclick = function() {
        classesModal.hide();
        assignmentsModal.show();
    }
}

function changeLength(elem) {
    let baseType;
    let hasSetTime;
    /*search server for the type name of Array.from(elem.children).find(elem => elem.selected).value
    and get base type & hasSetTime*/
    let lengthText = document.getElementById("assignment-length");
    if (hasSetTime) lengthText.placeholder = "Time limit (minutes)";
    if (baseType === "Homework" || baseType === "Quiz") {
        lengthText.placeholder = "# of questions"
    } else if (baseType === "Essay") {
        lengthText.placeholder = "# of pages"
    }
}

async function handleFormSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: form.method || "POST",
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            onSuccess(data);
        } else {
            onError(response.status, data);
        }
    } catch (err) {
        onNetworkError(err);
    }
}

document.getElementById("assignment-form").addEventListener("submit", handleFormSubmit);

function onSuccess(data) {
  console.log("Success:", data);
  // e.g. redirect, show a success message, update the UI
}

function onError(status, data) {
  console.error(`Error ${status}:`, data);
  // e.g. show validation errors, highlight fields, display a toast
}

function onNetworkError(err) {
  console.error("Network error:", err);
  // e.g. show a "check your connection" message
}