import speedtest
import tkinter as tk
from tkinter import messagebox
import threading

def test_speed():
    # Disable the button for avoiding multiple clicks
    test_button.config(state=tk.DISABLED)
    result_text.set("Testing speed... Please wait.")

    def run_speed_test():
        try:
            st = speedtest.Speedtest()
            st.get_best_server()  # select best server

            download_speed = st.download() / 1_000_000  # converts download speed into Mbps
            upload_speed = st.upload() / 1_000_000  # converts upload speed into Mbps
            ping = st.results.ping  # display ping in ms

            result_text.set(f"Download Speed: {download_speed:.2f} Mbps\n"
                             f"Upload Speed: {upload_speed:.2f} Mbps\n"
                             f"Ping: {ping:.2f} ms")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to test speed.\n{e}")
        finally:
            # Re-enable the button 
            test_button.config(state=tk.NORMAL)

    # Start the speed test in a new thread
    threading.Thread(target=run_speed_test).start()

# GUI using Tkinter
root = tk.Tk()
root.title("Internet Speed Tester")
root.geometry("400x300")
root.resizable(True, True)

# Title Label
tk.Label(root, text="Internet Speed Tester", font=("Arial", 16, "bold")).pack(pady=10)

# Speed test button
test_button = tk.Button(root, text="Test Speed", font=("Arial", 12), command=test_speed)
test_button.pack(pady=10)

# Result Label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="center")
result_label.pack(pady=20)

# Run the tkinter in loop
root.mainloop()