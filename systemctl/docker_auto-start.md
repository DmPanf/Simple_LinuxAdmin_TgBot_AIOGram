## 🛠 Steps to Configure Docker Container Auto-Start

### 1. Verify Your Container's Status
First, confirm the container's name or ID:

```bash
docker ps -a
```

Look for your container in the list, e.g., `4ocr-20-got-ocr-app`.

---

### 2. Set a Restart Policy
Use the `--restart` flag to configure the container's restart behavior. For an existing container, update its settings as follows:

1. Stop and remove the container (if it’s already running without a restart policy):

   ```bash
   docker stop myapp
   docker rm myapp
   ```

2. Recreate and start the container with the desired restart policy:

   ```bash
   docker run -d --restart always --name myapp <image_name>
   ```

   Replace `<image_name>` with the image your container uses (e.g., `4ocr-20-got-ocr-app`).

---

### 3. Restart Policy Options

Docker provides several restart policy options:

- `no` (default): Do not restart the container.
- `always`: Always restart the container unless explicitly stopped.
- `on-failure`: Restart the container only if it exits with a non-zero exit code.
- `unless-stopped`: Restart the container unless it has been explicitly stopped by the user.

---

### 4. Update an Existing Container's Restart Policy
If you want to update the restart policy of an existing container without recreating it:

```bash
docker update --restart always 4ocr-20-got-ocr-app
```

---

### 5. Verify the Restart Policy
Check that the restart policy is applied:

```bash
docker inspect myapp --format '{{ .HostConfig.RestartPolicy.Name }}'
```

The output should be `always`, `on-failure`, `unless-stopped`, or `no`, depending on the policy set.

---

### 6. Enable Docker to Start on Boot
Ensure the Docker daemon itself starts on system boot:

```bash
sudo systemctl enable docker
```

Check its status to confirm:

```bash
sudo systemctl status docker
```

---

### 7. Test the Setup
1. Reboot your system:

   ```bash
   sudo reboot
   ```

2. After the system reboots, check if the container is running:

   ```bash
   docker ps
   ```

---

### 🏆 Result
