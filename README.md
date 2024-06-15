RC-Recommunity.
Website to get info about a large varient of RC models!

























notes for myself:

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

[Promethues Working IP for grafana communication]
10.1.0.242:9090