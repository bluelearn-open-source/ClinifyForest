function giveup() {
    document.getElementById('hidden').value = -1
    document.getrange.submit()
}
function canceltimer() {
    val = document.getElementById('hidden').value = 1
    console.log(val)
    document.getrange.submit()
}
duration = (document.getElementById('session_duration').textContent)
document.getElementById('Mynavbar').classList.add('d-none')
document.getElementById('range').classList.add('d-none')
document.getElementById('startbtn').classList.add('disabled')


let mysession = setInterval(() => {

    session_end = document.getElementById('session_end').textContent
    server_begin_to_session_end = Date.parse(session_end)

    const server_begin_to_now = new Date().getTime()

    let diff = server_begin_to_session_end - server_begin_to_now

    const m = Math.floor((server_begin_to_session_end / (1000 * 60)) - (server_begin_to_now / (1000 * 60)))
    const s = Math.floor(((server_begin_to_session_end / (1000)) - (server_begin_to_now / (1000))) % 60)
    session_minutes = m
    session_seconds = s
    document.getElementById('timer').innerHTML = `
    <h4 id="minutes" class="display-4 text-warning">30</h4>
    <h4 id="separator" class="display-4 text-warning">:</h4>
    <h4 id="seconds" class="display-4 text-warning">00</h4>
    `
    document.getElementById('startbtn').classList.add('d-none')
    document.getElementById('cancelbtn').classList.remove('d-none')
    if (duration == '0:30:00' && ((server_begin_to_session_end - server_begin_to_now) < ((1 * 1800000) - 10000))) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else if (duration == '1:00:00' && server_begin_to_session_end - server_begin_to_now < (2 * 1800000) - 10000) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else if (duration == '1:30:00' && server_begin_to_session_end - server_begin_to_now < (3 * 1800000) - 10000) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else if (duration == '2:00:00' && server_begin_to_session_end - server_begin_to_now < (4 * 1800000) - 10000) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else if (duration == '2:30:00' && server_begin_to_session_end - server_begin_to_now < (5 * 1800000) - 10000) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else if (duration == '3:00:00' && server_begin_to_session_end - server_begin_to_now < (6 * 1800000) - 10000) {
        document.getElementById('giveupbtn').classList.remove('d-none')
        document.getElementById('cancelbtn').classList.add('d-none')
    }
    else {
        document.getElementById('cancelbtn').classList.remove('d-none')
    }
    if (session_seconds % 2 == 0) {
        document.getElementById('minutes').classList.add('white-text-timer')
        document.getElementById('seconds').classList.add('white-text-timer')
        document.getElementById('separator').classList.add('white-text-timer')
    }
    else {
        document.getElementById('minutes').classList.remove('white-text-timer')
        document.getElementById('seconds').classList.remove('white-text-timer')
        document.getElementById('separator').classList.remove('white-text-timer')
    }
    if (diff <= 0) {
        clearInterval(mysession)
        document.getElementById("seconds").innerHTML = "00"
        document.getElementById("minutes").innerHTML = "00"
        document.getElementById('hidden').value = 0
        link = document.getElementById('audiosource').textContent
        new Audio(link).play()
        document.getElementById('treemodalbtn').click()
        setTimeout(function () { document.getrange.submit() }, 5000);
    }
    else {
        if (session_seconds < 10) {
            document.getElementById("seconds").innerHTML = "0" + session_seconds;
        }
        else {
            document.getElementById("seconds").innerHTML = session_seconds;
        }
        if (session_minutes < 10) {
            document.getElementById("minutes").innerHTML = "0" + session_minutes;
        }
        else {
            document.getElementById("minutes").innerHTML = session_minutes;
        }
    }

}, 1000)



