import asyncio
from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND
import signal, time

notifier = DesktopNotifier(app_name="H2O Clock 🐳🚰")

async def main(i):
    await notifier.send(title="Aqua levels decreasing 💧",
                        message=f"Did you drink {i+1} glass of water today?",
                        urgency=Urgency.Critical,
                        buttons=[
                            Button(
                                title="Mark as read",
                                on_pressed=lambda: print("Marked as read"),
                            )
                        ],
                        # reply_field=ReplyField(
                        #     on_replied=lambda text: print("Brutus replied:", text),
                        # ),
                        on_dispatched=lambda: print("Notification showing"),
                        # on_clicked=lambda: print("Notification clicked"),
                        # on_dismissed=lambda: print("Notification dismissed"),
                        sound=DEFAULT_SOUND)
    
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, stop_event.set)
    loop.add_signal_handler(signal.SIGTERM, stop_event.set)

    await stop_event.wait()

for i in range(6):
    asyncio.run(main(0))
    time.sleep(i*120)