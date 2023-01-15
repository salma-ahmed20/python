import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no= '+201003281895',
            message= msg,
            tab_close= True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print('message sent!')
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    send_whatsapp_message(msg="Hi Monicaaa ^_^")