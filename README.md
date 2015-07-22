# xl_sol

## Windows用クライアントアプリ

* Excel を読み込んでWebアプリにデータを登録
* Webアプリには REST API がある前提（今回は Django REST Frameworkで開発されていて、認証に Token Authenticationを利用されている前提）
* 汎用性を持った作りにすることが目標
* 以下はDjango REST Framework の開発参考。

## Web API 参考(Django Rest Framework)

http://www.django-rest-framework.org/api-guide/authentication/

### settings 

* INSTALL_APPS

```
    'rest_framework',
    'rest_framework.authtoken',
```

* REST_FRAMEWORK

```
    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],
        # 本番環境では Browsable API を disabled する
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        )
    }
```

### urls.py

```
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
```                       
                       
### 対象のViewSet

```
    authentication_classes = (TokenAuthentication, )
```
