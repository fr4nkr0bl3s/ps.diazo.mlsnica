$(document).ready(function() {
	search_tile = $('.on-carousel .listing-search-tile');
		if(search_tile.length>0){
			p_min=search_tile.find('#formfield-form-widgets-price_min label');
			p_max=search_tile.find('#formfield-form-widgets-price_max label');
			p_min.hide();
			p_max.hide();
			// now the bedrooms
			b_label=search_tile.find('#formfield-form-widgets-beds label');
			b_text_min =b_label.text().trim()+' (Min)';
			b_text_max =b_label.text().trim()+' (Max)';
			b_label.hide();
			search_tile.find('#form-widgets-beds-min option[value=--MINVALUE--]').text(b_text_min);
			search_tile.find('#form-widgets-beds-max option[value=--MAXVALUE--]').text(b_text_max);
			state=search_tile.find('#formfield-form-widgets-location_state label').text();
			search_tile.find('#form-widgets-location_state option:first-child').text(state);
			state_label=search_tile.find('#formfield-form-widgets-location_state label').hide();
	}
});