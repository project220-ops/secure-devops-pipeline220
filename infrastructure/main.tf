provider "google" {
  credentials = file("<path-to-your-gcp-credentials>.json")
  project     = var.project_id
  region      = var.region
}

resource "google_compute_instance" "ml-instance" {
  name         = "ml-instance"
  machine_type = "n1-standard-4"
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "your-username:${file("<path-to-your-ssh-key>.pub")}"
  }
}
