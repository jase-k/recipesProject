console.log("javascript connected!")

var radioButtons = document.getElementsByClassName('radio')
var submitButton = document.querySelector('#create')

submitButton.addEventListener('click', ()=>{
    
    for(var i = 0 ; i < radioButtons.length; i++){
        if(radioButtons[i].checked){
            submitButton.type = 'submit'
            return
        }
    }
    alert("You must select an option for 'Cooked in under 30 Minutes?'")
    
})

console.log(submitButton)

    console.log("Adding event listener to ", radioButtons)

