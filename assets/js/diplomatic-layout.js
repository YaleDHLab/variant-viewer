(function() {

  var layoutButtons = document.querySelectorAll('.layout-button'),
      textImageLayoutButton = document.querySelector('.text-image-layout'),
      imageLayoutButton = document.querySelector('.image-layout'),
      textLayoutButton = document.querySelector('.text-layout')
      pageImageContainer = document.querySelector('.page-image-container'),
      pageTextContainer = document.querySelector('.page-text-container'),
      pageImage = document.querySelector('.page-image');

  /**
  * Display text and image
  **/

  textImageLayoutButton.addEventListener('click', function(e) {
    pageImageContainer.style.width = '50%';
    pageImageContainer.style.display = 'inline-block';
    pageImageContainer.style.textAlign = 'right';
    pageImage.style.width = '100%';
    pageTextContainer.style.left = '50%';
    pageTextContainer.style.width = '50%';
    pageTextContainer.style.display = 'inline-block';

    updateButtonState(e);
  })

  /**
  * Display image only
  **/

  imageLayoutButton.addEventListener('click', function(e) {
    pageImageContainer.style.width = '100%';
    pageImageContainer.style.display = 'inline-block';
    pageImageContainer.style.textAlign = 'center';
    pageImage.style.width = '50%';
    pageTextContainer.style.display = 'none';

    updateButtonState(e);
  })

  /**
  * Display text only
  **/

  textLayoutButton.addEventListener('click', function(e) {
    pageImageContainer.style.display = 'none';
    pageTextContainer.style.width = '100%';
    pageTextContainer.style.display = 'inline-block';
    pageTextContainer.style.left = '0%';
    pageTextContainer.style.textAlign = 'center';

    updateButtonState(e);
  })

  function updateButtonState(e) {
    var elem = e.target;
    while (!elem.className.includes('layout-button')) {
      elem = elem.parentElement;
    }

    for (var i=0; i<layoutButtons.length; i++) {
      var button = layoutButtons[i];
      button.className = button.className.replace(' active', '');
    }

    elem.className += ' active';
  }

})()