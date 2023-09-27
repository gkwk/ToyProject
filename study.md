# django MySQL 사용법
- django의 settings.py에서, DATABASE의 sqlite3 코드를 제거하고 MySQL 코드의 주석을 해제한 뒤 환경에 맞게 변수를 수정한다.

# ETC

- django 비밀번호 찾기 시 숨겨진 username을 변경해도 링크만 만료되고 다른 user의 비밀번호는 변경되지 않는 것을 확인
- class view에서는 reverse_lazy를 사용해야 한다.
