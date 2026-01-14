start = """<html>
<head>
    <title>
        Projects - Tanmay Chhatbar
    </title>
    <meta charset="utf-8" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/fullPage.js/3.1.2/fullpage.css" rel="stylesheet"/>
    <link rel="stylesheet" href="./css/main.css" type="text/css"/>
    
</head>

<body> 
"""

#######################################################################################################

anchors = """['about_me','auto_model','auto_robo','aero','electronics','3dmodel','automation','activity']"""
ntt = """['About me','Automotive data & analysis','Automotive robotics','Aeromodelling','Electronics','3D Modelling and Animation','Automation','Activity']"""
fullpage_div_start = """    <div id="fullPage">
        <div class="section">
            <div class="slide 01">
                <title>Tanmay Chhatbar - About Me</title>
    <meta charset="UTF-8">
    <meta name="description" content="Hey! I'm Tanmay!
    I love vehicles and technology!
    Visit my webpage to know more!">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        type="text/css">

    <link href="css/style.css" type="text/css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.css" rel="stylesheet"
        type="text/css">
    <style>
        body {
            position: absolute;
            background: #000;
            width: 100%;
            height: 100%;
        }
        .btn-custom {
            color: darkgray;
            text-decoration: underline;
            margin-left: 30;
        }
        .btn-custom:visited {
            color: darkslategray;
        }
    </style>
</head>
<!-- choose between one of the two next lines for background image -->
<div style="margin-left: 5%; margin-top: 2%; background-image: url('media/index_bg.png'); background-size: 50%; background-repeat: no-repeat; background-position: right top;">
    <!-- <div style="margin-left: 5%;"> -->
        <div class="col-md-12 text">
            <div class="img mb-6 pt-5"><img class="rounded-circle" src="media/photo.jpeg" alt=""
                    style="height:30vh;width:height;"></div>
            <div class="desc pt-3" margin-left="100px">
                <h3 class="subheading">Hello! I'm</h3>
                <h1 class="mb-6">Tanmay Chhatbar</h1>
                <br>

                <p class="mb-7">
                    Doctoral Student at Clemson University (CU-ICAR)
                </p>
                <br>
                <hr color="white" width="50%" align="left"/>
                <p class="mb-6">
                    <script type="text/javascript">
                        function getQueryVariable(variable) {
                            var query = window.location.search.substring(1);
                            var vars = query.split('&');
                            for (var i = 0; i < vars.length; i++) {
                                var pair = vars[i].split('=');
                                if (decodeURIComponent(pair[0]) == variable) {
                                    return decodeURIComponent(pair[1]);
                                }
                            }
                        }
                        var id = Number(getQueryVariable('id'))
                        
                    </script>
                </p>
                
                <div>
                    <h4><a href="resume_0126.pdf" class="btn-custom">My Résumé</a> 🔗</h4>
                    <br>
                    <h4><a href="#auto_model" class="btn-custom">My projects</a> 🔗</h4>
                    <br>
                    <h4><a href="/blog_gen.html" class="btn-custom">My blog</a> 🔗</h4>
                    <br>
                    <hr color="white" width="75%" align="left"/>
                    
                    <a href = "mailto: tchhatb@clemson.edu" class="btn-custom">University e-mail ✉</a>
                    <br><br>
                    <a href = "mailto: tanmaychhatbar@gmail.com" class="btn-custom">Personal e-mail ✉</a>
                </div>
                <br><br><br>
            </div>
        </div>
    </div>
    <!-- JavaScript -->
    <!--<script src="js/jquery-3.3.1.slim.min.js"></script>
<script src="js/popper.min.js"></script>-->
    <script src="js/bootstrap.min.js" type="text/javascript"></script>


            </div>
        </div>
"""

#######################################################################################################
logo_size = 24
accounts = f"""<ul id="infoMenu">
        <li><a class="mylinks" href="index.html"><img src="media/logo_homepage.png" width=24px></a></li>
        <li><a class="mylinks" href="https://linkedin.com/in/tanmaychhatbar" target="_blank"><img src="media/logo_linkedin.png" width=24px></a></li>
        <li><a class="mylinks" href="https://github.com/TanmayChhatbar" target="_blank"><img src="media/logo_github_light.png" width=24px></a></li>
        <li><a class="mylinks" href="https://grabcad.com/tanmay.chhatbar-1" target="_blank"><img src="media/logo_grabcad.png" width=24px></a></li>
        <li><a class="mylinks" href="https://www.youtube.com/c/TanmayChhatbar/" target="_blank"><img src="media/logo_yt_tp.png" width=24px></a></li>
        <li><a class="mylinks" href="https://www.printables.com/@tanmaychhatbar" target="_blank"><img src="media/logo_printables.jpg" width=24px></a></li>
        <li><a class="mylinks" href="https://www.instagram.com/tanmaychhatbar/" target="_blank"><img src="media/logo_insta.png" width=24px></a></li>
        <p style="text-align: right; padding-right: 2em; color: #418FDD"><b>Tanmay Chhatbar</b></p>
    </ul>\n"""
end = f"""    </div>
    {accounts}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fullPage.js/3.1.2/fullpage.min.js"></script>
    <script>
        new fullpage('#fullPage', {{
            autoScrolling: true,
            navigation: true,
            anchors: {anchors},
            navigationTooltips: {ntt},
            showActiveTooltip: true,
            slidesNavigation: true,
            controlArrows: false,
            scrollingSpeed: 250,
            dragAndMove: true,
            lazyLoading: true,
        }})
    </script>
    <br />
</body>
</html>"""


#######################################################################################################

def fullpage_div(div_i, data):
    # if len(data) > 1:
    stt = """        <div class="section">"""
    i = 1
    for slide in data:
        title = slide[0]
        detail = slide[1]
        links = slide[2]
        bg = slide[4]
        # add basic info
        st = f"""
            <div class="slide s{div_i}{i}">
                <video class="bg-video" data-autoplay muted loop playsinline>
                    <source src="media/{bg}" type="video/mp4" />
                </video>
                <h1>{title}</h1>
                <h3>{detail}</h3>
"""
        # add text information
        if len(slide) > 3 and slide[3] != "":
            info = slide[3]
            st = st + f"""                <p class="info">\n                    {info}\n                </p>
"""
        # add youtube links
        if len(links) > 0:
            st = st + """                </br>
                <p>
"""
        for link in links:
            if link == "":
                link = "comingsoon.html"
            st = st + f"""                    <iframe src="{link}"></iframe>
"""     
        if len(links) > 0:
            st = st + """                </p>
"""

        # end section division
        st = st + """            </div>"""

        stt = stt + st
        i = i + 1
    stt = stt + """
        </div>
"""
    return stt

#######################################################################################################

datas = list()
datas.append(list())
