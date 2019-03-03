function Click(id){
	classname = ".dropdown-"+id.toString()
	$(classname).slideToggle("fast");
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
	"thumbs-down",
	"github-alt",
	"magic",
	"remove",
	"time",
	"hdd",
	"asterisk",
	"legal",
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
