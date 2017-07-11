(function() {
  if (!window.location.hash) window.location.hash = 0;

  var pages = document.querySelectorAll('.page-content'),
      container = document.querySelector('.diplomatic-footer-buttons'),
      buttons = container.querySelectorAll('.diplomatic-footer-button'),
      pageButtons = container.querySelectorAll('.page'),
      startButton = container.querySelector('.start'),
      endButton = container.querySelector('.end'),
      previousButton = container.querySelector('.previous'),
      nextButton = container.querySelector('.next'),
      hash = parseInt(window.location.hash.substring(1));

  updateButtons();

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
      updateButtons();
    })
  }

  /**
  * Callbacks for event listeners
  **/

  function updateButtons() {
    updateButtonLabels();
    updateHighlightedPage();
    updateButtonStates();
  }

  function updateHighlightedPage() {
    var pageClass = 'diplomatic-footer-button page ';

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
      var startVal = pages.length - 5;
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
    var buttonClass = 'diplomatic-footer-button ',
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

    nextButton.className = hash === pages.length-1 ?
        nextClass + 'deactivated'
      : nextClass;

    endButton.className = hash === pages.length-1 ?
        endClass + 'deactivated'
      : endClass;
  }
})()