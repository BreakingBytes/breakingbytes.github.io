Title: Vertically Centered
Date: 2017-05-25 23:48
Category: JavaScript
Tags: HTML, web, jQuery
Authors: Mark Mikofski
Summary: Use jQuery to vertically center an element in a window.

I am porting a site, and the original login box would verticaly center, even as
I change the size of the window. There were several StackOverflow answers that
suggested creating a CSS class, which seemed perfect, but they didn't seem to
work. Then I noticed they had some JavaScript in their file to pad the top of
the login `<div>` element. I made some simplifications using jQuery and voila!

    /* vertically center login form */
    function set_login_form_container_margin_top(sp_banner, log_form, minht) {
    var sp_banner_height =  $(sp_banner).height();  // height of banner
    var window_height = $( window ).height();  // window height
    var login_form_height = $(log_form).height();  // login form
    // find the new height = half difference between window and banner + login form
    var new_height = (window_height - login_form_height - sp_banner_height) / 2;
    console.log('new_height = ' + new_height);
    // set the margin on the top of the login form container
    $(log_form).css('margin-top', new_height < minht ? minht : new_height + 'px');
    }
