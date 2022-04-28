# install
IF not exist env (
  echo インストール中...
  python -m venv env
)

# update
echo アップデート中...
git pull origin main
env\Scripts\pip install -U -r requirements.txt
