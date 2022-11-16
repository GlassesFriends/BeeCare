$(document).ready(function() {
    
  	// .cover-img class MANDATORY  attrs 
    // bg-size(number 1-4 .. 1 being full screen 3 = 1/4 of screen, % or px) null = full screen - px 
    // parallax - true : false.  default: false
	// bg-pos-y: number in px
    // bg-pos-x: number in px
    // bg-pos: numer in px
	$('.cover-img').each(function(index, el) {
        $(el).attr('id', 'bg_'+index);
        bgPos = $(el).attr('bg-pos');
        bgPosY = $(el).attr('bg-pos-y');
        bgPosX = $(el).attr('bg-pos-x');
		bgSize = $(el).attr('bg-size').split(",");
		bgSize[0] = parseFloat(bgSize[0]);
		parallax = $(el).attr('parallax');
		bgurl = $(el).attr('url');
        bgColor = $(el).attr('color');
		$("#"+el.id).css("background", "url("+bgurl+") no-repeat center center");
        if(typeof bgPos !== "undefined"){
            $("#"+el.id).css("background-position", bgPos);
        }  
        if(typeof bgPosY !== "undefined"){
            $("#"+el.id).css("background-position-y", bgPosY);
        }  
        if(typeof bgPosX !== "undefined"){
            $("#"+el.id).css("background-position-x", bgPosX);
        }
          if(typeof bgColor !== "undefined"){
            $("#"+el.id).css("background-color", "#"+bgColor);
        } 
		$(el).addClass('row');

		if(bgSize.length < 2){
			if(!$.isNumeric(bgSize[0]) ){
				bgSize[0] = 1;
			} 

			if(bgSize[0] <= 4){
				bgPx(el, bgSize, parallax);
			} else if(bgSize[0] > 4){
				bgPercent(el, bgSize, parallax);
			}

		} else {
			bgSize[1] = $.trim(bgSize[1]);
		}



		if(bgSize[1] === '%'){
			bgPercent(el, bgSize, parallax);
		} else if(bgSize[1] === 'px'){
			bgPx(el, bgSize, parallax);
		}

	});

});

// ****** BACKGROUND COVER JS ****** // 

function bgPercent(el, bgSize, parallax){

	 $("#"+el.id).css({
	 	'padding-bottom' 		: 	bgSize[0]+"%",   // if bgSize = 0 height = content
	 	'background-attachment' : 	((parallax === 'true') ? 'fixed' : ''),
        'background-size'       :   '100%',
	 });
}

function bgPx(el, bgSize, parallax){
	h = $(window).height();
	$("#"+el.id).css({
		"width"					: 	'100%',
		"height"				: 	h/bgSize[0], 
		'background-attachment' : 	((parallax === 'true') ? 'fixed' : ''),
        'background-size'       :   '100%',
	});
}




















