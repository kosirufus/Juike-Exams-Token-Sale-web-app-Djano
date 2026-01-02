set -o errexit

pip install -r requirements.txt

python main/manage.py collectstatic --no-input

python main/manage.py migrate