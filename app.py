# app.py
import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="TODO App", page_icon="✅", layout="centered")

# ===================
# session_state 初期化
# ===================
if "todos" not in st.session_state:
    st.session_state.todos = []

# ===================
# メイン画面
# ===================
st.title("✅ TODO App")

# --- TODO追加フォーム ---
with st.form("add_todo", clear_on_submit=True):
    new_task = st.text_input("新しいタスク")
    submitted = st.form_submit_button("追加")

    if submitted and new_task:
        st.session_state.todos.append(
            {"task": new_task, "done": False, "created_at": datetime.now()}
        )
        st.rerun()

# --- TODO一覧表示 ---
st.subheader(f"📋 タスク一覧（{len(st.session_state.todos)}件）")

if not st.session_state.todos:
    st.info("タスクがありません。上のフォームから追加してください。")
else:
    for i, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{'✅' if todo['done'] else '⬜'} {todo['task']}")
        with col2:
            # ここに完了/削除ボタンを追加していく
            pass
