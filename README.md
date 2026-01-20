# 30分 Vibe Coding チャレンジ - TODO App

Streamlit を使った TODO アプリのスターターコードです。

## プロジェクトのダウンロード

```bash
git clone https://github.com/kengirie/streamlit-startercode.git
cd streamlit-startercode
```

※ または ZIP でダウンロードして解凍してください。

## 前提条件

- Python がインストールされていること

```bash
python --version
```

上記コマンドでバージョンが表示されればOKです。

## 環境構築

### 1. 仮想環境の作成

```bash
python -m venv venv
```

### 2. 仮想環境の有効化

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. 依存パッケージのインストール

```bash
pip install streamlit
```

### 4. アプリの起動

```bash
streamlit run app.py
```

初回起動時に以下のメッセージが表示されますが、何も入力せず Enter を押してスキップしてください：

```text
Welcome to Streamlit!
Email:
```

ブラウザが自動で開き、`http://localhost:8501` でアプリが表示されます。

## 現在の機能

- タスクの追加
- タスク一覧の表示

## チャレンジのヒント

30分で以下の機能を追加してみましょう：

- [ ] タスクの完了/未完了の切り替え
- [ ] タスクの削除
- [ ] 完了済みタスクのフィルタリング
- [ ] タスクの編集機能
- [ ] データの永続化（ファイル保存など）

Happy Coding!
