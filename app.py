import streamlit as st

# アプリのタイトルと説明
st.set_page_config(page_title="お天気アドバイザー", page_icon="🌤️")
st.title("🌤️ お天気アドバイザー")
st.write("今の気温と天気を教えてください。最適な服装をアドバイスします。")

# --- 入力エリア（サイドバーまたはメイン画面） ---
st.divider() # 区切り線

# 気温をスライダーで設定（範囲: -10度〜40度、初期値: 20度）
temperature = st.slider("現在の気温（度）を選択してください", -10, 40, 20)

# 雨の状況をチェックボックスで確認
is_raining = st.checkbox("雨は降っていますか？")

# --- アドバイスのロジック ---
def get_advice(temp, rain):
    # 気温のアドバイス
    if temp <= 10:
        t_msg = "🥶 **かなり寒いです。** 厚手のコートやマフラーを準備しましょう。"
    elif 11 <= temp <= 20:
        t_msg = "🧥 **少し肌寒いですね。** ジャケットやカーディガンがおすすめです。"
    elif 21 <= temp <= 28:
        t_msg = "👕 **過ごしやすい気温です。** 長袖シャツや半袖に薄手の上着でOK！"
    else:
        t_msg = "☀️ **暑いです！** 半袖で過ごしましょう。水分補給も忘れずに。"
    
    # 雨のアドバイス
    r_msg = "☔ **傘を忘れずに！**" if rain else "☁️ 傘は持たなくて良さそうです。"
    
    return t_msg, r_msg

# --- 判定ボタンと結果表示 ---
if st.button("アドバイスをもらう"):
    t_advice, r_advice = get_advice(temperature, is_raining)
    
    # 綺麗な枠（Success/Info）で表示
    st.subheader("💡 本日のコーディネート案")
    st.info(t_advice)
    st.success(r_advice)
else:
    st.write("上のボタンを押すと、結果が表示されます。")