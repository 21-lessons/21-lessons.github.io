import jquery from 'jquery';
window.$ = window.jQuery = jquery;

+function ($) {
  'use strict';

  // When the DOM is ready, run this function
  $(document).ready(function() {
    //Set the carousel options
    $('#quote-carousel').carousel({
      pause: true,
      interval: 4000,
    });
  });
}(jQuery);
