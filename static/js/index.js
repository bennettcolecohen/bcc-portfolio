document.getElementById('toggle').addEventListener('click', function(){ 
    var nav = document.getElementById('nav'); 
    if (nav.classList.contains('-right-full')){ 
        nav.classList.remove('-right-full')
        nav.classList.add('right-0')
    }
    else { 
        nav.classList.remove('right-0')
        nav.classList.add('-right-full')
    }
})