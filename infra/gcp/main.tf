terraform {
}


provider "google" {
  credentials = file(var.gcp_credentials_file)
  project     = var.gcp_project_id
  region      = var.gcp_region
  zone        = var.gcp_zone
}

resource "google_compute_instance" "monitoring_node" {
  name         = "monitoring-ethereum"
  machine_type = "e2-standard-4"

  boot_disk {
    initialize_params {
      image = "centos-8"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
  }

  metadata = {
    ssh-keys = "ethereum:${file(var.ssh_public_key_file)}"
  }
}

resource "google_compute_firewall" "default" {
 name    = "wireguard"
 network = "default"

 allow {
   protocol = "udp"
   ports    = ["0-65535"]
 }
}


resource "google_compute_instance" "blockchain_node" {
  name         = "node"
  machine_type = "e2-standard-4"

  boot_disk {
    initialize_params {
      image = "centos-8"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "default"
    access_config {
    }
  }

  metadata = {
    ssh-keys = "ethereum:${file(var.ssh_public_key_file)}"
  }
}