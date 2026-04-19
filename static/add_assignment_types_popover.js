const button = document.getElementById("assignment-type-add-popover-button");
const formContent = document.getElementById("assignment-type-add-popover-form").innerHTML;
new bootstrap.Popover(button, {
    html: true,
    content: formContent,
    sanitize: false,
    container: "#assignments-modal",
    direction: "right",
    title: "Add Assignment Type",
});


const tooltipTriggerList = document.querySelectorAll(
  "[data-bs-toggle='tooltip']"
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

document.getElementById('assignment-type-add-popover-button').addEventListener('shown.bs.popover', function () {
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

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

document.getElementById("assignment-type-form").addEventListener("submit", handleFormSubmit);

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