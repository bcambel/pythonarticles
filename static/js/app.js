(function($){
	$(init);
	function init(){
		$(".articles").masonry({
								   itemSelector : 'a',
								   columnWidth : 400
							   });
	}
})(jQuery);