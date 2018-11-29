function Resize(){
	wid = document.body.clientWidth
	a = document.getElementsByClassName("container")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 1100 ) a[i].style.width = "100%"
		else a[i].style.width = "1100px"
	}

	ma = document.getElementsByClassName("main")
	for( var i = 0 ; i < ma.length ; i++ ){
		if( wid < 1200 ) ma[i].style.width = "90%"
		else ma[i].style.width = "100%"
	}

	a = document.getElementsByClassName("topbarfiller")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 500 ) a[i].style = "font-size:0px";
		else a[i].style = "font-size:20px";
	}

	a = document.getElementsByClassName("block");
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 600 ){
			a[i].style.width = "93%"
			a[i].style.padding = "5px 10px"
		}else{
			a[i].style.width = "93%"
			a[i].style.padding = "5px 20px"
		}
	}
}
