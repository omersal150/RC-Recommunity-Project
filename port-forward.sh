#!/bin/bash

# Forward port 8080 from the rc-recommunity-flask deployment
kubectl port-forward -n mongo-namespace deployment/rc-recommunity-flask 8080:8080 &

# Forward port 27017 from the mongo-service service
kubectl port-forward -n mongo-namespace service/mongo-service 27017:27017 &

# Forward port 3000 from the grafana deployment
kubectl port-forward svc/grafana 3000:3000 -n monitoring-namespace &


# Forward port 9090 from the prometheus deployment
kubectl port-forward svc/prometheus 9090:9090 -n monitoring-namespace
