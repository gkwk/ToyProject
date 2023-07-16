프론트엔드 : 부트스트랩  
백엔드 : django<br>
mlflow 사용법 : mlflow db 폴더에서 mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts<br>
Sqlite3 대신 MySQL을 사용하려면 settings.py의 DATABASE에서 sqlite3부분을 주석처리하고 MySQL부분의 주석을 해제 및 환경에 맞게 변수를 수정한다.<br>