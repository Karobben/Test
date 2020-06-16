#!/usr/bin/env python3

import asyncio, sys

from blivedm import BLiveClient

class MyBLiveClient(BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = BLiveClient._COMMAND_HANDLERS.copy()
    _COMMAND_HANDLERS['SEND_GIFT'] = lambda client, command: client._my_on_gift(
        command['data']['giftName'], command['data']['num'], command['data']['uname'],
        command['data']['coin_type'], command['data']['total_coin']
    )
    #
    async def _on_get_popularity(self, popularity):
        A= f'人气：{popularity}'
        F= open(sys.path[0] +'/tmp.int','w')
        F.write(A+"\n")
        F.close()
    async def _on_get_danmaku(self, content, user_name):
        B = f'{user_name}：{content}'
        F2= open(sys.path[0] +'/tmp.msg','a')
        F2.write(B+"\n")
        F2.close()

    async def _my_on_gift(self, gift_name, gift_num, user_name, coin_type, total_coin):
        C = f'{user_name} 赠送{gift_name}x{gift_num} （{coin_type}币x{total_coin}）'
        F3= open(sys.path[0] +'/tmp.msg','a')
        F3.write(C+"\n")
        F3.close()

async def async_main():
    # 139是黑桐谷歌的直播间
    # 如果SSL验证失败就把第二个参数设为False
    client = MyBLiveClient(21154895, True)
    future = client.run()
    try:
        # 5秒后停止，测试用
        # await asyncio.sleep(5)
        # future.cancel()
        await future
    finally:
        await client.close()


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(async_main())
    finally:
        loop.close()


if __name__ == '__main__':
    main()
