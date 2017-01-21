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

                var mDivider=$("<div></div>").addClass("mDivider");
                mDiv.append(mTitle).append(mContent).append(mTime);
                mDiv.append(mDivider);

                $('#myFrame').append(mDiv);

                mTitle.click(function () {
                    window.location.href="http://127.0.0.1:8000/blog/"+blog.fields.revisedId;
                })
        }
}

