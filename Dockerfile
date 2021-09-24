FROM python:3 AS main

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

FROM alpine
RUN apk add --no-cache ffmpeg
COPY --from=main . .
WORKDIR /app
CMD ["python","dumdiscord.py"]

