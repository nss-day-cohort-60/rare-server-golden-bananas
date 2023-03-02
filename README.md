# rare-server-golden-bananas
Our server for team golden bananas


This is the API for the [rare-client-golden-bananas](https://github.com/nss-day-cohort-60/rare-client-golden-bananas)


## Installation
Follow the steps below to download and run this project on your computer
- [ ] Client is required for full functionality. [View client repo here](https://github.com/nss-day-cohort-60/rare-client-golden-bananas)
- [ ] Clone this repository
- [ ] From server directory, run "pipenv install"
- [ ] Make sure to be in a virtual environment. "pipenv shell"
- [ ] Run this code:
```bash
rm db.sqlite3
rm -rf ./rareapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations rareapi
python3 manage.py migrate rareapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata rare_users
python3 manage.py loaddata categories
python3 manage.py loaddata posts
```
- [ ] Run "python manage.py runserver"

For more help with installations, go to [ChatGPT](https://chat.openai.com/chat)


## Sprint Team Contribution

### Pavan Patel
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Pavan688)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pavankumar-patel-916597265/)

* Created server-side code to handle requests.
* Clientside MyPost view.
* Clientside create post view.
* Managed local storage content.
* Created category delete functionality.
* Github pull-requests, code-review, merges.

### Charles Seals
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/charlesseals)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/charlesseals/)

* Created Django models and fixtures.
* Clientside MyPost view.
* Clientside create post view.
* Managed local storage content.
* Created category delete functionality.
* Github pull-requests, code-review, merges.


### Jordon Perkins
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jordon-perkins)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jordon-perkins)

* Clientside view all posts embedded content.
* Clientside view single post details.
* Created category delete functionality.
* Clientside JSX to match property decorators.
* Github pull-requests, code-review, merges.


### Nathan Pyles
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Deadwing91)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nathanlpyles)

* Clientside view all filter posts by category.
* Created category delete functionality.
* Github pull-requests, code-review, merges.
* README.md

## Tech Stack

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
