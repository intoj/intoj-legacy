function Resize(){
	wid = document.body.clientWidth
	a = document.getElementsByClassName("container")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 1100 ) a[i].style.width = "100%"
		else a[i].style.width = "1100px"
	}

	ma = document.getElementsByClassName("main")
	for( var i = 0 ; i < ma.length ; i++ ){
		if( wid < 1200 ) ma[i].style.width = "95%"
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

	stateclassname = ["judge-Accepted","judge-Wrong","judge-Time","judge-Memory","judge-Runtime","judge-Waiting","judge-Running","judge-Compile","judge-Partical","judge-Unknown","judge-Hacked"]
	longstate = ["Accepted","Wrong Answer","Time Limit Exceed","Memory Limit Exceed","Runtime Error","Waiting","Running","Compile Error","Partical Accepted","Unknown Error","Hacked"]
	shortstate= ["AC","WA","TLE","MLE","RE","Wait","Run","CE","PC","UKE","Hack"]
	for( var i = 0 ; i < stateclassname.length ; i++ ){
		a = document.getElementsByClassName(stateclassname[i]);
		for( var j = 0 ; j < a.length ; j++ )
			if( wid < 580 ){
				if(!a[j].innerHTML.match(/shortstate[i]/))
					a[j].innerHTML = a[j].innerHTML.replace(longstate[i],shortstate[i])
			}else{
				if(!a[j].innerHTML.match(longstate[i]))
					a[j].innerHTML = a[j].innerHTML.replace(shortstate[i],longstate[i])
			}
	}
}
