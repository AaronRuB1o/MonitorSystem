# MonitorSystem: All-in-One Monitoring & Organization Tree App

## Project Summary

MonitorSystem is an all-in-one Django-based application designed to showcase an interactive organizational chart and real-time monitoring dashboard. This project is containerized with Docker, orchestrated via Kubernetes (Minikube for local development), and integrated with a MySQL backend. Ideal for learning full-stack infrastructure and DevOps principles.

---

## Why I Built This

I wanted to build something that combines real-time data, infrastructure automation, and cloud integration — and also looks good on a resume. It started as a test to get Django running in Docker, and grew into a full DevOps stack with monitoring and org chart features.

## Achievements

### App Features

- Organizational Chart (OrgChart.js + static CSV parser)
- Monitoring dashboard with real-time data table
- Admin dashboard via Django Admin

### DevOps Milestones

- ✅ Dockerized both Django & MySQL apps
- ✅ Docker Compose support for local dev
- ✅ Kompose: Converted docker-compose to Kubernetes YAMLs
- ✅ Minikube: Local K8s cluster setup with deployments + services
- ✅ PersistentVolumeClaims used for MySQL storage
- ✅ Liveness and Readiness Probes added for health checks
- ✅ SQL backup + restore pipeline tested inside pods
- ✅ Static files + JS libs integrated in Django structure
- ✅ Verified Git workflow for version control

### Cloud Readiness

- ✅ Researched AWS services: EKS, CloudWatch, Watchtower
- ✅ EKS pricing analyzed (determined not ideal for free-tier dev)
- ✅ Watchtower considered as an alternative lightweight monitoring tool
- ✅ Roadmap for pushing Docker image to Docker Hub / ECR prepared

---

## Requirements

| Tool     | Version |
| -------- | ------- |
| Python   | 3.11+   |
| Django   | 4.2+    |
| Docker   | 24+     |
| Minikube | latest  |
| kubectl  | latest  |
| Kompose  | latest  |

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2. Docker Compose (local development)

```bash
docker-compose up --build
```

Visit: [http://localhost:8000](http://localhost:8000)

### 3. Kompose to Kubernetes

```bash
kompose convert -o k8s/
kubectl apply -f k8s/
```

To expose service:

```bash
minikube service web
```

### 4. Minikube Image Build (IMPORTANT)

```cmd
@FOR /f "tokens=*" %i IN ('minikube -p minikube docker-env --shell cmd') DO @%i
docker build -t web .
kubectl rollout restart deployment web
```

### 5. Apply SQL Backup

```bash
kubectl exec -it <mysql-pod> -- bash
mysql -uAaron -p -DCompanyDB < /path/to/backup.sql
```

### 6. Django Commands

```bash
python manage.py migrate
python manage.py createsuperuser
```

Visit Django Admin: `http://localhost:<port>/admin`

---

## File Structure (Important Parts)

```
project/
├── calc/static/CompanyTree/images/
├── calc/static/CompanyTree/js/
├── calc/static/MonitorSystem/css/
├── Dockerfile
├── docker-compose.yml
├── k8s/ (kompose-generated Kubernetes YAMLs)
├── manage.py
├── monitoring/ (Main app)
├── README.md
```

---

## Roadmap (Next Steps)

- Push Docker images to Docker Hub or ECR
- Explore CloudWatch for deeper metrics
- Use Kubernetes Secrets or .env for config management
- Add CI/CD pipeline via GitHub Actions

---

## Contributions

Open to feedback, PRs, and collaboration! Feel free to fork or raise an issue.

---

## Author

Built and maintained by **AaronRuB1o**

## References
[Django to Docker and Docker-Compose](https://medium.com/@dryalcinmehmet/drf-part-6-mastering-django-rest-framework-docker-and-docker-composing-the-project-d2b926fefb84)
[K8s Probes](https://stackoverflow.com/questions/65858309/why-do-i-need-3-different-kind-of-probes-in-kubernetes-startupprobe-readinessp)
[Kompose Convert to K8s resources](https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
[Using Minikube as Replacement Docker](https://minikube.sigs.k8s.io/docs/tutorials/docker_desktop_replacement/#cmd)

## Disclaimer
All personal data has been anonymized. The names, usernames, and emails etc. in this repository are synthetic and randomly generated for demonstration purposes only.