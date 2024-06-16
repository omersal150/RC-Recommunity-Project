RC-Recommunity.
Website to get info about a large varient of RC models!

























notes for myself:

All project links:
Main website
http://127.0.0.1:30000/

ArgoCD
https://127.0.0.1:30080/

Grafana
http://127.0.0.1:32200/

Prometheus
http://127.0.0.1:32100/

Jenkins
http://127.0.0.1:31000/

MongoDB
mongodb://mongo-service.mongo-namespace:27017/rc_recommunity


[[Delete all port forwarding in rc recommunity namespace]]
kubectl delete job port-forward-job -n rc-recommunity


[[attonate and label mongo namespace]]
kubectl label namespace mongo-namespace app.kubernetes.io/managed-by=Helm
kubectl annotate namespace mongo-namespace meta.helm.sh/release-name=rc-recommunity
kubectl annotate namespace mongo-namespace meta.helm.sh/release-namespace=mongo-namespace

[[attonate and label monitoring namespace]]
kubectl label namespace monitoring-namespace app.kubernetes.io/managed-by=Helm
kubectl annotate namespace monitoring-namespace meta.helm.sh/release-name=monitoring
kubectl annotate namespace monitoring-namespace meta.helm.sh/release-namespace=monitoring-namespace

[[attonate and label jenkins namespace]]
kubectl annotate namespace jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate namespace jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite

kubectl annotate serviceaccount jenkins-sa -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate serviceaccount jenkins-sa -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite

kubectl annotate secret jenkins-sa-token -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate secret jenkins-sa-token -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite

kubectl annotate pv jenkins-pv meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate pv jenkins-pv meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label pv jenkins-pv app.kubernetes.io/managed-by=Helm --overwrite

kubectl annotate pvc jenkins-pvc -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate pvc jenkins-pvc -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label pvc jenkins-pvc -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite

kubectl annotate role jenkins-secrets-reader -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate role jenkins-secrets-reader -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label role jenkins-secrets-reader -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite

kubectl annotate rolebinding jenkins-agent-rolebinding -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate rolebinding jenkins-agent-rolebinding -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label rolebinding jenkins-agent-rolebinding -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl annotate service jenkinsmasternodeport -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate service jenkinsmasternodeport -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label service jenkinsmasternodeport -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl annotate service jenkinsmasterclusterip -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate service jenkinsmasterclusterip -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label service jenkinsmasterclusterip -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl label service jenkinsmasternodeport -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl annotate service jenkinsmasternodeport -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate service jenkinsmasternodeport -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label service jenkinsmasterclusterip -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl annotate service jenkinsmasterclusterip -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate service jenkinsmasterclusterip -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite
kubectl label deployment jenkins-master -n jenkins-namespace app.kubernetes.io/managed-by=Helm --overwrite
kubectl annotate deployment jenkins-master -n jenkins-namespace meta.helm.sh/release-name=jenkins --overwrite
kubectl annotate deployment jenkins-master -n jenkins-namespace meta.helm.sh/release-namespace=jenkins-namespace --overwrite


[Promethues Working IP for grafana communication]
kubectl get pods -n monitoring-namespace -o wide
:9090 port after port forwarding it