prov:
	@ansible-playbook devops/finish.yml -i devops/development --connection=local

run:
	@python manage.py runserver 0.0.0.0:3000 --settings=settings.development &
	@echo "running"