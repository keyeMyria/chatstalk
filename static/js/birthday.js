$(function () {
    $('#years').append('<option selected disabled value="non">Year</option>');
    $('#months').append('<option selected disabled value="non">Month</option>');

for (i = new Date().getFullYear(); i > 1900; i--){
    $('#years').append($('<option />').val(i).html(i));
}

for (i = 1; i < 13; i++){
    $('#months').append($('<option />').val(i).html(i));
}
 updateNumberOfDays();

$('#years, #months').on("change", function(){
    updateNumberOfDays();
});



function updateNumberOfDays(){
    $('#days').html('');
    month=$('#months').val();
    year=$('#years').val();
    days=daysInMonth(month, year);
    $('#days').append('<option selected disabled value="non">Day</option>');

    for(i=1; i < days+1 ; i++){
            $('#days').append($('<option />').val(i).html(i));
    }
}

function daysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}
})