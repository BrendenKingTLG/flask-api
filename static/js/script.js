const searchForm = document.getElementById("search-form")

searchForm.addEventListener('submit', (e) =>{
    e.preventDefault();
    const fd = new FormData(searchForm);
    const obj = Object.fromEntries(fd);
    search = obj.search.toLowerCase();
    if (search == "") {
        search = "all"
    }
    let character = "/characters/" + search;

    const frame = document.getElementById("frame");
    const newChar = document.createElement("iframe");

    frame.innerText = "";
    newChar.setAttribute("src", character);
    frame.appendChild(newChar);

})