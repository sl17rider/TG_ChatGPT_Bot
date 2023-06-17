import openai
from aiogram import Bot, Dispatcher, executor, types
from config import bot_token, openai_token


bot = Bot(token=bot_token)
dp = Dispatcher(bot)
openai.api_key = openai_token


@dp.message_handler()
async def send(message: types.Message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        await message.answer(response['choices'][0]['text'])
    except Exception as ex:
        await message.answer(f'Произошла ошибка:\n\n{ex}')


if __name__ == '__main__':
    executor.start_polling(dp)
