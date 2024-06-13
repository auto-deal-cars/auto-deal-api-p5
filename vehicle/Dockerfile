FROM public.ecr.aws/lambda/python:3.9

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . /var/task/

CMD ["adapters.controllers.create_vehicle_controller.register_vehicle"]
