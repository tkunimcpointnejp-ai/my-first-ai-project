from weather_advice import get_advice


def test_get_advice_cold_rainy_and_calm_wind():
    result = get_advice(5, True, 1)

    assert "かなり寒いです。厚手のコートを着ましょう。" in result
    assert "傘を忘れずに持っていきましょう！" in result
    assert "風はほぼありません。" in result


def test_get_advice_cool_not_rainy_light_wind():
    result = get_advice(15, False, 5)

    assert "少し肌寒いですね。ジャケットなどがおすすめです。" in result
    assert "傘は不要そうです。" in result
    assert "軽い風があります。" in result


def test_get_advice_comfortable_rainy_strong_wind():
    result = get_advice(24, True, 10)

    assert "過ごしやすい気温です。" in result
    assert "傘を忘れずに持っていきましょう！" in result
    assert "風が強めです。肌寒く感じるかもしれません。" in result


def test_get_advice_hot_not_rainy_very_strong_wind():
    result = get_advice(35, False, 16)

    assert "暑いです！熱中症に気をつけてください。" in result
    assert "傘は不要そうです。" in result
    assert "非常に強い風です。外出時は注意してください。" in result


def test_get_advice_boundary_values():
    assert "かなり寒いです。厚手のコートを着ましょう。" in get_advice(10, False, 2.9)
    assert "少し肌寒いですね。ジャケットなどがおすすめです。" in get_advice(11, False, 3)
    assert "過ごしやすい気温です。" in get_advice(21, False, 7.9)
    assert "暑いです！熱中症に気をつけてください。" in get_advice(29, False, 15)
