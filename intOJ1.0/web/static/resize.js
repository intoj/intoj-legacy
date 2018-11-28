function Resize(){
	wid = document.body.clientWidth
	a = document.getElementsByClassName("container")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 1200 ) a[i].style.width = "100%"
		else a[i].style.width = "1200px"
	}
	ma = document.getElementsByClassName("main")[0]
	if( wid < 1200 ) ma.style.width = "90%"
	else ma.style.width = "100%"
	a = document.getElementsByClassName("topbarfiller")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 500 ) a[i].style = "font-size:0px";
		else a[i].style = "font-size:20px";
	}
}
