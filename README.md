# client-ble-low-power

Este repositório contém um script Python para escanear dispositivos Bluetooth Low Energy (BLE) próximos e se comunicar com um dispositivo ESP32 usando a biblioteca `bleak`.

## Requisitos

- Python 3.7 ou superior
- pip (Python package installer)

## Instalação

1. Clone o repositório:
    ```bash
        git clone https://github.com/seu-usuario/client-ble-low-power.git
        cd client-ble-low-power
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
        python -m venv venv
        source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
        pip install bleak
    ```

4. Atualize o nome/endereço(MAC) do `ESP32` no script main.py:
    ```bash
        DEVICE_NAME = ""
    ```

5. Execute o script `main.py` para se comunicar com o ESP32:
    ```bash
        python3 main.py # No Windows use python main.py
    ```
