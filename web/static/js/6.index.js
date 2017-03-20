// external js: isotope.pkgd.js


// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.element-item',
  layoutMode: 'fitRows',
  getSortData: {
    name: '.name',
    symbol: '.symbol',
    number: '.number parseInt',
    category: '[data-category]',
    weight: function( itemElem ) {
      var weight = $( itemElem ).find('.weight').text();
      return parseFloat( weight.replace( /[\(\)]/g, '') );
    }
  }
});

// filter functions
var filterFns = {
  // show if number is greater than 50
  
  // show if name ends with -ium
  
};

// bind filter button click
$('#filters').on( 'click', 'button', function() {
  var filterValue = $( this ).attr('data-filter');
  // use filterFn if matches value
  filterValue = filterFns[ filterValue ] || filterValue;
  $grid.isotope({ filter: filterValue });
});

// bind sort button click


// change is-checked class on buttons
$('.button-group').each( function( i, buttonGroup ) {
  var $buttonGroup = $( buttonGroup );
  $buttonGroup.on( 'click', 'button', function() {
    $buttonGroup.find('.is-checked').removeClass('is-checked');
    $( this ).addClass('is-checked');
  });
});

function clicked() {
  // var resize;

  $("div").click(function() {
    if ($("div.ha").hasClass("loading-start")) {
      if ($("div.ha").hasClass("loading-end")) {
        return $("div.ha").attr("class", "ha");
      }
    } else {
      setTimeout((function() {
        return $("div.ha").addClass("loading-start");
      }), 0);
      setTimeout((function() {
        return $("div.ha").addClass("loading-progress");
      }), 500);
      return setTimeout((function() {
        return $("div.ha").addClass("loading-end");
      }), 1500);
    }
  });

  // resize = function() {
    // return $("body").css({
      // "margin-top": ~~((window.innerHeight - 260) / 2) + "px"
    // });
  // };

  // $(window).resize(resize);

  // resize();

};


function count()
{
	// alert("hihihi");
	for(var i=0; i<=document.querySelectorAll('input[type="checkbox"]').length;i++){
		
		if($("input:eq("+i+")").parent().css("display") === "none"){
				// alert("yes!");
				$("input:eq("+i+")").removeAttr('checked');
		};
		
		// if($("input:eq("+i+")").parent().css("display") === "block"){
				// alert("yes!");
				// $("input:eq("+i+")").attr('checked');
		// };
		
		// if(i == 2){
			// alert($("input:eq("+i+")").attr("id"));
			// alert($("input:eq("+i+")").parent().css("display"));
			// if($("input:eq("+i+")").parent().css("display") === "none"){
				// alert("yes!");
				// $("input:eq("+i+")").removeAttr('checked');
			// };
		// };
	};
	alert(document.querySelectorAll('input[type="checkbox"]:checked').length);
};

$('#myform').submit(function(e){
    e.preventDefault();
   alert("form is valid, do ajax now"); 
});