# 俺の百名蒸 - My 100 Distilleries

## ファイル構成
- `template.html` - HTMLテンプレート（編集対象）
- `data_raw.json` - 283蒸留所データ
- `build.py` - テンプレートにデータを埋め込んでindex.htmlを生成
- `index.html` - ビルド済みファイル（デプロイ対象）

## 開発
```bash
python3 build.py
open index.html
```

## Netlifyへのデプロイ
GitHubリポジトリをNetlifyに接続すると、pushのたびに自動デプロイされる。
ビルドコマンド: `python3 build.py` / 公開ディレクトリ: `.`（`netlify.toml`で設定済み）

## OGP画像
`ogp.png`（1200x630px推奨）を同ディレクトリに配置し、
template.html内のog:imageのURLを本番URLに更新すること。
