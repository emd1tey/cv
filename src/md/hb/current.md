# EMDITEY

<div class="emditey-container">
    <div class="rainbow-preloader">
        <div class="rainbow-stripe"></div>
        <div class="rainbow-stripe"></div>
        <div class="rainbow-stripe"></div>
        <div class="rainbow-stripe"></div>
        <div class="rainbow-stripe"></div>
        <div class="shadow"></div>
        <div class="shadow"></div>
    </div>

    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <filter id="goo">
                <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur" />
                <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 21 -9" result="cm" />
                <feBlend/>
            </filter>
            <linearGradient id="coralGrad" x1="400" x2="400" y2="600" gradientUnits="userSpaceOnUse">
                <stop offset="0.2" stop-color="#212130"/>
                <stop offset="0.5" stop-color="#F49A4A"/>
                <stop offset="1" stop-color="#CF1D33"/>
            </linearGradient>
            <circle id="dot" cx="0" cy="0" r="6" fill="#CF1D33"/>
            <line id="connector" x1="0" x2="0" y1="0" y2="0" stroke-width="3" stroke-dasharray="" stroke-linecap="round" />
        </defs>
        <g id="lineContainer" stroke="url(#coralGrad)" />
        <g id="dotContainer" />
    </svg>

    <div id="centered">
        <div id="hours">123123</div>
        <span id="timer"></span>
    </div>
</div>

<style>
.emditey-container {
    background: url("/img.png");
    background-size: cover;
    background-position: center center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-color: black;
    overflow: hidden;
    text-align: center;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    height: 100vh;
    width: 100%;
}

.emditey-container #hours {
    transition: 2s cubic-bezier(1,-0.11,.94,1.55);
    color: white;
    text-align: right;
    display: inline-block;
    transform-origin: right bottom;
    font-size: xx-large;
    font-family: 'Raleway', sans-serif;
}

.emditey-container .drop {
    transform: rotate(-30deg)!important;
}

.emditey-container .rainbow-preloader .rainbow-stripe {
    border-style: solid;
    border-radius: 100%;
    position: absolute;
    border-width: 12px;
}

.emditey-container .rainbow-preloader .rainbow-stripe:before {
    border-radius: 100%;
    display: block;
}

.emditey-container .rainbow-preloader {
    height: 90px;
    left: 50%;
    margin-left: -90px;
    margin-top: -90px;
    overflow: hidden;
    position: absolute;
    top: 50%;
    width: 180px;
}

.emditey-container .rainbow-preloader:before, .rainbow-preloader:after {
    background: linear-gradient(45deg, transparent 33.333%, #6b9903 33.333%, #6b9903 66.667%, transparent 66.667%), linear-gradient(-45deg, transparent 33.333%, #6b9903 33.333%, #6b9903 66.667%, transparent 66.667%);
    background-size: 6px 34px;
    bottom: 0;
    content: '';
    display: block;
    height: 12px;
    left: 0;
    position: absolute;
    width: 66px;
    z-index: 10;
}

.emditey-container .rainbow-preloader:after {
    left: auto;
    right: 0;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(1) {
    border-color: #f15a5a;
    clip: rect(0, 84px, 42px, 0);
    height: 60px;
    left: 48px;
    -webkit-transform: rotate(180deg);
    top: 48px;
    width: 60px;
    z-index: 5;
    -webkit-animation: rainbow-in-out 5s 0.1s infinite;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(1):before {
    border: 3px solid #ed2b2b;
    height: 48px;
    width: 54px;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(2) {
    border-color: #f0c419;
    clip: rect(0, 108px, 54px, 0);
    height: 84px;
    left: 36px;
    -webkit-transform: rotate(180deg);
    top: 36px;
    width: 84px;
    z-index: 4;
    -webkit-animation: rainbow-in-out 5s 0.2s infinite;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(2):before {
    border: 3px solid #c9a20d;
    height: 72px;
    width: 78px;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(3) {
    border-color: #4eba6f;
    clip: rect(0, 132px, 66px, 0);
    height: 108px;
    left: 24px;
    -webkit-transform: rotate(180deg);
    top: 24px;
    width: 108px;
    z-index: 3;
    -webkit-animation: rainbow-in-out 5s 0.3s infinite;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(3):before {
    border: 3px solid #3c9958;
    height: 96px;
    width: 102px;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(4) {
    border-color: #2d95bf;
    clip: rect(0, 156px, 78px, 0);
    height: 132px;
    left: 12px;
    -webkit-transform: rotate(180deg);
    top: 12px;
    width: 132px;
    z-index: 2;
    -webkit-animation: rainbow-in-out 5s 0.4s infinite;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(4):before {
    border: 3px solid #237596;
    height: 120px;
    width: 126px;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(5) {
    border-color: #955ba5;
    clip: rect(0, 180px, 90px, 0);
    height: 156px;
    left: 0px;
    -webkit-transform: rotate(180deg);
    top: 0px;
    width: 156px;
    z-index: 1;
    -webkit-animation: rainbow-in-out 5s 0.5s infinite;
}

.emditey-container .rainbow-preloader .rainbow-stripe:nth-child(5):before {
    border: 3px solid #774984;
    height: 144px;
    width: 150px;
}

@-webkit-keyframes rainbow-in-out {
    0% {
        -webkit-transform: rotate(180deg);
    }
    33% {
        -webkit-transform: rotate(360deg);
    }
    66% {
        -webkit-transform: rotate(360deg);
    }
    100% {
        -webkit-transform: rotate(540deg);
    }
}

@-webkit-keyframes timer {
    from {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    to {
        -webkit-transform: rotate(-20deg);
        transform: rotate(-20deg);
    }
}

@keyframes timer {
    from {
        -webkit-transform: rotate(0deg);
        transform: rotate(0deg);
    }
    to {
        -webkit-transform: rotate(-20deg);
        transform: rotate(-20deg);
    }
}

.emditey-container #centered {
    top: 50%;
    left: 50%;
    position: fixed;
    transform: translate(-50%, 50%);
}

.emditey-container #timer {
    font-size: xx-large;
    text-align: center;
    font-family: 'Raleway', sans-serif;
    color: white;
}

.page__content#home .timer {
    -webkit-transform-origin: 100%;
    -ms-transform-origin: 100%;
    transform-origin: 100%;
    -webkit-animation: timer 0.7s cubic-bezier(0.52, 0.91, 0.68, -0.76) 1s forwards;
    animation: timer 0.7s cubic-bezier(0.52, 0.91, 0.68, -0.76) 1s forwards;
    display: inline-block;
    z-index: 1;
    position: relative;
}
</style>

<script src="//cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenMax.min.js"></script>
<script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/ModifiersPlugin-latest-beta.js"></script>
<script>
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('div#hours').classList.add('drop');
    setTimeout(() => {
        document.querySelector('audio').play();
    }, 5000);
});

window.onload = function() {
    initializeTimer();
}

function initializeTimer() {
    var endDate = new Date(2024, 6, 4, 23, 59);
    var currentDate = new Date();
    var seconds = (endDate - currentDate) / 1000;
    if (seconds > 0) {
        var minutes = seconds / 60;
        var hours = minutes / 60;
        minutes = (hours - Math.floor(hours)) * 60;
        hours = Math.floor(hours);
        seconds = Math.floor((minutes - Math.floor(minutes)) * 60);
        minutes = Math.floor(minutes);

        setTimePage(hours, minutes, seconds);

        function secOut() {
            if (seconds == 0) {
                if (minutes == 0) {
                    if (hours == 0) {
                        showMessage(timerId);
                    } else {
                        hours--;
                        minutes = 59;
                        seconds = 59;
                    }
                } else {
                    minutes--;
                    seconds = 59;
                }
            } else {
                seconds--;
            }
            setTimePage(hours, minutes, seconds);
        }
        timerId = setInterval(secOut, 1000);
    } else {
        alert("Время истекло");
    }
}

function setTimePage(h, m, s) {
    var element = document.getElementById("timer");
    if (m < 10) m = `0${m}`;
    if (s < 10) s = `0${s}`;
    document.querySelector('div#hours').innerHTML = h;
    element.innerHTML = " : " + m + " : " + s;
}

class CoralStrand {
    select(s) {
        return document.querySelector(s);
    }

    selectAll(s) {
        return document.querySelectorAll(s);
    }

    constructor() {
        this.isVertical = true;
        this.mainTl = new TimelineMax();
        const dot = this.select('#dot');
        const connector = this.select('#connector');
        const lineContainer = this.select('#lineContainer');
        const dotContainer = this.select('#dotContainer');
        const tl = new TimelineMax();
        const width = 800;
        const height = 600;
        const centreX = this.randomBetween(100, width - 100);
        const centreY = this.randomBetween(40, height);
        const num = this.randomBetween(6, 23);
        const strandHeight = num * 30;
        const amp = num * 10;
        const duration = this.randomBetween(10, 30) / 5;
        const staggerOffset = num / 100;
        const cloneArr = [];
        const step = (this.isVertical) ? strandHeight / (num) : width / (num);
        this.mainTl.add(tl);

        let alpha = num / 30;

        for (var i = 0; i < num; i++) {
            let dotClone = dot.cloneNode(true);
            dotContainer.appendChild(dotClone);
            let x = (this.isVertical) ? centreX : i * (step);
            let y = (this.isVertical) ? height - (i * (step)) : centreY;
            let r = (num - i) / 1.5;
            TweenMax.set(dotClone, {
                x,
                y,
                alpha: 0.5 - (i / num),
                attr: {
                    r: 0
                }
            })
            cloneArr.push(dotClone);
        }

        var dotTl = new TimelineMax();
        dotTl.staggerFromTo(cloneArr, duration, {
            cycle: {
                x: (count, el) => {
                    return (this.isVertical) ? centreX + (count * 10) : el._gsTransform.x
                },
                y: (count, el) => {
                    return (this.isVertical) ? el._gsTransform.y : centreY + ((count + 1) * 20)
                }
            },
            scale: 1,
            transformOrigin: '50% 50%'
        }, {
            scale: 1.2,
            cycle: {
                x: (count, el) => {
                    return (this.isVertical) ? centreX - (count * 10) : el._gsTransform.x
                },
                y: (count, el) => {
                    return (this.isVertical) ? el._gsTransform.y : centreY - ((count + 1) * 20)
                }
            },
            transformOrigin: '50% 50%',
            repeat: -1,
            ease: Sine.easeInOut,
            yoyoEase: Sine.easeInOut
        }, staggerOffset)

        this.mainTl.add(dotTl, 0)

        cloneArr.forEach((c, i) => {
            let clone = connector.cloneNode(true);

            lineContainer.appendChild(clone);
            clone.setAttribute('stroke-width', num - i);
            clone.setAttribute('opacity', 1 - (i / num));
            let tl = new TimelineMax();
            tl.to(clone, 1, {
                repeat: -1,
                yoyoEase: Power1.easeOut,
                attr: {
                    x1: '+=0',
                    x2: '+=0',
                    y1: '+=0',
                    y2: '+=0'
                },
                modifiers: {
                    attr: {
                        x1: () => {
                            return cloneArr[i]._gsTransform.x
                        },
                        x2: () => {
                            return (i < num - 1) ? cloneArr[i + 1]._gsTransform.x : cloneArr[i]._gsTransform.x
                        },
                        y1: () => {
                            return cloneArr[i]._gsTransform.y
                        },
                        y2: () => {
                            return (i < num - 1) ? cloneArr[i + 1]._gsTransform.y : cloneArr[i]._gsTransform.y
                        }
                    }
                }
            })

            this.mainTl.add(tl, 0)
        })

        this.mainTl.seek(this.randomBetween(1000, 3000))
    }

    randomBetween(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }
}

TweenMax.set('svg', {
    visibility: 'visible'
})

for (var i = 0; i < 16; i++) {
    let app = new CoralStrand();
}
</script>
<audio controls loop="loop" style="display:none">
    <source src="../music.mp3">
    <p>Ваш браузер не поддерживает аудио</p>
</audio>
