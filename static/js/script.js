function displayResults() {
    document.getElementById("results").style.display = "block";
  }

function sortPriceDown() {
    document.getElementById("pricedownbtn").style.display = "none";
    document.getElementById("priceupbtn").style.display = "block";
    var value = 1;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/sort', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.send('value=' + value);
  }
function sortPriceUp() {
    document.getElementById("pricedownbtn").style.display = "block";
    document.getElementById("priceupbtn").style.display = "none";
    var value = 2;
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/sort', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.send('value=' + value);
  }

function sortBedDown() {
    document.getElementById("beddownbtn").style.display = "none";
    document.getElementById("bedupbtn").style.display = "block";
  }
function sortBedUp() {
    document.getElementById("beddownbtn").style.display = "block";
    document.getElementById("bedupbtn").style.display = "none";
  }

  function sortBathDown() {
    document.getElementById("bathdownbtn").style.display = "none";
    document.getElementById("bathupbtn").style.display = "block";
  }
function sortBathUp() {
    document.getElementById("bathdownbtn").style.display = "block";
    document.getElementById("bathupbtn").style.display = "none";
  }


function getData() {
    var text = document.getElementById("input-text").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("data-container").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/", true);
    xhttp.send();
}
