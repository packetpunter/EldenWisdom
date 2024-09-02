FROM python:3.12-slim

WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["fastapi", "run", "main.py", "--port","80"]