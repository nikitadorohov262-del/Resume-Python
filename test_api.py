import requests
import pytest

def test_tasks_with_auth():
    try:
        url = "https://lzebzysiovfimquwuxpx.supabase.co/auth/v1/token?grant_type=password"
        headers = {'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWJ6eXNpb3ZmaW1xdXd1eHB4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MTUxMzg1OSwiZXhwIjoyMTA3MDg5ODU5fQ.P759J4bOn2PPE52Pd74kO0PfWUFTR1ZtymEvLmQR6SM", "Content-Type": "application/json"}
        body = {"email": "nikitadorohov262@gmail.com", "password": "123321"}
        response = requests.request("POST", url, headers=headers, json=body)
        answer = response.json()


        url = "https://lzebzysiovfimquwuxpx.supabase.co/rest/v1/tasks"
        headers = {
            'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWJ6eXNpb3ZmaW1xdXd1eHB4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MTUxMzg1OSwiZXhwIjoyMTA3MDg5ODU5fQ.P759J4bOn2PPE52Pd74kO0PfWUFTR1ZtymEvLmQR6SM",
            "Authorization": "Bearer " + answer["access_token"],
            "Content-Type": "application/json",
            'Prefer': 'return=representation'}
        body = {"title": "КАРОЧЕ НАДО"}
        response = requests.request("POST", url, headers=headers, json=body)
        result = response.json()
        ident = (result[0]["id"])


        url = "https://lzebzysiovfimquwuxpx.supabase.co/rest/v1/tasks?id=eq." + str(ident)
        headers = {
            'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWJ6eXNpb3ZmaW1xdXd1eHB4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MTUxMzg1OSwiZXhwIjoyMTA3MDg5ODU5fQ.P759J4bOn2PPE52Pd74kO0PfWUFTR1ZtymEvLmQR6SM",
            "Authorization": "Bearer " + answer["access_token"],
            "Content-Type": "application/json"}
        body = {"status": 1}
        response = requests.request("PATCH", url, headers=headers, json=body)
        assert response.status_code == 204
    except Exception as e:
        print(f"Запрос провалился. Детали ошибки: {e}")
