var subtask_before = ""
function Get_Judge_Status(rid){
	htmlobj=$.ajax({
		url: "/record/"+rid+"/ref",
		data: rid,
		success: function(data,status){
			var val = eval("("+data+")");
			// console.log(val);
			if( val.success == 0 ){
				Message_Error(val.message)
				return
			}else{
				status_before = $("#status").text()
				if( status_before != val.record[4] ){
					$("#overview").html(val.record_html)
				}else{
					$("#overview_score").html(val.record[5].toString())
					$("#overview_score").css("color",val.score_color)
					$("#overview_time_usage").text(val.record[8]+"ms")
					$("#overview_memory_usage").text(val.record[9]+"M")
				}
				if( subtask_before != val.subtasks_html ){
					subtask_before = val.subtasks_html;
					$("#subtasks").html(val.subtasks_html)
				}
				Render()
				Cannotselect()
			}
		},
		error: function(){
			setTimeout("Message_Error('获取状态失败, 可能是网络出锅或服务器出锅. 请尝试刷新界面.')",200)
		}
	});
}

function Auto_Refresh(cnt,rid){
	// console.log("Refresh x "+cnt.toString());
	// console.log($("#status").text());
	timeout = 200
	if( $("#status").text() > 1 || cnt > 6000 ) return;
	Get_Judge_Status(rid)
	setTimeout(function(){Auto_Refresh(cnt+1,rid)},timeout);
}

function Refresh_Begin(rid){
	Auto_Refresh(1,rid);
}
