import pyttsx3
import io
import sys

engine = pyttsx3.init()

# 获取语音包
voices = engine.getProperty('voices')
for voice in voices:
    print('id = {}\tname = {} \n'.format(voice.id, voice.name))
# 设置使用的语音包
# engine.setProperty('voice', 'zh')  # 开启支持中文
engine.setProperty('voice', voices[0].id)

# 改变语速  范围为0-200   默认值为200
rate = engine.getProperty('rate')  # 获取当前语速
engine.setProperty('rate', rate - 70)

# 设置音量  范围为0.0-1.0  默认值为1.0
engine.setProperty('volume', 0.7)

engine.save_to_file('', 'output.mp3')
engine.runAndWait()
# 朗读
# engine.runAndWait()