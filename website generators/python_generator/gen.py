from helpers import *

#TODO
# videos
#   FT Edge video
# tb3 ppt
# fun section background

# page 1 - Automomtive data and modelling
ttl = "Multi-wheeled vehicle modelling"
dt = "Deep Orange 13-14 - Clemson University"
lns = ["https://www.youtube.com/embed/B7_-ia0J6QU","https://www.youtube.com/embed/IsC2Qz7YGao","https://www.youtube.com/embed/obmg_0Rq8ow"]
info = """Estimation of forces and resultant motion is an important component of vehicle design and control.<br>
\t\t\t\t\tWe have modelled tools of varying complexity to better understand the dynamic limits of the vehicle we develop. Some of them are shown below.<br><br>
\t\t\t\t\t<ol class="feat">
\t\t\t\t\t\t<li> An overview of the Deep Orange 13-14 project.</li>
\t\t\t\t\t\t<li> Shows the most complex, most "true" model, created in Simscape Multibody.<br>It considers the tracks around the wheels and its interaction with the ground.</li>
\t\t\t\t\t\t<li> Shows a much simpler, real-time capable model developed in MATLAB.</li>
\t\t\t\t\t\t</ol>"""
# \t\t\t\t\t\t<li> Compilation of funny and failed simulations, just for laughs.</li>
datas[0].append([ttl, dt, lns, info])

ttl = "Tractor-trailer modelling"
dt = "CU-ICAR"
lns = ["https://www.youtube.com/embed/hhK23FUT47k"]
info = """A fully configurable simplified tractor-trailer model was created. For small angles, this model should provide realistic results. The model is hence useful as a plant model to develop, verify and optimize controllers in simulation. <br>
					The following assumptions were made to simplify the model.<br><br>
					<ol class="feat">
						<li> Linear tyre model.</li>
						<li> No lateral load transfer. </li>
						<li> No moments due to hitch forces. </li>
                        <li> No suspension, ideal flat road. </li>
                    </ol>"""
datas[-1].append([ttl, dt, lns, info])

ttl = "Vehicle datalogger"
dt = "Data collection during AutoX events"
lns = [""]
info = """As a challenge, I engineered a datalogger for my car to collect inertial and GPS data while participating in AutoX events.<br>The result was this ESP32-based device, for which more information can be found on <a style="color:grey" href="https://github.com/TanmayChhatbar/car_datalogger" target="_blank"><u>GitHub</u></a>.<br><br><u>TTGO TS 1.4</u> ESP32-based board, with built-in <u>MPU9250 IMU</u> and a microSD card reader, was used.<br><u>Adafruit Ultimate GPS</u> module is used to get GPS data.<br>Inertial data is collected at around 300Hz, GPS data is collected at 5Hz."""
datas[-1].append([ttl, dt, lns, info])

# page 2 - automotive robotics
ttl = "Autonomous robot"
dt = "Clemson University - International Center of Automotive Research"
lns = ["https://www.youtube.com/embed/YXchdEtqzsE"]
info = """The course 'Autonomy: Science and Systems' at CU-ICAR required programming a <u>Turtlebot3</u> robot to take on the following challenges.</p>\n\t\t\t\t<ul class="feat"><li>Wall following</li><li>Obstacle avoidance</li><li>Line following</li><li>Stop-sign detection</li><li>Apriltag following</li></ul>\n\t\t\t\t<p class="info">
\t\t\t\t\tThe Turtlebot3 is equipped with a <u>Raspberry Pi 4</u> computer which is responsible for much of the onboard data processing and publishing.<br><u>OpenCR</u> board is in charge of receiving commands from the Pi and powering and controlling power-intensive components including servos, motors, LiDAR and camera(s).<br>Computationally intensive tasks were offloaded onto a more powerful <u>Linux laptop</u>.
\t\t\t\t\t<br><br>The video goes over the final demonstration."""
datas.append([[ttl, dt, lns, info]])

ttl = "Small scale ADAS"
dt = "Clemson University - International Center of Automotive Research"
lns = ["https://www.youtube.com/embed/nMBGIg3d_ZA"]
info = """As part of our capstone project for the course 'Automotive Electronics Integration', we were tasked to introduce and demonstrate ADAS systems in a scale vehicle.<br><br>An <u>Arduino Uno</u> board was the central processor for the project.<br><u>HC-SR04</u> ultrasonic sensors were used to detect the sidewalls acting as lanes, and the presence of a head-on obstacle.<br><br>The video goes over our approach and results in introducing features including:<ul class="feat"><li>Lane-Keep Assist</li><li>Adaptive Cruise Control</li></ul>"""
datas[-1].append([ttl, dt, lns, info])

ttl = "Motorcycle gear shifting automation"
dt = "Capstone Project - Bachelor's in Mechanical Engineering"
lns = ["https://www.youtube.com/embed/eVmGcuafOZo"]
info = "For our undergraduate project, we decided to design and fabricate a <u>bolt-on automation system</u> to convert a motorcycle's controls into those similar to an automatic scooter.<br>This included automating the <u>clutch, gears and throttle</u> to follow rider input while considering engine RPM, speed, etc. <br><br>This video was made as a submission to the CS50 MOOC course, and shows a representation of what we had imaged for the project."
datas[-1].append([ttl, dt, lns, info])

# page 3 - aero
ttl = "Boeing Aeromodelling 2019-20 - IIT Kharagpur"
dt = "Finishing 3<sup>rd</sup> place overall"
lns = ["https://www.youtube.com/embed/G851yVFitqQ", "https://www.youtube.com/embed/twtrokqZ5k0"]
info = """IIT hosts Aeromodelling competitions sponsored by Boeing at a national level. Through our previous attempts, we steadily improved our results.<br>This was our third attempt at fetching results to be proud of, and proud, we are.<br>The results of this competition serves to be the highlight of our aeromodelling career through my undergraduate studies.
\t\t\t\t\t<br><br>The aircraft fuselage was designed and manufactured to be as light as possible, with a maximum payload capacity of <u>42 golf balls</u>. The balsa-wood wings were designed to be light, and yet capable of withstanding the payload weight high-g aerial maneuvers."""
datas.append([[ttl, dt, lns, info]])

ttl = "SAE Aero Design East 2019"
dt = "7th* in Mission Performance"
lns = ["https://www.youtube.com/embed/clXUVxfD-9w","https://www.youtube.com/embed/wKr7KCYWeT8"]
info = "SAE Aero Design East, a competition held in Fort Worth, Texas, was an international-level challenge taken up by <u>6 students</u> from our university.<br>An aircraft with a 12ft wingspan, weighing less than 7.5kg was designed and manufactured to lift <u>17.5kg of additional payload</u>, including 50-odd tennis balls, and steel plates.<br><br>The aircraft performed well through heavy crosswinds for a first-year team to bag <u>7th place</u> in Mission Performance."
datas[-1].append([ttl, dt, lns, info])

ttl = "Speedy G"
dt = "\"I am Speed!\", said the Little Bird"
lns = ["https://www.youtube.com/embed/T2X-0we-XOU"]
info = "Who doesn't like fast vehicles? Named after the iconic Looney Tunes character, Speedy G is a tiny 600mm RC plane that we designed to use a 1300mAh 3S battery powering a 2207 T-Motor drone motor through a 35A ESC, spinning a 2-blade 7x4 prop.<br><br>The design is almost entirely foamboard. The wings have no central spar. Instead, it is a stressed skin design. The front of the fuselage needed to be hollow for access to the battery, and is balsa. The motor mounts are 3D printed out of ABS.<br><br>We've measured doing over 160kph with GPS, around 100mph!"
datas[-1].append([ttl, dt, lns, info])

ttl = "The adventures of foomie"
dt = "The tiniest little RC plane I made"
info = "This project was taken up as a challenge, to make an <u>indestructible RC aircraft</u>.<br>It turned out to be quite a fun flyer, and the negligible chance of serious risk to the plane itself or the people around it encouraged us to learn faster and engage in activities that are otherwise too dangerous for hobby flying."
lns = ["https://www.youtube.com/embed/uV_CYRJlwYE", "https://www.youtube.com/embed/nO6BWNPSGuY"]
datas[-1].append([ttl, dt, lns, info])

ttl = "Aerobatics"
dt = "What fun is flying straight"
lns = [""]
info = "It's a pleasure to watch an aircraft tumble and roll and loop as much as we used to as kids. Aerobatic planes are probably the most fun flyers one can experience, regardless of the scale.<br>This plane was designed by FliteTest to be the most convenient way of experiencing aerobatics, and it is an absolutely beauty in the hands of a skilled pilot. Trust me, I've seen my mentor fly the wings off it (literally)"
datas[-1].append([ttl, dt, lns, info])

# page 4 - Electronics
ttl = "i1Pro 3 automated plotter"
dt = "Designed, manufactured and programmed by self"
lns = ["https://www.youtube.com/embed/pWplQDCc0bk"]
info = "In 2021, I took up a project for one of my mentors to automate a color-scanning tool using hobby-grade electronics.<br>An <u>Arduino Nano</u> board with a stepper board was used, running fully custom-written <u>path calculation</u> software.<br>An intuitive <u>UI</u> was introduced along with a joystick to guide the process in multiple scanning modes and velocities, including a manual mode.<br>The hardware was designed in <u>CAD</u>, with a number of parts being <u>3D printed</u>.<br><br>The video shows testing of the solution."
datas.append([[ttl, dt, lns, info]])

ttl = "DIY Smartwatch"
dt = "Designed, manufactured and programmed by self"
lns = ["https://www.youtube.com/embed/iW4tt_eioQQ"]
info = """Expenditure on education and improvement is okay, buying frivolous objects is not.<br>I wanted a smartwatch.<br>There's only one solution. <a style="color:grey" href="https://github.com/TanmayChhatbar/esp32_smartwatch" target="_blank"><u>DIY</u></a><br><br>The watch is capable of connecting to WiFi to <u>fetch time</u>, as well as keeping count of the number of <u>steps</u> the user walks daily."""
datas[-1].append([ttl, dt, lns, info])

# page 5 - 3D Modelling and animation
ttl = "Project render - Car"
dt = "In learning Blender modelling software"
lns = ["https://www.youtube.com/embed/FBkQdyRUgO4"]
info = "I learnt how to use blender, the software out of interest.<br>This short clip serves to showcase my skills in modelling and animation as a submission for one of the certified courses on a MOOC that taught blender.<br><br>All animations on this page, and their assets have been modelled, textured and rendered by me."
datas.append([[ttl, dt, lns, info]])

ttl = "Project render - Motorcycle"
dt = "Improving skills in blender"
lns = ["https://www.youtube.com/embed/YfYLm5pLQ34?si=wQeznKJEq7l3ROvF"]
info = "For this render, I took an untextured asset from the internet. All textures are procedurally generated, except the logos.<br>I modelled and textured the custom tyre model based on the motorcycle I owned, as well as an Akra exhaust.<br>The project was rendered in cycles."
datas[-1].append([ttl, dt, lns, info])

ttl = "3D Printer simulation"
dt = "Using 3D Modelling and animation to visualize errors in g-code with blender"
lns = ["https://www.youtube.com/embed/HRwWg1wcDF0?si=mLBbzmQVIc-hi_OC"]
info = "Using Python scripting inside Blender, I import g-code generated by a slicing software for a household 3D printer. <br>This facilitates virtual verification that the motion of the printer stands to reason, and won't potentially damage the printer. <br>The visualization is just an added feature. <br><br>More details on <a href=\"https://github.com/TanmayChhatbar/blender_3d_print_animation\" class=\"btn-custom\">GitHub</a> 🔗"
datas[-1].append([ttl, dt, lns, info])

# page 6 - improvements
ttl = "Industry robotics"
dt = "Stagnation isn't good for mind or business"
info = """During my undergraduate studies, I designed and manufactured multiple automation solutions and miscellaneous devices for streamlining workflow in processing of potato starch, soaps and detergents. for use in a factory.<br>These include:
\t\t\t\t\t<ol class="feat">
\t\t\t\t\t\t<li>Automatic bottle fillers for packaging soaps and detergents</li>
\t\t\t\t\t\t<li>Sound-based acid flow-rate and quantity estimation for positive displacement pumps.</li>
\t\t\t\t\t\t<li>Packaging heatshrink auto-cutter.</li>
\t\t\t\t\t</ol>"""
lns = ["https://www.youtube.com/embed/XmRJAW47A9g","https://www.youtube.com/embed/5h9r28wX8vo","https://www.youtube.com/embed/MwPSW_m9hzk"]
datas.append([[ttl, dt, lns, info]])

ttl = "Home Automation"
dt = "Stagnation isn't good at home either"
info = "Who likes to stand up and walk over to the switch board to turn the lights on?<br>Who enjoys trying to find the AC remote when it's really hot and you're desperate to be lazy?"
lns = ["https://www.youtube.com/embed/3ymYBt0vYeg","https://www.youtube.com/embed/ehGC3uAFM-8"]
datas[-1].append([ttl, dt, lns, info])

# page 7 - last
ttl = "What is fun, motivates you"
dt = "What is love, baby"
info = "Don't hurt me, don't hurt me, no more"
lns = ["https://www.youtube.com/embed/WI3La0e9X_I?si=0w_R1Xm7GftYk6Tj","https://www.youtube.com/embed/L_vGYdL0Qy8","https://www.youtube.com/embed/rsrUuE2ELrc"]
datas.append([[ttl, dt, lns, info]])

# backup current html to new file
with open('./index.html', 'r') as f, open('./index_backup.html', 'w') as b:
    b.write(f.read())

# generate new
with open('./index.html','w', encoding="utf-8") as f:
    f.write(start)
    f.write(fullpage_div_start)
    i = 1
    for data in datas:
        f.write(fullpage_div(i, data))
        i = i + 1
    f.write(end)