// 打开视频遮罩
$('.video-item').click(function () {
  if ($("#helper-wrapper").css('display') === 'block') {
    $('.player-shadow').css('right', '4.43rem');
  } else {
    $('.player-shadow').css('right', '0');
  }
  $("#hepler-icon-open").hide();
  $('.player-shadow').show();
  $('.player-shadow').css('display', 'flex');
  $(this).siblings().removeClass('active');
  $(this).addClass('active');
});

// 关闭视频遮罩
$('#player-btn-close').click(function () {
  if ($("#helper-wrapper").css('display') === 'none') {
    $("#hepler-icon-open").show();
  }
  $('.player-shadow').hide();
});