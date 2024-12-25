### Анализ проблемы:

сервис не работал из-за следующих возможных причин:

1. **Конфликт ssh-процессов:**
   - Вероятно, когда вы пробрасывали порт через систему, демоны `ssh` могли конфликтовать между собой. После ручного завершения процесса (`kill 21022`) система, скорее всего, автоматически перезапустила проброс порта, но уже без конфликта.

2. **Сервис был не полностью настроен:**
   - Если вы использовали `systemd` для управления пробросом, возможно, настройки службы были некорректны или она запускалась неправильно.

3. **Автоматическое восстановление через другой процесс:**
   - На сервере уже могла быть настроена автоматизация проброса порта, которая восстанавливала его после завершения конфликтующего процесса.

---

### Рекомендации для повышения устойчивости системы:

#### 1. **Проверка доступности сервиса:**

Используйте скрипт на Python или `curl` для периодической проверки доступности URL (например, `https://ocr.api-serv.app/docs`):

##### Python:
```python
import requests

def check_service():
    url = "https://ocr.api-serv.app/docs"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Service is available.")
        else:
            print(f"Service returned status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Service check failed: {e}")

check_service()
```

##### Bash (с использованием `curl`):
```bash
#!/bin/bash
URL="https://ocr.api-serv.app/docs"
if curl -s --head --request GET $URL | grep "200 OK" > /dev/null; then
   echo "Service is available."
else
   echo "Service is unavailable."
fi
```

---

#### 2. **Автоматический перезапуск при недоступности:**

Создайте скрипт для проверки доступности и автоматического перезапуска, если сервис недоступен.

##### Bash Script:
```bash
#!/bin/bash
URL="https://ocr.api-serv.app/docs"
SSH_CMD="/usr/bin/ssh -R 0.0.0.0:8084:localhost:8084 bunta@api-serv -N -q"

# Check if service is available
if ! curl -s --head --request GET $URL | grep "200 OK" > /dev/null; then
   echo "Service is down. Restarting SSH tunnel..."
   pkill -f "$SSH_CMD"
   nohup $SSH_CMD &
else
   echo "Service is running."
fi
```

- Запланируйте выполнение скрипта через `cron`:
  ```bash
  crontab -e
  ```
  Добавьте запись для запуска каждые 5 минут:
  ```bash
  */5 * * * * /path/to/check_and_restart.sh
  ```

---

#### 3. **Настройка через `systemd`:**

Обновите конфигурацию `systemd` для автоматического перезапуска проброса порта:

1. Отредактируйте файл службы:
   ```bash
   sudo nano /etc/systemd/system/ssh_tunnel.service
   ```

2. Настройте `ExecStart` и добавьте `ExecStartPre` для проверки доступности сервиса перед запуском:
   ```ini
   [Unit]
   Description=SSH Tunnel Service
   After=network.target

   [Service]
   ExecStartPre=/usr/bin/curl -s --head --request GET https://ocr.api-serv.app/docs | grep "200 OK" || exit 1
   ExecStart=/usr/bin/ssh -R 0.0.0.0:8084:localhost:8084 bunta@api-serv -N -q
   Restart=always
   RestartSec=5
   User=bunta

   [Install]
   WantedBy=multi-user.target
   ```

3. Перезагрузите `systemd`:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart ssh_tunnel.service
   ```

---

#### 4. **Мониторинг с использованием сторонних инструментов:**

Используйте инструменты мониторинга, такие как **Prometheus**, **Grafana**, или **UptimeRobot** для автоматической проверки доступности URL и уведомления о сбоях.

---

### Итог:

- Проверьте настройки и устраните конфликты `ssh`-процессов.
- Настройте автоматическую проверку доступности сервиса.
- Используйте `systemd` или скрипт для автоматического перезапуска туннеля.
- Для более надежного мониторинга внедрите сторонние инструменты. 
