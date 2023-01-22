import time
import json
import requests

def send_ding_msg(msg):
    # 请求的URL，WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=8d3a0cac0bb37ec689e2333ae099561f7f8d3f6ffd42843d2b54475ff96ed254  '
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "isAtAll": False
        }
    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)

    # 发送请求
    info = requests.post(url=webhook, data=message_json.encode("utf-8"), headers=header)
    # 打印返回的结果


if __name__=="__main__":
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    msg_info = "IEMD 1234567890 "
    msg_info = f"warn: {localtime} 有异常需要处理：\n".format(localtime) + msg_info         
    send_ding_msg(msg_info)   
    





