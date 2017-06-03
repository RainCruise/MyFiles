var spinner;
var queryStr='';
var curPage=1;



function trunc(s,limit){
	if(s.length>limit){
		return s.substring(0,limit-3)+"...";
	} else {
		return s;
	}
}

function genItem(doc,tokens){	
	showTitle = trunc(doc.title,22);
	for(i=0;i<tokens.length;++i){
		showTitle = showTitle.replace(new RegExp(tokens[i],'gi'),"<em>"+tokens[i]+"</em>");		
		doc.abst = doc.abst.replace(new RegExp(tokens[i],'gi'),"<em>"+tokens[i]+"</em>");
	}
	
	showUrl = trunc(doc.url,60);
	html="<li class=doc_item> <h3><a href=\""+doc.url+"\">"+showTitle+"</a></h3>"+
		"<cite>"+showUrl+"</cite>" +
		"<p class=\"content\">"+doc.abst+"</p>"+
		"</li>";
	node = $(html);
	return node;
}


function do_search(page,query){
	//alert(1);		
	
	$.get("/LaiChenSearch/servlet/MyServer",{"page":page,"query":query},function(result){
		showResult(result);
	});
	//$("#el").show().spin();
	$("#resultSet").hide("drop",{},1000);
	
	
	return false;
}

function genPageBar(total){
	//alert("gen"+total);
	pageBar = $("#pageBar");
	pageBar.empty();
	
	for(var i=1;i<=total;++i){
		node = null;
		if(i==curPage){
			node = $('<strong><span class="fk"><img src="image/currentPage.png" class="fkcur"/></span><span class="pc">'+i+'</span></strong>');
			
		} else {			
			cls = (i%2==1?"fkdown":"fkup");
			if(i>curPage)
			    node = $('<a href="#"><span class="fk"><img src="image/rightPage.png" class="'+cls+'"/></span><span class="pc">'+i+'</span></a>');
			else 
				node = $('<a href="#"><span class="fk"><img src="image/leftPage.png" class="'+cls+'"/></span><span class="pc">'+i+'</span></a>');
			node[0].i = i;			
			node[0].onclick=function(){		
				curPage = this.i;
				do_search(this.i,queryStr);
			};			
		}		
		pageBar.append(node);
	}	
}
function showResult(result){	
	$("#el").fadeOut(500,function(){
		$("#resultSet").show("drop",{},1000);
	});
	
		
	
	
	res = $("#result");
	res.empty();
	genPageBar(result.totalPages);
	for(var i=0;i<result.docs.length;++i){
		doc = result.docs[i];
		child_node = genItem(doc,result.tokens);
		res.append(child_node);		
	}	
}
$(document).ready(function(){
	
	
	$("#search").click(function(){
		queryStr = $("#query").val();
		curPage = 1;
		do_search(1,queryStr);
	});
	
});
