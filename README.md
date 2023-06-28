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

### 2. Build TensorRT engine
```bash
/usr/src/tensorrt/bin/trtexec --onnx=model/yolov8.onnx --saveEngine=model/yolov8.engine --explicitBatch --fp16 --workspace=1024
```
This usually takes 10-20 minutes on Jetson Nano, wait patiently until it ends. It is generally **not recommended** to open any other program during the process. This command will generate a TensorRT engine file `yolov8.engine` in `model` folder. You'll need it to make `utils/vision` function properly.

### 3. Write main.py
Write your program in `main.py`. You can refer to the project wiki for information about the APIs provided.

I would recommended you to write your code without serial connection first, and test your code with the following command:
```bash
python3 main.py
```

### 4. Test your code with STM32
If you want to test your code with STM32. Connect the STM32 board to your Jetson Nano with serial port, and run the following command:
```bash
ls -al /dev/ttyUSB*
```
If you can see something like `/dev/ttyUSB0`, then you can test your code with the command mentioned above in Section 3.