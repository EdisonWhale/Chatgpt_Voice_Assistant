# VocaWhale AI Assistant

This project is a web-based Voice Assistant application named "VocaWhale AI Assistant" that provides AI-driven voice interaction using OpenAI's GPT model and ElevenLabs. The front end is built using React.js and the backend uses FastAPI.

<br>

<p align="center">
  <img src="https://github.com/EdisonWhale/Chatgpt_Voice_Assistant/assets/103423072/bde17238-d403-4ed9-9081-39ad2e549e44" width="400">
</p>


<br>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Ensure that you have the following installed on your local machine:

- Node.js and yarn (you can check their versions with `node -v` and `yarn -v`)
- Python 3.10 and pip (you can check their versions with `python3 --version` and `pip3 --version`)
- API Keys from OpenAI and Eleven Labs

For the application to function properly, you'll need API keys from OpenAI and Eleven Labs. You can obtain them from their respective websites:

- OpenAI: [https://beta.openai.com/](https://beta.openai.com/)
- Eleven Labs: [https://beta.elevenlabs.io/](https://beta.elevenlabs.io/)

Keep these keys safe, as you'll need to input them into the `.env` file in the setup process.

# Instructions

### Step 1: Clone the repo

```shell
git clone https://github.com/EdisonWhale/Chatgpt_Voice_Assistant.git

```

## Setup backend

Change directory into backend

```shell
cd chatbot/backend
```

### Setup virtual environment

Create a Virtual Environment

```shell
python3 -m venv venv
```

Activate Virtual Environment (MAC)

```shell
source venv/bin/activate
```

Activate Virtual Environment (Windows)

```shell
source venv/Scripts/activate
```

Upgrade PIP

```shell
pip3 install --upgrade pip
```

### Install Python packages

Install required Python packages

```shell
pip3 install openai python-decouple fastapi "uvicorn[standard]" python-multipart
```

Or use this alternative method (although this alternative method might not work if using Windows)

```shell
pip3 install -r requirements.txt
```

### Create Environment Variables

Update your .env file with the following. You can see your .env by typing sudo nano .env or just by clicking on the file if you are in VS Code.

```plain
OPEN_AI_ORG=enter-you-key-here
OPEN_AI_KEY=enter-you-key-here
ELEVEN_LABS_API_KEY=enter-you-key-here
```

### Start your backend server

Start your backend server

```shell
uvicorn main:app
```

Alternatively, you can ensure your server resets every time you make a change by typing:

```shell
uvicorn main:app -- reload
```

You can check your server is working by going to:

```plain
http://localhost:8000/health
```

## Setup frontend

Change directory into frontend

```shell
cd ..
cd chatbot/frontend
```

Install packages

```shell
yarn --exact
```

Build application

```shell
yarn build
```

Start server in dev mode

```shell
yarn dev
```

You can check your dev server is working by going to:

```plain
http://localhost:5173/health
```

or alternatively in live mode:

```shell
yarn start
```

You can check your live server is working by going to:

```plain
http://localhost:4173/health
```

## Tech Stack
- Frontend: React.js, Typescript
- Backend: FastAPI
- Voice to Text and Text to Voice: OpenAI's GPT model, Elevenlabs

## Contact

Made with ❤️ by Edison  
[www.Edisonwhale.com](http://www.edisonwhale.com)

Have any questions?  
Email me!  
Edison@gatech.edu
