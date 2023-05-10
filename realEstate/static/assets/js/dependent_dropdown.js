function dependentDropdown(countrySelectId, stateSelectId, citySelectId) {
    // disable the state and city dropdowns initially
    $(stateSelectId + ', ' + citySelectId).prop('disabled', true);

    $(countrySelectId).change(function() {
        const countryId = $(this).val();
        if (countryId) {
            $.ajax({
                url: "/admindrop/states/",
                type: "POST",
                data: {country: countryId},
                success: function(result) {
                    console.log(result);
                    const stateSelect = $(stateSelectId);
                    stateSelect.prop('disabled', false);
                    stateSelect.empty();
                    stateSelect.append('<option value="">State</option>');
                    for(const state of result) {
                        stateSelect.append(`<option value="${state.id}">${state.name}</option>`);
                    }
                    // disable the city dropdown when the country is changed
                    $(citySelectId).prop('disabled', true).val('');
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        } else {
            // disable the state and city dropdowns when no country is selected
            $(stateSelectId + ', ' + citySelectId).prop('disabled', true).val('');
        }
    });

    $(stateSelectId).change(function() {
        const stateId = $(this).val();
        if (stateId) {
            $.ajax({
                url: "/admindrop/cities/",
                type: "POST",
                data: {state: stateId},
                success: function(result) {
                    console.log(result);
                    const citySelect = $(citySelectId);
                    citySelect.prop('disabled', false);
                    citySelect.empty();
                    citySelect.append('<option value="">City</option>');
                    for(const city of result) {
                        citySelect.append(`<option value="${city.id}">${city.name}</option>`);
                    }
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        } else {
            // disable the city dropdown when no state is selected
            $(citySelectId).prop('disabled', true).val('');
        }
    });
}
