const searchForm = document.getElementById("search-form");

if (searchForm){
searchForm.addEventListener('submit', (e) =>{
    e.preventDefault();
    let search = document.getElementById("search-home").value.toLowerCase();
    if (search == "") {
        search = "all"
    }
    let character = "/characters/" + search;

    const frame = document.getElementById("frame");
    let newChar = document.createElement("iframe");

    frame.innerText = "";
    newChar.setAttribute("src", character);
    frame.appendChild(newChar);

})
}