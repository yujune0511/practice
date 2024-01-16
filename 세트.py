#집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 (java는 가능 python은 불가)
print(java - python)
print(java.difference(python))

#python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹음
java.remove("김태호")
print(java)