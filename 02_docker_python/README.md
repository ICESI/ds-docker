```
RUN useradd -ms /bin/bash python_user
USER python_user
WORKDIR /home/python_user
EXPOSE 8000
CMD ["python","simple_server.py"]
```
