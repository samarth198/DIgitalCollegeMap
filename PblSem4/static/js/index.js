var time = document.getElementById("time");
var date = document.getElementById("date");
var day = document.getElementById("day");
var week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
setInterval(() => {
    var d = new Date();
    time.innerHTML = d.toLocaleTimeString();
    date.innerHTML = d.toLocaleDateString();
    day.innerHTML = week[d.getDay()];
}, 1000);