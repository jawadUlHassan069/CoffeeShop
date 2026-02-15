FROM python:3.11-slim
WORKDIR /labtask2
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /labtask2/
RUN chmod +x startup.sh
EXPOSE 8000
CMD ["./startup.sh"]