import tkinter as tk

# 介面
root = tk.Tk()
root.title("交易預測")
root.geometry("400x300")
# root.iconbitmap('圖標.ico')  # 圖標


# 股票選擇單
stock_label = tk.Label(root, text="選擇股票:")
stock_label.place(x=50, y=50)

# 股票選擇下拉選單
stock_options = ["", "AMD", "NVIDIA", "TSMC", "INTEL"]
selected_stock = tk.StringVar()
selected_stock.set(stock_options[0])

stock_menu = tk.OptionMenu(root, selected_stock, *stock_options)
stock_menu.place(x=150, y=50, width=200)

# 變數
gap_prediction_label = tk.Label(root, text="隔日漲跌預測:")
gap_prediction_label.place(x=50, y=100)

# 開市預測標籤-變數
open_prediction_label = tk.Label(root, text="開市預測:")
open_prediction_label.place(x=50, y=150)

# 關市預測標籤-變數
close_prediction_label = tk.Label(root, text="關市預測:")
close_prediction_label.place(x=50, y=200)

# 結果顯示
gap_prediction_result = tk.Label(root, text="")
gap_prediction_result.place(x=150, y=100)

open_prediction_result = tk.Label(root, text="")
open_prediction_result.place(x=150, y=150)

close_prediction_result = tk.Label(root, text="")
close_prediction_result.place(x=150, y=200)

# 預測按鈕
def ai_trader():
    gap_prediction = 0.004
    open_prediction = 165
    close_prediction = 164
    stock = selected_stock.get()
    if stock == "":
        gap_prediction_result.config(text="請選擇股票")
        open_prediction_result.config(text="")
        close_prediction_result.config(text="")
    else:
        # 顯示預測結果
        gap_prediction_result.config(text=f"{gap_prediction}")
        open_prediction_result.config(text=f"{open_prediction}")
        close_prediction_result.config(text=f"{close_prediction}")

# 預測按鈕
ai_button = tk.Button(root, text="預測", width=10, command=ai_trader)
ai_button.place(x=300, y=100)

# 圓形按鈕 (AI交易員)
def ai_trader_circle():
    print("好啦你成功了沒白學")

# # AI交易員按鈕的背景
canvas = tk.Canvas(root, width=100, height=100)
canvas.place(x=300, y=150)

# AI交易員按鈕
circle = canvas.create_oval(10, 10, 90, 90, fill="lightgray")
canvas.create_text(50, 50, text="AI交易員")

# 使圓形成為按鈕，可悲綁定事件
canvas.tag_bind(circle, "<Button-1>", lambda event: ai_trader_circle())
canvas.tag_bind("AI交易員", "<Button-1>", lambda event: ai_trader_circle())

root.mainloop()
