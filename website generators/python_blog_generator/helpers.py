import os
from datetime import datetime

blog = []
start = """<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Blog - Tanmay Chhatbar</title>

    <link href="css/blog_bootstrap.min.css" rel="stylesheet">
    <link href="css/blog_simple-blog-template.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="blog_gen.html">Brain speech - Tanmay</a>
        </div>
      </div>
      <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">

      <div class="row">

        <!-- Blog Entries Column -->
        <div class="col-md-12">
"""

end = """
      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

    <!-- Footer -->
    <footer>
      <div class="container">
        <div class="row">
          <div id='footer' class="col-lg-12">
            <p>
              Blog template credits &copy; <a href="https://github.com/earlbread/simple-blog-template" >earlbread</a>

                <span style="display: inline; float: right; padding-right: 2em; color: #418FDD"><b>
                  <a class="mylinks" href="index.html"><img src="media/logo_homepage.png" width=24px></a>
                  <a class="mylinks" href="https://linkedin.com/in/tanmaychhatbar" target="_blank"><img src="media/logo_linkedin.png" width=24px></a>
                  <a class="mylinks" href="https://github.com/TanmayChhatbar" target="_blank"><img src="media/logo_github.png" width=24px></a>
                  <a class="mylinks" href="https://grabcad.com/tanmay.chhatbar-1" target="_blank"><img src="media/logo_grabcad.png" width=24px></a>
                  <a class="mylinks" href="https://www.youtube.com/c/TanmayChhatbar/" target="_blank"><img src="media/logo_yt.png" width=24px></a>
                  <a class="mylinks" href="https://www.printables.com/@tanmaychhatbar" target="_blank"><img src="media/logo_printables.jpg" width=24px></a>
                  <a class="mylinks" href="https://www.instagram.com/tanmaychhatbar/" target="_blank"><img src="media/logo_insta.png" width=24px></a>
                  <a href="/index.html">Tanmay Chhatbar</a></b>
                </span>
            
            </p>
          </div>
          <!-- /.col-lg-12 -->
          
        </div>
        <!-- /.row -->
      </div>
    </footer>


    <!-- jQuery -->
    <script src="js/blog_jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/blog_bootstrap.min.js"></script>

  </body>

</html>
"""

def blognotes(data):
    stlen = len(data[-1])
    tmp = data[-1:146]+"..." if stlen>150 else data[-1:stlen]
    tmp = tmp[-1].replace("\n"," ")
    txt = f"""<h2 class="post-title">
            <a href="{data[2]+".html"}">{data[0]}</a>
          </h2>
          <!-- <p class="lead">
            by Tanmay
          </p> -->
          <p><span class="glyphicon glyphicon-time"></span> Posted on {data[1]}</p>
          <p>{tmp}</p>
          <a class="btn btn-default" href="{data[2]+".html"}">Read More</a>

          <hr>"""
    return txt


def postnotes(data):
    txt = f"""
          <h1 class="post-title">{data[0]}</h1>

          <p class="lead">
            by Tanmay
          </p>

          <hr>
          <p><span class="glyphicon glyphicon-time"></span> Posted on {data[1]}</p>
          <hr>

          {data[-1]}
          <hr>"""
    return txt


def filetoblog(filename):
    with open(filename, 'r') as f:
        data = []
        tmp = f.readlines()
        data.append(tmp[0].strip())    # title
        dt_m = datetime.fromtimestamp(os.path.getmtime(filename))
        data.append(datetime.strftime(dt_m,"%B %d, %Y at %I:%M %p"))
        data.append("post_"+datetime.strftime(dt_m, "%Y%m%d"))
        data.append("".join(tmp[1:]))
        return data

poststart = """<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Blog - Tanmay Chhatbar</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/blog_bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/blog_simple-blog-template.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

  </head>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="blog_gen.html">Brain speech</a>
        </div>
        <!-- /.navbar-collapse -->
      </div>
      <!-- /.container -->
    </nav>


    <!-- Page Content -->
    <div class="container">

      <div class="row">

        <!-- Blog Post Content Column -->
        <div class="col-lg-12">

"""

postend = """
          <hr>
          
        </div>
      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

    <!-- Footer -->
    <footer>
      <div class="container">
        <div class="row">
          <div id='footer' class="col-lg-12">
            <p>
              Blog template credits &copy; <a href="https://github.com/earlbread/simple-blog-template" >earlbread</a>

                <span style="display: inline; float: right; padding-right: 2em; color: #418FDD"><b>
                  <a class="mylinks" href="index.html"><img src="media/logo_homepage.png" width=24px></a>
                  <a class="mylinks" href="https://linkedin.com/in/tanmaychhatbar" target="_blank"><img src="media/logo_linkedin.png" width=24px></a>
                  <a class="mylinks" href="https://github.com/TanmayChhatbar" target="_blank"><img src="media/logo_github.png" width=24px></a>
                  <a class="mylinks" href="https://grabcad.com/tanmay.chhatbar-1" target="_blank"><img src="media/logo_grabcad.png" width=24px></a>
                  <a class="mylinks" href="https://www.youtube.com/c/TanmayChhatbar/" target="_blank"><img src="media/logo_yt.png" width=24px></a>
                  <a class="mylinks" href="https://www.printables.com/@tanmaychhatbar" target="_blank"><img src="media/logo_printables.jpg" width=24px></a>
                  <a class="mylinks" href="https://www.instagram.com/tanmaychhatbar/" target="_blank"><img src="media/logo_insta.png" width=24px></a>
                  <a href="/index.html">Tanmay Chhatbar</a></b>
                </span>
            
            </p>
          </div>
          <!-- /.col-lg-12 -->
          
        </div>
        <!-- /.row -->
      </div>
    </footer>

    <!-- jQuery -->
    <script src="js/blog_jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/blog_bootstrap.min.js"></script>

  </body>

</html>"""