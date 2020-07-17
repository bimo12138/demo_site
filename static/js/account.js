/**
 * Create By 13716 on 2019/5/17 22:10
 */
$(function () {
    $("#submit_btn").click(function (event) {
        event.preventDefault();
        let username = $("#username").val();
        let password = $("#password").val();
        if(username && password) {
            ajaxSetting.post({
                url: "/login",
                data: {
                    "username": username,
                    "password": password
                },
                'success': function (data) {
                    if(data['code'] === 200) {
                        alertjs.alertSuccess("登陆成功！");
                        window.setTimeout(function () {
                            window.location = "/"
                        }, 2000)
                    } else {
                        alertjs.alertError(data['message']);
                    }
                },
                'fail': function () {
                    alertjs.alertNetworkError("请检查网络之后重试！");
                }
            })
        }else {
            alertjs.alertError("请输入用户名和密码！");
        }
    })
});
$(function () {
    $("#register_submit_btn").click(function (event) {
        event.preventDefault();
        let username = $("#username").val();
        let password = $("#password").val();
        let password_check = $("#password_check").val();
        if(username && password && password_check) {
            if (password === password_check) {
                ajaxSetting.post({
                    url: "/register",
                    data: {
                        "username": username,
                        "password": password,
                        "password_check": password_check
                    },
                    'success': function (data) {
                        if (data['code'] === 200) {
                            alertjs.alertSuccess("注册成功！");
                            window.setTimeout(function () {
                                window.location = "/"
                            }, 2000)
                        } else {
                            alertjs.alertError(data['message']);
                        }
                    },
                    'fail': function () {
                        alertjs.alertNetworkError("请检查网络之后重试！");
                    }
                })
            } else {
                alertjs.alertError("请输入用户名和密码！");
            }
        }else {
            alertjs.alertError("两次密码输入不一致！");
        }
    })
});