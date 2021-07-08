import time
from plyer import notification
if __name__=="__main__":
    while True:
     notification.notify(
        title="Please Drink Water Now!!",
        message = "Health experts commonly recommend to drink about 2 liters water a day.",
        app_icon= "D:\pyhon projects\water drink alert\GlassWater.ico ",
        timeout = 10
    )
     time.sleep(60*60)