output "k8s_endpoint" {
  value = digitalocean_kubernetes_cluster.main.endpoint
}

output "droplet_ip" {
  value = digitalocean_droplet.vm.ipv4_address
}

output "db_uri" {
  value = digitalocean_database_cluster.db.uri
}

