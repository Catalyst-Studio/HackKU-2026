let stopwatch = document.getElementById("assignment-stopwatch");
let startTime, elapsedTime = 0, timerInterval

function timeToString(time) {
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 1000;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(3, "0");

  return `${formattedMM}:${formattedSS}.${formattedMS}`;
}

function startAssignment() {
  startTime = Date.now() - elapsedTime;
  timerInterval = setInterval(function printTime() {
        elapsedTime = Date.now() - startTime;
        stopwatch.innerHTML = timeToString(elapsedTime);
  }, 10);
}

function stopAssignment() {
  clearInterval(timerInterval);
}

function resetAssignment() {
  clearInterval(timerInterval);
  stopwatch.textContent = "00:00.000";
  elapsedTime = 0;
}

function finishAssignment() {
  clearInterval(timerInterval);
  elapsedTime = 0;
  //add stopwatch.textContent to server
  stopwatch.textContent = "00:00.000";
}