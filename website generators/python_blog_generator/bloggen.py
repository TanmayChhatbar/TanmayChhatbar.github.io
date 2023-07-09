from helpers import *

blog.append(filetoblog("./blogs/Blog using Python test.txt"))

# backup current html to new file
# with open('./blog_gen.html', 'r') as f, open('./blog_gen_backup.html', 'w') as b:
#     b.write(f.read())

# generate new
with open('./blog_gen.html','w') as f:
    # write headers
    f.write(start)

    # write part of each blog
    for data in blog:
        f.write(blognotes(data))
        
        # write new html for each blog
        with open(f'{data[2]+".html"}','w') as f2: # make new page
            f2.write(poststart)
            f2.write(postnotes(data))
            f2.write(postend)

    # write footer
    f.write(end)