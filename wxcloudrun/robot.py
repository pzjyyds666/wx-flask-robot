import werobot
print('load robot.py')

robot = werobot.WeRoBot(
    token='test_token',# 对应公众号的token设置
#     encoding_aes_key='xxxxxx',# 明文传输不需要填写
#     app_id='xxxxx'#明文传输不需要填写
)


@robot.handler
def handel_reply(message):
    return 'received'