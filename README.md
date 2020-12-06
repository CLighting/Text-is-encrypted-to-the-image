# Text-is-encrypted-to-the-image
把文字加密到图片中，如果没有相同的图片，就无法破解图片里的文字
仅支持png格式存储，jpg会造成图片压缩，导致无法解密。


make_chinese_list.py
把网上拷贝来的常用汉字（GB2312），以utf-8形式存储，并存一份json文件方便解密

encryption_code.py
加密过程，文字长度不能长于图片 长x宽/2的大小

decryption_code.py
解码过程
