# AI学習プロジェクト

## 概要
このリポジトリは、AI（GeminiやGitHub Copilotなど）を活用して、プログラミングスキルを習得していくための学習記録です。

## 決意表明
「AIを最高のパートナーとして、創造したいものを形にできるエンジニアを目指します！」

## 学習ロードマップ
- [ ] ステップ1：GitHubの基本操作をマスターする ← **現在ここ！**
- [ ] ステップ2：AIと協力して小さなアプリを作る
- [ ] ステップ3：GitHub Pagesでプロジェクトを公開する

## 作成したアプリ: 地域別 気温グラフ
地域と期間を指定すると、日ごとの最高気温・最低気温をグラフ表示するStreamlitアプリです。

### 実行方法
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### デプロイ（Docker）
1. イメージをビルド:
```bash
docker build -t my-first-ai-project:latest .
```
2. コンテナを起動:
```bash
docker run -p 8501:8501 my-first-ai-project:latest
```

### デプロイ（Streamlit Community Cloud）
1. GitHub にプッシュします。
2. Streamlit Community Cloud にリポジトリを接続します。
3. ビルドコマンドは通常不要です。`requirements.txt` を参照してインストールされます。

#### 注意
- PaaS（例: Heroku）へデプロイする場合は `Procfile` を利用してください。
- セキュリティ上の理由から、APIキー等の機密情報は環境変数で管理してください。
