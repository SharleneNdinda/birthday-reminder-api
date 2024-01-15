<div id="top"></div>
<div align="center">

  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
</div>

<br />
<div align="center">
  <a href="">
    <img src="images/hero.png" alt="Logo" width="256" height="256">
  </a>

<h3 align="center">Birthday Reminder API</h3>

  <p align="center">
    <a href="">Report Bug</a>
    ·
    <a href="">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>

  </ol>
</details>

## About The Project

### Built With

* [Django](https://www.django.com/)
* [Celery]()


<p align="right">(<a href="#top">back to top</a>)</p>


### 🚀 Getting Started

1. Clone repository and setup virtual environment. Install all project requirements.
```sh
  $ pip install -r requirements/base.txt
```

2. Setup Postgres on your local machine and run migrations.
```sh
  $ python manage.py migrate
```

3. Run development server.
```sh
  $ python manage.py runserver
```


<p align="right">(<a href="#top">back to top</a>)</p>

## 💯 Usage

### 🔑 Authentication 

birthday-reminder api uses JWT as the primary form of authentication. 
The endpoints provided for obtaining a token and refreshing a token are:
```sh
$ /api/token
$ /api/token/refresh
```