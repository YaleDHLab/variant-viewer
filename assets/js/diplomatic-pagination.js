(function() {

  if (!window.location.hash) window.location.hash = '#_';

  var pageText = document.querySelector('.page-text'),
      pageImage = document.querySelector('.page-image'),
      container = document.querySelector('.page-buttons'),
      buttons = container.querySelectorAll('.page-button'),
      pageButtons = container.querySelectorAll('.page'),
      startButton = container.querySelector('.start'),
      endButton = container.querySelector('.end'),
      previousButton = container.querySelector('.previous'),
      nextButton = container.querySelector('.next'),
      editionSelect = document.querySelector('.witness-select'),
      params = getSearchParams();

  setSelectedEdition();
  updatePagination();

  /**
  * Attach pagination event listeners
  **/

  for (var i=0; i<buttons.length; i++) {
    var button = buttons[i];

    button.addEventListener('click', function(e) {
      var elem = e.target;
      while (!elem.hasAttribute('data-page')) {
        elem = elem.parentNode;
      }

      params.page = parseInt(elem.dataset.page);
      updatePagination();
    })
  }

  /**
  * Attach edition changing event listeners
  **/

  editionSelect.addEventListener('change', function(e) {
    params.edition = parseInt(e.target.value);
    params.page = 1;
    updatePagination();
  })

  /**
  * Make the select value reflect the url params on page load
  **/

  function setSelectedEdition() {
    var options = editionSelect.querySelectorAll('option');
    for (var i=0; i<options.length; i++) {
      var option = options[i],
          value = parseInt(option.getAttribute('value'))
      if (value === params.edition) {
        option.setAttribute('selected', true);
      }
    }
  }

  /**
  * Search param getters and setters
  **/

  function getSearchParams() {
    var params = {},
        search = window.location.hash.substring(2);
    if (search[0] === '?') search = search.substring(1);
    if (search.length) {
      var terms = search.split('&');
      if (terms.length > 0) {
        for (var i=0; i<terms.length; i++) {
          var splitTerm = terms[i].split('=');
          params[splitTerm[0]] = parseInt(splitTerm[1]);
        }
      }
    }

    return params;
  }

  function setSearchParams() {
    if (!params.page) params.page = 1;
    if (!params.edition) params.edition = 1;
    var search = '?';

    Object.keys(params).forEach(function(i) {
      search += i + '=' + params[i] + '&';
    })

    // trim the trailing &
    search = search.substring(0, search.length-1);
    window.location.hash = '#_' + search;
  }

  /**
  * Callbacks for event listeners
  **/

  function updatePagination() {
    setSearchParams();
    loadPageContent();
    updateButtonLabels();
    updateHighlightedButton();
    updateButtonStates();
  }

  /**
  * Leverage data cached in page script tags to
  * create json calls
  **/

  function loadPageContent() {
    var page = editions[params.edition-1].pages[params.page-1];
    pageText.innerHTML = page.lines.join('');
    pageImage.src = baseurl + page.image;
  }

  function updateHighlightedButton() {
    var pageClass = 'page-button page ';

    for (var i=0; i<pageButtons.length; i++) {
      var pageButton = pageButtons[i],
          pageNumber = parseInt(pageButton.dataset.page);

      pageButton.className = pageNumber === params.page ?
          pageClass + 'active' :
          pageClass;
    }
  }

  function updateButtonLabels() {
    var pages = getEditionPages();

    if ((params.page > 2) && (params.page < pages.length-2)) {
      var startVal = params.page-2;
    } else if (params.page <= 2) {
      var startVal = 1;
    } else {
      var startVal = pages.length - 4;
    }

    for (var i=0; i<pageButtons.length; i++) {
      var button = pageButtons[i];
      button.dataset.page = startVal + i;
      button.textContent = startVal + i;
    }

    previousButton.dataset.page = params.page - 1;
    nextButton.dataset.page = params.page + 1;
    endButton.dataset.page = pages.length;
  }

  function updateButtonStates() {
    var buttonClass = 'page-button ',
        startClass = buttonClass + ' start ',
        endClass = buttonClass + ' end ',
        previousClass = buttonClass + ' previous ',
        nextClass = buttonClass + ' next ',
        pages = getEditionPages();

    startButton.className = params.page === 1 ?
        startClass + 'deactivated'
      : startClass;

    previousButton.className = params.page === 1 ?
        previousClass + 'deactivated'
      : previousClass;

    nextButton.className = params.page === pages.length ?
        nextClass + 'deactivated'
      : nextClass;

    endButton.className = params.page === pages.length ?
        endClass + 'deactivated'
      : endClass;
  }

  function getEditionPages() {
    return editions[params.edition-1].pages;
  }

})()