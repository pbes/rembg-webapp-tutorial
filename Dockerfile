FROM python:3.9

# download this https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
# copy model to avoid unnecessary download
# COPY u2net.onnx /home/.u2net/u2net.onnx

RUN mkdir -p /root/.u2net
RUN wget -O /root/.u2net/u2net.onnx https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "5100", "app:app"]