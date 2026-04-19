let modal;
window.addEventListener('load', (event) => {
    modal = bootstrap.Modal.getOrCreateInstance("#homework-availability-modal");
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

function addHomeworkAvailabilityTimes() {
    if (document.querySelector("form").isValid) {
        modal.hide();
        //add to server
    }
}