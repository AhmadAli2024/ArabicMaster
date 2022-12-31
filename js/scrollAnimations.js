window.addEventListener('scroll', reveal);

function reveal(){
    let reveals = document.querySelectorAll('.reveal');
    for(let i=0; i<reveals.length; i++){
        let hWindow = window.innerHeight;
        let revealtop = reveals[i].getBoundingClientRect().top;
        let revealpoint = 60;

        if(revealtop < hWindow - revealpoint){
            reveals[i].classList.add('revealed');
        }
        else{
            reveals[i].classList.remove('revealed');
        }
    }
}

function setRoom(room){
    document.getElementById('room-type').value = room;
}