const numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

function spellingDigit(n) {
    let number = numbers[n];
    let i = 0;
    return () => Object.keys(numbers).includes(n.toString()) && i < number.length
        ? number[i++]
        : undefined;
}