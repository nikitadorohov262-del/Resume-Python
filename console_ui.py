import requests

while True:
   print("  ___МЕНЮ___  ")

   url = "https://lzebzysiovfimquwuxpx.supabase.co/auth/v1/token?grant_type=password"
   headers = {
       'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWJ6eXNpb3ZmaW1xdXd1eHB4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MTUxMzg1OSwiZXhwIjoyMTA3MDg5ODU5fQ.P759J4bOn2PPE52Pd74kO0PfWUFTR1ZtymEvLmQR6SM",
       "Content-Type": "application/json"}
   body = {"email": "nikitadorohov262@gmail.com", "password": "123321"}
   response = requests.request("POST", url, headers=headers, json=body)
   answer = response.json()

   url = "https://lzebzysiovfimquwuxpx.supabase.co/rest/v1/tasks"
   headers = {
       'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx6ZWJ6eXNpb3ZmaW1xdXd1eHB4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5MTUxMzg1OSwiZXhwIjoyMTA3MDg5ODU5fQ.P759J4bOn2PPE52Pd74kO0PfWUFTR1ZtymEvLmQR6SM",
       "Authorization": "Bearer " + answer["access_token"],
       "Content-Type": "application/json",
       'Prefer': 'return=representation'}
   response = requests.request("GET", url, headers=headers)
   anw = response.json()

   choice = input("1 - Посмотреть задачи. 2 - Добавить задачу. 0 - Выход: ")
   if choice == "1":
       a = len(anw)
       print("Список задача")
       for i in range(0, a):
           print(f"Задача №{i + 1}: ", anw[i]["title"],)
       print("\n")
   elif choice == "2":
       print("Создаю задачу...")

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

       print("Готово !\n")
   elif choice == "0":
       print("Завершаю работу...")
       break
   else:
       print("Неверный ввод, попробуйте еще раз!")