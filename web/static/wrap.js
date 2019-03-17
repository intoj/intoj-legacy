function Wrap(){
	a = $(".listitem > *.dynamicsize")
	for( var i = 0 ; i < a.length ; i++ ){
		listitem = a[i].closest("span.listitem")
		font_sz = 17
		for( var j = 1 ; j <= 5 ; j++ ){
			listitem_width = $(listitem).width()
			a_width = $(a[i]).width()
			if( listitem_width <= a_width ){
				$(a[i]).css("font-size",font_sz-1)
				font_sz--
			}
		}
	}
}
