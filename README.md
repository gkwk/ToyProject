# 프론트엔드
- Node.js 18.17.1
- React
- Bootstrap

# 백엔드
- Python 3.10.12
- django

# 구동 방법
## MLFlow
```zsh
$ cd path/path/mlflow
$ mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts
```
## django
```zsh
$ cd path/path/ToyProject
$ python manage.py runserver
```
## React
```zsh
$ cd path/path/frontend
$ npm start
```
### prettier
```zsh
$ cd path/path/frontend
$ npm run format
```
### eslint
```zsh
$ cd path/path/frontend
$ npm run lint
```

# AI_test.csv
$$ y = 4x_0 + 5x_1 + 2x_2 + 7_x3 + 0.1x_4 + 15x_5 + 0.05x_6+ x_7 $$
`ref : https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions`