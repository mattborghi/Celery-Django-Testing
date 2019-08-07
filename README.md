# Minimal Celery Configuration

Under ```minimal_celery/```, to initiate the pipenv environment:

```sh
> python -m pipenv shell
```

To install a new package:

```sh
> python -m pipenv install <package>
```

Run celery first by executing our program (```tasks.py```) with the worker argument:

```sh
> celery -A tasks worker -l info
```

or on Windows

```sh
> celery -A tasks worker -l info gevent
```

Then run the main python script:

```sh
> python main.py
```
