sudo apt update 

sudo apt install -y docker.io 

docker --version 

sudo usermod -aG docker $USER 

nano Docker file 
```
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

docker build -t iris-api .

docker images 

docker run -d -p  8000:8000 iris-api 
// returns container id
// -d run container in a detached mode 
// -p for port mapping 
// can use image id as well 


docker logs `container_id`

docker ps 
//containers running 

docker stop `container_name`


Kubernetes: 
1. enable gke 
2. gloud services enable artifactregistry.googleapis.com 
3. gcloud artifacts repositories create my-repo --repository-format=docker --location=us-central1 --description="Docer repo for ML models"
4. gcloud auth configure-docker us-central1-docker.pkg.dev
5. docker images 
6. docker tag `image_name` us-central1-docker.pkg.dev/`project_id`/`repo_name`/`image_name`
//us-central1-docker.pkg.dev ➡ Artifact Registry domain
7. docker push us-central1-docker.pkg.dev/`project_id`/`repo_name`/`image_name`

8. gcloud container clusters get-credentials `cluster_name` --zone us-central1 --project `project_id`
9. kubectl get pods 
10. kubectl get service 
