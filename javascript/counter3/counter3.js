document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = hello;
});

let counter = 0;

function hello() {
    counter++;
    document.querySelector('#counter').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Counter is at ${counter}!`);
    }
}
