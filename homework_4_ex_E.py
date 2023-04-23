n = int(input())

topics = {}


current_message = 0

for i in range(n):
    num = int(input())
    if num == 0:
        topic = input()
        message = input()
        current_message += 1
        topics[topic] = []
        topics[topic].append(current_message)
    else:
        message = input()
        current_message += 1
        for key in topics:
            if num in topics[key]:
                topics[key].append(current_message)
                break


sorted_d = dict(sorted(topics.items(), key=lambda x: -len(x[1])))

for key in sorted_d:
    print(key)
    break
