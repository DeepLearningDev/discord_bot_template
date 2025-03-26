# Hikari and Crescent Discord Bot Template

This repository provides a ready-to-use template for creating Discord bots using Python. It includes essential dependencies and setup instructions, allowing you to quickly get started on building your own Discord bot.

## Features

- Compatible with Discord's API through both **discord.py** and **hikari** libraries
- Easy command handling with **hikari-crescent**
- Environment variable management using **python-dotenv**
- Event loop optimizations for Windows via **winloop** (or **uvloop** for Linux/MacOS)

## Dependencies

- `discord.py==2.4.0`
- `hikari==2.2.0`
- `hikari-crescent==1.2.0`
- `python-dotenv==1.0.1`
- `winloop==0.1.8` *(use `uvloop` instead if not on Windows)*

## Installation

1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd discord-bot-template
```

2. **Create and Activate Virtual Environment** *(optional but recommended)*

- On Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

- On Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

> **Note:** If you're on Linux or MacOS, replace `winloop` with `uvloop`:

```bash
pip uninstall winloop
pip install uvloop
```

4. **Configure Environment Variables**

Create a `.env` file in the root directory and add your Discord bot token:

```env
TOKEN=your-bot-token-here
```

## Running Your Bot

To run your bot:

```bash
python -m botname
```

Ensure your bot token is correctly set up in the `.env` file.

## Project Structure

```
discord-bot-template/
├── .env
├── .gitignore
├── README.md
├── LICENSE
├── botname/
│   ├── __init__.py
│   ├── __main__.py
│   └── plugins/
│       └── example_command.py
└── requirements.txt
```

## Customization

- Place your commands within the `botname/plugins/` folder.

## License

This template is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions, suggestions, and improvements are always welcome! Feel free to open an issue or submit a pull request.

Happy coding! 🎉


