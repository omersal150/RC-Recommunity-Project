#!/bin/bash

# Store the Argo CD initial admin password in a variable
PASSWORD=$(kubectl -n argocd-namespace get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d)

# Login
./argocd login 192.168.68.60:30080 --username admin --password $PASSWORD --insecure

# Update password
./argocd account update-password --current-password $PASSWORD --new-password 3372 --insecure

# Log in with the new password
./argocd login 192.168.68.60:30080 --username admin --password 3372 --insecure

# Create or update rc-recommunity
./argocd app create rc-recommunity \
  --project default \
  --repo https://github.com/omersal150/RC-Recommunity-Project \
  --path charts/appchart \
  --revision HEAD \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --helm-set-file values=values.yaml \
  --sync-policy automated \
  --self-heal \
  --upsert

# Create or update the Jenkins application
./argocd app create jenkins \
  --project default \
  --repo https://github.com/omersal150/RC-Recommunity-Project \
  --path charts/jenkinschart \
  --revision HEAD \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace jenkins \
  --helm-set-file values=values.yaml \
  --sync-policy automated \
  --self-heal \
  --upsert
