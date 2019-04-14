function Update(obj,html){
	if( $(obj).html() != html ){
		$(obj).html(html)
		// console.log($(obj).html());
		// console.log(html)
	}
}
var can_see_messages
function Generate_Subtask_Html(subtask){
	var s = '\
<div id="subtask_{id}">\n\
<div class="listline listline-animation unselect" onclick="Click({id});">\n\
	<span class="listitem onewide center"> #{id} </span>\n\
	<span class="listitem sixwide center" id="subtask_{id}_judge_status">\n\
		<span class="judge-{status}" long_or_short="long">\n\
			<i class="icon-{statusicon}" aria-hidden="true"></i>  {statusname}\n\
		</span>\n\
	</span>\n\
	<span class="listitem twowide center" id="subtask_{id}_score">\n\
		<span style="color:{score_color};">\n\
			{score}<span style="font-size: 10px" class="dropdown-{id}" show_or_hide="hide" hidden="hidden">/{full_score}</span>\n\
		</span>\n\
	</span>\n\
	<span class="listitem twowide center" id="subtask_{id}_time_usage"> {time_usage} ms </span>\n\
	<span class="listitem twowide center" id="subtask_{id}_memory_usage"> {memory_usage} M </span>\n\
</div>\n'.format({
	id: subtask['id'],
	status: subtask['status'],
	statusicon: statusicon[subtask['status']],
	statusname: tostatus[subtask['status']],
	score_color: Score_Color(subtask['score'],subtask['full_score']),
	score: subtask['score'],
	full_score: subtask['full_score'],
	time_usage: subtask['time_usage'],
	memory_usage: subtask['memory_usage']
})
	if(can_see_messages){
		s += '\
<div class="dropdown dropdown-{id}" hidden="hidden">\n\
	<div class="markdown">\n'.format({id:subtask['id']})
		if( subtask['checker_message'] != "" )
			s += '\
<h3> 比较器信息 </h3>\n\
<pre><code class="hljs language-plain"><code class="hljs plaintext">{0}\n\
</code></code></pre>\n'.format(subtask['checker_message'])
		if( subtask['judger_message'] != "" )
			s += '\
<h3> 比较器信息 </h3>\n\
<pre><code class="hljs language-plain"><code class="hljs plaintext">{0}\n\
</code></code></pre>\n'.format(subtask['judger_message'])
		s += '\
	</div>\n\
</div>\n\
</div>\n'
	}
	return s
}

var current_status = -1
var last_subtasks = new Array()
var updcnt = 0
function Get_Judge_Status(rid){
	htmlobj=$.ajax({
		url: "/record/"+rid+"/ref",
		data: rid,
		success: function(data,status){
			var val = eval("("+data+")");
			if( val.success == 0 ){
				Message_Error(val.message)
				return
			}else{
				record = val.record
				current_status = record['status']
				Update('#overview_judge_status',Judge_Status(record['status']))
				Update('#overview_score',Judge_Score(record['score']))
				if( current_status >= 4 || current_status <= 1 ){
					Update('#overview_time_usage',record['time_usage'].toString()+" ms")
					Update('#overview_memory_usage',record['memory_usage'].toString()+" M")
				}
				Update('#compilation',record['compilation'])
				Update('#system_message',record['system_message'])
				subtasks = eval("("+record['result']+")")['subtasks']
				if( record['result'] != "" && current_status != 0 ){
					for( subtask_id in subtasks ){
						subtask = subtasks[subtask_id]
						if( last_subtasks[subtask_id] != undefined && last_subtasks[subtask_id]['status'] == subtask['status'] ) continue
						last_subtasks[subtask_id] = subtask
						subtask_html = Generate_Subtask_Html(subtask)
						subtask_htmlid = '#subtask_{0}'.format(subtask['id'])
						if( $(subtask_htmlid).length > 0 ){
							$(subtask_htmlid).prop('outerHTML',subtask_html)
							updcnt += 1
							console.log(updcnt);
						}else{
							$("#subtasks").append(subtask_html)
						}
					}
				}
			}
		},
		error: function(){
			Message_Error("获取状态失败, 可能是网络出锅或服务器出锅. 请尝试刷新界面.")
		}
	});
}

function Auto_Refresh(cnt,rid){
	timeout = 200
	if( current_status <= 1 && cnt <= 6000 )
		Get_Judge_Status(rid)
	setTimeout(function(){Auto_Refresh(cnt+1,rid)},timeout);
}

function Refresh_Begin(rid,nowuser_can_see_messages){
	can_see_messages = nowuser_can_see_messages
	Auto_Refresh(1,rid);
}
