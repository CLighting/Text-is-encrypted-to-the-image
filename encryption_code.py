# 读入图片
def read_img():
    import cv2
    path = input("原图路径： ")
    img = cv2.imread(path)
    return img, img.shape


# 映射
def word_to_num(shape):
    import json
    words = list(input("需要加密的话（支持中、英及混合）： "))
    assert (shape[0] * shape[1]) / 2 > len(words), 'picture is too small'
    with open('data/word_code.json') as f:
        word_code = json.load(f)
    nums_list = []
    for word in words:
        nums = word_code.get(word)
        nums_list.append(nums)

    return nums_list


# 加密
def write_to_img(nums_list, img):
    import numpy as np
    import cv2
    path = input("改写后图片存储路径： ")
    # 生成随机位置
    value_equal = True
    while value_equal:
        random_place_x = np.random.randint(0, img.shape[1], len(nums_list))
        random_place_y = np.random.randint(0, img.shape[0], len(nums_list))
        random_place = []
        for i in range(len(nums_list)):
            random_place.append([random_place_x[i], random_place_y[i]])
        # 按x大小排序
        random_place.sort(key=lambda x: x[0])
        count = 0
        for place in range(len(nums_list)):
            if place == 0:
                print(random_place[place][0], random_place[place][1])
            index_x = random_place[place][0]
            index_y = random_place[place][1]
            if (img[index_x][index_y] == np.array(nums_list[place])).all():
                break
            else:
                print('de', img[index_x][index_y])
                img[index_x][index_y] = np.array(nums_list[place])
                count += 1
                print("en", img[index_x][index_y])
        value_equal = False

    cv2.imwrite(path, img)


if __name__ == '__main__':
    print("===仅支持png图片格式===")
    img, shape = read_img()
    nums_list = word_to_num(shape)
    write_to_img(nums_list, img)
