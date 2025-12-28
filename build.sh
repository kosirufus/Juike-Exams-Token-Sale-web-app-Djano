set -o errexit

pip install -r requirements.txt

python backend/main/manage.py collectstatic --no-input

python backend/main/manage.py migrate