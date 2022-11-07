# Uptime Monitor

Website monitoring software.

## Technology used

### Backend

- Python3
- Django
- Django Rest Framework
- PostgreSql

### Frontend

- React
- Redux
- Material

Template based on [https://github.com/minimal-ui-kit/material-kit-react](https://github.com/minimal-ui-kit/material-kit-react)

## Demo

todo

## Development

### Without Docker

For local development without docker you need

- python 3.8 or newer
- postgresql server
- yarn

#### Backend

```
cd backend
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements/local.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Optionally, you may need to create an *.env* file in the backend folder to overwrite the environment variables used in *
config/settings.py*.

If everything went smoothly, open
[localhost:8000/api/v1/docs](localhost:8000/api/v1/docs)
in your browser.

#### Frontend

```
cd frontend
yarn install
yarn start
```

### With Docker

docker configuration will be available soon

## License

MIT License

Copyright (c) 2022 Piotr Grzelka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
