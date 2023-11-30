import sys

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import logging

from pyngrok import ngrok

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else "8000"

public_url = ngrok.connect(port).public_url

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return """
        <!DOCTYPE html>
        <html>
            <head>
                    <title>Index</title>  
            </head>

            <body>
                <h1> Server Index </h1>
                <p><a href={0}>Multiqc report trimgalore</a></p>
                <p><a href={1}>Multiqc report</a></p>
                
            </body>

        </html>
        """.format(
            'multiqc_report_trimgalore.html',
            'multiqc_report.html'
        )

app.mount("/", StaticFiles(directory="results"), name="html_files")
logger.info("ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='debug')