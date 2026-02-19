from datetime import date, timedelta
import math

import pandas as pd
import requests
import streamlit as st

ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
PREFECTURES = [
    "北海道",
    "青森県",
    "岩手県",
    "宮城県",
    "秋田県",
    "山形県",
    "福島県",
    "茨城県",
    "栃木県",
    "群馬県",
    "埼玉県",
    "千葉県",
    "東京都",
    "神奈川県",
    "新潟県",
    "富山県",
    "石川県",
    "福井県",
    "山梨県",
    "長野県",
    "岐阜県",
    "静岡県",
    "愛知県",
    "三重県",
    "滋賀県",
    "京都府",
    "大阪府",
    "兵庫県",
    "奈良県",
    "和歌山県",
    "鳥取県",
    "島根県",
    "岡山県",
    "広島県",
    "山口県",
    "徳島県",
    "香川県",
    "愛媛県",
    "高知県",
    "福岡県",
    "佐賀県",
    "長崎県",
    "熊本県",
    "大分県",
    "宮崎県",
    "鹿児島県",
    "沖縄県",
]
PREFECTURE_COORDS = {
    "北海道": (43.0642, 141.3469),
    "青森県": (40.8244, 140.7400),
    "岩手県": (39.7036, 141.1527),
    "宮城県": (38.2688, 140.8721),
    "秋田県": (39.7186, 140.1024),
    "山形県": (38.2404, 140.3633),
    "福島県": (37.7503, 140.4675),
    "茨城県": (36.3418, 140.4468),
    "栃木県": (36.5658, 139.8836),
    "群馬県": (36.3911, 139.0608),
    "埼玉県": (35.8569, 139.6489),
    "千葉県": (35.6046, 140.1233),
    "東京都": (35.6895, 139.6917),
    "神奈川県": (35.4478, 139.6425),
    "新潟県": (37.9026, 139.0232),
    "富山県": (36.6953, 137.2113),
    "石川県": (36.5947, 136.6256),
    "福井県": (36.0652, 136.2216),
    "山梨県": (35.6642, 138.5684),
    "長野県": (36.6513, 138.1810),
    "岐阜県": (35.3911, 136.7222),
    "静岡県": (34.9769, 138.3831),
    "愛知県": (35.1802, 136.9066),
    "三重県": (34.7303, 136.5086),
    "滋賀県": (35.0045, 135.8686),
    "京都府": (35.0116, 135.7681),
    "大阪府": (34.6937, 135.5023),
    "兵庫県": (34.6913, 135.1830),
    "奈良県": (34.6851, 135.8048),
    "和歌山県": (34.2260, 135.1675),
    "鳥取県": (35.5039, 134.2383),
    "島根県": (35.4723, 133.0505),
    "岡山県": (34.6618, 133.9350),
    "広島県": (34.3853, 132.4553),
    "山口県": (34.1858, 131.4714),
    "徳島県": (34.0658, 134.5593),
    "香川県": (34.3401, 134.0434),
    "愛媛県": (33.8416, 132.7657),
    "高知県": (33.5597, 133.5311),
    "福岡県": (33.5902, 130.4017),
    "佐賀県": (33.2494, 130.2988),
    "長崎県": (32.7503, 129.8777),
    "熊本県": (32.8031, 130.7079),
    "大分県": (33.2382, 131.6126),
    "宮崎県": (31.9111, 131.4239),
    "鹿児島県": (31.5602, 130.5581),
    "沖縄県": (26.2124, 127.6809),
}


def fetch_daily_temperatures(base_url: str, lat: float, lon: float, start: date, end: date) -> list[dict]:
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
    }
    response = requests.get(base_url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json().get("daily", {})

    times = data.get("time") or []
    max_temps = data.get("temperature_2m_max") or []
    min_temps = data.get("temperature_2m_min") or []
    return [
        {"date": t, "max_temp": max_temp, "min_temp": min_temp}
        for t, max_temp, min_temp in zip(times, max_temps, min_temps)
    ]


def fetch_temperature_range(lat: float, lon: float, start: date, end: date) -> list[dict]:
    today = date.today()
    rows: list[dict] = []

    if start <= today:
        archive_end = min(end, today)
        rows.extend(fetch_daily_temperatures(ARCHIVE_URL, lat, lon, start, archive_end))

    if end > today:
        forecast_start = max(start, today + timedelta(days=1))
        rows.extend(fetch_daily_temperatures(FORECAST_URL, lat, lon, forecast_start, end))

    return sorted(rows, key=lambda x: x["date"])


def build_sample_temperatures(lat: float, start: date, end: date) -> list[dict]:
    days = (end - start).days + 1
    rows: list[dict] = []
    for i in range(days):
        current = start + timedelta(days=i)
        day_of_year = current.timetuple().tm_yday
        seasonal = 15 + 10 * math.sin((2 * math.pi * (day_of_year - 80)) / 365)
        lat_adjust = (36.0 - lat) * 0.6
        weekly = 1.8 * math.sin((2 * math.pi * i) / 7)
        max_temp = round(seasonal + lat_adjust + 4.0 + weekly, 1)
        min_temp = round(seasonal + lat_adjust - 4.0 + weekly * 0.8, 1)
        rows.append(
            {"date": current.isoformat(), "max_temp": max_temp, "min_temp": min_temp}
        )
    return rows


st.set_page_config(page_title="地域別 気温グラフ", page_icon="🌡️")
st.title("🌡️ 地域別 気温グラフ")
st.write("地域と期間を指定すると、日ごとの最高/最低気温を表示します。")

with st.form("temp_graph_form"):
    prefecture = st.selectbox("都道府県", PREFECTURES, index=12)
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("開始日", value=date.today() - timedelta(days=7))
    with col2:
        end_date = st.date_input("終了日", value=date.today())
    submitted = st.form_submit_button("グラフを表示")

if submitted:
    if start_date > end_date:
        st.error("開始日は終了日以前を指定してください。")
    else:
        lat, lon = PREFECTURE_COORDS[prefecture]
        data_source = "Open-Meteo"
        is_sample_data = False
        try:
            rows = fetch_temperature_range(lat, lon, start_date, end_date)
            if not rows:
                raise ValueError("指定期間の気温データを取得できませんでした。")
        except requests.RequestException as err:
            rows = build_sample_temperatures(lat, start_date, end_date)
            data_source = "サンプルデータ（オフライン）"
            is_sample_data = True
            st.warning(
                "天気APIに接続できないため、サンプルデータを表示しています。"
                f"（{type(err).__name__}）"
            )
        except ValueError as err:
            st.error(str(err))
            rows = []

        if rows:
            if is_sample_data:
                st.error("データ取得状態: サンプルデータ表示中（API接続失敗）")
            else:
                st.success("データ取得状態: API取得成功（実測/予報データ）")
            st.info(f"{prefecture} の気温を表示しています。データ元: {data_source}")
            df = pd.DataFrame(rows)
            st.line_chart(df, x="date", y=["max_temp", "min_temp"])
            st.dataframe(
                df.rename(
                    columns={
                        "date": "日付",
                        "max_temp": "最高気温(℃)",
                        "min_temp": "最低気温(℃)",
                    }
                ),
                use_container_width=True,
            )
