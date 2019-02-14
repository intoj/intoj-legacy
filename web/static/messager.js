function Messagerinit(){
	Messenger.options = {
	    extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-right',
		showCloseButton: true,
	    theme: 'air'
	}
}
function Message_Ok(message){
	Messenger().post({
		message: message,
		showCloseButton: true
	});
}
function Message_Error(message){
	Messenger().post({
		message: message,
		type: 'error',
		showCloseButton: true
	});
}
