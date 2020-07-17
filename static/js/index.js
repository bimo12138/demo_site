/**
 * Create By 13716 on 2019/5/17 12:44
 */


$('.carousel').carousel({
    interval: 3000
});
$(function () {
    $(".news .news_title_ul li").click(function () {
        if(!$(this).hasClass("news_active")) {
            // 去除旧状态
            $(".news ul .news_active").removeClass("news_active");
            // 添加新状态
            $(this).addClass("news_active");
            class_id = $(this).index();
            switch (class_id) {
                case 0: $(".news .news_body_action").addClass("news_body_hidden");
                        $(".news .news_body_action").removeClass("news_body_action");
                        $(".news .news_content").addClass("news_body_action");
                        $(".news .news_content").removeClass("news_body_hidden");
                        break;
                case 1: $(".news .news_body_action").addClass("news_body_hidden");
                        $(".news .news_body_action").removeClass("news_body_action");
                        $(".news .actions_content").addClass("news_body_action");
                        $(".news .actions_content").removeClass("news_body_hidden");
                        break;
                case 2: $(".news .news_body_action").addClass("news_body_hidden");
                        $(".news .news_body_action").removeClass("news_body_action");
                        $(".news .industry_news").addClass("news_body_action");
                        $(".news .industry_news").removeClass("news_body_hidden");
                        break;
                case 3: $(".news .news_body_action").addClass("news_body_hidden");
                        $(".news .news_body_action").removeClass("news_body_action");
                        $(".news .video_center").addClass("news_body_action");
                        $(".news .video_center").removeClass("news_body_hidden");
                        break;
            }
        }
    })
});
$(function () {
    $(".new_image_show .item").eq(0).addClass("active");
});

$(function () {
    let num = 0;
    function show_img() {
        num -= 5;
        $(".show_content").css("margin-left", num);
        if(num === -730) {
            num = 0;
            $(".show_content").css("margin-left", num);
            }
        }
    var int_a = setInterval(show_img, 50);
    $(".show_content").hover(function () {
        clearInterval(int_a);
    }, function () {
        int_a = setInterval(show_img, 50);
    });
});

