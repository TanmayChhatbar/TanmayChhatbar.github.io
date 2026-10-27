from html import escape
import re
from urllib.parse import parse_qs, urlparse

start = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="Projects by Tanmay Chhatbar, Doctoral Candidate at Clemson University CU-ICAR." />
    <title>Projects - Tanmay Chhatbar</title>
    <link rel="stylesheet" href="./css/main.css" type="text/css" />
</head>
<body>
"""

about_section = """<section class="intro" id="top">
    <div class="intro-content">
        <img src="media/photo.jpeg" alt="Portrait of Tanmay Chhatbar" />
        <div class="intro-copy">
            <h3>Hello! I'm</h3>
            <h1>Tanmay Chhatbar</h1>
            <p>Doctoral Candidate at Clemson University (CU-ICAR)</p>
            <div class="intro-actions">
                <div class="intro-button-row">
                    <a href="resume_0526.pdf" class="btn-custom resume-btn">My Resume</a>
                </div>
                <div class="intro-button-row">
                    <a href="mailto:tchhatb@clemson.edu" class="btn-custom email-btn">University e-mail</a>
                    <a href="mailto:tanmaychhatbar@gmail.com" class="btn-custom email-btn">Personal e-mail</a>
                </div>
                <ul class="intro-social-links" aria-label="Social media links">
                    <li><a class="mylinks" href="https://linkedin.com/in/tanmaychhatbar" target="_blank" rel="noopener noreferrer"><img src="media/logo_linkedin.png" width="24" alt="LinkedIn" /></a></li>
                    <li><a class="mylinks" href="https://github.com/TanmayChhatbar" target="_blank" rel="noopener noreferrer"><img src="media/logo_github_light.png" width="24" alt="GitHub" /></a></li>
                    <li><a class="mylinks" href="https://grabcad.com/tanmay.chhatbar-1" target="_blank" rel="noopener noreferrer"><img src="media/logo_grabcad.png" width="24" alt="GrabCAD" /></a></li>
                    <li><a class="mylinks" href="https://www.youtube.com/c/TanmayChhatbar/" target="_blank" rel="noopener noreferrer"><img src="media/logo_yt_tp.png" width="24" alt="YouTube" /></a></li>
                    <li><a class="mylinks" href="https://www.printables.com/@tanmaychhatbar" target="_blank" rel="noopener noreferrer"><img src="media/logo_printables.jpg" width="24" alt="Printables" /></a></li>
                    <li><a class="mylinks" href="https://www.instagram.com/tanmaychhatbar/" target="_blank" rel="noopener noreferrer"><img src="media/logo_insta.png" width="24" alt="Instagram" /></a></li>
                </ul>
            </div>
        </div>
    </div>
</section>
<hr class="topic-divider" />
"""

topic_metadata = [
    ("auto_model", "Automotive data &amp; analysis"),
    ("auto_robo", "Automotive robotics"),
    ("aero", "Aeromodelling"),
    ("electronics", "Electronics"),
    ("3dmodel", "3D Modelling and Animation"),
    ("automation", "Automation"),
    ("activity", "Activity"),
]

accounts = """<ul id="infoMenu">
        <li><a class="mylinks" href="index.html"><img src="media/logo_homepage.png" width="24" alt="Home" /></a></li>
        <p style="text-align: right; padding-right: 2em; color: #418FDD"><b>Tanmay Chhatbar</b></p>
    </ul>
"""

end = """</body>
</html>
"""


def youtube_video_id(url):
    if not url:
        return None
    parsed = urlparse(url)
    host = parsed.netloc.lower().split(":")[0]
    video_id = None
    if host.endswith("youtu.be"):
        video_id = parsed.path.strip("/").split("/")[0]
    elif host.endswith("youtube.com") or host.endswith("youtube-nocookie.com"):
        if parsed.path.startswith("/embed/"):
            video_id = parsed.path.split("/", 2)[2].split("/")[0]
        elif parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [None])[0]
    if video_id and re.fullmatch(r"[A-Za-z0-9_-]+", video_id):
        return video_id
    return None


def project_card(slide):
    title, detail, links, info, background = slide[:5]
    info = "\n".join(line.rstrip() for line in info.splitlines()).strip()
    plain_title = escape(re.sub(r"<[^>]+>", "", title))
    background = escape(str(background), quote=True)

    video = ""
    if background:
        video = f"""<video class="bg-video" autoplay muted loop playsinline aria-hidden="true" tabindex="-1">
                        <source src="media/{background}" type="video/mp4" />
                    </video>"""

    video_items = []
    preview_id = None
    for index, link in enumerate(links or []):
        if not link:
            continue
        video_id = youtube_video_id(link)
        if video_id:
            if preview_id is None:
                preview_id = video_id
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            video_items.append(
                f"""<a class="project-video-link" href="{video_url}" target="_blank" rel="noopener noreferrer" aria-label="Watch {plain_title} video {index + 1} on YouTube">
                            <img src="{thumbnail_url}" alt="YouTube thumbnail for {plain_title}" loading="lazy" />
                        </a>"""
            )
        elif link != "comingsoon.html":
            safe_url = escape(link, quote=True)
            video_items.append(
                f"<a class=\"project-video-link project-video-text\" href=\"{safe_url}\" target=\"_blank\" rel=\"noopener noreferrer\">Open project video</a>"
            )

    preview_thumbnail = ""
    if preview_id:
        thumbnail_url = f"https://img.youtube.com/vi/{preview_id}/hqdefault.jpg"
        preview_thumbnail = f"<img class=\"preview-thumbnail\" src=\"{thumbnail_url}\" alt=\"YouTube thumbnail for {plain_title}\" loading=\"lazy\" />"
    elif not video_items:
        preview_thumbnail = '<div class="preview-thumbnail preview-placeholder">Coming soon</div>'

    info_html = f"<div class=\"info\">{info}</div>" if info else ""
    links_html = ""
    if video_items:
        links_html = "<div class=\"project-video-links\">" + "".join(video_items) + "</div>"

    card_html = f"""            <details class="project-card">
                <summary class="card-preview">
                    {video}
                    <div class="preview-copy">
                        <h1>{title}</h1>
                        <h3>{detail}</h3>
                    </div>
                    {preview_thumbnail}
                </summary>
                <div class="project-details">
                    {info_html}
                    {links_html}
                </div>
            </details>
"""
    return "\n".join(line.rstrip() for line in card_html.splitlines()) + "\n"


def topic_section(topic_index, data):
    if topic_index >= len(topic_metadata):
        anchor, title = f"topic-{topic_index + 1}", f"Topic {topic_index + 1}"
    else:
        anchor, title = topic_metadata[topic_index]
    cards = "".join(project_card(slide) for slide in data)
    section = f"""<section class="topic" id="{anchor}">
    <h2>{title}</h2>
    <div class="project-grid">
{cards}    </div>
</section>
<hr class="topic-divider" />
"""
    return section
