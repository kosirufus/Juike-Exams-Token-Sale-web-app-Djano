set -o errexit

pip install -r requirements.txt

python main/manage.py collectstatic --no-input

python manage.py migrate