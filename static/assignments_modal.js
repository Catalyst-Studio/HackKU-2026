let assignmentsModal;
// window.addEventListener('load', (event) => {
//     assignmentsModal = bootstrap.Modal.getOrCreateInstance("#assignments-modal");
//     assignmentsModal.show();
// });

function addClass() {
    let classesModal = bootstrap.Modal.getOrCreateInstance("#classes-modal");
    assignmentsModal.hide();
    classesModal.show();
    document.getElementById("classes-modal-btn-close").onclick = function() {
        classesModal.hide();
        assignmentsModal.show();
    }; document.getElementById("classes-modal-submit").onclick = function() {
        addClassToServer();
        classesModal.hide();
        assignmentsModal.show();
    }
}

function addNewAssignment() {
    assignmentsModal.hide();
    //add to server
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