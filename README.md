# Сканер MAC-адресов

Этот скрипт выполняет сканирование сети на предмет новых устройств, подключённых к сети. Он проверяет таблицу ARP, чтобы выявить новые MAC-адреса, которых не было при последнем запуске, и сохраняет их для последующих проверок.

## Как работает

1. Скрипт пингует устройства в сети по диапазону IP-адресов (по умолчанию с `192.168.0.100` по `192.168.0.110`).
2. Затем он собирает таблицу ARP и извлекает все найденные MAC-адреса.
3. Скрипт проверяет, есть ли новые MAC-адреса, которых не было при предыдущем запуске.
4. Если новые MAC-адреса найдены, они сохраняются в файл `new_macs.txt`, а текущие MAC-адреса записываются в файл `known_macs.txt` для использования при следующем запуске.

## Как запустить

1. Убедитесь, что у вас установлен Python.
2. Скачайте скрипт `script.py` и поместите его в нужную директорию.
3. Создайте батник `scanner.bat` с следующим содержимым:

`batch
@echo off
:loop
cls
python C:\script\script.py
echo.
echo Нажмите любую клавишу для запуска сканирования снова...
pause >nul
goto loop`

4. Запустите файл scanner.bat. Скрипт будет запускаться в цикле, сканируя сеть и проверяя наличие новых устройств.
   
script.py — основной Python-скрипт для сканирования сети и обработки данных ARP.
scanner.bat — батник для автоматического запуска Python-скрипта в цикле.
known_macs.txt — файл для хранения известных MAC-адресов.
new_macs.txt — файл для хранения новых MAC-адресов, найденных при текущем сканировании.

5. Важно
Если файл known_macs.txt пуст или не существует, скрипт начнёт с пустого списка MAC-адресов.
Скрипт использует  команды ping и arp
