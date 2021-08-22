from vk_api import VkApi, exceptions
from vk_api.bot_longpoll import VkBotLongPoll

from data import config
from data.class_msg import Message, MessageSchema
from pprint import pprint
from marshmallow import EXCLUDE


def main():
# autorization by token of group bot 
	vk_session = VkApi(token=config.VK_TOKEN)
# call the longpool api
	longpoll = VkBotLongPoll(vk_session, config.VK_GROUP_ID)
# start session
	vk = vk_session.get_api()
# waiting for events
	for event in longpoll.listen():
		d = event.raw
		obj = d.get('object')
		print(obj)
		print(type(obj))
		sche = MessageSchema(unknown=EXCLUDE)
		mes = sche.load(obj)
		print(mes)


if __name__ == '__main__':
	main()
