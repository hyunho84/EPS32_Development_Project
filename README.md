# ESP32 Development Project

ESP32 + MicroPython 기반 임베디드 프로젝트입니다.  
센서 입력, 모터 제어 등 하드웨어 기능을 단계적으로 추가하며  
**실무에서 사용하는 구조를 기준으로 코드와 폴더를 구성**하는 것을 목표로 합니다.

---

## 📁 Project Structure

```text
project/
│
├─ app/            # 애플리케이션 실행 흐름
│   └─ main.py
│
├─ drivers/        # 하드웨어 제어 (GPIO, ADC, PWM 등)
│   ├─ temp_sensor.py
│   └─ stepper_motor.py
│
├─ services/       # 로직 / 제어 / 정책
│   └─ controller.py
│
├─ config/         # 설정값 (핀 번호, 임계값 등)
│   └─ settings.py
│
├─ tests/          # 개별 기능 테스트
│   └─ test_temp.py
│
└─ README.md
```

📌 Folder Responsibilities
drivers/

센서, 모터 등 하드웨어를 직접 제어

GPIO, ADC, PWM, I2C 등의 저수준 코드만 포함

판단 로직(if, 정책 등)은 포함하지 않음

services/

센서 값을 기반으로 한 판단 및 제어 로직

여러 드라이버를 조합하여 동작을 결정

하드웨어 API(machine, Pin 등)는 사용하지 않음

app/

프로그램의 실행 흐름과 주기 관리

메인 루프, 상태 관리 담당

추후 ESP-IDF / FreeRTOS Task 구조로 전환 가능

config/

핀 번호, 임계값 등 하드웨어 및 시스템 설정

하드코딩 방지를 위한 중앙 설정 파일

tests/

각 드라이버 및 기능을 단독으로 검증

통합 로직 이전에 개별 기능 정상 동작 확인

🚀 Execution Flow

main.py에서 전체 객체를 생성하고 연결

drivers를 통해 센서/모터 제어

services에서 판단 로직 수행

app에서 실행 루프 관리
