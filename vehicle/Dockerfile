FROM public.ecr.aws/lambda/python:3.10

COPY ./requirements.txt ./
COPY ./adapters ${LAMBDA_TASK_ROOT}/vehicle/adapters
COPY ./domain ${LAMBDA_TASK_ROOT}/vehicle/domain
COPY ./application ${LAMBDA_TASK_ROOT}/vehicle/application
COPY ./infrastructure ${LAMBDA_TASK_ROOT}/vehicle/infrastructure
COPY ./exceptions ${LAMBDA_TASK_ROOT}/vehicle/exceptions
COPY ./__init__.py ${LAMBDA_TASK_ROOT}/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["vehicle.adapters.controllers.create_vehicle_controller.register_vehicle"]
