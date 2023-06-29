# ZJUI Indonesia Summer School 2023
This is the repository for ZJUI Indonesia Summer School 2023.

## Prerequisites
### Hardware
- Jetson Nano Developer Kit / Jetson TX2 Developer Kit
- STM32 Board
### Software
- JetPack 4.6 or above (with all the components installed via SDK Manager)
- `pycuda`
- `pySerial`

## Procedure (for students)
### 1. Clone the repository
```bash
git clone https://github.com/nice-mee/zjui_indonesia_summer_school_2023.git
cd zjui_indonesia_summer_school_2023
```

> **Note**: Connection to GitHub is not stable in China. So we've already cloned the repository for you on Jetson TX2.

### 2. Build TensorRT engine
```bash
/usr/src/tensorrt/bin/trtexec --onnx=model/yolov8.onnx --saveEngine=model/yolov8.engine --explicitBatch --fp16 --workspace=1024
```
This usually takes 10-20 minutes on Jetson Nano, wait patiently until it ends. It is generally **not recommended** to open any other program during the process. This command will generate a TensorRT engine file `yolov8.engine` in `model` folder. You'll need it to make `utils.vision` function properly. Once `yolov8.engine` is generated, you don't need to run this command again.

### 3. Write main.py and test your code
Write your program in `main.py`. You can refer to the project wiki for information about the APIs provided.

I would recommended you to write the camera streaming and detection part first, and test your code with the following command:
```bash
python3 main.py
```

> **Optional**: For students who has some knowledge of Linux, you may want to set up a symbolic link with `update-alternatives` so that you can use `python` instead of `python3` to make things faster.

### 4. Test your code with serial connection
If your code calls anything inside `utils.serial`, you must do the following steps before testing your code:

1. Connect the USB to UART converter to your Jetson Nano, and run the following command:
    ```bash
    ls -al /dev/ttyUSB*
    ```
    You should see something like `/dev/ttyUSB0` showing up. If not, contact TA for help.

    > **Note**: Connecting the converter to STM32 is not required for testing, and I do not recommend doing this right away if you're not sure whether your code works as it may damage the device
2. Run the following command:
    ```bash
    sudo chmod 777 /dev/ttyUSB0
    ```
    This step ensures that your program has the permission to access the serial port. The effect will be **reset** after rebooting, so you'll need to run this command again if you reboot your Jetson Nano.