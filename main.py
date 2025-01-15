from fastapi import FastAPI, Response

app = FastAPI()


# @app.get('/')
# def home():
#     return "Hello World!"

# @app.get('/')
# def home():
#     content = "<h1>Hello World!</h1>"
#     response = Response(content, media_type="text/html")
#     return response

@app.get('/')
def home():
    with open('static/index.html') as f:
        content = f.read()
    response = Response(content, media_type="text/html")
    return response
