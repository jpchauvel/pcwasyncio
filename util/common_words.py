import aiofiles


async def load_common_words() -> list[str]:
    async with aiofiles.open("common_words.txt", mode="r") as fd:
        common_words: list[str] = await fd.readlines()
    return common_words
