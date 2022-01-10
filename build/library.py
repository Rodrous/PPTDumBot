from build.backEnd import getRandomLoadingMessage

async def loadingFunnyMessages(StartMsg: str = "Please wait,") -> str:
    loading_message_end = await getRandomLoadingMessage()
    return f"{StartMsg} {loading_message_end}..."
