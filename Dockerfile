FROM public.ecr.aws/lambda/python:3.8

COPY app/main.py ${LAMBDA_TASK_ROOT}/app.py

CMD [ "app.lambda_handler" ]