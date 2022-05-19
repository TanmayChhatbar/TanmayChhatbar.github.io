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

fullpage_div_start = """    <div id="fullPage" style="padding-top: 10px">
"""

#######################################################################################################
anchors = """['auto','plotter','aero']"""
ntt = """['Automotive projects','Plotter','Aeromodelling']"""
end = f"""
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/fullPage.js/3.1.2/fullpage.min.js"></script>

    <script>
        new fullpage('#fullPage', {{
            autoScrolling: true,
            navigation: true,
            anchors: {anchors},
            navigationTooltips: {ntt},
            showActiveTooltip: true,
            slidesNavigation: true,
            scrollingSpeed: 500,
        }})
    </script>
    <br />
</body>
</html>"""


#######################################################################################################

def fullpage_div(div_i, data):
    title = data[0]
    detail = data[1]
    links = data[2]
    if len(data) > 3:
        color = data[3]
    else:
        color = 'black'
    st = f"""        <div class="section s{div_i}">
            <div>
                <h1 align="center" style="color: {color}">
                    {title}
                </h1>
                <h3 align="center" style="color: {color}">
                    {detail}
                </h3>
                </br>
                <p align="center">
"""
    for link in links:
        st = st + f"""                	<iframe src={link}></iframe>\n"""
    st = st + """                </p>
            </div>
        </div>

""" 
    return st

#######################################################################################################

datas = list()