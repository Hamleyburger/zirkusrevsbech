    // GSAP for animation on the front page
    console.log("hey");

    $( document ).ready(function() {
        console.log( "ready!" );
        var tl = gsap.timeline({
            scrollTrigger: {
                //once: true,
                end: "+=2000", // end after scrolling 500px beyond the start
                scrub: 0.5, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
            }
        });
        
                tl.delay(0.1);
                tl.timeScale(0.1);
                tl.to(".flowers", { duration: 0.1, y: -550, x: -100 })


    });    

    
