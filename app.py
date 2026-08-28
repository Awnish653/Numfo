from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
title="AwnishxRaj Data Gateway",
version="1.0.0"
)

DEVELOPER = "AwnishxRaj"

LANDING_PAGE_HTML = """

<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AwnishxRaj Data Gateway - LIVE</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #050505;
            color: #00ffcc;
            font-family: 'Courier New', Courier, monospace;
        }

```
    #canvas-container {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    .overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        background: rgba(10, 10, 10, 0.85);
        padding: 50px;
        border: 1px solid #00ffcc;
        border-radius: 12px;
        box-shadow: 0 0 30px rgba(0, 255, 204, 0.3);
        backdrop-filter: blur(5px);
    }

    h1 {
        margin: 0 0 15px 0;
        font-size: 3em;
        text-transform: uppercase;
        letter-spacing: 5px;
        text-shadow: 0 0 15px #00ffcc;
    }

    p {
        font-size: 1.1em;
        margin: 8px 0;
        color: #ccc;
    }

    .highlight {
        color: #00ffcc;
        font-weight: bold;
    }

    .status-box {
        margin-top: 30px;
        font-weight: bold;
        padding: 15px;
        border-radius: 8px;
        background: rgba(0, 255, 204, 0.1);
        border: 1px solid rgba(0, 255, 204, 0.5);
    }

    .blinking {
        animation: blinker 1.5s linear infinite;
        display: inline-block;
    }

    .copyright {
        margin-top: 25px;
        font-size: 0.8em;
        color: #777;
    }

    @keyframes blinker {
        50% { opacity: 0; }
    }
</style>
```

</head>

<body>

```
<div id="canvas-container"></div>

<div class="overlay">
    <h1>SYSTEM ONLINE</h1>

    <p>
        API Gateway is
        <span class="highlight">Active & Secured</span>
    </p>

    <p>
        Data Engine:
        <span class="highlight">Connected</span>
    </p>

    <div class="status-box">
        <span class="blinking" style="color:#00ffcc;">●</span>
        HTTP 200 OK - LISTENING FOR QUERIES
    </div>

    <div class="copyright">
        © 2026 AwnishxRaj. All Rights Reserved.
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<script>
    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        2000
    );

    const renderer = new THREE.WebGLRenderer({
        antialias: true,
        alpha: true
    });

    renderer.setSize(window.innerWidth, window.innerHeight);

    document
        .getElementById("canvas-container")
        .appendChild(renderer.domElement);

    const geometry = new THREE.BufferGeometry();
    const vertices = [];

    for (let i = 0; i < 8000; i++) {
        vertices.push(THREE.MathUtils.randFloatSpread(3000));
        vertices.push(THREE.MathUtils.randFloatSpread(3000));
        vertices.push(THREE.MathUtils.randFloatSpread(3000));
    }

    geometry.setAttribute(
        "position",
        new THREE.Float32BufferAttribute(vertices, 3)
    );

    const material = new THREE.PointsMaterial({
        color: 0x00ffcc,
        size: 2.5,
        transparent: true,
        opacity: 0.8
    });

    const points = new THREE.Points(geometry, material);

    scene.add(points);

    camera.position.z = 1200;

    function animate() {
        requestAnimationFrame(animate);

        points.rotation.x += 0.0005;
        points.rotation.y += 0.001;

        renderer.render(scene, camera);
    }

    animate();

    window.addEventListener("resize", () => {
        camera.aspect =
            window.innerWidth / window.innerHeight;

        camera.updateProjectionMatrix();

        renderer.setSize(
            window.innerWidth,
            window.innerHeight
        );
    });
</script>
```

</body>
</html>
"""

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(
request: Request,
exc: StarletteHTTPException
):
if exc.status_code == 404:
return JSONResponse(
status_code=404,
content={
"status": "rejected",
"message": "Invalid endpoint. Use /FetchData?Number=XXXXXXXXXX",
"Developer": DEVELOPER
}
)

```
return JSONResponse(
    status_code=exc.status_code,
    content={
        "detail": exc.detail,
        "Developer": DEVELOPER
    }
)
```

@app.get("/", response_class=HTMLResponse)
def root_landing_page():
return HTMLResponse(
content=LANDING_PAGE_HTML,
status_code=200
)

@app.get("/FetchData")
def fetch_data(
Number: str = Query(
None,
description="Authorized phone identifier lookup"
)
):
if (
not Number
or not Number.isdigit()
or len(Number) < 10
or len(Number) > 15
):
return JSONResponse(
status_code=400,
content={
"status": "rejected",
"message": "Invalid parameter. STRICTLY use /FetchData?Number=XXXXXXXXXX",
"Developer": DEVELOPER
}
)

```
return {
    "status": "success",
    "Data": {
        "query": Number,
        "message": "Authorized data service is online"
    },
    "Developer": DEVELOPER,
    "Copyright": "© 2026 AwnishxRaj. All Rights Reserved."
}
```
