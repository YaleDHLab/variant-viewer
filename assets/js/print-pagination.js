(function() {
  var pageIndex = 0,
      img = document.querySelector('.print-image'),
      previousPage = document.querySelector('.previous-page'),
      nextPage = document.querySelector('.next-page');

  previousPage.addEventListener('click', function() {
    updatePage(-1);
  });
  nextPage.addEventListener('click', function() {
    updatePage(1);
  });

  function updatePage(val) {
    if (pageIndex > 0 && pageIndex < pages.length-1) {
      pageIndex += val;
    } else if (pageIndex === 0 && val === 1) {
      pageIndex += val;
    } else if (pageIndex === pages.length-1 && val === -1) {
      pageIndex += val;
    }

    img.src = baseurl + '/' + pages[pageIndex];

    var buttons = [previousPage, nextPage];
    for (var i=0; i<buttons.length; i++) {
      buttons[i].className = buttons[i].className.replace(' disabled', '');
    }

    if (pageIndex === 0) previousPage.className += ' disabled';
    if (pageIndex === pages.length-1) nextPage.className += ' disabled';
  }

  updatePage(0)
})()