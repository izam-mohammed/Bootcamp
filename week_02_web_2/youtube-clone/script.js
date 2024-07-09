const element = document.querySelector("#firstbutton");
let clicked = 0
const doc_m = document.querySelector(".main");
const doc_side = document.querySelector(".side-bar");

element.addEventListener("click", () => {
    console.log("clicked");
    if (clicked){
        clicked = 0;
        doc_m.classList.remove("col-md-10");
        doc_m.classList.add("col-md-12");
        doc_side.classList.add("d-md-none");

    }else{
        clicked = 1;
        doc_m.classList.remove("col-md-12");
        doc_m.classList.add("col-md-10");
        doc_side.classList.remove("d-md-none");
    }
});

