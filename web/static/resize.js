function Resize(){
	wid = document.body.clientWidth
	a = document.getElementsByClassName("container")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 1100 ) a[i].style.width = "100%"
		else a[i].style.width = "1100px"
	}

	a = document.getElementsByClassName("main")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 1200 ) a[i].style.width = "95%"
		else a[i].style.width = "100%"
	}

	a = document.getElementsByClassName("topbarword")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 700 ) a[i].style.display = "none";
		else a[i].style.display = "inline";
	}

	a = document.getElementsByClassName("topbarindex")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 500 ) a[i].style.height = "28px";
		else a[i].style.height = "35px";
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

	stateclassname = ["judge-0","judge-1","judge-2","judge-3","judge-4","judge-5","judge-6","judge-7","judge-8","judge-9","judge-10"]
	longstate = ["Waiting","Running","Unknown Error","Compile Error","Hacked","Wrong Answer","Time Limit Exceed","Memory Limit Exceed","Runtime Error","Partially Accepted","Accepted"]
	shortstate = ["WJ","Run","UKE","CE","Hack","WA","TLE","MLE","RE","PC","AC"]
	for( var i = 0 ; i < stateclassname.length ; i++ ){
		a = document.getElementsByClassName(stateclassname[i]);
		for( var j = 0 ; j < a.length ; j++ ){
			if( wid < 750 ){
				if( a[j].attributes.long_or_short.nodeValue == "long" ){
					a[j].innerHTML = a[j].innerHTML.replace(longstate[i],shortstate[i])
					a[j].attributes.long_or_short.nodeValue = "short"
				}
			}else{
				if( a[j].attributes.long_or_short.nodeValue == "short" ){
					a[j].innerHTML = a[j].innerHTML.replace(shortstate[i],longstate[i])
					a[j].attributes.long_or_short.nodeValue = "long"
				}
			}
		}
	}
}
