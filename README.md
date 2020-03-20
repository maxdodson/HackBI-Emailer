# <img src="https://raw.githubusercontent.com/maxdodson/HackBI-Emailer/master/static/favicon.ico" width="20"/> HackBI-Emailer
Small Flask web app for sending emails from local templates

## Requirements
[Python](https://www.python.org/downloads/)

[Git](https://git-scm.com/downloads)

## Setup
1. Run `git clone https://github.com/maxdodson/HackBI-Emailer.git`
#### Create a GitHub OAuth App
2. Follow [these instructions](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/) to create an OAuth app for GitHub
   > You can make your callback & homepage links anything. They won't be used.
3. Follow [these instructions](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line#creating-a-token) to generate a personal access token for your OAuth app. You only need to select the `gist` scope.
#### Create an environment variable to store your GitHub token
> If you're on Windows and are using Git Bash, try replacing `.bash_profile` in both places below with `.bashrc`
4. Insert your token into the following and run it (Mac/Linux):
   ```
   echo "export GITHUB_API_TOKEN='Bearer YOUR_TOKEN_GOES_HERE'" >> ~/.bash_profile
   ```
5. Then run `. ~/.bash_profile`
#### Launch the program
6. `cd` into the repository folder (Likely `cd HackBI-Emailer`)
7. Run `python3 server.py`
8. Open a web browser to `localhost:5000`
