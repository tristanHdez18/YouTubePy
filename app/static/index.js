$(document).ready(function(){
    $("#submit").removeAttr("form");
    $("#submit").removeAttr("type");
    $("#submit").attr("onclick", "submit_form()");
});

function submit_form() {
    if ($("#url").val() != "") {
        $('#info').removeClass("run-animation").addClass("run-animation");
        $("#info").show();
        $("#dlform").submit();
    }
}
