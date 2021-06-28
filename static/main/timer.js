duration = (document.getElementById('session_duration').textContent)
document.getElementById('Mynavbar').classList.add('d-none')
document.getElementById('range').classList.add('d-none')
document.getElementById('startbtn').classList.add('disabled')


let mysession = setInterval(() => {
    if (duration == '0:30:00') {
        document.getElementById('range').value = 1
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          25 Coins & 
          <i class="fas fa-tree text-success"></i>
          1 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -20 Coins & 
          <i class="fas fa-tree text-danger"></i>
          1 DeadTree
      </strong>
  </div>`
    }
    else if (duration == '1:00:00') {
        document.getElementById('range').value = 2
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          50 Coins & 
          <i class="fas fa-tree text-success"></i>
          2 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -40 Coins & 
          <i class="fas fa-tree text-danger"></i>
          2 DeadTree
      </strong>
  </div>`
    }
    else if (duration == '1:30:00') {
        document.getElementById('range').value = 3
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          75 Coins & 
          <i class="fas fa-tree text-success"></i>
          3 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -60 Coins & 
          <i class="fas fa-tree text-danger"></i>
          3 DeadTree
      </strong>
  </div>`
    }
    else if (duration == '2:00:00') {
        document.getElementById('range').value = 4
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          100 Coins & 
          <i class="fas fa-tree text-success"></i>
          4 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -80 Coins & 
          <i class="fas fa-tree text-danger"></i>
          4 DeadTree
      </strong>
  </div>`
    }
    else if (duration == '2:30:00') {
        document.getElementById('range').value = 5
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          125 Coins & 
          <i class="fas fa-tree text-success"></i>
          5 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -100 Coins & 
          <i class="fas fa-tree text-danger"></i>
          5 DeadTree
      </strong>
  </div>`
    }
    else if (duration == '3:00:00') {
        document.getElementById('range').value = 6
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          150 Coins & 
          <i class="fas fa-tree text-success"></i>
          6 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -120 Coins & 
          <i class="fas fa-tree text-danger"></i>
          6 DeadTree
      </strong>
  </div>`
    }
    else{
      document.getElementById('range').value = 1
      document.getElementById('treesinfo').innerHTML = "Plants 1 tree if you fail you kill a tree"
      document.getElementById('coinsinfo').innerHTML = `<div class="pb-2">
      <strong>
          Success:
          <i class="fas fa-dollar-sign text-warning"></i>
          25 Coins & 
          <i class="fas fa-tree text-success"></i>
          1 Tree
      </strong>
  </div>
  <div class="pt-2">
      <strong>
          Failure:
          <i class="fas fa-dollar-sign text-warning"></i>
          -20 Coins & 
          <i class="fas fa-tree text-danger"></i>
          1 DeadTree
      </strong>
  </div>`
    }

    session_end = document.getElementById('session_end').textContent
    server_begin_to_session_end = Date.parse(session_end)

    const server_begin_to_now = new Date().getTime()

    let diff = server_begin_to_session_end - server_begin_to_now

    const m = Math.floor((server_begin_to_session_end / (1000 * 60)) - (server_begin_to_now / (1000 * 60)))
    const s = Math.floor(((server_begin_to_session_end / (1000)) - (server_begin_to_now / (1000))) % 60)
    session_minutes = m
    session_seconds = s
    document.getElementById('timer').innerHTML = `
    <h4 id="minutes" class="display-5 text-black">30 </h4>
    <h4 id="separator" class="display-5 text-black px-1">:</h4>
    <h4 id="seconds" class="display-5 text-black"> 00</h4>
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
        new Audio('static/main/bell.mp3').play()
        document.title = "Tree Planted"
        document.getElementById('treemodalbtn').click()
        setTimeout(function () { document.getrange.submit() }, 5000);
    }
    else {
        if (session_seconds < 10) {
            document.getElementById("seconds").innerHTML = "0" + session_seconds;
            document.title = "Tree Growing - " + session_minutes + ":0" + session_seconds
        }
        else {
            document.getElementById("seconds").innerHTML = session_seconds;
            document.title = "Tree Growing - " + session_minutes + ":" + session_seconds
        }
        if (session_minutes < 10) {
            document.getElementById("minutes").innerHTML = "0" + session_minutes;
            document.title = "Tree Growing - 0" + session_minutes + ":" + session_seconds
        }
        else {
            document.getElementById("minutes").innerHTML = session_minutes;
            document.title = "Tree Growing - " + session_minutes + ":" + session_seconds
        }
    }

}, 1000)