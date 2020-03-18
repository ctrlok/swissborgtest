FROM python:2-alpine
RUN mkdir /app
ADD web.py /app/web.py
EXPOSE 8080
CMD ["python", "/app/web.py"]
