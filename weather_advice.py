# お天気アドバイザープログラム

def get_advice(temperature):
    """気温に応じてアドバイスを返す関数"""
    if temperature <= 10:
        return "かなり寒いです。厚手のコートを着ましょう！"
    elif 11 <= temperature <= 20:
        return "少し肌寒いですね。ジャケットやカーディガンがあると安心です。"
    elif 21 <= temperature <= 28:
        return "過ごしやすい気温です。長袖シャツや半袖に薄手の上着でOK！"
    else:
        return "暑いです！半袖で過ごしましょう。水分補給も忘れずに。"

def main():
    print("--- お天気アドバイザーへようこそ ---")
    try:
        # ユーザーから気温を入力してもらう
        temp_input = input("現在の気温（度）を入力してください: ")
        temp = float(temp_input)
        
        # アドバイスを表示
        advice = get_advice(temp)
        print(f"アドバイス: {advice}")
        
    except ValueError:
        print("エラー: 数字を入力してくださいね。")

if __name__ == "__main__":
    main()
