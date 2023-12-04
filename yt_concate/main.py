from yt_concate.steps.get_video_list import GetVideoList
from yt_concate.steps.step import StepException
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

steps = [
    GetVideoList(),
]
for step in steps:
    try:
        step.process()
    except StepException as e:
        print("Exception happen:", e)
        break
