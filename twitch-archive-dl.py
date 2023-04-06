import requests
import json
import os

# Twitch APIの認証情報
client_id = "YOUR_TWITCH_CLIENT_ID"
oauth_token = "YOUR_TWITCH_OAUTH_TOKEN"

# ダウンロード先のディレクトリを指定
download_dir = "PATH_TO_DOWNLOAD_DIR"

# アーカイブを取得するチャンネルのIDを指定
channel_id = "TWITCH_CHANNEL_ID"

# Twitch APIからアーカイブの情報を取得する関数
def get_channel_videos(channel_id):
    url = f"https://api.twitch.tv/helix/videos?user_id={channel_id}&type=archive"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {oauth_token}"
    }
    response = requests.get(url, headers=headers)
    return json.loads(response.text)["data"]

# アーカイブのURLからファイル名を生成する関数
def generate_filename(video_url):
    return video_url.split("/")[-1]

# アーカイブをダウンロードする関数
def download_video(video_url, filename):
    response = requests.get(video_url)
    with open(os.path.join(download_dir, filename), "wb") as f:
        f.write(response.content)

# チャンネルのアーカイブを取得し、ダウンロードする処理
videos = get_channel_videos(channel_id)
for video in videos:
    video_url = video["url"]
    filename = generate_filename(video_url)
    download_video(video_url, filename)