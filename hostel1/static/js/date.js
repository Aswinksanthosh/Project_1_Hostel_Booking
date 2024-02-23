var currYear = (new Date()).getFullYear();

$(document).ready(function() {
  $(".datepicker").datepicker({
    defaultDate: new Date(currYear-5,1,31),
    // setDefaultDate: new Date(2000,01,31),
    maxDate: new Date(currYear-5,12,31),
    yearRange: [1928, currYear-5],
    format: "yyyy/mm/dd"    
  });
});
