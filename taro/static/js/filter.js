const items = document.querySelectorAll('.filtered');
const itemBtns = document.querySelectorAll('.filter_btns');

function hideItems() {
  items.forEach((item) => {
    item.classList.remove('show');
    item.classList.add('hide');
  });
}

function showItems(i) { 
//Функция для показала блоков
//внутри себя так же будет вызывать функцию скрытие остальных блоков, кроме текущей.
  hideItems();

  items[i].classList.remove('hide');
  items[i].classList.show('show');
}

itemBtns.forEach((btn, i) => {
  btn.addEventListener('click', () => {
//Вешаем событие клика на все кнопки. Каждый будет показывать блоки, по порядку. 
    showItems(i);
  });
});