console.log("javascript connected!")

var radioButtons = document.getElementsByClassName('radio')
var submitButton = document.querySelector('#create')

submitButton.addEventListener('click', ()=>{
    if(submitButton.type == 'button'){
        alert("Must choose an Option for: 'Cook under 30 Minutes?'")
    }
})
console.log(submitButton)

for(var i = 0 ; i < radioButtons.length; i++){
    radioButtons[i].addEventListener("click", () =>{
        submitButton.type = 'submit'
    })
    console.log("Adding event listener to ", radioButtons[i])
}
