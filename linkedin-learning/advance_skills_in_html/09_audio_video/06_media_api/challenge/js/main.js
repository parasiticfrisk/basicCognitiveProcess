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
function seekMedia(e) {
    media.currentTime = e.offsetX / rail.offsetWidth * media.duration;
}

media.addEventListener('loadedmetadata', updateTime);
media.addEventListener('timeupdate', updateTime);
function updateTime() {
    position.textContent = timeDisplay(media.currentTime);
    duration.textContent = timeDisplay(media.duration);
    var currentlength = rail.clientWidth * (media.currentTime / media.duration);
    fill.style.width = currentlength + 'px';
}

function timeDisplay(t) {
    var minutes = Math.floor(t / 60);
    var seconds = Math.floor(t - minutes * 60);
    var minutevalue;
    if (minutes < 10) {
        minutevalue = '0' + minutes;
    } else {
        minutevalue = minutes;
    }
    var secondvalue;
    if (seconds < 10) {
        secondvalue = '0' + seconds;
    } else {
        secondvalue = seconds;
    }
    var mediatime = minutevalue + ':' + secondvalue;
    return mediatime;
}