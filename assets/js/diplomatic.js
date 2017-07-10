(function() {
  if (!window.location.hash) window.location.hash = 0;

  var nextPage = document.querySelector('.next-page'),
      previousPage = document.querySelector('.previous-page'),
      diplomaticPage = document.querySelector('.diplomatic-page'),
      pages = diplomaticPage.querySelectorAll('.page'),
      hash;

  nextPage.addEventListener('click', function() {
    setHash();
    updateLocation(1);
  })

  previousPage.addEventListener('click', function() {
    setHash();
    updateLocation(-1);
  })

  function updateLocation(offset) {
    window.location.href = '#' + (hash + offset);
    hash += offset;
    updateButtonStates();
  }

  function setHash() {
    hash = parseInt(window.location.hash.substring(1));
  }

  function updateButtonStates() {
    previousPage.className = hash === 0 ?
        'previous-page deactivated'
      : 'previous-page'

    nextPage.className = hash === pages.length -1 ?
        'next-page deactivated'
      : 'next-page'
  }

  setHash();
  updateButtonStates();
})()