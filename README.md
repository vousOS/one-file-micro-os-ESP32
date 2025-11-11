ua:потрібно встановити mpremote та screen 

mpremote: для загрузки файла в esp32 

screen: для підключення до esp32

команда для загрузки в память esp32: mpremote connect 'порт в який підключена esp32" fs cp mysimos.py :

комана для перевірки чи файл завантажився в память: mpremote connect 'порт в який підключена esp32" fs ls :

команда для запуску: import microos
                        microos.main()
