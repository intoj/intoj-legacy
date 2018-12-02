marked.setOptions({
	renderer: new marked.Renderer(),
	gfm: true,
	tables: true,
	escaped : true,
	breaks: false,
	pedantic: false,
	smartLists: true,
	smartypants: false,
	xhtml: true,
	sanitize: false,
	highlight: function(code,lang){ return hljs.highlightAuto(code).value; }
});
