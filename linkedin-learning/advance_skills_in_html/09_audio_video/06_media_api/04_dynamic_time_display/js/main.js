var media = document.querySelector('#videoelement');
var play = document.querySelector('#playbutton');
var pause = document.querySelector('#pausebutton');
var position = document.querySelector('#positiondisplay');
var duration = document.querySelector('#durationdisplay');
var rail = document.querySelector('#controlbarrail');
var fill = document.querySelector('#controlbarfill');

play.addEventListener('click', playMedia);
function playMedia() {
    media.play();
}

pause.addEventListener('click', pauseMedia);
function pauseMedia() {
    media.pause();
}

rail.addEventListener('click', seekMedia);
fill.addEventListener('click', seekMedia);
function seekMedia(e) { }

media.addEventListener('loadedmetadata', updateTime);
media.addEventListener('timeupdate', updateTime);
function updateTime() { }