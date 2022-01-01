FROM python:3-slim
RUN apt-get update
RUN apt install ffmpeg -y
RUN apt install git -y
WORKDIR "/app"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","dumdiscord.py"]