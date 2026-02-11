# お天気アドバイザープログラム（雨判定機能付き）

def get_advice(temperature, is_raining):
    """気温と雨の状況に応じてアドバイスを返す関数"""
    # まずは雨のチェック
    rain_msg = "傘を忘れずに持っていきましょう！" if is_raining else "傘は不要そうです。"
    
    # 次に気温のチェック
    if temperature <= 10:
        temp_msg = "かなり寒いです。厚手のコートを着ましょう。"
    elif 11 <= temperature <= 20:
        temp_msg = "少し肌寒いですね。ジャケットなどがおすすめです。"
    elif 21 <= temperature <= 28:
        temp_msg = "過ごしやすい気温です。"
    else:
        temp_msg = "暑いです！熱中症に気をつけてください。"
    
    return f"{temp_msg}\n{rain_msg}"

def main():
    print("--- パワーアップしたお天気アドバイザー ---")
    try:
        # 気温の入力
        temp_input = input("現在の気温（度）を入力してください: ")
        temp = float(temp_input)
        
        # 雨の入力（yかnで判定）
        rain_input = input("雨は降っていますか？ (y/n): ").lower()
        is_raining = (rain_input == 'y')
        
        # アドバイスを表示
        print("-" * 30)
        advice = get_advice(temp, is_raining)
        print(advice)
        print("-" * 30)
        
    except ValueError:
        print("エラー: 気温は数字で入力してください。")

if __name__ == "__main__":
    main()
