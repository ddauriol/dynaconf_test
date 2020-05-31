## Test DYNACONF .toml and .yaml
### Files
  
settings.yaml  
```yaml
default:
  DATABASES:
    default:
      ENGINE: ""
      NAME: "NAME"
      USER: postgres
      PASSWORD:
      HOST:
      PORT: PORT

```
  
.secrets.yaml  
```yaml
default:
  SECRET_KEY: t_21su#f56q3u15je6dsi5!jhxhz6#l*cbgr7%efk^$$@e)%zl

  DATABASES:
    default:
      ENGINE: ENGINE
      NAME: NAME
      PASSWORD: PASS
      HOST: HOST

```
  
settings.toml  
```toml
[default]
DATABASES__default__ENGINE=""
DATABASES__default__NAME= "NAME"
DATABASES__default__USER="USER"
DATABASES__default__PASSWORD= ""
DATABASES__default__HOST=""
DATABASES__default__PORT= "PORT"

```
  
.secrets.toml  
```toml
[default]
SECRET_KEY = "t_21su#f56q3u15je6dsi5!jhxhz6#l*cbgr7%efk^$$@e)%zl"

DATABASES__default__ENGINE="ENGINE"
DATABASES__default__NAME="NAME"
DATABASES__default__PASSWORD="PASS"
DATABASES__default__HOST="HOST"
  
```
## Test
.secrets.yaml and settings.yaml
```bash
-rw-r--r-- 1 ddauriol 197121  203 May 31 09:38 .secrets.yaml
-rw-r--r-- 1 ddauriol 197121  220 May 31 09:38 _.secrets.toml
-rw-r--r-- 1 ddauriol 197121  216 May 31 09:38 _settings.toml
-rw-r--r-- 1 ddauriol 197121  146 May 31 09:38 settings.yaml

Working in development environment 
DATABASES: {'default': {'ENGINE': 'ENGINE',
             'HOST': 'HOST',
             'NAME': 'NAME',
             'PASSWORD': 'PASS'}}
SECRET_KEY: 't_21su#f56q3u15je6dsi5!jhxhz6#l*cbgr7%efk^$$@e)%zl'
```
`Returned only .secrets.yaml contents`
  
.secrets.toml and settings.toml
```bash
ls -la
-rw-r--r-- 1 ddauriol 197121  220 May 31 09:36 .secrets.toml
-rw-r--r-- 1 ddauriol 197121  203 May 31 09:35 _.secrets.yaml
-rw-r--r-- 1 ddauriol 197121  146 May 31 09:35 _settings.yaml
-rw-r--r-- 1 ddauriol 197121  216 May 31 09:36 settings.toml
  
Working in development environment 
DATABASES: {'default': {'ENGINE': 'ENGINE',
             'HOST': '',
             'NAME': 'NAME',
             'PASSWORD': '',
             'PORT': 'PORT',
             'USER': 'USER'}}
```
`Returned only settings.toml contents`

.secrets.yaml and settings.toml
```bash
ls -la
-rw-r--r-- 1 ddauriol 197121  203 May 31 09:38 .secrets.yaml
-rw-r--r-- 1 ddauriol 197121  220 May 31 09:38 _.secrets.toml
-rw-r--r-- 1 ddauriol 197121  146 May 31 09:40 _settings.yaml
-rw-r--r-- 1 ddauriol 197121  216 May 31 09:40 settings.toml

Working in development environment 
DATABASES: {'default': {'ENGINE': 'ENGINE',
             'HOST': 'HOST',
             'NAME': 'NAME',
             'PASSWORD': 'PASS'}}
SECRET_KEY: 't_21su#f56q3u15je6dsi5!jhxhz6#l*cbgr7%efk^$$@e)%zl'
```
`Returned only .secrets.yaml contents`

.secrets.toml and settings.yaml
```bash
ls -la
-rw-r--r-- 1 ddauriol 197121  220 May 31 09:41 .secrets.toml
-rw-r--r-- 1 ddauriol 197121  203 May 31 09:41 _.secrets.yaml
-rw-r--r-- 1 ddauriol 197121  216 May 31 09:41 _settings.toml
-rw-r--r-- 1 ddauriol 197121  146 May 31 09:41 settings.yaml
  
Working in development environment 
DATABASES: {'default': {'ENGINE': '',
             'HOST': None,
             'NAME': 'NAME',
             'PASSWORD': None,
             'PORT': 'PORT',
             'USER': 'postgres'}}
```
` Returned only settings.toml contents`
___
Test valideted TOMl format
  
settings.toml
```toml
[DATABASES]
[DATABASES.default]
ENGINE=""
NAME= "NAME"
USER="USER"
PASSWORD= ""
HOST=""
PORT= "PORT"
```
  
.secrets.toml
```toml
[DATABASES]
[DATABASES.default]
ENGINE="ENGINE"
PASSWORD= "PASS"
HOST="HOST"
```
  
```bash
-rw-r--r-- 1 ddauriol 197121  107 May 31 10:00 .secrets.toml
-rw-r--r-- 1 ddauriol 197121  209 May 31 09:55 _.secrets.toml
-rw-r--r-- 1 ddauriol 197121  186 May 31 10:00 _.secrets.yaml
-rw-r--r-- 1 ddauriol 197121  204 May 31 09:53 _settings.toml
-rw-r--r-- 1 ddauriol 197121  146 May 31 10:00 _settings.yaml
-rw-r--r-- 1 ddauriol 197121   80 May 31 10:00 settings.toml
  
Working in development environment 
  
```
  
`Returned nothing`

___
```toml
[tool.poetry.dependencies]
python = "^3.8"
dynaconf = {extras = ["yaml"], version = "^2.2.3"}

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```