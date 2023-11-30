from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

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
