# 读入图片
def read_img(pic):
    import cv2
    path = input(pic)
    img = cv2.imread(path)
    return img


# 解密
def decryption_img(unencrypted, encryption):
    import json
    values_List = []
    for i in range(unencrypted.shape[0]):
        for j in range(unencrypted.shape[1]):
            if not (unencrypted[i][j] == encryption[i][j]).all():
                values_List.append(list(encryption[i][j]))

    with open('data/word_code.json') as f:
        words_dict = json.load(f)

    true_words = []

    for word_value in values_List:
        if word_value[-1] == 0:
            true_words.append(list(words_dict.keys())[list(words_dict.values()).index(word_value)])
        else:
            utf_code = bytes([word_value[0]]) + bytes([word_value[1]]) + bytes([word_value[2]])
            word = utf_code.decode('utf-8')
            true_words.append(word)

    print("被加密的文字： ", "".join(true_words))


if __name__ == '__main__':
    un_img = read_img("原来的图片的路径：")
    en_img = read_img("需要解密的图片的路径：")
    decryption_img(un_img, en_img)
