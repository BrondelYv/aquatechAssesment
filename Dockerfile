# prenant une image python sur docker-hub
FROM python:3.11-slim

# repertoire de travail
WORKDIR /app

# ajout des dépendences dans docker-cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# notre port d'écoute avec streamlit
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]