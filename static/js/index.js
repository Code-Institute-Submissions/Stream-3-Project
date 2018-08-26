

$(document).ready(function() {
    
    // news and special offers carousel on index.html page 
    $('#myCarousel').carousel({
	interval: 10000
	})
});

// Location of Ginas Beauty Studio on Google Maps on index.html page
function initMap() {
  // The location of Ginas Beauty Studio
  var ginas = {lat: 52.162543, lng:  -7.152748};
  // The map, centered at Gina's Beauty Studio
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 18, center: ginas});
  // The marker, positioned at Gina's Beauty
  var marker = new google.maps.Marker({position: ginas, map: map});
}
