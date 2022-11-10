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

fullpage_div_start = """    <div id="fullPage">
"""

#######################################################################################################
anchors = """['auto_robo','auto_model','aero','other','imp','fun']"""
ntt = """['Automotive robotics','Automotive data & analysis','Aeromodelling','Other projects','Improvements','Activity']"""
logo_size = 24
accounts = f"""<ul id="infoMenu">
        <li><a class="mylinks" href="index.html"><img src="images/logo_homepage.png" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://linkedin.com/in/tanmaychhatbar" target="_blank"><img src="images/logo_linkedin.png" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://github.com/TanmayChhatbar" target="_blank"><img src="images/logo_github_light.png" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://grabcad.com/tanmay.chhatbar-1" target="_blank"><img src="images/logo_grabcad.png" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://www.youtube.com/c/TanmayChhatbar/" target="_blank"><img src="images/logo_yt_light.png" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://www.printables.com/social/202355-tanmaychhatbar/about" target="_blank"><img src="images/logo_printables.jpg" width={logo_size}px></a></li>
        <li><a class="mylinks" href="https://www.instagram.com/tanmaychhatbar/" target="_blank"><img src="images/logo_insta.png" width={logo_size}px></a></li>
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
            scrollingSpeed: 500,
            dragAndMove: true,
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
        # add basic info
        st = f"""
            <div class="slide s{div_i}{i}">
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