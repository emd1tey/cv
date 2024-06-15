# PIdor dla klounov

<div class="klounov-container">
    <audio autoplay loop>
        <source src="../music.mp3" type="audio/mpeg">
        Ваш браузер не поддерживает элемент audio.
    </audio>

    <div id="timer-wrapper">Осталось времени: <span id="hours"></span>:<span id="minutes"></span>:<span id="seconds"></span></div>

    <div class="carousel">
        <img src="../images/1.jpg" class="active" alt="Image 1">
        <img src="../images/2.jpg" alt="Image 2">
        <img src="../images/3.jpg" alt="Image 3">
        <img src="../images/4.jpg" alt="Image 4">
        <img src="../images/5.jpg" alt="Image 5">
        <img src="../images/6.jpg" alt="Image 6">
        <img src="../images/7.jpg" alt="Image 7">
        <img src="../images/8.jpg" alt="Image 8">
    </div>
</div>

<style>
.klounov-container {
    height: 100vh;
    width: 100%;
    position: relative;
    overflow: hidden;
}

.klounov-container .carousel {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.klounov-container .carousel img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: none;
    opacity: 0;
    transition: opacity 1s ease-in-out;
}

.klounov-container .carousel img.active {
    display: block;
    opacity: 1;
}

.klounov-container #timer-wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: Arial, sans-serif;
    font-size: 24px;
    color: #FFF;
    z-index: 2;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 10px 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    initializeTimer();
    initCarousel();
});

function initializeTimer() {
    var endDate = new Date(2024, 6, 4, 23, 59);
    var timerId = setInterval(function() {
        var now = new Date();
        var remaining = endDate - now;

        if (remaining <= 0) {
            clearInterval(timerId);
            document.getElementById("timer-wrapper").textContent = "Время вышло!";
            return;
        }

        var hours = Math.floor(remaining / (1000 * 60 * 60));
        var minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((remaining % (1000 * 60)) / 1000);

        document.getElementById("hours").textContent = hours < 10 ? "0" + hours : hours;
        document.getElementById("minutes").textContent = minutes < 10 ? "0" + minutes : minutes;
        document.getElementById("seconds").textContent = seconds < 10 ? "0" + seconds : seconds;
    }, 1000);
}

function initCarousel() {
    const images = document.querySelectorAll('.carousel img');
    let currentImgIndex = 0;
    images[currentImgIndex].style.display = 'block';
    images[currentImgIndex].classList.add('active');

    setInterval(() => {
        images[currentImgIndex].classList.remove('active');
        images[currentImgIndex].style.opacity = 0;

        currentImgIndex = (currentImgIndex + 1) % images.length;

        images[currentImgIndex].style.display = 'block';
        setTimeout(() => {
            images[currentImgIndex].classList.add('active');
            images[currentImgIndex].style.opacity = 1;
        }, 50); // небольшая задержка для активации плавного перехода
    }, 5000);
}
</script>
