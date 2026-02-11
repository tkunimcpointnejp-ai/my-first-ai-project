# お天気アドバイザープログラム（雨判定機能付き）

def get_advice(temperature, is_raining, wind_speed):
    """気温、雨の状況、風速に応じてアドバイスを返す関数"""
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
    
    # 風速のチェック
    if wind_speed < 3:
        wind_msg = "風はほぼありません。"
    elif 3 <= wind_speed < 8:
        wind_msg = "軽い風があります。"
    elif 8 <= wind_speed < 15:
        wind_msg = "風が強めです。肌寒く感じるかもしれません。"
    else:
        wind_msg = "非常に強い風です。外出時は注意してください。"
    
    return f"{temp_msg}\n{rain_msg}\n{wind_msg}"

def main():
    print("--- パワーアップしたお天気アドバイザー ---")
    try:
        # 気温の入力
        temp_input = input("現在の気温（度）を入力してください: ")
        temp = float(temp_input)
        
        # 雨の入力（yかnで判定）
        rain_input = input("雨は降っていますか？ (y/n): ").lower()
        is_raining = (rain_input == 'y')
        
        # 風速の入力
        wind_input = input("風速（m/s）を入力してください: ")
        wind_speed = float(wind_input)
        
        # アドバイスを表示
        print("-" * 30)
        advice = get_advice(temp, is_raining, wind_speed)
        print(advice)
        print("-" * 30)
        
    except ValueError:
        print("エラー: 気温と風速は数字で入力してください。")

if __name__ == "__main__":
    main()
