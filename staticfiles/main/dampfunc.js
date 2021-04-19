function checkdf() {
    val = document.getElementById('deepfocus').checked
    if (val == true) {
        document.getElementById("dfwarn").classList.remove('d-none')
    }
    else {
        document.getElementById("dfwarn").classList.add('d-none')
    }
}



deepfocus = document.getElementById('deepfocus').checked
if (deepfocus == true) {
    // document.documentElement.requestFullscreen();
    navigator.keyboard.lock();
    document.body.requestPointerLock();
}




document.body.onkeyup = function (e) {
    if (e.keyCode == 32) {
        giveup()
    }
}




document.body.onkeyup = function (e) {
    if (e.keyCode == 8) {
      document.getElementById('cancelbtn').click()
    }
  }