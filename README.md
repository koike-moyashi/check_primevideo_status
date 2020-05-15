# check prime video status
指定したAmazon Prime Video (URL)が無料に変わったらSlackに通知します

## 準備
- python3とpipが必要です
- `pip install requests beautifulsoup4 lxml html5lib slackclient`

## 使い方
1. scrape_datasにURLを書きます。
```
scrape_datas = [
    { 'url' : 'https://www.amazon.co.jp/gp/video/detail/XXXXXX/'},
    { 'url' : 'https://www.amazon.co.jp/gp/video/detail/YYYYYY/'}
]
```

2. slack_tokenを設定します。
```
slack_token = 'XXXXX'
```
- Slack APIのTokenの取得・場所（Legacy tokens）
  - https://qiita.com/ykhirao/items/0d6b9f4a0cc626884dbb

3. 実行
- `python check_primevideo_status.py`
  - 動きが怪しかったら、すでに無料になっているURLを入れてテストしてみて下さい。
  
4. 定期実行
- cron等で１週間に１度実行します。
