$("#add_fav").click(function() {
    addfavorite();
});

function addfavorite() {
    var b = $('#add_fav').attr('class')
    $.ajax({
        type: 'POST',
        url: '/addfavor/',
        data: { 'favorite': b },
        success: function(response) {
            //var result = {{ response|safe }}
            alert(response +'\r收藏成功,請刷新頁面');
        },
        error: function() {
            alert('收藏失敗, 請洽客服');
        }
    })
}

function deletefavorite(target) {
    var delete_name = target
    $.ajax({
        type: 'POST',
        url: '/deletefavor/',
        data: { 'favorite': delete_name },
        success: function(response) {
            //var result = {{ response|safe }}
            alert(response + '\r刪除成功, 請刷新頁面');
        },
        error: function() {
            alert('刪除失敗, 請洽客服');
        }
    })
}