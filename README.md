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

## Usage
### Dashboard
* Any `.html` templates in the `static/` directory will be detected on startup and displayed on the Dashboard
   * Descriptions from each template will also be extracted and displayed (See example in any file in the `static/` folder)
* Clicking on a template on the Dashboard page will open a new page where you can preview and send the email (See Sending)
 
### New
* A page with a field to insert HTML and a preview window will be displayed
* The title field will autofill `.html` if necessary
* You will be prompted to enter a new title if a file with the same name exists in the `static/` folder
* Once you are finished editing, click the Publish button to publish the template (See Publishing)

### Sending
  > :warning: Sending is disabled for the Google Apps Script in `server.py` that's attached to my email. See [here](https://gist.github.com/maxdodson/96b666d4e839970c119b3c77497569d5) for the Apps Script code. Copy it to a new Apps Script and publish it as a web app. Then replace my link with yours.
  * If the template contains the `<?= ?>` dynamic tag, recipients must be inserted in the following format:
  ```
  {
      "name": "John Doe",
      "email": "john@email.com"
  },
  {
      "name": "Jane Doe",
      "email": "jane@email.com"
  }
  ```
  * If the template does not contain dynamic tags, recipients must be inserted in the following format:
  ```
  "john@email.com","jane@email.com"
  ```
### Publishing
* The HTML template will be saved locally in your `static/` directory
* If you set `href="__link__"` in the "Can't see this email?" link, a GitHub Gist will be created to host the email
   * `__link__` will automatically be replaced with the Gist link
  
