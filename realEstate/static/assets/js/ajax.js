function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

jQuery(function($){
    $(document).ready(function(){
        // Disable the State and City dropdowns by default
        $("#id_state, #id_city").prop("disabled", true);

        $("#id_country").change(function(){
            // When a Country is selected, fetch the list of States that belong to that Country
            $.ajax({
                url:"/admindrop/states/",
                type:"POST",
                data:{country: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_state");
                    cols.options.length = 0;
                    cols.options.add(new Option("State", ""));
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                    // Enable the State dropdown and disable the City dropdown
                    $("#id_state").prop("disabled", false);
                    $("#id_city").prop("disabled", true);
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });

        $("#id_state").change(function(){
            // When a State is selected, fetch the list of Cities that belong to that State
            $.ajax({
                url:"/admindrop/cities/",
                type:"POST",
                data:{state: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_city");
                    cols.options.length = 0;
                    cols.options.add(new Option("City", ""));
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                    // Enable the City dropdown
                    $("#id_city").prop("disabled", false);
                },
                headers: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
    }); 
});
