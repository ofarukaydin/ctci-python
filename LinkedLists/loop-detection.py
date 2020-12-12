def loop_detection(list):
    hashMap = set()
    for item in list:
        if item in hashMap:
            return item
        hashMap.add(item)
