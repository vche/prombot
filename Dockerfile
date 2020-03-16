FROM python:3

ADD prombot /prombot
ADD setup.py /

RUN pip install virtualenv
RUN virtualenv /pyvenv

# Install dependencies:
WORKDIR /
RUN /pyvenv/bin/pip install -e .

# Run the application:
CMD ["/pyvenv/bin/prombot"]

EXPOSE 9087
