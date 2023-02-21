# 导入ddddocr模块
import ddddocr

# 创建ddddocr实例
ocr = ddddocr.DdddOcr()
# 打开图片文件，读取图片内容
with open("local", 'rb')as f:
    img = f.read()
# 调用实例的classification方法，识别验证码
result = ocr.classification(img)
# 打印识别结果
print("验证码识别结果是：", result)
