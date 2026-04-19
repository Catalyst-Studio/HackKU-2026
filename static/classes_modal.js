let classesModal = bootstrap.Modal.getOrCreateInstance("#classes-modal");
classesModal.show();
async function handleFormSubmit(event) {
  event.preventDefault(); // Prevent default page reload

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch(form.action, {
      method: form.method || "POST",
      body: formData,
    });

    const data = await response.json(); // Parse JSON response

    if (response.ok) {
      onSuccess(data);
    } else {
      onError(response.status, data);
    }

  } catch (err) {
    onNetworkError(err);
  }
}

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

// Attach to your form
document.getElementById("classes-form").addEventListener("submit", handleFormSubmit);