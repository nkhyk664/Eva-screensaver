import datetime
import tkinter as tk

name1 = "到達予想時刻"
time1 = "2027/3/6, 19:04:27"
formatted_time1 = datetime.datetime.strptime(time1, "%Y/%m/%d, %H:%M:%S")

name2 = "到達予想時間"
time2 = "2027/3/6, 19:04"
formatted_time2 = datetime.datetime.strptime(time2, "%Y/%m/%d, %H:%M")

name3 = "日本標準時"


class Application(tk.Frame):
  def __init__(self, master):
    super().__init__(master)

    # ウィンドウ
    master.title("ヤシマ作戦風スクリーンセーバー")
    self.pack()

    # 「ヤシマ作戦」の文字
    self.kigou = tk.Label(self,
                      bg="black",
                      font=("ヒラギノ明朝 ProN", 80, "bold"),
                      text="第5使徒 襲来",
                      fg="#FFFFFF"
                    )
    self.kigou.grid(row=0,
                    sticky="w")

    # Aboutの文字
    self.About = tk.Label(self,
                      bg="black",
                      font=("", 30),
                      text="About",
                      fg="#FF9933"
                    )
    self.About.grid(row=1,
                    column=1,
                    padx=(0,200),
                    sticky="w"
                  )
    # 「到達予想時刻」の文字
    self.breach_time_string = tk.Label(self,
                                    bg="black",
                                    font=("ヒラギノ明朝 ProN", 70, "bold"),
                                    text=name1,
                                    fg="#FF9933"
                                  )
    self.breach_time_string.grid(row=2,
                                column=0,
                                padx=(0, 50),
                                sticky="w")
    # 「到達予想時刻」の7セグメントLED左側
    self.breach_time_seg1 = tk.Label(self,
                                  bg="black",
                                  font=("DSEG7 Classic", 60, "bold"),
                                  fg="#FF9933"
                                )
    self.breach_time_seg1.grid(row=2,
                              column=1,
                              sticky="w")
    # 「到達予想時刻」の7セグメントLED右側
    self.breach_time_seg2 = tk.Label(self,
                                  bg="black",
                                  font=("DSEG7 Classic", 60, "bold"),
                                  fg="#FF9933"
                                )
    self.breach_time_seg2.grid(row=2,
                              column=2,
                              padx=(0,300),
                              sticky="e"
                              )
    # 「到達予想時刻」の英語表記 "Estimated Time Breach"
    self.breach_time_en = tk.Label(self,
                                bg="black",
                                font=("", 30),
                                text="Estimated Time Breach",
                                fg="#FF9933"
                              )
    self.breach_time_en.grid(row=3,
                            column=0,
                            padx=(0, 120),
                            sticky="w"
                            )
    # 「到達予想時刻」のラベル"Day"
    self.breach_time_en_day = tk.Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Day",
                                    fg="#FF9933"
                                  )
    self.breach_time_en_day.grid(row=3,
                                column=1,
                                sticky="news"
                                )
    # 「到達予想時刻」のラベル"Time"
    self.breach_time_en_time = tk.Label(self,
                                    bg="black",
                                    font=("", 30),
                                    text="Time",
                                    fg="#FF9933"
                                  )
    self.breach_time_en_time.grid(row=3,
                                  column=2,
                                  sticky="news")

    # countdownの文字
    self.countdown = tk.Label(self,
                          bg="black",
                          font=("", 30),
                          text="Countdown",
                          fg="#FF9933"
                        )
    self.countdown.grid(row=4,
                        column=1,
                        padx=(0,200),
                        sticky="w")
    # 「到達予想時間」の文字
    self.remaining_time_string = tk.Label(self,
                                      bg="black",
                                      font=("ヒラギノ明朝 ProN", 70, "bold"),
                                      text=name2,
                                      fg="#FF9933"
                                    )
    self.remaining_time_string.grid(row=5,
                              column=0,
                              padx=(0, 50),
                              sticky="w")
    # 「到達予想時間」の7セグメントLED左側
    self.remaining_time_seg1 = tk.Label(self,
                                    bg="black",
                                    font=("DSEG7 Classic", 70, "bold"),
                                    fg="#FF9933"
                                  )
    self.remaining_time_seg1.grid(row=5,
                                  column=1,
                                  sticky="w")
    # 「到達予想時間」の7セグメントLED右側
    self.remaining_time_seg2 = tk.Label(self,
                                    bg="black",
                                    font=("DSEG7 Classic", 70, "bold"),
                                    fg="#FF9933"
                                  )
    self.remaining_time_seg2.grid(row=5,
                                  column=2,
                                  padx=(0,300),
                                  sticky="e")
    # 「到達予想時間」の英語表記 "Estimated Time Remaining"
    self.remaining_time_en = tk.Label(self,
                                  bg="black",
                                  font=("", 30),
                                  text="Estimated Time Remaining",
                                  fg="#FF9933"
                                )
    self.remaining_time_en.grid(row=6,
                                column=0,
                                padx=(0, 120),
                                sticky="w")
    # ラベル(Day)
    self.remaining_time_en_day = tk.Label(self,
                                      bg="black",
                                      font=("", 30),
                                      text="Day",
                                      fg="#FF9933"
                                    )
    self.remaining_time_en_day.grid(row=6,
                                    column=1,
                                    sticky="news")
    # ラベル(Time)
    self.remaining_time_en_time = tk.Label(self,
                                        bg="black",
                                        font=("", 30),
                                        text="Time",
                                        fg="#FF9933"
                                      )
    self.remaining_time_en_time.grid(row=6,
                                    column=2,
                                    sticky="news")

    # Liveの文字
    self.Live = tk.Label(self,
                      bg="black",
                      font=("", 30),
                      text="Live",
                      fg="#FF9933"
                    )
    self.Live.grid(row=7,
                  column=1,
                  padx=(0,200),
                  sticky="w")
    # 「日本標準時」の文字
    self.japan_std_time = tk.Label(self,
                                bg="black",
                                font=("ヒラギノ明朝 ProN", 70, "bold"),
                                text=name3,
                                fg="#FF9933"
                                )
    self.japan_std_time.grid(row=8,
                            column=0,
                            padx=(0, 120),
                            sticky="w"
                            )
    # 「日本標準時」の7セグメントLED左側
    self.japan_std_time_seg1 = tk.Label(self,
                                    bg="black",
                                    font=("DSEG7 Classic", 70, "bold"),
                                    fg="#FF9933")
    self.japan_std_time_seg1.grid(row=8,
                                  column=1,
                                  sticky="w")
    # 「日本標準時」の7セグメントLED右側
    self.japan_std_time_seg2 = tk.Label(self,
                                    bg="black",
                                    font=("DSEG7 Classic", 70, "bold"),
                                    fg="#FF9933"
                                    )
    self.japan_std_time_seg2.grid(row=8,
                                  column=2,
                                  padx=(0, 300),
                                  sticky="e"
                                  )
    # 「日本標準時」の英語表記 "Japan Standard Time"
    self.japan_std_time_en = tk.Label(self,
                                  bg="black",
                                  font=("", 30),
                                  text="Japan Standard Time",
                                  fg="#FF9933"
                                  )
    self.japan_std_time_en.grid(row=9,
                                column=0,
                                padx=(0, 120),
                                sticky="w"
                                )

    # update関数の呼び出し
    master.after(50, self.update)

  def update(self):
    # 現在時刻の取得
    today = datetime.datetime.now()

    # 到達予想時刻
    if today > formatted_time1:
      self.breach_time_seg1.configure(text="0")
      self.breach_time_seg2.configure(text="00:00:00")
    else:
      date_part = formatted_time1.strftime("%Y-%m-%d") #日付部分
      time_part = formatted_time1.strftime("%H:%M:%S") #時間部分
      self.breach_time_seg1.configure(text=date_part)
      self.breach_time_seg2.configure(text=time_part)

    # 到達予想時間
    if today > formatted_time2: # 期限到来時
      self.remaining_time_seg1.configure(text="0")
      self.remaining_time_seg2.configure(text="00:00:00.0")
    else:
      delta_days2 = formatted_time2 - today
      secs_time2 = int(delta_days2.total_seconds())
      # Days
      self.remaining_time_seg1.configure(text=delta_days2.days)
      # Time
      hour2 = (secs_time2 // 3600) % 24
      minute2 = (secs_time2 % 3600) // 60
      second2 = secs_time2 % 60
      tenth = delta_days2.microseconds // 100000
      self.remaining_time_seg2.configure(text=f"{hour2:02}:{minute2:02}:{second2:02}.{tenth}")
    # Live
    self.japan_std_time_seg1.configure(text=today.strftime("%m-%d"))
    self.japan_std_time_seg2.configure(text=today.strftime("%H:%M:%S"))
    # 0.01秒後に再表示
    self.master.after(10, self.update)

def main():
  root = tk.Tk()
  root.attributes("-fullscreen", True)
  # root.bind("<Escape>", lambda e: root.destroy())
  # root.bind("<Motion>", func=lambda x: root.destroy())
  # root.bind("<Key>", func=lambda x: root.destroy())
  app = Application(master=root)
  app.config(bg="black")
  app.mainloop()

if __name__ == "__main__":
  main()