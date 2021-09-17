let input = document.getElementById("input")
let submit_btn = document.getElementById("submit")
let output = document.getElementById("output")

submit_btn.addEventListener("click",function(){
    let arr = []
    for (let i = 0; i < input.value.length; i++){
        if (input.value.charAt(i) === "#"){
            arr.pop()
        }
        else{
            arr.push(input.value.charAt(i))
        }
    }
    output.innerText = arr.join("")    
})