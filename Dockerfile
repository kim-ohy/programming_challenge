FROM python:3.13
WORKDIR /app
ADD output.txt /app
ADD challenge_b.py /app
CMD ["python3", "challenge_b.py", "output.txt"]