## ビルド/デバッグ
```
docker-compose up -d
```

## djangoサーバー疎通確認
```
docker exec -it mybookshelf_web_1 bash
root@3b5b6ff69727:/code# curl http://localhost:8000
root@3b5b6ff69727:/code# exit
```

## docker-compose log確認
```
docker-compose logs
```

## django log確認
```
docker ps
docker logs <CONTAINER ID>
```

## 終了
```
docker-compose stop
```