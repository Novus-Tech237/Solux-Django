document.addEventListener('DOMContentLoaded', function() {
    // Get the pagination list
    var paginationList = document.querySelectorAll('.page-num');
  
    // Get the current URL
    var currentUrl = window.location.href;
  
    // Define the URLs for each pagination item
    var urlList = [
      "{% url 'tutos:listone' %}",
      "{% url 'tutos:listtwo' %}",
      "{% url 'tutos:listthree' %}"
    ];
  
    // Find the index of the current URL in the URL list
    var activeIndex = urlList.findIndex(function(url) {
      return currentUrl.includes(url);
    });
  
    // Add 'active' class to the pagination item with the current URL
    if (activeIndex > -1) {
      paginationList[activeIndex].classList.add('active');
    }
  });