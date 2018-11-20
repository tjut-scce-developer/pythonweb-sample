$(document).ready(function () {

    $("#regiter").hide();

    $("#go_signin").click(function () {
        $("#signin").show();
        $("#regiter").hide();
    });

    $("#go_register").click(function () {
        $("#signin").hide();
        $("#regiter").show();
    });

});