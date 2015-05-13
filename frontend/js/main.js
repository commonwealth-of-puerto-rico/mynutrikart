$(document).ready(function(){
    /* Device-Width / Viewport-Width Hack for IE and Windows Phone 8 */
    if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
        var msViewportStyle = document.createElement('style')
        msViewportStyle.appendChild(
            document.createTextNode(
                '@-ms-viewport{width:auto!important}'
            )
        )
        document.querySelector('head').appendChild(msViewportStyle)
    }

    /* Android Stock Browser Hack */
    $(function () {
        var nua = navigator.userAgent
        var isAndroid = (nua.indexOf('Mozilla/5.0') > -1 && nua.indexOf('Android ') > -1 && nua.indexOf('AppleWebKit') > -1 && nua.indexOf('Chrome') === -1)
        if (isAndroid) {
            $('select.form-control').removeClass('form-control').css('width', '100%')
        }
    })

   /* Handle Navigation */
    $("a.navmenu-brand, .navmenu-nav li a").click(function(){
        var target = $(this).attr("href");
        console.log(target);
        $("#views-list > .view").each(function(){
            var id = "#" + $(this).attr("id");
            if(("#" + $(this).attr("id")) !== target) {
                $(this).removeClass("active");
                $("a[href="+id+"].navmenu-brand,.navmenu-nav li a[href="+id+"]").parent().removeClass("active");
            } else {
                $(this).addClass("active");
                $("a[href="+id+"].navmenu-brand,.navmenu-nav li a[href="+id+"]").parent().addClass("active");
            }
        })
    })

})