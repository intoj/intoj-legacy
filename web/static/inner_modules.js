function Cannotselect(){
	$(".unselect").attr("onselectstart","return false");
	$(".unselect").attr("onselectstart","return false");
}

function Resize(){
	wid = document.body.clientWidth

	a = document.getElementsByClassName("topbarword")
	for( var i = 0 ; i < a.length ; i++ ){
		if( wid < 800 ) a[i].style.display = "none";
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
		a = $("."+stateclassname[i]);
		if( wid < 750 ){
			if( a.attr("long_or_short") == "long" ){
				a.html(function(j,text){return text.replace(longstate[i],shortstate[i])})
				a.attr("long_or_short","short")
			}
		}else{
			if( a.attr("long_or_short") == "short" ){
				a.html(function(j,text){return text.replace(shortstate[i],longstate[i])})
				a.attr("long_or_short","long")
			}
		}
	}
}

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

tostatus = [
	"Waiting",
	"Running",
	"Unknown Error",
	"Compile Error",
	"Hacked",
	"Wrong Answer",
	"Time Limit Exceed",
	"Memory Limit Exceed",
	"Runtime Error",
	"Partially Accepted",
	"Accepted"
]
statusicon = [
	"spinner icon-spin",
	"spinner icon-spin",
	"twitter",
	"github-alt",
	"magic",
	"remove",
	"time",
	"hdd",
	"asterisk",
	"adjust",
	"ok"
]
function Judge_Status(status){
	status = parseInt(status)
	html = "<span class=\"judge-" + status.toString() + "\">"
	html += "<i class=\"icon-" + statusicon[status] + "\"></i> "
	html += tostatus[status]
	html += "</span>"
	return html
}
