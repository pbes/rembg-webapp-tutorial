A simple flask app to remove the background of an image with [Rembg](https://github.com/danielgatis/rembg)

Watch the [tutorial](https://youtu.be/cw34KMPSt4k) on YouTube

## Run it

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
python app.py
```

## Build Docker image

```bash
docker build -t rembg-webapp .
```

## Run Docker container

```bash
docker run -p 5100:5100 rembg-webapp
```