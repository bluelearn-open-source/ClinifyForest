session_minutes = 30;
session_seconds = "00";
function checkr() {
  val = document.getElementById('range').value
  if (val == 1) {
    session_minutes = 30;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 1 tree if you fail you kill 1 tree"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +25 coins</div><div>Failure: -20 coins</div>`
  }
  else if (val == 2) {
    session_minutes = 60;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 2 trees if you fail you kill 2 trees"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +50 coins</div><div>Failure: -40 coins</div>`
  }
  else if (val == 3) {
    session_minutes = 90;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 3 trees if you fail you kill 3 trees"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +75 coins</div><div>Failure: -60 coins</div>`
  }
  else if (val == 4) {
    session_minutes = 120;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 4 trees if you fail you kill 4 trees"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +100 coins</div><div>Failure: -80 coins</div>`
  }
  else if (val == 5) {
    session_minutes = 150;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 5 trees if you fail you kill 5 trees"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +125 coins</div><div>Failure: -100 coins</div>`
  }
  else {
    session_minutes = 180;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
    document.getElementById('treesinfo').innerHTML = "Plants 6 trees if you fail you kill 6 trees"
    document.getElementById('coinsinfo').innerHTML = `<div>Success: +150 coins</div><div>Failure: -120 coins</div>`
  }
}

function giveup() {
  document.getElementById('hidden').value = -1
  document.getrange.submit()
}
function canceltimer() {
  val = document.getElementById('hidden').value = 1
  console.log(val)
  document.getrange.submit()
}
