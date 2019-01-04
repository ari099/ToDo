$(document).ready(function() {
   // Delete Task....
   $(".rm").on('click', function(e) {
      let id = $(this).attr('id');
      e.preventDefault();
      $.ajax({
         type: "POST",
         url: "/DeleteTask/" + id.substring(2, id.length + 1),
         success: function(result) {
            location.href = "/";
         },
         error: function(result) {
            location.href = "/";
         }
      });
   });
});