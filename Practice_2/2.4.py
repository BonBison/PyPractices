white_count = int(input("Введите количество пунктов «белого списка»: "))
white_list = []

for i in range(white_count):
    white_list.append(input().lower())

request_count = int(input("Введите количество запросов, которые нужно проанализировать: "))
request_list = []

for i in range(request_count):
    request_list.append(input().lower())

for request in request_list:

    if request in white_list:
        print("----------")
        print(request)