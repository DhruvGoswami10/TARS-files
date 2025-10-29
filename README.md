# TARS Control Modes

This repository now ships with two supported stacks for running your TARS replica:

- **TARSmaster** – a single file that boots the Tkinter command console, voice assistant, and controller listener together.
- **Bundle** – the original modular scripts (voice, controller, mechanism, run_master) packaged for headless Raspberry Pi deployments.

## Contents

```
TARS-files/
├── TARSmaster.py
├── bundle/
│   ├── controller.py
│   ├── mechanism.py
│   ├── run_master.py
│   └── voice.py
└── README.md
```

## Dependencies & Credentials

Both modes require the same system libraries and Python packages:

```
sudo apt update && sudo apt install -y \
  python3-pip python3-dev python3-smbus i2c-tools \
  libasound-dev portaudio19-dev ffmpeg && \
pip3 install --break-system-packages \
  evdev adafruit-circuitpython-pca9685 \
  adafruit-circuitpython-busdevice adafruit-blinka \
  speechrecognition openai boto3 requests pydub
```

You must also supply your own API keys before running:

- OpenAI API key (`openai.api_key`) for conversation.
- AWS Polly access & secret keys for speech.
- OpenWeatherMap API key plus a city name if you want weather banter.

## Usage

### TARSmaster (desktop / full experience)
```
python3 TARSmaster.py
```
This starts the GUI console, speech recognition, controller polling, and servo layer in one process.

Detailed guide: [TARSmaster Mode](https://www.notion.so/TARSmaster-Mode-29b81163f50b8015a006eaeec8a196b2)

### Bundle (modular / headless)
```
cd bundle
python3 run_master.py   # or run mechanism.py / controller.py / voice.py individually
```
Use this on the Pi when you need lightweight scripts without the Tkinter front-end.

Detailed guide: [Bundle Mode](https://www.notion.so/Bundle-Mode-Modular-Deployment-29b81163f50b8060ba8ffa51a6e1ef1b)

## Documentation

- [Raspberry Pi Setup](https://www.notion.so/Raspberry-Pi-Setup-for-TARS-29b81163f50b80feaad2cbecfa0b935d)
- [API Key Walkthrough](https://www.notion.so/API-Keys-Document-29b81163f50b80829ffce12c44a07c28)

---
Physical wiring notes will be published separately—keep an eye on Notion for those diagrams.
