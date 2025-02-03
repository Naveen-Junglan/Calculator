let inputs = document.getElementById('#input');
let text = document.querySelector('#text');


function add() {
    if (input.value === '') {
        alert('Please enter a task');
    } else {
        let ul = document.createElement('ul');
        ul.innerHTML = `${input.value} <button class="btn2" onclick="this.parentElement.remove()">Delete</button>`;
        text.appendChild(ul);
        input.value = '';
    }
}