/**
 * Created by admin on 2016/12/24.
 */

function setNavActive(index) {
    document.onload=function () {
        spiderNavs=document.getElementById("spiderNav")
        for(nav in spiderNavs){
            nav.removeClass("active")
        }
        spiderNavs[index].addClass("active")
    }


}

