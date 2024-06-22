FROM python:3.11.0-slim-bullseye

WORKDIR /api
ADD ./api ./api
ADD ./prisma ./prisma

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && prisma generate

EXPOSE 80 443 6379 8080
EXPOSE 8000

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["prisma db push --schema prisma/schema.prisma && uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload --use-colors --log-level debug"]