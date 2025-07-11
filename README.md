

# CI/CD and Observability Stack for Python Application (SRE-Focused)

This project demonstrates a CI/CD pipeline and observability workflow built around a containerized Python application. It combines  Terraform, Jenkins, ArgoCD, Prometheus, Grafana, and Kubernetes to apply SRE practices—automated deployment, monitoring, and alerting.

---

## Tech Stack

| Tool/Service           | Role                                                               |
| ---------------------- | ------------------------------------------------------------------ |
| **Python**             | Application development                                            |
| **Docker**             | Containerization of the Python app                                 |
| **Kubernetes**         | Orchestration of containerized workloads                           |
| **Terraform**          | Infrastructure as Code (Kubernetes clusters and related resources) |
| **GitHub Actions**     | CI trigger that calls Jenkins                                      |
| **Jenkins**            | Continuous Integration and Docker image build and push             |
| **ArgoCD**             | GitOps-based continuous delivery to Kubernetes                     |
| **Prometheus**         | Metrics collection                                                 |
| **Grafana**            | Dashboards and alerting                                            |

---

## 📁 Repository Structure

```
.
├── .github/workflows
│   └── trigger-jenkins.yml           # GitHub Actions workflow
│
├── CD-Python-App-main               # Kubernetes manifests
│   ├── application.yaml
│   ├── deployment.yaml
│   ├── postgres-deployment.yaml
│   ├── service.yaml
│   └── service_monitor.yaml         # Prometheus ServiceMonitor
│
├── CI-Python-App-main               # Python app + CI configuration
│   ├── Dockerfile
│   ├── Jenkinsfile
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
│
├── miscel
│   ├── helm-prom-values.yaml        # Helm values for Prometheus
│   ├── jenkins-pipeline.txt         # Notes or example Jenkins pipeline
│   └── my-grafana-dashboard.json    # Grafana dashboard configuration
│
├── terraform
│   └── README.md                    # Terraform documentation
```

---

## 🔁 CI/CD Workflow

1. **GitHub Actions** triggers on new commits and invokes a Jenkins pipeline.
2. **Jenkins**:

   * Builds the Docker image for the Python app
   * Pushes the image to a container registry
3. **ArgoCD**:

   * Syncs Kubernetes manifests from `CD-Python-App-main`
   * Deploys the updated application and database to Kubernetes
4. **Kubernetes**:

   * Schedules and runs the application containers
   * Manages networking, scaling, and resource usage
5. **Monitoring & Alerting**:

   * Prometheus scrapes metrics from the application using a ServiceMonitor
   * Grafana visualizes metrics and fires alerts
   * Alerts are sent via webhook

---

## 🔍 Observability and Alerting

* **Prometheus Operator** is installed via Helm (`helm-prom-values.yaml`)
* Custom `service_monitor.yaml` is used to expose application metrics
* Application specific dashboards are configured in Grafana using `my-grafana-dashboard.json`
* **Alerts** are defined in Grafana and used external webhook for notifications

---

## SRE Practices

* ✅ Declarative deployments via GitOps (ArgoCD)
* ✅ Reproducible infra via Terraform
* ✅ Immutable containers via Docker
* ✅ Orchestrated runtime with Kubernetes
* ✅ Continuous Integration using Jenkins
* ✅ Observability with Prometheus and Grafana
* ✅ Alerting for Error Rates via webhooks

---
