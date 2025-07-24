document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector("[data-search]");

    searchInput.addEventListener("input", (e) => {
        const searchValue = e.target.value;

        // Send an AJAX request to the server to perform the search
        fetch(`/search/?search_query=${searchValue}`)
            .then(response => response.json())
            .then(data => {
                // Update the displayed data based on the search result
                updateTable(data);
            })
            .catch(error => console.error('Error:', error));
    });
});


function updateTable(Odata) {
    const tableBody = document.querySelector('tbody');
    tableBody.innerHTML = '';

    Odata.forEach(item => {
        const row = document.createElement('tr');
        for (const key in item) {
            const cell = document.createElement('td');
            cell.textContent = item[key]; 
            row.appendChild(cell);
        }
        tableBody.appendChild(row);
    });
}


// ---------Responsive-navbar-active-animation-----------
function test(){
	var tabsNewAnim = $('#navbarSupportedContent');
	var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
	var activeItemNewAnim = tabsNewAnim.find('.active');
	var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
	var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
	var itemPosNewAnimTop = activeItemNewAnim.position();
	var itemPosNewAnimLeft = activeItemNewAnim.position();
	$(".hori-selector").css({
		"top":itemPosNewAnimTop.top + "px", 
		"left":itemPosNewAnimLeft.left + "px",
		"height": activeWidthNewAnimHeight + "px",
		"width": activeWidthNewAnimWidth + "px"
	});
	$("#navbarSupportedContent").on("click","li",function(e){
		$('#navbarSupportedContent ul li').removeClass("active");
		$(this).addClass('active');
		var activeWidthNewAnimHeight = $(this).innerHeight();
		var activeWidthNewAnimWidth = $(this).innerWidth();
		var itemPosNewAnimTop = $(this).position();
		var itemPosNewAnimLeft = $(this).position();
		$(".hori-selector").css({
			"top":itemPosNewAnimTop.top + "px", 
			"left":itemPosNewAnimLeft.left + "px",
			"height": activeWidthNewAnimHeight + "px",
			"width": activeWidthNewAnimWidth + "px"
		});
	});
}
$(document).ready(function(){
	setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
	setTimeout(function(){ test(); }, 500);
});
$(".navbar-toggler").click(function(){
	$(".navbar-collapse").slideToggle(300);
	setTimeout(function(){ test(); });
});



// --------------add active class-on another-page move----------
jQuery(document).ready(function($){
	// Get current path and find target link
	var path = window.location.pathname.split("/").pop();

	// Account for home page with empty path
	if ( path == '' ) {
		path = 'index.html';
	}

	var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
	// Add active class to target link
	target.parent().addClass('active');
});




/*
$(window).on('load',function () {
	var current = location.pathname;
	console.log(current);
$('#navbarSupportedContent ul li a').each(function(){
		var $this = $(this);
		// if the current path is like this link, make it active
		if($this.attr('href').indexOf(current) !== -1){
			$this.parent().addClass('active');
			$this.parents('.menu-submenu').addClass('show-dropdown');
			$this.parents('.menu-submenu').parent().addClass('active');
		}else{
			$this.parent().removeClass('active');
	}
	})
});*/


// Function to reset checkboxes
function resetCheckboxes() {
	var checkboxes = document.getElementsByName('column');
	for (var i = 0; i < checkboxes.length; i++) {
		checkboxes[i].checked = false;
	}
}

// Function to maintain the state of checkboxes after form submission
window.onload = function() {
	var checkboxes = document.getElementsByName('column');
	var params = new URLSearchParams(window.location.search);
	
	checkboxes.forEach(function(checkbox) {
		var columnValue = checkbox.value;
		if (params.getAll('column').includes(columnValue)) {
			checkbox.checked = true;
		}
	});
}

