resource "digitalocean_kubernetes_cluster" "main" {
  name    = "my-sre-cluster"
  region  = "nyc3"
  version = "latest"

  node_pool {
    name       = "default-pool"
    size       = "s-2vcpu-4gb"
    node_count = 2
  }
}

resource "digitalocean_droplet" "vm" {
  name   = "sre-droplet"
  region = "nyc3"
  size   = "s-1vcpu-2gb"
  image  = "ubuntu-22-04-x64"
  tags   = ["sre"]
}

resource "digitalocean_database_cluster" "db" {
  name       = "sre-db"
  engine     = "pg"
  version    = "15"
  size       = "db-s-1vcpu-1gb"
  region     = "nyc3"
  node_count = 1
}

