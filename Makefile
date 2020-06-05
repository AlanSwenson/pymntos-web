run-frontend:
	cd frontend && npm run dev
run-argon-frontend:
	yarn serve
run-backend:
	flask run --port 3000
build:
	cd frontend && npm run build