FROM python:3.12-slim

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt; \
    adduser myappuser && \
    chown myappuser. /app -R

EXPOSE 5000
ENV Name=World
USER myappuser

CMD ["python", "app.py"]
