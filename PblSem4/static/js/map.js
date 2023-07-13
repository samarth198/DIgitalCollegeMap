window.onload = function(){
const elems = document.querySelectorAll(".Classroom")
elems.forEach(element => {
    var str = element.innerText;
    if(str.includes("Occupied"))
    {
        // console.log(str.includes("Occupied"));
        element.classList.add("statusColor2");
    }
    else if(str.includes("Vacant"))
    {
        // console.log(str.includes("Occupied"));
        element.classList.add("statusColor1");
    }
    else
    {
        // console.log(str.includes("Occupied"));
        element.classList.add("statusColor3");
    }
});

}