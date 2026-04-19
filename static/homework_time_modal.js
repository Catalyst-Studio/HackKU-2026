let modal = bootstrap.Modal.getOrCreateInstance("#homework-availability-modal");
window.addEventListener('load', (event) => {
    modal.show();
});

function addTimeAvailability(elem) {
    let div = document.createElement("div");
    div.className = "d-flex";
    let count = elem.parentElement.parentElement.childElementCount;
    let newInput1 = elem.parentElement.querySelector("[id*='Time1']").cloneNode();
    newInput1.value = "";
    let newInput2 = elem.parentElement.querySelector("[id*='Time2']").cloneNode();
    newInput2.value = "";

    newInput1.id = newInput1.id.replace(newInput1.id.substring(9), count);
    newInput1.name = newInput1.id

    newInput2.id = newInput2.id.replace(newInput2.id.substring(9), count);
    newInput2.name = newInput2.id;

    let day = newInput1.id.substring(0, 3);

    div.id = day + "Flex" + "-" + Array.from(elem.parentElement.parentElement.children).filter(elem => elem.id.includes(day + "Flex")).length;

    newInput1.ariaLabel = day.substring(0, 1).toUpperCase() + day.substring(1) + "day Time 1" + count;
    newInput2.ariaLabel = day.substring(0, 1).toUpperCase() + day.substring(1) + "day Time 2" + count;

    div.appendChild(newInput1, elem.parentElement.children.length - 1);
    let lineBreak = document.createElement("p");
    lineBreak.className = "align-self-end";
    lineBreak.textContent = "-";
    div.appendChild(lineBreak);
    div.appendChild(newInput2);
    let removeButton = document.createElement("button");
    removeButton.className = "btn btn-danger m-2 flex-fill";
    removeButton.innerHTML = "<i class='iconoir-minus fs-5'>"
    removeButton.onclick = function () {
        elem.parentElement.parentElement.removeChild(div)
    }
    div.appendChild(removeButton);
    elem.parentElement.parentElement.insertBefore(div, elem.parentElement.parentElement[elem.parentElement.parentElement.childElementCount - 1]);
}

function checkTime(elem) {
    let otherTime;
    if (elem.id.includes("Time1")) otherTime = Array.from(elem.parentElement.children).find(elem => elem.id.includes("Time2"));
    else otherTime = Array.from(elem.parentElement.children).find(elem => elem.id.includes("Time1"));
    if (elem.value !== "" && otherTime.value !== "") {
        if (elem.id.includes("Time1") && otherTime.value <= elem.value) elem.value = otherTime.value;
        else if (elem.id.includes("Time2") && otherTime.value >= elem.value) {
            otherTime.value = Array.from(elem.parentElement.children).find(elem => elem.id.includes("Time1")).value = elem.value;
        } if (elem.value === otherTime.value) {
            elem.setCustomValidity("15 minute intervals are required!");
        } else {
            elem.setCustomValidity("");
        }
    }
}

async function handleFormSubmit(event) {
    event.preventDefault();
    if (document.getElementById("homework-availability-form").checkValidity()) {
        modal.hide();
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
document.getElementById("homework-availability-form").addEventListener("submit", handleFormSubmit);