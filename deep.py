import os
import cv2
import telebot
from main import maini
import multiprocessing

#async def long_function(img,fin):
  #main.maini(img, fin)

api = '6230585529:AAGNno0R7iS5vhNUdoKo4OnwZ0uSUhDYjpI'
deep = telebot.TeleBot(api)

@deep.message_handler(content_types=['photo'])
def photo_message(message):
  send = deep.send_message(message.chat.id, "загрузка...\nбот начинает снимать одежду, это займёт от 2 до 10 минут\nэто не самая лучшая версия бота по этому он и бесплатный\nнадеюсь что вы прислали хороший снимок\nВНИМАНИЕ ЕСЛИ ИЗОБРАЖЕНИЕ ВЫШЛО НЕ ХОРОШЕМ ТО ПОПРОБУЙТЕ СНОВА... ЕСЛИ ЭТО НЕ 1 ВАША ПОПЫТКА ОБРАТИТЕСЬ К ПОДДЕРЖКЕ")
  file_info = deep.get_file(message.photo[len(message.photo) - 1].file_id)
  downloaded_file = deep.download_file(file_info.file_path)
  src = "photo" + message.photo[1].file_id + ".png"
  with open(src, 'wb') as new_file:
    new_file.write(downloaded_file)
  # Load an image
  img = cv2.imread(src)
  # Get the current dimensions of the image
  height, width, _ = img.shape
  # Determine the ratio of the new height to the old height
  ratio = 512 / height
  # Calculate the new dimensions of the image
  new_height = round(height * ratio)
  new_width = round(width * ratio)
  # Resize the image
  resized_img = cv2.resize(img, (new_width, new_height))
  # Add padding to the image to make it 512x512
  h_diff = 512 - new_height
  w_diff = 512 - new_width
  top = h_diff // 2
  bottom = h_diff - top
  left = w_diff // 2
  right = w_diff - left
  padded_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right, cv2.BORDER_CONSTANT)
  # Save the edited image
  cv2.imwrite(f"input{src}.png", padded_img)
  os.remove(src)
  r(message, src)
def r(message,src):
  print("good")
  process = multiprocessing.Process(target=maini(img=f"input{src}.png"))
  process.start()
  process.join()
  os.remove(f"input{src}.png")
  with open(f"output{src}", 'wb') as f:
    deep.send_photo(message.chat.id,f)
  os.remove(f"output{src}")


if __name__ == '__main__':
  deep.infinity_polling(none_stop=True)




