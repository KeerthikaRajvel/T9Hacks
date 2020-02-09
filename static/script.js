// $.ajax({
  //   url : '/movie/'+movie,
  //   success: function(data) {
  //     console.log(data)
  //     var ids = data["ids"];
    //   for (var i = 0; i < ids.length; i++){
    //     twttr.widgets.createTweet(
    //         ids[i],   
    //         document.getElementById('tweets'),
    //         {
    //           theme: 'dark'
    //         }
    //       );
    //       }
    // }});
    // function embedTweet(){
    //   var movie = $("#searchbox").val();  
    //   console.log(ids)
    //     for (var i = 0; i < ids.length; i++){
    //       twttr.widgets.createTweet(
    //           ids[i],   
    //           document.getElementById('tweets'),
    //           {
    //             theme: 'dark'
    //           }
    //         );
    //   }}
    
  function showTweets(){
    console.log(ids)

    for (var i = 0; i < ids.length; i++){
      twttr.widgets.createTweet(
          ids[i],   
          document.getElementById('tweets'),
          {
            theme: 'light'
          }
        );
  }}
  
$('#searchbox').keypress(function(event){
  var keycode = (event.keyCode ? event.keyCode : event.which);
  if(keycode == '13'){
  var movie = $("#searchbox").val();
  console.log(movie)
  location.href = "/movie/"+movie;
  }
  //Stop the event from propogation to other handlers
  //If this line will be removed, then keypress event handler attached
  //at document level will also be triggered
  event.stopPropagation();
  });

  $("#searchbox").on('focus', function () {
    $(this).parent('label').addClass('active');
  });
  
  $("#searchbox").on('blur', function () {
    if($(this).val().length == 0)
      $(this).parent('label').removeClass('active');
  });
  