function createCountdown(count) {
    let num = count;
    return () => num <= 0 || !Number.isInteger(num) ? 0 : num--;
}

const cnt = createCountdown(2);

console.log(cnt());
console.log(cnt());
console.log(cnt());
console.log(cnt());