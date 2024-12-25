## 🚀 Reliable Service Setup with systemd

This guide provides a step-by-step process for setting up and debugging a reliable service using `systemd` on Linux. Whether you’re forwarding a port via SSH or running a bot, this tutorial will ensure your service runs consistently and restarts automatically in case of failure.

---

### 🛠️ Prerequisites

Before starting, ensure the following:
1. **Linux Distribution**: Ubuntu 20.04 or later is recommended.
2. **Required Tools**:
   - `systemd` (pre-installed on most Linux systems)
   - `ssh` (for SSH-based services)
3. **Access Permissions**: Root or sudo privileges for creating and managing system services.

---

### 📄 Step 1: Create a Service File

1. Navigate to the `systemd` configuration directory:

   ```bash
   sudo nano /etc/systemd/system/<your_service_name>.service
   ```

2. Paste the configuration template below and customize it:

   ```ini
   [Unit]
   Description=<Your Service Description>
   After=network.target

   [Service]
   ExecStart=<Your Command to Run the Service>
   WorkingDirectory=<Optional: Working Directory Path>
   Restart=always
   RestartSec=5
   User=<User>
   StandardOutput=journal
   StandardError=journal

   [Install]
   WantedBy=multi-user.target
   ```

   ### Example: SSH Port Forwarding Service
   ```ini
   [Unit]
   Description=SSH Port Forwarding Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/ssh -R 0.0.0.0:8080:localhost:8080 user@server -N -q
   Restart=always
   RestartSec=5
   User=bunta
   StandardOutput=journal
   StandardError=journal

   [Install]
   WantedBy=multi-user.target
   ```

   ### Example: Bot Service
   ```ini
   [Unit]
   Description=Telegram Bot Service
   After=network.target

   [Service]
   ExecStart=/path/to/venv/bin/python /path/to/bot.py
   WorkingDirectory=/path/to/project
   Restart=always
   RestartSec=5
   User=your_user
   StandardOutput=journal
   StandardError=journal

   [Install]
   WantedBy=multi-user.target
   ```

---

## ⚙️ Step 2: Enable and Start the Service

1. Reload `systemd` to apply the new service file:

   ```bash
   sudo systemctl daemon-reload
   ```

2. Enable the service to start at boot:

   ```bash
   sudo systemctl enable <your_service_name>
   ```

3. Start the service:

   ```bash
   sudo systemctl start <your_service_name>
   ```

---

## 🔍 Step 3: Debugging the Service

1. Check the service status:

   ```bash
   sudo systemctl status <your_service_name>
   ```

2. View logs for debugging:

   ```bash
   sudo journalctl -u <your_service_name>
   ```

3. Check if the process is running:

   ```bash
   ps -ef | grep <process_name_or_command>
   ```

---

## ✅ Verification

- Ensure the service performs as expected:
  - **For SSH Tunnel**: Verify the port forwarding with `netstat` or by testing the connection.
  - **For Bots**: Confirm the bot is responding correctly to commands.

---

## 🚨 Troubleshooting

- **Error Code `217/USER`**: Ensure the user specified in `User=<user>` exists and has the necessary permissions.
- **Service Not Starting**: Verify the `ExecStart` command works manually in the terminal.
- **Restart Loops**: Check logs to identify misconfigurations or issues with the service command.

---

## 🎉 Enjoy!
