// function toggleSortButton(icon) {
//   const sortButton = document.getElementById('sort-button');
//   const currentUrl = new URL(window.location.href);
//   const currentOrder = currentUrl.searchParams.get('order_by');
//
//   if (currentOrder === 'pub_date') {
//     icon.classList.toggle("change");
//     currentUrl.searchParams.set('order_by', '-pub_date');
//   } else {
//     // icon.classList.toggle("change");
//     currentUrl.searchParams.set('order_by', 'pub_date');
//   }
//
//   setTimeout(() => {
//     window.location.href = currentUrl.toString();
//   }, 500);
// }

function toggleSortButton(icon) {
  const sortButton = document.getElementById('sort-button');
  const currentUrl = new URL(window.location.href);
  const currentOrder = currentUrl.searchParams.get('order_by');

  if (currentOrder === 'pub_date') {
    icon.classList.toggle("change");
    currentUrl.searchParams.set('order_by', '-pub_date');
  } else {
    icon.classList.toggle("change");
    currentUrl.searchParams.set('order_by', 'pub_date');
  }

  setTimeout(() => {
    window.location.href = currentUrl.toString();
  }, 400);
}



