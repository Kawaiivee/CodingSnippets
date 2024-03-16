(function ($) {
  $(document).ready(function () {
    (function () {
      document.
      var finnListItem = $('#finnListItem');
      var finnAgeItem = $('#finnAge');

      console.log(finnListItem);  // Log the entire element to check if it's found
      console.log($('#finnAge'));  // Log the '#finnAge' selector to check if it's found

      console.log(finnListItem.html());

      finnListItem.attr("style", "color: " + finnAgeItem.text() + ";");
    })();
  });
})(jQuery);