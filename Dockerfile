FROM python:3.9-slim
LABEL org.opencontainers.image.source=https://github.com/OliAltF4/Wasserpegel-Rhein-Bonn
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
# the "-u" paramenter is needed to display the log messages to stdout with the print command
CMD ["python","-u", "app.py"] 
