(function($) {

	// Ensure the DOM is ready
	$(document).ready(function() {

		// Toggle the side menu when the menu button is clicked
		$('#menu-toggle').on('click', function() {
			var $sideMenu = $('#side-menu');
			$sideMenu.toggleClass('open');
		});

		// Close the side menu when a link is clicked
		$('#side-menu a').on('click', function() {
			$('#side-menu').removeClass('open');
		});

	});

})(jQuery);
