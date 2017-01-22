/**
 * Created by admin on 2016/12/24.
 */

//把接收到了blogs插入到博客页面中
function insertBlogs(blogs) {
    for(var i=0;i<blogs.length;i++){
                blog=blogs[i];

                var mDiv=$("<div></div>");
                var mTitle=$("<h2></h2>").text(blog.fields.title);
                var mContent=$("<p></p>").addClass("mContent").text(blog.fields.shortContent);
                var mTime=$("<p></p>").text(blog.fields.revisedTime);
                var mId=$("<p></p>").addClass("blogId").text(blog.fields.revisedId);
        
                var mDivider=$("<div></div>").addClass("mDivider");
                mDiv.append(mTitle).append(mContent).append(mTime).append(mId);
                mDiv.append(mDivider);

                $('#myFrame').append(mDiv);

                //点击blog区块的时候跳转到对应的blog中
                mDiv.click(function () {
                    // alert($(this).find("p").last().text());
                    window.location.href="http://127.0.0.1:8000/blog/"+$(this).find("p").last().text();
                })
        }
}

