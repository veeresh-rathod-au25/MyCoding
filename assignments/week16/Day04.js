var isPalindrome = function (string) {
    if (string == string.split('').reverse().join('')) {
        alert(string + ' is palindrome.');
    }
    else {
        alert(string + ' is not palindrome.');
    }
}

document.getElementById('form_id').onsubmit = function() {
   isPalindrome(document.getElementById('your_input').value);
}

function countSquares(a, b)
{
   let cnt = 0;
    
    for (let i = a; i <= b; i++)
 
        for (let j = 1; j * j <= i;j++)
            if (j * j == i)
                cnt++;
 
    return cnt;
}
 
 
    let a = 9;
    let b = 25;
    document.write( "Count of squares is ",
              countSquares(a, b));
 