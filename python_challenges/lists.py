topic =["allgebra","compuetrscience",'ece','eee']

print(topic[-1])
print(f'my fav subject is {topic[1].upper()}.')


new_topic=topic.pop()

print("removing the topic "+ new_topic)

topic.append(input("enter a new_topic:"))
print(topic)