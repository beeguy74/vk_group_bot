from environs import Env

env = Env()
env.read_env()

VK_TOKEN = env.str("VK_TOKEN")
VK_GROUP_ID = env.int("VK_GROUP_ID")
TG_URL = env.str("TG_BOT_TOKEN")
