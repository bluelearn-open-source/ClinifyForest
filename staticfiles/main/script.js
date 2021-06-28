session_minutes = 30;
session_seconds = "00";
function checkr() {
  val = document.getElementById('range').value
  if (val == 1) {
    session_minutes = 30;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
  else if (val == 2) {
    session_minutes = 60;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
  else if (val == 3) {
    session_minutes = 90;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
  else if (val == 4) {
    session_minutes = 120;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
  else if (val == 5) {
    session_minutes = 150;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
  else {
    session_minutes = 180;
    session_seconds = "00";
    document.getElementById('minutes').innerHTML = session_minutes
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
