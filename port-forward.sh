#!/bin/bash

# Forward port 27017 from the mongo-service service
kubectl port-forward -n mongo-namespace service/mongo-service 27017:27017 &

# Forward port 3000 from the grafana deployment
kubectl port-forward deployment/grafana 32200:32200 -n monitoring-namespace &

# Forward port 9090 from the prometheus deployment
kubectl port-forward deployment/prometheus 32100:32100 -n monitoring-namespace &

# Forward port 31000 from the jenkins deployment
kubectl port-forward deployment/jenkins-master 31000:31000 -n jenkins-namespace &

# Forward port 8080 from the jenkins deployment
kubectl port-forward deployment/jenkins-master 8080:8080 -n jenkins-namespace &

# Forward port 9090 from the prometheus deployment
$ kubectl port-forward deployment/prometheus 9090:9090 -n monitoring-namespace
