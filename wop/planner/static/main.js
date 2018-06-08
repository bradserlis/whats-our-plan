console.log('your javascript file is working') 


$(document).ready(function(){
  M.AutoInit();

  $('.new-activity-button').on('click', function(){
    var toastHTML = '<span>I am toast content</span><button class="btn-flat toast-action">Undo</button>';
    M.toast({html: toastHTML});
})

})

