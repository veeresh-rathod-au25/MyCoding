function calculateAmt(inquiry, withdrawal, deposit){
    var availableBal = 10000; 
    var a= inquiry(availableBal);
    var b= deposit(availableBal);
    var c= withdrawal(availableBal);
    if(a){

        availableBal =  inquiry(availableBal);
    }
    else if(b){
        availableBal =  availableBal - withdrawal;
        if(withdrawal > availableBal){
            alert("You have insufficient funds");  
        }
    }
    else{
        availableBal =  availableBal + deposit;
    }
    return availableBal;
}
