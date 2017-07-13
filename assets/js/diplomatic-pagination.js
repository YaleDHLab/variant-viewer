(function() {
  if (!window.location.hash) window.location.hash = 1;

  var pageText = document.querySelector('.page-text'),
      pageImage = document.querySelector('.page-image'),
      container = document.querySelector('.page-buttons'),
      buttons = container.querySelectorAll('.page-button'),
      pageButtons = container.querySelectorAll('.page'),
      startButton = container.querySelector('.start'),
      endButton = container.querySelector('.end'),
      previousButton = container.querySelector('.previous'),
      nextButton = container.querySelector('.next'),
      hash = parseInt(window.location.hash.substring(1));

  updatePagination();

  /**
  * Attach event listeners
  **/

  for (var i=0; i<buttons.length; i++) {
    var button = buttons[i];

    button.addEventListener('click', function(e) {
      var elem = e.target;
      while (!elem.hasAttribute('data-page')) {
        elem = elem.parentNode;
      }

      hash = parseInt(elem.dataset.page);
      window.location.href = '#' + hash;
      updatePagination();
    })
  }

  /**
  * Callbacks for event listeners
  **/

  function updatePagination() {
    loadPageContent();
    updateButtonLabels();
    updateHighlightedPage();
    updateButtonStates();
  }

  /**
  * Leverage data cached in page script tags to
  * create json calls
  **/

  function loadPageContent() {
    pageText.innerHTML = pages[hash-1].lines.join('');
    pageImage.src = baseurl + pages[hash-1].image;
  }

  function updateHighlightedPage() {
    var pageClass = 'page-button page ';

    for (var i=0; i<pageButtons.length; i++) {
      var pageButton = pageButtons[i],
          pageNumber = parseInt(pageButton.dataset.page);

      pageButton.className = pageNumber === hash ?
          pageClass + 'active' :
          pageClass;
    }
  }

  function updateButtonLabels() {
    if ((hash > 2) && (hash < pages.length-2)) {
      var startVal = hash-2;
    } else if (hash <= 2) {
      var startVal = 1;
    } else {
      var startVal = pages.length - 4;
    }

    for (var i=0; i<pageButtons.length; i++) {
      var button = pageButtons[i];
      button.dataset.page = startVal + i;
      button.textContent = startVal + i;
    }

    previousButton.dataset.page = hash - 1;
    nextButton.dataset.page = hash + 1;
  }

  function updateButtonStates() {
    var buttonClass = 'page-button ',
        startClass = buttonClass + ' start ',
        endClass = buttonClass + ' end ',
        previousClass = buttonClass + ' previous ',
        nextClass = buttonClass + ' next ';

    startButton.className = hash === 1 ?
        startClass + 'deactivated'
      : startClass;

    previousButton.className = hash === 1 ?
        previousClass + 'deactivated'
      : previousClass;

    nextButton.className = hash === pages.length ?
        nextClass + 'deactivated'
      : nextClass;

    endButton.className = hash === pages.length ?
        endClass + 'deactivated'
      : endClass;
  }
})()