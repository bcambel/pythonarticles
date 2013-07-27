(function($){
	var $leftMenu, $article, html;
	$(init);
	function init(){
		// $(".articles").masonry({
		// 						   itemSelector : 'a',
		// 						   columnWidth : 230
		// 					   });
		$article = $('article');
		$leftMenu = $('#left-menu');
		if($leftMenu.length>0){
			renderLeftMenu();
		}
	}

	function renderLeftMenu(){
		html = [];
		$('h2',$article).each(function(i,x){
			html.push("<li><a href='#section");
			html.push(i);
			html.push("'>")
			html.push($(x).text());
			html.push("</a></li>");
			$(x).attr("id","section"+i.toString());
		});
		$("ul",$leftMenu).html(html.join(""));
	}
})(jQuery);