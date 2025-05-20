import threading
import voice
import controller

voice_thread = threading.Thread(target=voice.main)
controller_thread = threading.Thread(target=controller.main)

voice_thread.start()
controller_thread.start()

voice_thread.join()
controller_thread.join()