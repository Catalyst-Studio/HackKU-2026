const button = document.getElementById("assignment-type-add-popover-button");
const formContent = document.getElementById("assignment-type-add-popover-form").innerHTML;
new bootstrap.Popover(button, {
    html: true,
    content: formContent,
    sanitize: false,
    container: "body",
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