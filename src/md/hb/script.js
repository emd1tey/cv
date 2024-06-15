window.onload = function()
{
     initializeTimer();
}


function initializeTimer() {
	var endDate = new Date(2024,6,4,23,59);
	var currentDate = new Date();
	var seconds = (endDate-currentDate) / 1000;
	if (seconds > 0) {
		var minutes = seconds/60;
		var hours = minutes/60;
		minutes = (hours - Math.floor(hours)) * 60;
		hours = Math.floor(hours);
		seconds = Math.floor((minutes - Math.floor(minutes)) * 60);
		minutes = Math.floor(minutes);

		setTimePage(hours,minutes,seconds);

		function secOut() {
		  if (seconds == 0) {
			  if (minutes == 0) {
				  if (hours == 0) {
					  showMessage(timerId);
				  }
				  else {
					  hours--;
					  minutes = 59;
					  seconds = 59;
				  }
			  }
			  else {
				  minutes--;
				  seconds = 59;
			  }
		  }
		  else {
			  seconds--;
		  }
		  setTimePage(hours,minutes,seconds);
		}
		timerId = setInterval(secOut, 1000)
	}
	else {
		alert("тобипизда");
	}
}

function setTimePage(h,m,s) {
	var element = document.getElementById("timer");
	if(m < 10)
		m = `0${m}`;
	if(s < 10)
		s = `0${s}`;
	document.querySelector('div#hours').innerHTML = h;
	element.innerHTML =" : "+m+" : "+s;
}



























class CoralStrand {


 select(s){return document.querySelector(s);}
 selectAll(s){return document.querySelectorAll(s);}




  constructor(){
   this.isVertical = true;
   this.mainTl = new TimelineMax();
   const dot = this.select('#dot');
   const connector = this.select('#connector');
   const lineContainer = this.select('#lineContainer');
   const dotContainer = this.select('#dotContainer');
   const tl = new TimelineMax();
   const width = 800;
   const height = 600;
   const centreX = this.randomBetween(100, width-100);
   const centreY = this.randomBetween(40, height);
   const num = this.randomBetween(6, 23);
   const strandHeight = num * 30;
   const amp = num*10;
   const duration = this.randomBetween(10, 30)/5;
   const staggerOffset = num/100;
   const cloneArr = [];
   const step = (this.isVertical) ? strandHeight/(num) : width/(num);
   this.mainTl.add(tl);

   let alpha = num/30;

   for(var i = 0; i < num; i++){
    let dotClone = dot.cloneNode(true);
    dotContainer.appendChild(dotClone);
    let x = (this.isVertical) ? centreX : i * (step);
    let y = (this.isVertical) ? height - (i * (step)) : centreY;
    let r = (num - i)/1.5;
    TweenMax.set(dotClone, {
     x,
     y,
     alpha: 0.5 -  (i / num),
     attr:{
      r:0
     }
    })
    cloneArr.push(dotClone);
   }

   var dotTl = new TimelineMax();
   dotTl.staggerFromTo(cloneArr, duration, {

    cycle:{
     x:(count, el) =>{
      return (this.isVertical) ? centreX +  (count * 10) : el._gsTransform.x
     },
     y:(count, el) =>{
       return (this.isVertical) ? el._gsTransform.y : centreY +  ((count+1) * 20)
      }
    },
    scale:1,
    transformOrigin:'50% 50%'
   },{
    scale:1.2,
    cycle:{
     x:(count, el) =>{
      return (this.isVertical) ? centreX -  (count * 10) : el._gsTransform.x
     },
     y:(count, el) =>{
      return (this.isVertical) ? el._gsTransform.y : centreY -  ((count+1) * 20)
     }
    },

    transformOrigin:'50% 50%',
    repeat:-1,
    ease:Sine.easeInOut,
    yoyoEase:Sine.easeInOut
   },staggerOffset)

   this.mainTl.add(dotTl, 0)


   cloneArr.forEach((c, i) => {
    let clone = connector.cloneNode(true);

    lineContainer.appendChild(clone);
    clone.setAttribute('stroke-width', num - i);
    clone.setAttribute('opacity', 1 - (i/num));
    let tl = new TimelineMax();
    tl.to(clone, 1, {
     repeat:-1,
     yoyoEase:Power1.easeOut,
     attr:{
      x1:'+=0',
      x2:'+=0',
      y1:'+=0',
      y2:'+=0'
     },
     modifiers:{
      attr:{
       x1:() => {
        return cloneArr[i]._gsTransform.x
       },
      x2:() => {
        return (i < num-1) ? cloneArr[i+1]._gsTransform.x : cloneArr[i]._gsTransform.x
       },
      y1:() => {
        return cloneArr[i]._gsTransform.y
       },
      y2:() => {
         return (i < num-1) ? cloneArr[i+1]._gsTransform.y : cloneArr[i]._gsTransform.y
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

for( var i = 0; i < 16; i++){

 let app = new CoralStrand();
}
