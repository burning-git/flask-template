import requests
import json
import time

# 钉钉机器人显示
def sendDingdingMsg(message="wow数据同步完成"):

    # 更改为自己的钉钉机器人
    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=3060de9bd4dfc9b5f1523f04ca97490fc3189aa583889ccafe3562fa5356dc8a"

    # please set charset= utf-8
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    # 这里的message是你想要推送的文字消息
    stringBody = {
        "msgtype": "text",
        "text": {"content": "wowData:" + message},
        "at": {
            "atMobiles": [""],
            "isAtAll": "false"  # @所有人 时为true，上面的atMobiles就失效了
        }
    }
    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)



if __name__ == '__main__':
    sendDingdingMsg()


