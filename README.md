ua:потрібно встановити mpremote та screen 

mpremote: для загрузки файла в esp32 

screen: для підключення до esp32

команда для загрузки в память esp32: mpremote connect 'порт в який підключена esp32" fs cp microos.py :

комана для перевірки чи файл завантажився в память: mpremote connect 'порт в який підключена esp32" fs ls :

команда для запуску: import microos а потім microos.main()

![](exsemple.png)

us: you need to install mpremote and screen 

mpremote: to upload a file to esp32 

screen: to connect to esp32

command to load esp32 into memory: mpremote connect "port to which esp32 is connected" fs cp microos.py:

command to check if the file is loaded into memory: mpremote connect "port the esp32 is connected to" fs ls :

run the command: import microos and then microos.main()
