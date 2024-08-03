# https://mastergroosha.github.io/aiogram-3-guide/quickstart/

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr  для конфиденциальных данных, например, токена бота
    bot_token: SecretStr

    # Начиная со второй версии pydantic, настройки класса настроек задаются через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан  с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings()
